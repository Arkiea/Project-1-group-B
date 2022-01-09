# Define a function to create interactive plotly charts using prophet
def create_forecast(data, start_date, asset_name):
    
    # Rename columns to satisfy module requirements
    data.columns = ['ds','y']
    
    # Filter data based on date specified
    data = data[data['ds'] >= start_date]
    
    # Assign variable
    m = Prophet()

    # Fit data
    m.fit(data)
    
   # Make future predictions of the stock price for 1 year in advance
    future = m.make_future_dataframe(periods = 365)

    # Predict future values and store in dataframe forecast
    forecast = m.predict(future)
    
    # Create figure
    trace = go.Scatter(
    name = 'Actual price',
    mode = 'markers',
    x = list(forecast['ds']),
    y = list(data['y']),
    marker=dict(
        color='#FFBAD2',
        line=dict(width=1)))
    
    # Include the second trace that forecasts the asset price
    trace1 = go.Scatter(
        name = 'Asset trending',
        mode = 'lines',
        x = list(forecast['ds']),
        y = list(forecast['yhat']),
        marker=dict(
            color='red',
            line=dict(width=3)))
    
    # Create the upper band 
    upper_band = go.Scatter(
        name = 'Upper band',
        mode = 'lines',
        x = list(forecast['ds']),
        y = list(forecast['yhat_upper']),
        line = dict(color='#57b88f'),
        fill = 'tonexty')
    
    # Create the lower band
    lower_band = go.Scatter(
        name= 'Lower band',
        mode = 'lines',
        x = list(forecast['ds']),
        y = list(forecast['yhat_lower']),
        line= dict(color='#1705ff'))
    
    # Include actual price data
    tracex = go.Scatter(
        name = 'Actual price',
       mode = 'markers',
       x = list(data['ds']),
       y = list(data['y']),
       marker=dict(
          color='black',
          line=dict(width=2) ))
    
    # Create list of the components of the chart created above
    data_fig = [tracex, trace1, lower_band, upper_band, trace]
    
    # Specify the layout of the chart figure
    layout = dict(title = 'Price Forecast of' + ' ' + asset_name,
                  xaxis = dict(title = 'Dates', ticklen = 2, zeroline = True))
    
    # Initiate figure build
    figure = dict(data = data_fig, 
                  layout= layout)
    
    # Produce figure
    return py.offline.iplot(figure)

# Define the chart for top and bottom performers over the Covid-19 Period
def top_bottom_performers(data):
    

    # Create the bar chart for top 10 and bottom 10 performers throughout the Covid Period
    performance = data.hvplot.bar(title = 'Top and Bottom Performers Within The S&P 500 Throughout Covid-19', 
                                  x = 'Ticker', y = 'Percentage Change (%)', 
                                  color = 'Percentage Change (%)', alpha = 0.5,
                                  groupby = 'Performance',
                                  rot = 90).opts(width = 600, 
                                                 height = 500, 
                                                 xlabel = 'Company', 
                                                 ylabel = 'Percentage Change YOY (%)')
    
    # Return the figure
    return performance

# Create function for assessing correlation between cryto and FG index
def fear_greed_crypto(data, crypto):
    
    # Create figure with secondary y-axis
    crypto_fg = make_subplots(specs = [[{"secondary_y" : True}]])

    # Add traces
    crypto_fg.add_trace(
        go.Scatter(x = data['Date'], y = data[crypto], name = "Price ($USD)"),
        secondary_y = False,
    )

    crypto_fg.add_trace(
        go.Scatter(x = data['Date'], y = data['Moving Avg FG Index'], name = "Fear Greed Index Value"),
        secondary_y=True,
    )

    # Add figure title
    crypto_fg.update_layout(
        title_text = "Correlation between " + crypto + ' and the Fear and Greed Index'
    )

    # Set x-axis title
    crypto_fg.update_xaxes(title_text = "Date")
    
    # Add in covid reference band
    crypto_fg.add_vrect(x0 = "2020-02-01", x1 = "2020-05-30", 
              annotation_text = "Peak Covid Impact", annotation_position = "top left",
              fillcolor = "red", opacity = 0.25, line_width = 0)

    # Set y-axes titles
    crypto_fg.update_yaxes(title_text = "<b>Value</b> $USD", secondary_y = False)
    crypto_fg.update_yaxes(title_text = "<b>Fear Greed</b> Value", secondary_y = True)

    return crypto_fg.show()

# Create the function for assessing fear and greed index vs cryptocurrencies
def fear_greed_crypto(data, crypto, crypto_two):
    
    # Create the plot
    crypto_plt = data.hvplot.line(x = 'Date', 
                                     y = crypto,
                                     yformatter = '%.0f').opts(width = 750,height = 250, 
                                                               xlabel = 'Date', 
                                                               ylabel = '$ (USD)')
    
    crypto_two_plt = data.hvplot.line(x = 'Date', 
                                     y = crypto_two,
                                     yformatter = '%.0f').opts(width = 750,height = 250, 
                                                               xlabel = 'Date', 
                                                               ylabel = '$ (USD)')
    
    # Return the figure
    return crypto_plt + crypto_two_plt

# Create function that returns
def create_covid_map(data, year, color):
    
    # Create the map
    covid_map = px.scatter_mapbox(
        data[data['date'] == year],
        lat = "Latitude",
        lon = "Longitude",
        size = "Cases",
        color_discrete_sequence = [color],
        zoom = 4,
        mapbox_style = 'dark',
        hover_data = data[['Country','Cases','Deaths']],
        width = 950,
        title = "Global Covid-19 Cases by Country " + '(' + str(year) + ')'
        )

    #Adjust pitch and bearing to adjust the rotation
    covid_map.update_layout(margin = {"r":0,"t":0,"l":0,"b":0}, 
                  mapbox = dict(
                      pitch = 60,
                      bearing = 30
                  ))

    # Display the map
    return covid_map

# Create economic impacts map
def create_economic_map(data, eco_indicator):
    
    # Create the map
    eco_map = px.scatter_mapbox(
        data,
        lat = "Latitude",
        lon = "Longitude",
        size = eco_indicator,
        color = 'Impact',
        zoom = 4,
        mapbox_style = 'dark',
        hover_data = data[['Country','Change in GDP (Year on Year)','Change in Inflation Rate (Year on Year)']],
        width = 950,
        title = "Impact of Covid 19 on GDP Per Capita Growth"
        )

    #Adjust pitch and bearing to adjust the rotation
    eco_map.update_layout(margin = {"r":0,"t":0,"l":0,"b":0}, 
                  mapbox = dict(
                      pitch = 60,
                      bearing = 30
                  ))

    # Display the map
    return eco_map

# Define a function that creates a correlation heatmamp between cryptocurrencies and the FG crypto index
def correlation_feargreed_crpyto(data):
    
    # Establish correlation between multiple asset classes and fear greed index
    data = data[['Bitcoin','Ethereum','S&P 500','Fear and Greed Value']].corr()
    
    # Create heatmap
    corr_matrix = sns.heatmap(data, annot=True).\
                    set_title("Correlation Between Fear & Greed Index and various assets", 
                              fontdict= { 'fontsize': 18, 'fontweight':'bold'})
    
    # Return plot
    return corr_matrix