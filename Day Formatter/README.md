# Day Formatter

A simple Python program that converts a day number (1-7) into a formatted day of the week. You can choose from three formats: full name, abbreviation, or single letter.

---

## Features

- Converts **day numbers (1-7)** into:
  - Full day name (e.g., "Monday")
  - Abbreviation (e.g., "Mon")
  - Single letter (e.g., "M")
- Handles invalid inputs gracefully with error messages.
- Lightweight and easy to integrate into other projects.

---

## Usage

```python
from day_formatter import DayFormat

# Full day name
day_number = 3
format = "name"
day = DayFormat(day_number, format)
print(f"Day number {day_number} in format '{format}' is {day}")
# Output: Day number 3 in format 'name' is Wednesday

# Abbreviation
day_number = 5
format = "abbreviation"
day = DayFormat(day_number, format)
print(f"Day number {day_number} in format '{format}' is {day}")
# Output: Day number 5 in format 'abbreviation' is Fri

# Single letter
day_number = 6
format = "letter"
day = DayFormat(day_number, format)
print(f"Day number {day_number} in format '{format}' is {day}")
# Output: Day number 6 in format 'letter' is S

# Invalid input
day_number = 9
format = "name"
day = DayFormat(day_number, format)
print(f"Day number {day_number} in format '{format}' is {day}")
# Output: Error: Day number must be between 1 and 7
