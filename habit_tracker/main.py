#فایل main برنامه برای ساختن منوی cli 
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from habit_tracker.models.tracker import HabitTracker

TRANSLATIONS = {
    'en': {
        'menu_title': "HABIT TRACKER MENU",
        'options': [
            "Add New Habit",
            "Mark Habit as Completed",
            "View All Habits",
            "Edit Habit",
            "Delete Habit",
            "Change Language",
            "Exit"
        ],
        'prompts': {
            'select_option': "Select an option (1-7): ",
            'habit_name': "Enter habit name: ",
            'frequency': "Frequency (daily/weekly): ",
            'invalid_frequency': "Invalid frequency! Use 'daily' or 'weekly'",
            'habit_added': "✅ Habit '{}' added!",
            'error': "❌ Error: {}",
            'no_habits': "No habits found!",
            'habit_deleted': "✅ Habit '{}' deleted!",
            'not_found': "❌ Habit not found!",
            'goodbye': "Goodbye! 👋",
            'mark_success': "✅ Habit '{}' marked as completed today!",
            'mark_failed': "❌ Habit '{}' not found.",
            'edit_old': "Enter current habit name: ",
            'edit_new': "Enter new name: ",
            'edit_success': "✅ Habit renamed to '{}'",
            'edit_fail': "❌ Habit not found or name already taken."
        }
    },
    'fa': {
        'menu_title': "منوی ردیابی عادت‌ها",
        'options': [
            "اضافه کردن عادت جدید",
            "ثبت تکمیل عادت",
            "مشاهده تمام عادت‌ها",
            "ویرایش عادت",
            "حذف عادت",
            "تغییر زبان",
            "خروج"
        ],
        'prompts': {
            'select_option': "گزینه مورد نظر را انتخاب کنید (۷-۱): ",
            'habit_name': "نام عادت را وارد کنید: ",
            'frequency': "تناوب (روزانه/هفتگی): ",
            'invalid_frequency': "مقدار نامعتبر! فقط 'روزانه' یا 'هفتگی' مجاز است",
            'habit_added': "✅ عادت '{}' اضافه شد!",
            'error': "❌ خطا: {}",
            'no_habits': "عادتی یافت نشد!",
            'habit_deleted': "✅ عادت '{}' حذف شد!",
            'not_found': "❌ عادت پیدا نشد!",
            'goodbye': "خدانگهدار! 👋",
            'mark_success': "✅ عادت '{}' برای امروز ثبت شد!",
            'mark_failed': "❌ عادت '{}' پیدا نشد.",
            'edit_old': "نام فعلی عادت را وارد کنید: ",
            'edit_new': "نام جدید عادت را وارد کنید: ",
            'edit_success': "✅ نام عادت به '{}' تغییر یافت.",
            'edit_fail': "❌ عادت پیدا نشد یا نام جدید تکراری است."
        }
    }
}

class HabitTrackerApp:
    def __init__(self):
        self.tracker = HabitTracker()
        self.language = 'en'

    def t(self, key, *args):
        return TRANSLATIONS[self.language]['prompts'][key].format(*args)

    def display_menu(self):
        print("\n" + "=" * 30)
        print(TRANSLATIONS[self.language]['menu_title'])
        print("=" * 30)
        for i, option in enumerate(TRANSLATIONS[self.language]['options'], 1):
            print(f"{i}. {option}")

    def change_language(self):
        print("\n1. English\n2. فارسی")
        choice = input("Select language: ").strip()
        if choice == "1":
            self.language = 'en'
        elif choice == "2":
            self.language = 'fa'
        else:
            print("Invalid choice! Keeping current language.")

    def run(self):
        while True:
            print("\n🌐 Select Language | انتخاب زبان")
            print("1. English")
            print("2. فارسی")
            choice = input("➤ Your choice: ").strip()
            if choice == "1":
                self.language = 'en'
                break
            elif choice == "2":
                self.language = 'fa'
                break
            else:
                print("❌ Invalid choice! / گزینه نامعتبر!")

        while True:
            self.display_menu()
            choice = input(self.t('select_option')).strip()

            if choice == "1":
                name = input(self.t('habit_name')).strip()
                freq = input(self.t('frequency')).strip().lower()
                if freq in ("daily", "weekly", "روزانه", "هفتگی"):
                    freq = "daily" if freq in ("daily", "روزانه") else "weekly"
                    try:
                        self.tracker.add_habit(name, freq)
                        print(self.t('habit_added', name))
                    except ValueError as e:
                        print(self.t('error', str(e)))
                else:
                    print(self.t('invalid_frequency'))

            elif choice == "2":
                name = input(self.t('habit_name')).strip()
                habit = self.tracker.get_habit(name)
                if habit:
                    habit.mark_completed()
                    print(self.t('mark_success', name))
                else:
                    print(self.t('mark_failed', name))

            elif choice == "3":
                habits = self.tracker.get_all_habits()
                if not habits:
                    print(self.t('no_habits'))
                for habit in habits:
                    streaks = habit.calculate_streaks()
                    print(f"- {habit.name} ({habit.frequency}) | Current: {streaks['current_streak']} 🔁 | Max: {streaks['longest_streak']} 🏆")

            elif choice == "4":
                old_name = input(self.t('edit_old')).strip()
                new_name = input(self.t('edit_new')).strip()
                try:
                    success = self.tracker.edit_habit(old_name, new_name)
                    if success:
                        print(self.t('edit_success', new_name))
                    else:
                        print(self.t('edit_fail'))
                except ValueError:
                    print(self.t('edit_fail'))

            elif choice == "5":
                name = input(self.t('habit_name')).strip()
                if self.tracker.remove_habit(name):
                    print(self.t('habit_deleted', name))
                else:
                    print(self.t('not_found'))

            elif choice == "6":
                self.change_language()

            elif choice == "7":
                print(self.t('goodbye'))
                break

            else:
                print("❌ Invalid choice!")

if __name__ == "__main__":
    app = HabitTrackerApp()
    app.run()
