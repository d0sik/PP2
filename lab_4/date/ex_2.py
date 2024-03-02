#Write a Python program to print yesterday, today, tomorrow.

from datetime import datetime, timedelta

current_date = datetime.now()

yesterday_date = current_date - timedelta(days=1)
tomorrow_date = current_date + timedelta(days=1)

yesterday_date_str = yesterday_date.strftime("%Y-%m-%d")
current_date_str = current_date.strftime("%Y-%m-%d")
tomorrow_date_str = tomorrow_date.strftime("%Y-%m-%d")

print(f"Yesterday date: {yesterday_date_str}")
print(f"Current date: {current_date_str}")
print(f"Tomorrow date: {tomorrow_date_str}")