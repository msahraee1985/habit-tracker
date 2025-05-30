#فایلی که کلاس HabitTracker رو درش می سازیم این فایل و کلاسش فانکشن های لازم برای انجام عملیات روی داده های گرفته شده رد منو فراهم میکنه
from habit_tracker.models.habit import Habit
from typing import List, Optional,Iterator
from habit_tracker.utils.iterators import HabitIterator



class HabitTracker: #کلاس اصلی پروژه
    def __init__(self):
        self.habits: List[Habit] = [] # لیست خالی برای ذخیره عادت ها با تایپ هینت

    def add_habit(self, name: str, frequency: str) -> Habit: #تابع ایجاد یک عادت
        if not name.strip():  # بررسی خالی نبودن نام عادت
            raise ValueError("Habit name cannot be empty.")
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
            if self.get_habit(new_name) and new_name != old_name:#اگر اسم جدید رو قبلان داشتیم و برابر نبود با اسم قبلی تابع
                raise ValueError(f"Habit with name '{new_name}' already exists")#ولی اگه کاربر همون اسم فعلی رو دوباره زده، مشکلی نیست!
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



    def get_habits_by_frequency(self, frequency: str):
        """Generator برای فیلتر کردن عادت‌ها بر اساس فرکانس"""
        for habit in self.habits:
            if habit.frequency == frequency:
                yield habit# از yield استفاده کردیم که لیزی باشه


   
    def __iter__(self): # استفاده از کلاس ایتریتور برای زدن حلقه رو هبیت
         return HabitIterator(self.habits)
