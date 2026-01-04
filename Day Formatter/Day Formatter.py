#Day Formatter
#This program takes a day number (1-7) and a format (name, abbreviation, letter) and returns the corresponding day in the specified format.


def DayFormat(day_number, format):
    formats = {"name":["Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday"],
               "abbreviation":["Mon","Tue","Wed","Thu","Fri","Sat","Sun"],
               "letter":["M","T","W","T","F","S","S"]}
    
    if format not in formats.keys(): raise Exception(f"\"format\" of {format} is invalid. It must be one of \"name\",\"abbreviation\",\"letter\"")
    if day_number > 7 or day_number < 1: raise Exception(f"\"day_number\" of {day_number} is out of range. It must be between 1-7 (inclusive)")

    return formats[format][day_number - 1]
    
day_number=3
format="name"
day=DayFormat(day_number, format)
print("Day number", day_number, "in format", format, "is", day)

day_number=3
format="name"
day=DayFormat(day_number, format)
print("Day number", day_number, "in format", format, "is", day)

day_number=5
format="abbreviation"
day=DayFormat(day_number, format)
print("Day number", day_number, "in format", format, "is", day)

day_number=6
format="letter"
day=DayFormat(day_number, format)
print("Day number", day_number, "in format", format, "is", day)

try:
    day_number=9
    format="name"
    day=DayFormat(day_number, format)
    print("Day number", day_number, "in format", format, "is", day)
except Exception as ex:
    print(f"Error. {ex}")