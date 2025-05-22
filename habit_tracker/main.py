#فایل main برنامه برای ساختن منوی cli ساخت ترجه و ارتباط با فایل tracker
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))) # برای مشخص کردن مسیر ایمپورت
from habit_tracker.utils.file_handler import FileHandler
from habit_tracker.models.tracker import HabitTracker # کلاس HabitTracker رو ایمپورت میکنیم 
from habit_tracker.utils.decorators import log_execution # جنریتور

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
} # برای خلاقیت بیشتر منو رو دو زبانه کردم و اینجا یک دیکشنری درست کردم که تایتل های منو ها و پرامپت های منو رو بتونم ترجمه کنم


class HabitTrackerApp: #این کلاس رابط CLI پروژه است
    def __init__(self):
        self.tracker = HabitTracker() # یک شیئ از کلاس HabitTracker رو میدیم به کلاس habittrackerapp
        self.file_handler = FileHandler()# ایجاد شیء برای مدیریت فایل JSON
        self.tracker.habits = self.file_handler.load_data()# بارگذاری اطلاعات از فایل هنگام شروع برنامه
        self.language = 'en' #cزبان پیش فرض منو رو انگلیسی قرار میدیم
        
    def t(self, key, *args):# با توجه به زبان جاری متن مناسب رو از دیکشنری ترجمه بر میگردونه
        return TRANSLATIONS[self.language]['prompts'][key].format(*args)


    @log_execution
    def display_menu(self):#این تابع مسئول چاپ منوی اصلی CLI برای کاربره — به زبان انتخاب‌شده (انگلیسی یا فارسی)
        print("\n" + "=" * 30)#چاپ خط جدا کننده در منو 
        print(TRANSLATIONS[self.language]['menu_title'])#عنوان منو
        print("=" * 30)#خط خالی
        for i, option in enumerate(TRANSLATIONS[self.language]['options'], 1):
            print(f"{i}. {option}") # پرینت گزینه های منو با کلاس enumerate خود پایتون

    def change_language(self):#متد انتخاب زبان
        print("\n1. English\n2. فارسی")
        choice = input("Select language: ").strip()# برای حذف کاراکترهای اظافه
        if choice == "1":
            self.language = 'en'
        elif choice == "2":
            self.language = 'fa'
        else:
            print("Invalid choice! Keeping current language.")

    @log_execution
    def run(self):
        while True:#انتخواب اولیه زبان در ابتدای برنامه
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

        while True:# منوی اصلی 
            self.display_menu() #تابع چاپ گزینه های منو
            choice = input(self.t('select_option')).strip() # گرفتن انتخاب کاربر 

            if choice == "1":# اگر کاربر گزینه 1 رو انتخاب کنه
                name = input(self.t('habit_name')).strip() # نام عادت رو ازش می گیریم
                freq = input(self.t('frequency')).strip().lower() # فرکانس عادت رو ازش می گیریم
                if freq in ("daily", "weekly", "روزانه", "هفتگی"): #فرکانس گرفته شده رو اعتبار سنجی میکنیم 
                    freq = "daily" if freq in ("daily", "روزانه") else "weekly" #فرکانس رو مقدار دهی میکنیم فقط به انگلیسی
                    try:#اکسپشن ولیو ارور رو هندل میکنیم
                        self.tracker.add_habit(name, freq) # از کلاس HabitTracker متد add_habit() رو صدا میزنیم
                        self.file_handler.save_data(self.tracker.habits)  # ذخیره تغییرات بعد از افزودن عادت
                        print(self.t('habit_added', name))
                    except ValueError as e:
                        print(self.t('error', str(e)))
                else:# اگر فرکانس مورد نظر نبود
                    print(self.t('invalid_frequency'))

            elif choice == "2":#مارک زدن انجام یک عادت 
                name = input(self.t('habit_name')).strip() #نام عادتی که می خوایم مارک بزنیم رو از کاربر می گیره 
                habit = self.tracker.get_habit(name)# از متد گت هبیت تلاش میکنه اون عادت رو پیدا کنه 
                if habit:
                    habit.mark_completed()# اگر پیدا کرد متد مارک کامپلیتد رو صدا میزنه
                    self.file_handler.save_data(self.tracker.habits)  # ذخیره تغییرات بعد از ثبت انجام عادت
                    print(self.t('mark_success', name))
                else:# اگر پیدا نکرد پیام خطا میده 
                    print(self.t('mark_failed', name))

            elif choice == "3":#گزینه دیدن تمام عادت های ثبت شده 
                habits = self.tracker.get_all_habits() # صدا زدن متد گت آل هبیت از هبیت ترکر
                if not habits:#اگر هبیت خالی بود
                    print(self.t('no_habits'))
                for habit in habits: #
                    streaks = habit.calculate_streaks() # از کلاس habit یک دیکشنری شامل استریک فعلی و بلندترین استریک می فرسته
                    print(f"- {habit.name} ({habit.frequency}) | Current: {streaks['current_streak']} 🔁 | Max: {streaks['longest_streak']} 🏆")
                    # نام هبیت و تکرار و بیشترین تکرار رو چاپ میکنه
            elif choice == "4":# ویرایش نام عادت
                old_name = input(self.t('edit_old')).strip()
                new_name = input(self.t('edit_new')).strip()
                try:
                    success = self.tracker.edit_habit(old_name, new_name) #متد ادیت هبیت رو از هبیت تراکرز فراخوانی میکنیم
                    if success: # اگر مقدار success true برگرده
                        self.file_handler.save_data(self.tracker.habits)  # ذخیره تغییرات بعد از ویرایش عادت
                        print(self.t('edit_success', new_name))
                    else:
                        print(self.t('edit_fail'))
                except ValueError: #هندل کردن value error
                    print(self.t('edit_fail'))

            elif choice == "5":# پاک کردن عادت 
                name = input(self.t('habit_name')).strip()# اسم عادت رو از کاربر میگیریم 
                if self.tracker.remove_habit(name): # تابع remove_habit رو کال میکنیم 
                    self.file_handler.save_data(self.tracker.habits)  # ذخیره تغییرات بعد از حذف عادت

                    print(self.t('habit_deleted', name))
                else:
                    print(self.t('not_found'))

            elif choice == "6": # تابع تغییر زبان رو که قبلن ساختیم کال میکنیم 
                self.change_language()

            elif choice == "7":# برای خروج از حلقه اصلی برنامه و چون از while True استفاده کردیم دیگه نیازی نیست از exite استفاده کنیم
                print(self.t('goodbye'))
                break

            else:
                print("❌ Invalid choice!")

if __name__ == "__main__":# همون عبارتی که تو دوره آموزش دادید که در صورتی که در فایل اصلی هستیم برنامه اجرا بشه
    app = HabitTrackerApp()
    app.run()
