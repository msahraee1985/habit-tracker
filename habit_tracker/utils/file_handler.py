#ذخیره و بازخوانی داده ها در فایل جیسون
import json
from pathlib import Path
from typing import List
from datetime import date
from habit_tracker.models.habit import Habit

class FileHandler:
    def __init__(self, file_path: str = "habit_tracker/data/habits.json"):
        self.file_path = Path(file_path)
        self.file_path.parent.mkdir(parents=True, exist_ok=True)

    def save_data(self, habits: List[Habit]) -> None:
        try:
            data = {
                "habits": [
                    {
                        "name": habit.name,
                        "frequency": habit.frequency,
                        "completion_dates": [d.isoformat() for d in habit.completion_dates]
                    }
                    for habit in habits
                ]
            }

            with open(self.file_path, 'w') as f:
                json.dump(data, f, indent=4)

        except (IOError, json.JSONEncodeError) as e:
            raise RuntimeError(f"Error saving data: {str(e)}")

    def load_data(self) -> List[Habit]:
        try:
            if not self.file_path.exists():
                return []

            with open(self.file_path, 'r') as f:
                data = json.load(f)

            habits = []
            for item in data.get("habits", []):
                habit = Habit(item["name"], item["frequency"])
                habit.completion_dates = [date.fromisoformat(d) for d in item["completion_dates"]]
                habits.append(habit)

            return habits

        except (FileNotFoundError, json.JSONDecodeError, KeyError) as e:
            raise RuntimeError(f"Error loading data: {str(e)}")

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        pass  # می‌تونی لاگ یا ذخیره نهایی اینجا بزاری
