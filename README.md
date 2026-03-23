# Cycle Tracker

Cycle Tracker is a Python command-line tool for recording menstrual cycle start dates, viewing cycle history,
and estimating the next period start date.

## Features

- Add a new period start date
- View saved period start dates
- Calculate average cycle length
- Calculate median cycle length
- Predict the next period start date
- Ignore outlier cycle lengths in statistics and prediction while still keeping all saved dates in history

## Project Structure

```
cycle_tracker_project/
├── pyproject.toml
├── README.md
├── .gitignore
└── cycle_tracker/
    ├── __init__.py
    ├── __main__.py
    ├── cli.py
    ├── storage.py
    └── predictor.py
```

## Requirements

- Python 3.1o or newer
- uv installed

##Installation

- Clone the repository and move into the project folder:
```
git clone https://github.com/youssefoueslati-DS/cycle-tracker-project.git
cd cycle-tracker-project
```

## Usage

- Run the package with:
```
uv run -m cycle_tracker <command>
```

-Add a period start date:
```
uv run -m cycle_tracker add 2026-03-10
```

-Show history:
```
uv run -m cycle_tracker history
```

-Show statistics:
```
uv run -m cycle_tracker stats
```

-Predict the next period
```
uv run -m cycle_tracker predict
```
## How it works

The program stores period start dates. And from the saved dates,
it calculates cycle lengths as the differences between consecutive start dates.
To reduce the effect of missed entries or unusual gaps:
 -	all dates remain saved in history
 -	unusually short or long cycle lengths are excluded from statistics
 -	prediction is based on the median valid cycle length

## Possible improvements

- Reminder
- Better visualizations

## Author

Youssef Oueslati
