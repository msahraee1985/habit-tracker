from typing import List, Optional
from habit_tracker.models.habit import Habit

class HabitTracker: #کلاس اصلی پروژه
    def __init__(self):
        self.habits: List[Habit] = [] #لیست خالی برای ذخیره عادت ها 

    def add_habit(self, name: str, frequency: str) -> Habit: #تابع ایجاد یک عادت
        if self.get_habit(name):#چک کردن نام تکراری برای عادت
            raise ValueError(f"Habit with name '{name}' already exists")

        new_habit = Habit(name, frequency)
        self.habits.append(new_habit)
        return new_habit #ایجاد یک شی از کلاس عادت 

    def remove_habit(self, name: str) -> bool: #متد حذف عادت 
        habit = self.get_habit(name)
        if habit:
            self.habits.remove(habit)
            return True
        return False

    def edit_habit(self, old_name: str, new_name: str) -> bool: #متد تغیر نام یک عادت
        habit = self.get_habit(old_name)
        if habit:
            if self.get_habit(new_name) and new_name != old_name:
                raise ValueError(f"Habit with name '{new_name}' already exists")
            habit.name = new_name
            return True
        return False

    def get_habit(self, name: str) -> Optional[Habit]: #برگردوندن عادت بر اساس نام عادت
        for habit in self.habits:
            if habit.name == name:
                return habit
        return None

    def get_all_habits(self) -> List[Habit]: # لیست همه عادت ها
        return self.habits

    def __iter__(self): # ایتریتور بذای پیمایش کلاس هبیت تراکر
        return iter(self.habits)

    def get_habits_by_frequency(self, frequency: str):
        """Generator برای فیلتر کردن عادت‌ها بر اساس فرکانس"""
        for habit in self.habits:
            if habit.frequency == frequency:
                yield habit
