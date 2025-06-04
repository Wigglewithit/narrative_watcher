import os
import shutil
import importlib.util
import inspect
import concurrent.futures
from datetime import datetime

scraper_dir = "scraper/working"
todo_dir = "scraper/todo"
os.makedirs(todo_dir, exist_ok=True)
moved = []

def log_status(message):
    timestamp = datetime.now().strftime("%H:%M:%S")
    print(f"[{timestamp}] {message}")

def run_with_timeout(func, timeout=6):
    with concurrent.futures.ThreadPoolExecutor(max_workers=1) as executor:
        future = executor.submit(func)
        try:
            return future.result(timeout=timeout)
        except Exception:
            return None

log_status("🚀 Starting audit and cleanup of scrapers...\n")

for filename in os.listdir(scraper_dir):
    if not filename.endswith(".py"):
        continue

    filepath = os.path.join(scraper_dir, filename)
    module_name = filename[:-3]

    log_status(f"⏳ Checking {filename}...")

    spec = importlib.util.spec_from_file_location(module_name, filepath)
    module = importlib.util.module_from_spec(spec)

    try:
        spec.loader.exec_module(module)
        scrape_funcs = [
            func for name, func in inspect.getmembers(module, inspect.isfunction)
            if name.startswith("scrape_")
        ]

        if not scrape_funcs:
            reason = "❌ No scrape_ function"
        else:
            result = run_with_timeout(scrape_funcs[0], timeout=6)
            if not isinstance(result, list) or len(result) == 0:
                reason = "⚠️ Empty or invalid result"
            else:
                log_status(f"✅ {filename} looks good.\n")
                continue  # Good file

        # Move broken file
        shutil.move(filepath, os.path.join(todo_dir, filename))
        moved.append((filename, reason))
        log_status(f"📦 Moved {filename} → {reason}\n")

    except Exception as e:
        shutil.move(filepath, os.path.join(todo_dir, filename))
        moved.append((filename, f"❌ Error on import: {e}"))
        log_status(f"📦 Moved {filename} → Import error\n")

# Final Summary
log_status("✅ Audit complete.\n")
print("=== Moved to scraper/todo/ ===")
for file, reason in moved:
    print(f"{file:<25} → {reason}")
