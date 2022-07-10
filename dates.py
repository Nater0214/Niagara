# dates.py
# Handles all of the dates


# Imports
from datetime import date

# Methods
def all() -> list[date]:
    """Returns all dates as datetime.date objects"""
    
    # Get lines
    with open("dates.txt", 'rt') as file:
        lines = [line.rstrip() for line in file]

    # Convert lines into datetime.date objects and return
    # I had to write this as three lines and merge them lol
    return [date(date_part[0], date_part[1], date_part[2]) for date_part in [[int(n) for n in date_part] for date_part in [line.split('-') for line in lines]]]


def last_date() -> date:
    """Returns the date closest to today. It should be the last date in the file, unless it was messed up."""

    # I know this isn't proper use of the walrus operator but I dont care; it still works
    return (dates_ := all())[len(dates_) - 1]


def save() -> bool:
    """Saves the current date\n
    Returns the success of saving (False if today is already there)"""

    today = date.today()

    # Check if today is already saved
    if today == last_date():
        return False
    
    # Write today's date to file
    with open("dates.txt", 'at') as file:
        file.write(str(date.today()) + '\n')
    
    return True


def undo_today() -> bool:
    """Undoes saving the current date if it was already saved\n
    Returns the success of undoing (False if today's date is not there)"""

    today = date.today()

    # Check if today isn't already saved
    if not today == last_date():
        return False
    
    # Get lines
    with open("dates.txt", 'rt') as file:
        lines = [line.rstrip() for line in file]
    
    # Remove last line and reform other lines into a file
    lines.pop()
    out = '\n'.join(lines)
    out += '\n'

    # Write new lines to file
    with open("dates.txt", 'wt') as file:
        file.write(out)
    
    return True