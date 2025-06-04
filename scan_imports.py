import os
import re

PROJECT_ROOT = "."  # Or set to full path like "./PycharmProjects/YourProject"
target_dir = os.path.join(PROJECT_ROOT)

pattern = re.compile(r'^from scraper\.(?!working)(\w+)\s+import\s+(scrape_\w+)', re.MULTILINE)

for subdir, _, files in os.walk(target_dir):
    for file in files:
        if file.endswith(".py"):
            path = os.path.join(subdir, file)
            with open(path, "r", encoding="utf-8") as f:
                content = f.read()
                matches = pattern.findall(content)
                if matches:
                    print(f"\n🔍 {path}")
                    for match in matches:
                        print(f"  - from scraper.{match[0]} import {match[1]}")

