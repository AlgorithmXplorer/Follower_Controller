from datetime import datetime
from datetime import timedelta

# The purpose of this function is to ensure that the bot runs at the start of every hour.
# To do this, it calculates how many seconds are left until the next hour and outputs it.
def timer() -> int:
    now = datetime.now()
    one_hour_later = now + timedelta(hours=1)
    new_time = datetime(
        year=one_hour_later.year, 
        month= one_hour_later.month,
        day= one_hour_later.day,
        hour= one_hour_later.hour,
        minute= 00,
        second= 00
        )
    diff = new_time - datetime.now()
    return diff.seconds
