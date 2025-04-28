#! python3

class Time:
    """
    Represents a time of day.
    Attributes: hour, minute, second
    """

def mul_time(time, num):

    mins = time.hour * 60 + time.minute
    secs = mins * 60 + time.second

    calc = secs * num
    
    calc_time = Time()
    minutes, calc_time.second = divmod(calc, 60)
    calc_time.hour, calc_time.minute = divmod(minutes, 60)
    print(f"{calc_time.hour} hours, {calc_time.minute} minutes, {calc_time.second} seconds.")

dist = 10
calc_dist = 1 / dist

t = Time()
t.hour = 2
t.minute = 24
t.second = 3

mul_time(t, calc_dist)