from csv import DictReader
from tabulate import tabulate


def read_assignment_file(file_name: str) -> list:
    """Function to read in the CSV childcare assignment file

    Args:
        file_name (str): File name of the CSV file detailing childcare
            assignment duties

    Returns:
        list: List of tuples, with each tuple representing each row of the file
    """

    assignments = []
    with open(file_name, "r") as f:
        reader = DictReader(f)
        for row in reader:
            assignments.append((row["date"], row["AM_PM"], row["helper"]))

    return assignments


def print_assignments(assignments: list) -> bool:
    """Function to print assignments as a formatted table in plaintext

    Args:
        assignments (list): List of tuples representing all childcare
            assignments

    Returns:
        bool: True if successful
    """

    headers = ["date", "AM/PM", "helper"]
    print(tabulate(assignments, headers=headers))

    return True


if __name__ == "__main__":

    assignments = read_assignment_file(file_name="childcare_assignment.csv")
    print_assignments(assignments)
