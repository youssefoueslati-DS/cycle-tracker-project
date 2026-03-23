from datetime import datetime, timedelta
from statistics import median


MIN_CYCLE_LENGTH = 15
MAX_CYCLE_LENGTH = 45


def parse_dates(date_strings: list[str]) -> list[datetime]:
    return [datetime.strptime(date_str, "%Y-%m-%d") for date_str in date_strings]


def get_cycle_lengths(date_strings: list[str]) -> list[int]:
    dates = parse_dates(date_strings)

    if len(dates) < 2:
        return []

    cycle_lengths = []
    for i in range(1, len(dates)):
        delta = dates[i] - dates[i - 1]
        cycle_lengths.append(delta.days)

    return cycle_lengths


def get_valid_cycle_lengths(date_strings: list[str]) -> list[int]:
    cycle_lengths = get_cycle_lengths(date_strings)

    return [
        length
        for length in cycle_lengths
        if MIN_CYCLE_LENGTH <= length <= MAX_CYCLE_LENGTH
    ]


def get_average_cycle_length(date_strings: list[str]) -> float | None:
    valid_lengths = get_valid_cycle_lengths(date_strings)

    if not valid_lengths:
        return None

    return sum(valid_lengths) / len(valid_lengths)


def get_median_cycle_length(date_strings: list[str]) -> float | None:
    valid_lengths = get_valid_cycle_lengths(date_strings)

    if not valid_lengths:
        return None

    return float(median(valid_lengths))


def predict_next_period(date_strings: list[str]) -> str | None:
    typical_cycle_length = get_median_cycle_length(date_strings)

    if typical_cycle_length is None:
        return None

    last_date = datetime.strptime(date_strings[-1], "%Y-%m-%d")
    predicted_date = last_date + timedelta(days=round(typical_cycle_length))

    return predicted_date.strftime("%Y-%m-%d")