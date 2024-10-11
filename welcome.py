from time1 import get_hours,get_date
from output1 import output
import database

def greet():
    previous_date = database.get_last_seen()
    today_date = get_date()
    database.update_last_seen(today_date)

    if previous_date==today_date:
        output("Welcome back sir")
    else:
        hour = int(get_hours())
        if hour>=4 and hour<12:
            output("Good Morning sir")
        elif hour>=12 and hour<16:
            output("Good Afternoon sir ")
        else:
            output("Good Evening sir")