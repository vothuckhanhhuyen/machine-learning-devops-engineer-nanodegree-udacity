def days_until_launch(current_day, launch_day):
    """"Returns the days left before launch.
    
    current_day (int) - current day in integer
    launch_day (int) - launch day in integer
    """
    days = launch_day - current_day
    
    if days < 0:
        return 0
    else:
        return days
