import os
import importlib.util
import inspect

scraper_dir = os.path.join(os.path.dirname(__file__), "scraper", "working")
results = []

for filename in os.listdir(scraper_dir):
    if filename.endswith(".py"):
        path = os.path.join(scraper_dir, filename)
        module_name = filename[:-3]

        spec = importlib.util.spec_from_file_location(module_name, path)
        module = importlib.util.module_from_spec(spec)

        try:
            spec.loader.exec_module(module)
            scrape_funcs = [
                func for name, func in inspect.getmembers(module, inspect.isfunction)
                if name.startswith("scrape_")
            ]
            if not scrape_funcs:
                results.append((filename, "❌ No scrape_ function found"))
            else:
                for func in scrape_funcs:
                    try:
                        result = func()
                        if not isinstance(result, list) or len(result) == 0:
                            results.append((filename, "⚠️ Returned empty or non-list"))
                        else:
                            results.append((filename, f"✅ Headlines: {len(result)}"))
                    except Exception as e:
                        results.append((filename, f"❌ Error on run: {e}"))
        except Exception as e:
            results.append((filename, f"❌ Import error: {e}"))

print("\n=== SCRAPER AUDIT RESULTS ===")
for file, status in results:
    print(f"{file:<25} {status}")
