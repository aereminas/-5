import random
import math
import statistics

def analyze_data(num_elements=100, lower_bound=1, upper_bound=100):
    data_points = []
    for _ in range(num_elements):
        value = random.randint(lower_bound, upper_bound)
        data_points.append(value)

    average = statistics.mean(data_points)
    median_value = statistics.median(data_points)
    standard_deviation = statistics.stdev(data_points)
    total_sum = sum(data_points)
    sqrt_of_sum = round(math.sqrt(total_sum), 2)

    print(f"Среднее значение: {average:.2f}, Медиана: {median_value:.2f}, Стандартное отклонение: {standard_deviation:.2f}, Корень из суммы: {sqrt_of_sum:.2f}")

analyze_data()

