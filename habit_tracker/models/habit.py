# برای مدل کردن عادتها و تعیین فرکانس انجام آنها محاسبه استریک و نشان دادن طولانی ترین استریک
from datetime import date
from typing import List, Dict

class Habit:  #تعریف کلاس اصلی عادت
    def __init__(self, name: str, frequency: str):
        self.name = name
        self.frequency = frequency.lower() # ساخت فرکانس و تبدیلش به حروف کوچک برای جلوگیری از بروز مغایرت
        self.completion_dates: List[date] = [] # ایجاد یک لیست برای جمع آوری تاریخ هایی که عر عادت انجام میشه

        if self.frequency not in ('daily', 'weekly'):
            raise ValueError("Frequency must be either 'daily' or 'weekly'")# پرتاب خطا در صورت رعایت نکردن فرمت فرکانس
                               
    def mark_completed(self, completion_date: date = date.today()) -> None: #تعریف متد برای اختصاص تاریخ به انجام شدن یک عادت

        if completion_date not in self.completion_dates:
            self.completion_dates.append(completion_date)
            self.completion_dates.sort()# ثبت تاریخی که قبلا ثبت نشده باشه و مرتب کردنش

    def calculate_streaks(self) -> Dict[str, int]: #متد محاسبه استریک فعلی و بیشترین استریک
        if not self.completion_dates:
            return {"current_streak": 0, "longest_streak": 0} #اگه هنوز هیچ تاریخی ثبت نشده، هر دو صفر هستند.

        current_streak = 1
        longest_streak = 1
        streaks = []

        for i in range(1, len(self.completion_dates)):#محاسبه فاصله به تعداد روز بین تکرارعادت
            delta = (self.completion_dates[i] - self.completion_dates[i-1]).days

            if (self.frequency == 'daily' and delta == 1) or \
               (self.frequency == 'weekly' and 1 <= delta <= 7):#محاسبه اینکه تکرار عادن مطابق الگوی هفتگی و روزانه هست 
                
                current_streak += 1 #افزایش استریک فعلی
                longest_streak = max(longest_streak, current_streak)# محاسبه بلندترین استریک
            else:
                streaks.append(current_streak)
                current_streak = 1 # اگر مطابق الگوی روزانه یا هفتگی نبود استریک فعلی بسته و از اول شروع میشه

        return {
            "current_streak": current_streak,
            "longest_streak": max(streaks + [longest_streak]) if streaks else longest_streak
        }# در پایان استریک فعلی و بیشترین استریک رو برمیگردونه

    def __str__(self) -> str:
        return f"Habit: {self.name} ({self.frequency})"# مجیک متد برای نشون دادن نام عادت و تکرارش

    def __repr__(self) -> str:
        return f"Habit(name='{self.name}', frequency='{self.frequency}')"# مجیک متد ریپرزنتیشن برای نشان دادن جزئیات بیشتر

    def __eq__(self, other) -> bool:# مجیک متد برای برابر قرار دادن دو عادت اگر نام و تکرارشون یکی باشه
        if not isinstance(other, Habit):
            return False
        return self.name == other.name and self.frequency == other.frequency
