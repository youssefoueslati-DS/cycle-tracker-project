import json
from pathlib import Path

DATA_FILE = Path.home() / ".cycle_tracker_data.json"


def load_data() -> dict:
    if not DATA_FILE.exists():
        return {"period_starts": []}

    with DATA_FILE.open("r", encoding="utf-8") as file:
        return json.load(file)


def save_data(data: dict) -> None:
    with DATA_FILE.open("w", encoding="utf-8") as file:
        json.dump(data, file, indent=2)


def add_period_start(date_str: str) -> None:
    data = load_data()

    if date_str not in data["period_starts"]:
        data["period_starts"].append(date_str)
        data["period_starts"].sort()

    save_data(data)


def get_period_starts() -> list[str]:
    data = load_data()
    return data["period_starts"]