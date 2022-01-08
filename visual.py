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
    py.offline.iplot(figure)

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

# Create the function for assessing fear and greed index vs cryptocurrencies (need to understand how to combine charts to compare)
def fear_greed_crypto(data):
    
    # Create the plot
    crypto_plt = data.hvplot.line(x = 'Date', 
                                     y = 'Bitcoin',
                                     yformatter = '%.0f').opts(height = 500, 
                                                               xlabel = 'Date', 
                                                               ylabel = '$ (USD)')
    
    # Create second plot for fear greed secondary axis
    fg_plot = data.hvplot.line(x = 'Date', 
                                     y = 'Moving Avg FG Index',
                                     yformatter = '%.0f').opts(height = 500, 
                                                               xlabel = 'Date', 
                                                               ylabel = 'Fear Greed Value')
    
    # Return the figure
    return crypto_plt + fg_plot