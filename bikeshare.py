import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv', 'Chicago': 'chicago.csv', 'New York City': 'new_york_city.csv', 'new york city': 'new_york_city.csv', 'washington': 'washington.csv', 'Washington': 'washington.csv' }

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('\nHello! Let\'s explore some US bikeshare data!\n')
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    city = input("Would you like to see data for Chicago, New York City, or Washington?:\n").lower()
    cities = ["chicago", "new york city", "washington", "all"]
    while city not in cities:
        city = input("Please enter an accepted city (Not Case Sensitive):\n").lower()

    # TO DO: get user input for month (all, january, february, ... , june)
    month = input("\nWhich month? January, February, March, April, May, June, or All?:\n").lower()
    months = ["january", "february", "march", "april", "may", "june", "all"]
    while month not in months:
        month = input("Please enter an accepted month or enter 'All':\n").lower()

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    day = input("\nWhich day? Monday, Tuesday, Wednesday, Thursday, Friday, Saturday, Sunday or All?:\n").lower()
    days = ["monday", "tuesday", "wednesday", "thursday", "friday", "saturday", "sunday", "all"]
    while day not in days:
        day = input("Please enter an accepted day or enter 'All':\n").lower()

    print('-'*70)
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

"Data regarding time of the trip"
def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    popular_month = df['month'].mode()[0]
    print(f"\nThe most popular month is: {popular_month}")

    # TO DO: display the most common day of week
    popular_day = df['day_of_week'].mode()[0]
    print(f"\nThe most popular day of the week is: {popular_day}")

    # TO DO: display the most common start hour
    #Obtain hour data for Start Time
    df['hour'] = df['Start Time'].dt.hour
    popular_start_hour = df['hour'].mode()[0]
    print(f"\nThe most popular start hour is: {popular_start_hour}")

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*70)

"Data regardingthe bike stations"
def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    popular_start_station = df['Start Station'].mode()[0]
    print(f"\nThe most commonly used start station is:\n{popular_start_station}")

    # TO DO: display most commonly used end station
    popular_end_station = df['End Station'].mode()[0]
    print(f"\nThe most commonly used end station is:\n{popular_end_station}")

    # TO DO: display most frequent combination of start station and end station trip
    #Create a new column combining the data from Start and Stop station separated by 'and'
    df['Start n Stop Points'] = df['Start Station'].str.cat(df['End Station'], sep=" and ")
    popular_start_stop = df['Start n Stop Points'].mode()[0]
    print(f"\nThe most popular Start and stop point combination is:\n{popular_start_stop}")

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*70)

"Data regarding trip duratrion"
def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total_duration = df['Trip Duration'].sum()
    print(f"\nThe total trip duration is:\n{total_duration} seconds")

    # TO DO: display mean travel time
    mean_trip_duration = df['Trip Duration'].mean()
    print(f"\nThe average trip duration is:\n{mean_trip_duration} seconds")

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*70)

"Data regarding user statistics"
def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    user_type_count = df['User Type'].value_counts()
    print(f"\nThe total number of each user type is:\n{user_type_count}")

    # TO DO: Display counts of gender
    try:
        gender = df['Gender'].value_counts()
        print(f"\nThe amount of users by gender is:\n{gender}")
    except:
        print("\nThere is no 'Gender' data in this file.")

    # TO DO: Display earliest, most recent, and most common year of birth
    try:
        oldest_year = df['Birth Year'].min()
        common_year = df['Birth Year'].mode()[0]
        youngest_year = df['Birth Year'].max()
        print(f"\nThe oldest user(s) was born in the year:\n{oldest_year}")
        print(f"\nThe user with the most common age was born in the year:\n{common_year}")
        print(f"\nThe youngest user(s) was born in the year:\n{youngest_year}")
    except:
        print("\nThere is no 'Birth Year' data in this file.")

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*70)

#Createing function that upon request from the user, will show 5 rows of data at a time
def display_data(df):
    view_data = input("Would you like to see 5 rows of trip data? Please enter Yes or No:\n").lower()
    start_loc = 0
    display_more = "yes"
    while display_more == "yes":
        print(df.iloc[start_loc:(start_loc+5)])
        start_loc += 5
        display_more = input("Would you like to see 5 more rows of data?:\n").lower()


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        display_data(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break

if __name__ == "__main__":
	main()
#Code already refactored. Adding comment to re-commit project with proper commit message format per Project Review.
