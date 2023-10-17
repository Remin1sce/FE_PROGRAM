def calculate_highest_average(levels):
    n = len(levels)
    if n < 5:
        return "Insufficient data"

    max_average = float('-inf')
    for i in range(n - 4):
        average = sum(levels[i:i+5]) / 5
        max_average = max(max_average, average)

    return round(max_average, 2)

# Read input
water_levels = []
while True:
    try:
        line = input()
        if line == "$":
            break
        water_level = float(line)
        water_levels.append(water_level)
    except EOFError:
        break

# Calculate and print the highest average
result = calculate_highest_average(water_levels)
print(result)