from csv import DictReader
from tabulate import tabulate


def read_assignment_file(file_name: str = "childcare_assignment.csv") -> tuple:

    assignments = []
    with open(file_name, "r") as f:
        reader = DictReader(f)
        for row in reader:
            assignments.append([row["date"], row["AM_PM"], row["helper"]])

    return assignments


if __name__ == "__main__":

    assignments = read_assignment_file()
    print(tabulate(assignments, headers=["date", "AM/PM", "helper"]))
