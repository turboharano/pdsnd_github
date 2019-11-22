import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

def get_filters():

    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """

    print('Hello! Let\'s explore some US bikeshare data!')
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    cities=['chicago','new york city','washington']
    while True:
        city = input('\nWould you like to see data for Chicago, New York City, or Washington?: ').lower()
        if city.lower() not in cities:
            print('The input is not a city option. Please, try again.')
        else:
            break

    print('Loading {} data...'.format(city))

    # TO DO: get user input for month (all, january, february, ... , june)
    months=('all', 'january', 'february', 'march', 'april', 'may', 'june')      
    while True:
        month=input('\nWhich month would you like to filter the data? all, january, february, march, april, may or june: ').lower()
        if month.lower() not in months:
            print('The input is not a month option. Please, try again.')
        else:
            break
    print('Loading {} data...'.format(month))


    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    days=('all', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday')
    while True:
        day=input('\nWhich day? all, monday, tuesday, wednesday, thursday, friday, saturday or sunday: ').lower()
        if day.lower() not in days:
            print('The input is not a day of week option. Please, try again.')
        else:
            break
    print('Loading {} data...'.format(day))


    print('-'*40)
    return city, month, day


def load_data(city, month, day):

    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """

    df=pd.read_csv(CITY_DATA[city])
    df['Start Time']=pd.to_datetime(df['Start Time'])
    df['month']=df['Start Time'].dt.month
    df['day_of_week']=df['Start Time'].dt.weekday_name
    if month!='all':
	    months=['january','february','march','april','may','june']
	    month = months.index(month)+1
	    df=df[df['month']==month]
    if day!='all':
	    df=df[df['day_of_week']==day.title()]
    return df


def time_stats(df):

    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()


    # TO DO: display the most common month
    common_month=df['month'].mode()[0]
    print('Most common month: ', common_month)

    # TO DO: display the most common day of week
    common_day_week=df['day_of_week'].mode()[0]
    print('Most common day of week: ', common_day_week)

    # TO DO: display the most common start hour
    df['hour']=df['Start Time'].dt.hour
    common_hour=df['hour'].mode()[0]
    print('Most common start hour: ', common_hour)

    print("\nCalculation delayed %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):

    """Displays statistics on the most popular stations and trip."""


    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()


    # TO DO: display most commonly used start station
    common_start_station=df['Start Station'].mode()[0]
    print('Most commonly used start station: ', common_start_station)


    # TO DO: display most commonly used end station
    common_end_station=df['End Station'].mode()[0]
    print('Most commonly used end station: ', common_end_station)


    # TO DO: display most frequent combination of start station and end station trip
    common_start_end_station=df.groupby(['Start Station', 'End Station']).size().sort_values(ascending=False).reset_index(name='count').head(1)
    print('Most frequent trip: \n', common_start_end_station)


    print("\nCalculation delayed %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):

    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total_travel_time=df['Trip Duration'].sum()
    print('Total travel time: ', total_travel_time)

    # TO DO: display mean travel time
    mean_travel_time=df['Trip Duration'].mean()
    print('Mean travel time: ', mean_travel_time)


    print("\nCalculation delayed %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):

    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    user_types=df['User Type'].value_counts()
    print('User types count:\n', user_types)

    # TO DO: Display counts of gender
    gender_counts=df['Gender'].value_counts()
    print('\nGender count:\n', gender_counts)

    # TO DO: Display earliest, most recent, and most common year of birth
    earliest=df['Birth Year'].min()
    print('\nEarliest year of birth: ', earliest)

    recent=df['Birth Year'].max()
    print('Most recent year of birth: ', recent)

    most_common=df.groupby(['Birth Year']).size().sort_values(ascending=False).reset_index(name='count').head(1)
    print('Most common year of birth:\n', most_common)
 

    print("\nCalculation delayed %s seconds." % (time.time() - start_time))
    print('-'*40)

    
def user_type_only(df):

    """Displays user type only."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    user_types=df['User Type'].value_counts()
    print('User types count:\n', user_types)

    print("\nCalculation delayed %s seconds." % (time.time() - start_time))
    print('-'*40)
    
    
def display_raw_data(df):

    """Displays raw data."""
    
    lower_bound=0
    upper_bound=5
    raw = input('\nWould you like to retrieve raw data? Enter yes(y) or no(n).\n')
    while True:
        if raw.lower() in ['no','n','stop']:
            print('Exiting...')
            break
        elif raw.lower() in ['yes', 'y', '']:
            print(df[df.columns[0:]].iloc[lower_bound:upper_bound])
            lower_bound += 5
            upper_bound += 5
            raw = input('\nContinue next 5 lines? Enter yes("Enter") or stop.\n')
        else:
            print('Invalid input, please, try again!')
            raw = input('\nWould you like to retrieve (or continue retrieving) raw data? Enter yes(y) or no(n).\n')
            
            
    print('-'*40)
        
        
def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)
        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        if city != 'washington':
            user_stats(df)
        else:
            user_type_only(df)
        display_raw_data(df)

        restart = input('\nWould you like to restart? Enter yes(y) or anything else if no.\n')
        if restart.lower() not in ['yes','y']:
            break
        

if __name__ == "__main__":
	main()