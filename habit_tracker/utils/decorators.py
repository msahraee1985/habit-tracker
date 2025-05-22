import time
from functools import wraps

def log_execution(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        # چاپ نام تابع قبا از اجرا
        print(f"▶️ Executing function: '{func.__name__}'...")
        
        # ثبت زمان شروع
        start = time.time()
        
        # اجرای تابع
        result = func(*args, **kwargs)
        
        #ثبت زمان پایان
        end = time.time()
        
        # چاپ نام تابع و زمان اجراش 
        print(f"✅ Finished '{func.__name__}'. Execution time: {end - start:.4f} seconds")
        
        #برگرداندن نتیجه 
        return result

    return wrapper

