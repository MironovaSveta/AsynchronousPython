def sum_numbers_classic(numbers):
    total = 0
    for num in numbers:
        total += num
    return total

numbers = [1, 2, 3, 4, 5]
result = sum_numbers_classic(numbers)
print("Sum of numbers (classic):", result)