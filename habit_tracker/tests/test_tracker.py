
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from datetime import date, timedelta
from habit_tracker.models.habit import Habit
from habit_tracker.models.tracker import HabitTracker
import pytest
def test_add_habit():# تست اظافه کردن عادت
    tracker = HabitTracker()
    tracker.add_habit("Read", "daily")
    assert len(tracker.habits) == 1
    assert tracker.habits[0].name == "Read"

def test_duplicate_habit():#تست عادت تکراری
    tracker = HabitTracker()
    tracker.add_habit("Read", "daily")
    try:
        tracker.add_habit("Read", "daily")
        assert False, "Expected ValueError"
    except ValueError:
        assert True

def test_mark_completed():#تست مارک کردن عادت انجام شده
    tracker = HabitTracker()
    habit = tracker.add_habit("Exercise", "daily")
    habit.mark_completed()
    assert len(habit.completion_dates) == 1
    assert habit.completion_dates[0] == date.today()

def test_streak_calculation_daily(): #  روزانه تست محاسبه استریک
    habit = Habit("Meditation", "daily")
    
   
    today = date.today() # فرض کنیم کاربر در ۳ روز اخیر پشت‌سر هم عادت رو انجام داده
    habit.completion_dates = [
        today - timedelta(days=2),
        today - timedelta(days=1),
        today
    ]

    result = habit.calculate_streaks()

    assert result["current_streak"] == 3
    assert result["longest_streak"] == 3

def test_streak_calculation_weekly():# تست محاسبه استریک هفتگی 
    habit = Habit("Gym", "weekly")
    today = date.today()
    habit.completion_dates = [
        today - timedelta(days=14),  # دو هفته پیش
        today - timedelta(days=7),   # هفته پیش
        today                        # این هفته
    ]
    result = habit.calculate_streaks()
    assert result["current_streak"] == 3
    assert result["longest_streak"] == 3

def test_remove_habit(): # تست تابع حذف عادت
    tracker = HabitTracker()
    tracker.add_habit("Sleep Early", "daily")
    removed = tracker.remove_habit("Sleep Early")
    assert removed is True
    assert tracker.get_habit("Sleep Early") is None

def test_edit_habit():# تست تابع ادیت عادت
    tracker = HabitTracker()
    tracker.add_habit("Walk", "daily")
    success = tracker.edit_habit("Walk", "Morning Walk")
    assert success is True
    assert tracker.get_habit("Walk") is None
    assert tracker.get_habit("Morning Walk") is not None

def test_edit_to_duplicate_name():# تست عادت تکراری در هنگام ادیت عادت
    tracker = HabitTracker()
    tracker.add_habit("Read", "daily")
    tracker.add_habit("Study", "daily")
    with pytest.raises(ValueError):
        tracker.edit_habit("Study", "Read")  # چون "Read" وجود داره
