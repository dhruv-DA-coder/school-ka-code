from datetime import datetime

def get_day_of_year_and_julian_day(date_str):
    # Parse the input date string
    date_obj = datetime.strptime(date_str, "%b %d %Y")

    # Calculate day of the year
    day_of_year = date_obj.timetuple().tm_yday

    # Calculate Julian day
    a = (14 - date_obj.month) // 12
    y = date_obj.year + 4800 - a
    m = date_obj.month + 12 * a - 3
    julian_day = date_obj.day + ((153 * m + 2) // 5) + 365 * y + y // 4 - y // 100 + y // 400 - 32045

    return day_of_year, julian_day

# Example usage
date_str = input("enter date as the first three letters of the the month followed by date , which is followed by the year (eg:- apr 15 2023):")
day_of_year, julian_day = get_day_of_year_and_julian_day(date_str)

print("Day of the year:", day_of_year)
print("Julian day:", julian_day)
