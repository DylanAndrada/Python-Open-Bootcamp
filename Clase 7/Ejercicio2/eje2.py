import time as t
import datetime as dt


def home_time():
    a = dt.datetime.now()
    print(a.hour)
    if a.hour < 19:
        time_to_wait = dt.timedelta(hours = 19, minutes = 00) - dt.timedelta(hours = a.hour, minutes = a.minute)
        print("Aun no es hora de irse, quedan:", time_to_wait)
    else:
        print("Ya es hora de irse")

home_time()