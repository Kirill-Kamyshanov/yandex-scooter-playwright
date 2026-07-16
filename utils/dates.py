from datetime import date, timedelta


def date_for_test(days: int = None) -> tuple[int, str, str]:
    """Возвращает раздельную дату для тестов. Принимает число дней от текущей даты"""
    months = {
        "1": "январь",
        "2": "февраль",
        "3": "март",
        "4": "апрель",
        "5": "май",
        "6": "июнь",
        "7": "июль",
        "8": "август",
        "9": "сентябрь",
        "10": "октябрь",
        "11": "ноябрь",
        "12": "декабрь"
    }
    date_in_future = date.today() + timedelta(days=days) if days is not None else date.today()
    year_in_week = str(date_in_future.year)
    month_in_week = months[str(date_in_future.month)]
    day_in_week = date_in_future.day
    return day_in_week, month_in_week, year_in_week
