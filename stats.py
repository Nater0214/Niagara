# stats.py
# Handles generating stats


# Imports
from statistics import mean
from datetime import timedelta

import dates


# Methods
def average_days_between() -> int:
    """Calculates the averade days between each event"""

    dates_ = dates.all()

    amounts_deltas = [dates_[i + 1] - dates_[i] for i in range(len(dates_) - 1)]
    return round(mean([amount.days for amount in amounts_deltas]))

average_days_between()