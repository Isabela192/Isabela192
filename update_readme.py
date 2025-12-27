import re
from datetime import datetime


def update_readme():
    days_left = (datetime(2026, 1, 1) - datetime.now()).days

    with open("README.md", "r", encoding="utf-8") as file:
        content = file.read()

    updated_content = re.sub(r"(There are )\d+( days remaining in 2025)", rf"\g<1>{days_left}\g<2>", content, count=1)

    with open("README.md", "w", encoding="utf-8") as file:
        file.write(updated_content)
