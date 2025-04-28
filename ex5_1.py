import time

def convert_time(t):
    days = int(t // 86400)
    rem_secs_d = t - (days * 86400)
    hours = int(rem_secs_d // 3600)
    rem_secs_h = rem_secs_d - (hours * 3600)
    minutes = int(rem_secs_h // 60)
    seconds = int(rem_secs_h % 60)

    # conversion of UTC to Pacific Time
    if hours == 1:
        hours_adj = 6
    elif hours == 2:
        hours_adj = 7
    elif hours == 3:
        hours_adj = 8
    elif hours == 4:
        hours_adj = 9
    elif hours == 5:
        hours_adj = 10
    elif hours == 6:
        hours_adj = 11
    elif hours == 7:
        hours_adj = 12
    else:
        hours_adj = hours - 7

    print("There have been", days, "days since January 1st, 1970")
    print("The current time is", hours_adj,":", minutes,":",seconds,".")

moment = time.time()
convert_time(moment)




#else:
#    print(f"The current time")