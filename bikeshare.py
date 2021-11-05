#################################################
# This is my Udacity Project for Python Lesson  #
#################################################
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
    # get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs    
    while True:
        city = input('\nWhich city would you like to explore? chicago, new york city or washington.\n').lower()
        if city in ['chicago', 'new york city', 'washington']:
            break
        else:
            print('Please enter one of the following cities: chicago, new york city or washington.\n')

    # get user input for month (all, january, february, ... , june)
    while True:
        month = input('\nWhich month would you like to explore? all, january, february, ... , june.\n').lower()
        if month in ['all', 'january', 'february', 'march', 'april', 'may', 'june']:
            break
        else:
            print('Please enter one of the following months: all, january, february, ... , june.\n')

    # get user input for day of week (all, monday, tuesday, ... sunday)
    while True:
        day = input('\nWhich day would you like to explore? all, Saturday, Sunday, ... , Friday.\n').lower()
        if day in ['all', 'saturday', 'sunday', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday']:
            break
        else:
            print('Please enter one of the following days: all, Saturday, Sunday, ... , Friday.\n')

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
    # load data file into a dataframe
    df = pd.read_csv(CITY_DATA[city])

    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # extract month and day of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.strftime("%A") #df['Start Time'].dt.day_name() 


    # filter by month if applicable
    if month != 'all':
        # use the index of the months list to get the corresponding int
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1
    
        # filter by month to create the new dataframe
        df = df[df['month']==month]

    # filter by day of week if applicable
    if day != 'all':
        # filter by day of week to create the new dataframe
        df = df[df['day_of_week']==day.capitalize()]

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # display the most common month
    popular_month = df['month'].mode()[0]
    print('The most common month: ', popular_month)


    # display the most common day of week
    popular_day = df['day_of_week'].mode()[0]
    print('The most common day: ', popular_day)

    # display the most common start hour
    # extract hour from the Start Time column to create an hour column
    df['hour'] = pd.to_datetime(df['Start Time']).dt.hour

    # find the most common hour (from 0 to 23)
    popular_hour = df['hour'].mode()[0]
    print('The most common hour: ', popular_hour)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # display most commonly used start station
    popular_start_station = df['Start Station'].mode()[0]
    print('The most common start station: ', popular_start_station)

    # display most commonly used end station
    popular_end_station = df['End Station'].mode()[0]
    print('The most common end station: ', popular_end_station)

    # display most frequent combination of start station and end station trip
    popular_start_end_station = ('From: '+ df['Start Station'] + ' To: ' + df['End Station']).mode()[0]
    print('frequent combination of start station and end station trip: ', popular_start_end_station)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # display total travel time
    total_travel_time = df['Trip Duration'].sum()
    print('The total travel time: ', total_travel_time)


    # display mean travel time
    mean_travel_time = df['Trip Duration'].mean()
    print('The mean travel time: ', mean_travel_time)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Display counts of user types
    users_type_counts = df['User Type'].value_counts()
    print('The counts of user types: \n', users_type_counts)

    # Display counts of gender
    if 'Gender' in list(df.columns):
        gender_counts = df['Gender'].value_counts()
        print('The counts of gender: \n', gender_counts)

    if 'Birth Year' in list(df.columns):
        # Display earliest, most recent, and most common year of birth
        earliest_birth_year = df['Birth Year'].min()
        print('The earliest birth year: ', earliest_birth_year)

        recent_birth_year = df['Birth Year'].max()
        print('The most recent birth year: ', recent_birth_year)

        common_birth_year = df['Birth Year'].mode()[0]
        print('The most common birth year: ', common_birth_year)    


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)

        explore_data = 'yes'
        index = 0
        while explore_data == 'yes':
            explore_data = input('\nWould you like to continue with exploring 05 raw of data? Enter yes or no.\n')
            if explore_data.lower() != 'yes':
                break
            print(df.iloc[index:index+5,:])
            index = index + 5


        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
