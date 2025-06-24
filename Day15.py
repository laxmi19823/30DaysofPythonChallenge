import time

def log_execution_time(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        print(f"⏱️ Starting '{func.__name__}'...")
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f"✅ Finished '{func.__name__}' in {end_time - start_time:.4f} seconds\n")
        return result
    return wrapper

@log_execution_time
def process_data():
    time.sleep(2)  
    print("📊 Data processed successfully!")

process_data()
