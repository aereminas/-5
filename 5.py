import random
import datetime
import array

def generate_timestamp():
    """Generates a random timestamp within the last 5 years."""
    current_time = datetime.datetime.now().timestamp()
    past_time = current_time - 5 × 365 × 24 * 3600
    return int(random.uniform(past_time, current_time))

timestamps = array.array('q')
for _ in range(10):
    timestamps.append(generate_timestamp())

for i in range(len(timestamps) - 1):
    timestamp1 = timestamps[i]
    timestamp2 = timestamps[i + 1]
    date1 = datetime.datetime.fromtimestamp(timestamp1).date()
    date2 = datetime.datetime.fromtimestamp(timestamp2).date()

    time_difference = abs((date1 - date2).days)
    print(f"Разница между {date1} и {date2}: {time_difference} дней")
