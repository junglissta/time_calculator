week_days = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']

# function to return the number of days in the correct format for the final result string
def day_count(days):
    # if there is only 1 day later
    if days == 1:
        return '(next day)'
    # if there are more than 1 day later
    elif days > 1:
        # return the number of days later in parentheses
        return f'({days} days later)'
    
# function to return the number of minutes in the correct format for the final result string
def min_count(min):
    # if the number of minutes is less than 10, add a leading zero
    if min < 10:
        return f'0{min}'
    # if the number of minutes is more than or equal to 10, return the number as is
    else:
        return f'{min}'

# function to return the day of the week in the correct format for the final result string
def day_week(week_day,days):
    # find the index of the current day in the week_days list and add the number of days passed to it
    # take the modulo 7 to find the index of the day after the specified number of days
    result = (week_days.index(week_day) + days) % 7
    # return the day of the week as a capitalized string
    return f'{week_days[result].capitalize()}'
        

# main function to add the time and duration and return the final result string
def add_time(start, duration, day = ''):
    # initialize variables for number of days passed, final time string, and a counter for while loop
    days = 0
    time = ''
    while_time = 0
    # make the day lowercase for easier comparison
    day = day.lower()
    # if the start time is in PM
    if 'PM' in start:
        # remove the PM from the start time string
        start = start.replace('PM', '')
        # split the start time into hours and minutes and convert them to integers
        split_start = [int(i) for i in start.split(':')]
        # split the duration time into hours and minutes and convert them to integers
        split_duration = [int(i) for i in duration.split(':')]
        
        # add the hours and minutes of start time and duration
        time_hour = split_start[0] + split_duration[0]
        time_minutes = split_start[1] + split_duration[1]
        # if the total number of hours is more than 12, modulo 12 to get the correct hour in PM
        # set the while_time counter to the total number of hours to use in the while loop
        if time_hour > 12:
            time_hour = time_hour % 12
            # if the total number of hours is 0 after modulo, set the hour to 12
            if time_hour == 0:
                time_hour = 12
            while_time = split_start[0] + split_duration[0]
        # if the total number of minutes is more than 60, add the number of extra hours to
        if time_minutes >= 60:
            time_hour += time_minutes // 60
            time_minutes = time_minutes % 60
            while_time = split_start[0] + split_duration[0] + 1
        period = 'PM'
        
        while True:
            if while_time < 12:
                break
            if period == 'PM':
                period = 'AM'
                days += 1
            else:
                period = 'PM'
            
            while_time -= 12
        
    elif 'AM' in start:
        start = start.replace('AM', '')
        split_start = [int(i) for i in start.split(':')]
        split_duration = [int(i) for i in duration.split(':')]
        time_hour = split_start[0] + split_duration[0]
        time_minutes = split_start[1] + split_duration[1]
        if time_hour > 12:
            time_hour = time_hour % 12
            if time_hour == 0:
                time_hour = 12
            while_time = split_start[0] + split_duration[0]
        if time_minutes >= 60:
            time_hour += time_minutes // 60
            time_minutes = time_minutes % 60
            while_time = split_start[0] + split_duration[0] + 1
        period = 'AM'
        
        while True:
            if while_time < 12:
                break
            if period == 'AM':
                period = 'PM'
                
            else:
                period = 'AM'
                days += 1
            
            while_time -= 12
    
    if day != '' and days == 0:
        return f'{time_hour}:{min_count(time_minutes)} {period}, {day_week(day, days)}'
    elif day != '' and days > 0:
        return f'{time_hour}:{min_count(time_minutes)} {period}, {day_week(day, days)} {day_count(days)}'

    elif days == 0 and day == '':
        return f'{time_hour}:{min_count(time_minutes)} {period}'
    
    else:
        return f'{time_hour}:{min_count(time_minutes)} {period} {day_count(days)}'
     



  

