import time
import pandas as pd
import numpy as np

######################################################################################################################
#  Project Description:                                                                                              #
#      In this project, Python script will be used to explore data related to bike share systems for three major     #
#      cities in the United States Chicago, New York City, and **Washington.                                         #
#####################################################################################################################

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
    print("")
    print('Hello! Let\'s explore some US bikeshare data!')
    print("")
    # get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    correct_city_name = ['chicago','new york city','washington']

    while True:
        user_selected_city = input("Would you like to explore data for (chicago, new york city, washington)?:  ")
        print("")
        if user_selected_city.lower() in correct_city_name:
            city = user_selected_city
            break
        else:
            print("Invalid choice !!! Please select one of the three cities (chicago, new york city, washington)")
            print("")




    # get user input for month (all, january, february, ... , june)
    correct_month = ['all' , 'january' , 'february' , 'march' , 'april' , 'may' , 'june']
    while True:
        user_selected_city = input("Which month? (All, January , February , March , April , May or June) :  ")
        print("")
        if user_selected_city.lower() in correct_month:
            month = user_selected_city
            break
        else:
            print("Invalid choice !!! Please select the correct month (All , January , February , March , April , May or June)")
            print("")


    # get user input for day of week (all, monday, tuesday, ... sunday)
    correct_day = ['all' , 'monday' , 'tuesday' , 'wednesday' , 'thursday', 'friday' , 'saturday' , 'sunday' ]
    while True:
        user_selected_day = input("Which day? (All , Monday , Tuesday , Wednesday , Thursday , Friday , Saturday , Sunday) :  ")
        print("")
        if user_selected_day.lower() in correct_day:
            day = user_selected_day
            break
        else:
            print("Invalid choice !!! Please select the correct day (All , Monday , Tuesday , Wednesday , Thursday , Friday , Saturday , Sunday)")
            print("")


    print('-'*40)
    return city , month , day


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
    city = city.lower()
    month = month.lower()
    day = day.lower()

    # load data file into a dataframe
    df = pd.read_csv(CITY_DATA[city])

    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # extract month and day of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name

    # filter by month if applicable
    if month != 'all':
        # use the index of the months list to get the corresponding int
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1

        # filter by month to create the new dataframe
        df = df[df['month'] == month]

    # filter by day of week if applicable
    if day != 'all':
        # filter by day of week to create the new dataframe
        df = df[df['day_of_week'] == day.title()]

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    print("")
    start_time = time.time()

    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # display the most common month
    df['month'] =  df['Start Time'].dt.month
    most_common_month = df['month'].mode()[0]
    print("The most common month: ",most_common_month)
    print("")

    # display the most common day of week
    df['day_of_week'] =  df['Start Time'].dt.weekday_name
    most_common_day_of_week = df['day_of_week'].mode()[0]
    print("The most common day of week: ",most_common_day_of_week)
    print("")

    # display the most common start hour
    df['hour'] =  df['Start Time'].dt.hour
    most_common_hour = df['hour'].mode()[0]
    print("The most common start hour: ",most_common_hour)
    print("")

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    print("")
    start_time = time.time()

    # display most commonly used start station
    most_commonly_used_start_station_1 = df['Start Station'].mode()[0]
    count_of_most_commonly_used_start_station_2 = df['Start Station'].value_counts()[0]
    print("The most commonly used start station: {} with count number: {}.".format(most_commonly_used_start_station_1,count_of_most_commonly_used_start_station_2))
    print("")


    # display most commonly used end station
    most_commonly_used_end_station_1 = df['End Station'].mode()[0]
    count_of_most_commonly_used_end_station_2 = df['End Station'].value_counts()[0]
    print("The most commonly used end station: {} with count number: {}.".format(most_commonly_used_end_station_1,count_of_most_commonly_used_end_station_2))
    print("")


    # display most frequent combination of start station and end station trip
    most_frquent_combination_trip = df[['Start Station', 'End Station']].mode()
    print("The most frequent combination of start station and end station trip")
    print(most_frquent_combination_trip)
    print("")


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    print("")
    start_time = time.time()

    # display total travel time
    total_travel_time = df['Trip Duration'].sum()
    print("The total travel time is: {}.".format(total_travel_time))
    print("")

    # display mean travel time
    mean_travel_time = df['Trip Duration'].mean()
    print("The mean travel time is: {}.".format(mean_travel_time))
    print("")


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    print("")
    start_time = time.time()

    # Display counts of user types
    if 'User Type' in df.columns:
        counts_of_user_types = df['User Type'].value_counts()
        print("counts of user types: .....")
        print(counts_of_user_types)
        print("")

    # Display counts of gender
    if 'Gender' in df.columns:
        counts_of_gender = df['Gender'].value_counts()
        print("counts of gender: .....")
        print(counts_of_gender)
        print("")

    # Display earliest, most recent, and most common year of birth


    if 'Birth Year' in df.columns:

        earliest_year_of_birth = df['Birth Year'].min()
        print("The earliest year of birth is {}.".format(earliest_year_of_birth))
        print("")


        most_recent_year_of_birth = df['Birth Year'].max()
        print("The most recent year of birth is {}.".format(most_recent_year_of_birth))
        print("")

        most_common_year_of_birth = df['Birth Year'].mode()[0]
        count_most_common_year_of_birth = df['Birth Year'].value_counts().values[0]
        print("The most common year of birth is {} with count number {}.".format(most_common_year_of_birth,count_most_common_year_of_birth))



    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def main():
    while True:
        city,month,day = get_filters()

        df = load_data(city,month,day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
