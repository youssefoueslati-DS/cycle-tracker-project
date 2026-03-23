import sys
from datetime import datetime

from .predictor import get_average_cycle_length, predict_next_period
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
    print("  uv run -m cycle_tracker predict")
    print("  uv run -m cycle_tracker stats")


def handle_add(args: list[str]) -> None:
    if len(args) != 1:
        print("Error: add requires one date in the format YYYY-MM-DD")
        return

    date_str = args[0]

    if not is_valid_date(date_str):
        print("Error: invalid date. Use YYYY-MM-DD")
        return

    was_added = add_period_start(date_str)

    if was_added:
        print(f"Added period start date: {date_str}")
    else:
        print(f"Date already exists: {date_str}")


def handle_history() -> None:
    dates = get_period_starts()

    if not dates:
        print("No saved period start dates yet.")
        return

    print("Saved period start dates:")
    for index, date_str in enumerate(dates, start=1):
        print(f"{index}. {date_str}")


def handle_predict() -> None:
    dates = get_period_starts()
    predicted_date = predict_next_period(dates)

    if predicted_date is None:
        print("Not enough data to predict the next period.")
        return

    print(f"Estimated next period start: {predicted_date}")


def handle_stats() -> None:
    dates = get_period_starts()
    average_cycle_length = get_average_cycle_length(dates)

    if average_cycle_length is None:
        print("Not enough data to calculate statistics.")
        return

    print(f"Average cycle length: {average_cycle_length:.1f} days")


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
    elif command == "predict":
        handle_predict()
    elif command == "stats":
        handle_stats()
    else:
        print(f"Error: unknown command '{command}'")
        print_usage()