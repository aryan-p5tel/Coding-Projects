#Day Formatter
#This program takes a day number (1-7) and a format (name, abbreviation, letter) and returns the corresponding day in the specified format.


def DayFormat(day_number, format):
    if format == "name":
        if day_number == 1:
            return "Monday"
        elif day_number==2:
            return "Tuesday"
        elif day_number==3:
            return "Wednesday"
        elif day_number=="4":
            return "Thursday"
        elif day_number==5:
            return "Friday"
        elif day_number==6:
            return "Saturday"
        elif day_number==7:
            return "Sunday"
        else:
            return "Error: Day number must be between 1 and 7"
    elif format == "abbreviation":
        if day_number == 1:
            return "Mon"
        elif day_number==2:
            return "Tue"
        elif day_number==3:
            return "Wed"
        elif day_number=="4":
            return "Thu"
        elif day_number==5:
            return "Fri"
        elif day_number==6:
            return "Sat"
        elif day_number==7:
            return "Sun"
        else:
            return "Error: Day number must be between 1 and 7"
    elif format == "letter":
        if day_number == 1:
            return "M"
        elif day_number==2:
            return "T"
        elif day_number==3:
            return "W"
        elif day_number=="4":
            return "T"
        elif day_number==5:
            return "F"
        elif day_number==6:
            return "S"
        elif day_number==7:
            return "S"
        else:
            return "Error: Day number must be between 1 and 7"
    else:
        return "Error: Format must be name, abbreviation or letter"
    
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
day_number=9
format="name"
day=DayFormat(day_number, format)
print("Day number", day_number, "in format", format, "is", day)

