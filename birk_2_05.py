from datetime import datetime

def get_season(dt):
        if dt.month in [1, 2, 12]:
            return "Зима"
        elif dt.month in [3, 4, 5]:
            return " Весна"
        elif dt.month in [6, 7, 8]:
            return "Лето"
        elif dt.month in [9, 10, 11]:
           return "Осень"
        else:
            return
current_datetime=datetime.now()
season=get_season(current_datetime)
print("Какое сейчас время года ?", season)

def get_time_of_day(time):
    if time <= 12:
        return "Утро"
    elif time <= 18:
        return "День"
    elif time <= 24:
        return "Вечер"
    else:
        return "Ночь"
now = datetime.now()
print("Какое сейчас время суток ?", get_time_of_day(now.hour))








