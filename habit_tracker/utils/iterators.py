

class HabitIterator:
    """
    یک کلاس Iterator سفارشی برای پیمایش روی لیست عادت‌ها.
    """

    def __init__(self, habits):
        self._habits = habits
        self._index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self._index < len(self._habits):
            habit = self._habits[self._index]
            self._index += 1
            return habit
        else:
            raise StopIteration


def completed_dates_generator(habit):
    """
    یک generator ساده برای بازگرداندن تاریخ‌های انجام‌شده یک عادت.
    """
    for d in habit.completion_dates:
        yield d
