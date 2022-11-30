week_days = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']

def day_count(days):
    if days == 1:
        return '(next day)'
    elif days > 1:
        return f'({days} days later)'
    
def min_count(min):
    if min < 10:
        return f'0{min}'
    else:
        return f'{min}'

def day_week(week_day,days):
    result = (week_days.index(week_day) + days) % 7
    return f'{week_days[result].capitalize()}'
        



def add_time(start, duration, day = ''):
    days = 0
    time = ''
    while_time = 0
    day = day.lower()
    if 'PM' in start:
        start = start.replace('PM', '')
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
     



  

