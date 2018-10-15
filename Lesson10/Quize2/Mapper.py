import sys
import string
import logging

from util import mapper_logfile

logging.basicConfig(filename=mapper_logfile, format='%(message)s',
                    level=logging.INFO, filemode='w')


def mapper():
    '''
    For this exercise, compute the average value of the ENTRIESn_hourly column
    for different weather types. Weather type will be defined based on the
    combination of the columns fog and rain (which are boolean values).
    For example, one output of our reducer would be the average hourly entries
    across all hours when it was raining but not foggy.

    Each line of input will be a row from our final Subway-MTA dataset in csv format.
    You can check out the input csv file and its structure below:
    https://s3.amazonaws.com/content.udacity-data.com/courses/ud359/turnstile_data_master_with_weather.csv

    Note that this is a comma-separated file.

    This mapper should PRINT (not return) the weather type as the key (use the
    given helper function to format the weather type correctly) and the number in
    the ENTRIESn_hourly column as the value. They should be separated by a tab.
    For example: 'fog-norain\t12345'

    Since you are printing the output of your program, printing a debug
    statement will interfere with the operation of the grader. Instead,
    use the logging module, which we've configured to log to a file printed
    when you click "Test Run". For example:
    logging.info("My debugging message")
    Note that, unlike print, logging.info will take only a single argument.
    So logging.info("my message") will work, but logging.info("my","message") will not.
    '''

    # Takes in variables indicating whether it is foggy and/or rainy and
    # returns a formatted key that you should output.  The variables passed in
    # can be booleans, ints (0 for false and 1 for true) or floats (0.0 for
    # false and 1.0 for true), but the strings '0.0' and '1.0' will not work,
    # so make sure you convert these values to an appropriate type before
    # calling the function.
    def format_key(fog, rain):
        return '{}fog-{}rain'.format(
            '' if fog else 'no',
            '' if rain else 'no'
        )

    first_line = True
    for line in sys.stdin:
        data = line.strip().split(",")
        if first_line:
            fog_index = data.index("fog")
            rain_index = data.index("rain")
            ENTRIESn_hourly_index = data.index("ENTRIESn_hourly")
            logging.info(fog_index)
            logging.info(rain_index)
            logging.info(ENTRIESn_hourly_index)
            first_line = False
        else:
            key = format_key(float(data[fog_index]), float(data[rain_index]))
            value = data[ENTRIESn_hourly_index]
            print ("{0}\t{1}".format(key, value))


mapper()