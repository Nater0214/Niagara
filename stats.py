# stats.py
# Handles generating stats


# Imports
from statistics import mean
from datetime import timedelta, date

import dates


# Methods
def average_between() -> int:
    """Calculates the average days between each event"""

    dates_ = dates.all()

    return round(mean([amount.days for amount in [dates_[i + 1] - dates_[i] for i in range(len(dates_) - 1)]]))


def average_deviation() -> int:
    """Calculates the average deviation from the average amount of days"""

    dates_ = dates.all()
    average = timedelta(days=average_between())

    return round(mean([deviation.days for deviation in [abs(amount - average) for amount in [dates_[i + 1] - dates_[i] for i in range(len(dates_) - 1)]]]))


def predict_next_date() -> date:
    """Predicts the next date of the event"""

    return dates.last_date() + timedelta(days=average_between())


def predict_next_date_range() -> tuple[date]:
    """Predicts the next date range of the event"""

    return (predict_next_date() - timedelta(days=average_deviation()), predict_next_date() + timedelta(days=average_deviation()))