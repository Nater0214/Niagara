# dates.py
# Handles all of the dates


# Imports
from datetime import date

# Methods
def all() -> list:
    """Returns all dates as datetime.date objects"""
    
    with open("dates.txt", 'rt') as file:
        lines = [line.rstrip() for line in file]
    
    date_parts = [line.split('-') for line in lines]
    date_parts = [[int(n) for n in date_part] for date_part in date_parts]
    return [date(date_part[0], date_part[1], date_part[2]) for date_part in date_parts]


def save() -> bool:
    """Saves the current date\n
    Returns the success of saving (False if today is already there)"""

    today = date.today()
    
    if today in all():
        return False
        
    with open("dates.txt", 'at') as file:
        file.write(str(date.today()) + '\n')
    
    return True


def undo_today() -> bool:
    """Undoes saving the current date if it was already saved\n
    Returns the success of undoing (False if today's date is not there)"""

    today = date.today()

    if not today in all():
        return False
    
    with open("dates.txt", 'rt') as file:
        lines = [line.rstrip() for line in file]
    
    lines.pop()
    out = '\n'.join(lines)
    out += '\n'

    with open("dates.txt", 'wt') as file:
        file.write(out)
    
    return True