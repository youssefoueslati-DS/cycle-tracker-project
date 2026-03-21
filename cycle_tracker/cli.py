
import sys
from datetime import datetime

from .storage import add_period_start, get_period_starts


def is_valid_date(date_str: str) -> bool:
    try:
        datetime.strptime(date_str, "%Y-%m-%d")
        return True
    except ValueError:
        return False


def print_usage() -> None:
    print("Usage:")
    print("  uv run -m cycle_tracker add YYYY-MM-DD")
    print("  uv run -m cycle_tracker history")


def handle_add(args: list[str]) -> None:
    if len(args) != 1:
        print("Error: add requires one date in the format YYYY-MM-DD")
        return

    date_str = args[0]

    if not is_valid_date(date_str):
        print("Error: invalid date. Use YYYY-MM-DD")
        return

    add_period_start(date_str)
    print(f"Added period start date: {date_str}")


def handle_history() -> None:
    dates = get_period_starts()

    if not dates:
        print("No saved period start dates yet.")
        return

    print("Saved period start dates:")
    for index, date_str in enumerate(dates, start=1):
        print(f"{index}. {date_str}")


def main() -> None:
    args = sys.argv[1:]

    if not args:
        print_usage()
        return

    command = args[0]

    if command == "add":
        handle_add(args[1:])
    elif command == "history":
        handle_history()
    else:
        print(f"Error: unknown command '{command}'")
        print_usage()