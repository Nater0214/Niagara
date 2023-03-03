# stats.py
# Handles generating stats


# Imports
from statistics import mean
from datetime import timedelta

import src.dates as dates


# Methods
def average_between() -> int:
    """Calculates the average days between each event"""

    dates_ = dates.all()

    amounts_deltas = [dates_[i + 1] - dates_[i] for i in range(len(dates_) - 1)]
    return round(mean([amount.days for amount in amounts_deltas]))


def average_deviation() -> int:
    """Calculates the average deviation from the average amount of days"""

    dates_ = dates.all()
    average = timedelta(days=average_between())

    amounts_deltas = [dates_[i + 1] - dates_[i] for i in range(len(dates_) - 1)]
    deviation_deltas = [abs(amount - average) for amount in amounts_deltas]

    return round(mean([deviation.days for deviation in deviation_deltas]))