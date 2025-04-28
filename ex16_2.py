#! python3

import datetime

today = datetime.datetime.today()

if today.weekday() == 0:
    print("Monday")
elif today.weekday() == 1:
    print("Tuesday")
elif today.weekday() == 2:
    print("Wednesday")
elif today.weekday() == 3:
    print("Thursday")
elif today.weekday() == 4:
    print("Friday")
elif today.weekday() == 5:
    print("Saturday")
else:
    print("Sunday")

def your_age(year, month, day):
    birthdate = datetime.datetime(year, month, day)
    age = (today - birthdate) // datetime.timedelta(days=365.2425)
    print(f"You are {age} years old.")

    today2 = datetime.date.today()
    next_birthday = datetime.date(today2.year, birthdate.month, birthdate.day)
    if next_birthday < today2:
        next_birthday = next_birthday.replace(year = today2.year + 1)

    time_to_bday = abs(next_birthday - today2)
    days = str(time_to_bday.days)
    hours = str(time_to_bday.seconds/3600)
    minutes = str(time_to_bday.seconds/60)
    seconds = str(time_to_bday.seconds)
    print(f"It is {days} days, {hours} hours, {minutes} minutes, and {seconds} seconds till your next birthday.")

your_age(1974, 12, 6)

def n_day(n):

    # 1st birthday
    year1 = int(input("What is the year of the first birthday?"))
    month1 = int(input("What is the month of the first birthday?"))
    day1 = int(input("What is the day of the first birthday?"))

    # 2nd birthday
    year2 = int(input("What is the year of the second birthday?"))
    month2 = int(input("What is the month of the second birthday?"))
    day2 = int(input("What is the day of the second birthday?"))

    birthdate1 = datetime.datetime(year1, month1, day1)
    birthdate2 = datetime.datetime(year2, month2, day2)

    today = datetime.datetime.now()

    age1 = (today - birthdate1) // datetime.timedelta(days=365.2425)
    age2 = (today - birthdate2) // datetime.timedelta(days=365.2425)

    if age1 > age2:
        
        for i in range(age1):
            if birthdate1.day() + i == (birthdate2.day() + i) * n:
                dub_date = datetime.date(birthdate1.day() + i)
                print(f"Person 1 is {n} times as old as Person 2 on {dub_date}")
        
    else:
        
        for i in range(len(age2)):
            if birthdate2 + i == (birthdate1 + i) * n:
                dub_date = datetime.date(birthdate2 + i)
                print(f"Person 2 is {n} times as old as Person 1 on {dub_date}")

n_day(2)