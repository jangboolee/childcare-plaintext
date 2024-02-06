import re
from datetime import datetime
from tabulate import tabulate


def get_dates() -> tuple:

    date_pattern = r"202[4-9]-[01]\d-[0-3]\d"

    while True:
        start_date_str = input("Enter start date (YYYY-MM-DD): ")
        if re.match(date_pattern, start_date_str):
            while True:
                end_date_str = input("Enter end date (YYYY-MM-DD): ")
                if re.match(date_pattern, end_date_str):
                    print(f"Start: {start_date_str} | End: {end_date_str}")
                    break
                else:
                    print("Enter in valid ISO format (YYYY-MM-DD)")
            break
        else:
            print("Enter in valid ISO format (YYYY-MM-DD)")

    dates = (
        datetime.strptime(start_date_str, "%Y-%m-%d"),
        datetime.strptime(end_date_str, "%Y-%m-%d"),
    )

    return dates


def get_caretakers(dates: tuple) -> list:
    duration = dates[1] - dates[0]
    print(duration.days)


if __name__ == "__main__":

    dates = get_dates()
    get_caretakers(dates)
