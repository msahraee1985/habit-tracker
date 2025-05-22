import time
from functools import wraps

def log_execution(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print(f"▶️ تابع '{func.__name__}' در حال اجراست...")
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"✅ تابع '{func.__name__}' اجرا شد. زمان اجرا: {end - start:.4f} ثانیه")
        return result
    return wrapper
