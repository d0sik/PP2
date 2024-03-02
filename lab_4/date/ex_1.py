#Write a Python program to subtract five days from current date.
from datetime import datetime, timedelta

current_date = datetime.now()

new_date = current_date - timedelta(days=5)

current_date_str = current_date.strftime("%Y-%m-%d")
new_date_str = new_date.strftime("%Y-%m-%d")

print(f"Current date: {current_date_str}")
print(f"Date five days ago: {new_date_str}")