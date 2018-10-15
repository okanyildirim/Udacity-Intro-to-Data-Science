import datetime


def reformat_subway_dates(date):
    '''
    The dates in our subway data are formatted in the format month-day-year.
    The dates in our weather underground data are formatted year-month-day.

    In order to join these two data sets together, we'll want the dates formatted
    the same way.  Write a function that takes as its input a date in the MTA Subway
    data format, and returns a date in the weather underground format.

    Hint:
    There are a couple of useful functions in the datetime library that will
    help on this assignment, called strptime and strftime.
    More info can be seen here and further in the documentation section:
    http://docs.python.org/2/library/datetime.html#datetime.datetime.strptime
    '''

    #date_formatted =date[-4:]+"-"+date[0:3]+date[3:5]
    #date.split()
    date_formatted=datetime.datetime.strptime(date,'%m-%d-%Y')
    date_formatted=datetime.datetime.strftime(date_formatted,'%Y-%m-%d')
    return date_formatted
print(reformat_subway_dates("12-15-1995"))