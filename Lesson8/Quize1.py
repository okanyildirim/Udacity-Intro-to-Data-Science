import pandas
from ggplot import *
from numpy import mean
import pandasql

def plot_weather_data(turnstile_weather):
    '''
    You are passed in a dataframe called turnstile_weather.
    Use turnstile_weather along with ggplot to make a data visualization
    focused on the MTA and weather data we used in assignment #3.
    You should feel free to implement something that we discussed in class
    (e.g., scatterplots, line plots, or histograms) or attempt to implement
    something more advanced if you'd like.

    Here are some suggestions for things to investigate and illustrate:
     * Ridership by time of day or day of week
     * How ridership varies based on Subway station (UNIT)
     * Which stations have more exits or entries at different times of day
       (You can use UNIT as a proxy for subway station.)

    If you'd like to learn more about ggplot and its capabilities, take
    a look at the documentation at:
    https://pypi.python.org/pypi/ggplot/

    You can check out:
    https://s3.amazonaws.com/content.udacity-data.com/courses/ud359/turnstile_data_master_with_weather.csv

    To see all the columns and data points included in the turnstile_weather
    dataframe.

    However, due to the limitation of our Amazon EC2 server, we are giving you a random
    subset, about 1/3 of the actual data in the turnstile_weather dataframe.
    '''

    #agg = turnstile_weather.groupby(['TIMEn'], as_index=False).aggregate(mean)
    #q=  """select TIMEn,sum(ENTRIESn_hourly) from turnstile_weather group by TIMEn;"""
    #df=pandasql.sqldf(q, locals())
    #1-Ridership by time of day or day of week
    #plot=ggplot(df,aes(x='TIMEn',y='sum(entriesn_hourly)'))+ geom_point(color='red')+ geom_line(color='blue')+ggtitle("Ridership by time of day or day of week")+ xlab('TIMEn')+ylab('ENTRIESn_hourly')
    plot = ggplot(turnstile_weather, aes(x='Hour',y='ENTRIESn_hourly')) + geom_histogram(binwidth=1) + scale_x_continuous(limits=[1,24]) + ggtitle('Ridership by time of day') + xlab("Hour") + ylab("ENTRIESn_hourly")
    #2-How ridership varies based on Subway station(UNIT)
    #plot=ggplot(turnstile_weather,aes(x='UNIT',y='ENTRIESn_hourly'))+ geom_point(color='red')+ geom_line(color='blue')+ggtitle("How ridership varies based on Subway station(UNIT)")+ xlab('UNIT')+ylab('ENTRIESn_hourly')

    #3-Which stations have more exits or entries at different times of day
    #plot=ggplot(df,aes(x='TIMEn',y='ENTRIESn_hourly',color='UNIT'))+ geom_point()+ geom_line()+ggtitle("Which stations have more exits or entries at different times of day")+ xlab('UNIT')+ylab('ENTRIESn_hourly')

    return plot
