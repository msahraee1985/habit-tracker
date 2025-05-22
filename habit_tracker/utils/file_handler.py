#ذخیره و بازخوانی داده ها در فایل جیسون
import json #برای ذخیره‌سازی و بازخوانی داده‌ها در فرمت JSON
from pathlib import Path #ابزار حرفه‌ای‌تر برای مدیریت مسیر فایل‌ها
from typing import List #برای تایپ‌گذاری لیست‌ها در فانکشن‌ها
from datetime import date #برای کار با تاریخ‌های انجام‌شده عادت‌ها
from habit_tracker.models.habit import Habit #ایمپورت کلاس عادت برای ساختن و بازیابی شیءها

class FileHandler:
    def __init__(self, file_path: str = "habit_tracker/data/habits.json"):
        self.file_path = Path(file_path) # تبدیل رشته به شی path
        self.file_path.parent.mkdir(parents=True, exist_ok=True) #اطمینان از این که پوشه مقصد خودش وجود داره اگر نبود خودش میسازه

    def save_data(self, habits: List[Habit]) -> None: #این متد لیست عادت ها رو میگیره و به جیسون تبدیال میکنه
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

            with open(self.file_path, 'w') as f: #ذخیره عادت ها
                json.dump(data, f, indent=4)

        except (IOError, json.JSONEncodeError) as e: #هندل کردن ارور ها
            raise RuntimeError(f"Error saving data: {str(e)}")

    def load_data(self) -> List[Habit]:#این متد فایل habits.json رو می‌خونه و لیستی از شیءهای Habit می‌سازه
        try:
            if not self.file_path.exists():# اگر فایل وجود نداشته باشه یک لیست خالی برمیگردونه و برنامه کرش نمیکنه
                return []

            with open(self.file_path, 'r') as f:
                data = json.load(f)

            habits = []
            for item in data.get("habits", []):
                habit = Habit(item["name"], item["frequency"])
                habit.completion_dates = [date.fromisoformat(d) for d in item["completion_dates"]]
                habits.append(habit)

            return habits

        except (FileNotFoundError, json.JSONDecodeError, KeyError) as e:# در صورت خراب بودن JSON یا نبودن کلید، خطای قابل فهم تولید می‌کنه.
            raise RuntimeError(f"Error loading data: {str(e)}")

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        pass  
