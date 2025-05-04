import random
import datetime

def generate_date():
    current_year = datetime.datetime.now().year
    year = random.randint(current_year - 5, current_year)
    month = random.randint(1, 12)
    day = random.randint(1, 28)  # Ensure valid date
    return datetime.date(year, month, day)

date_list = []
for _ in range(10):
    date_list.append(generate_date())

for i in range(len(date_list) - 1):
    date1 = date_list[i]
    date2 = date_list[i + 1]
    difference = abs((date1 - date2).days)
    print(f"Разница между {date1} и {date2}: {difference} суток")
