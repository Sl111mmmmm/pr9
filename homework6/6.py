numbers = [1, 2, 3, 500, 1, -100]
print("список:", numbers)

min_index = numbers.index(min(numbers))
max_index = numbers.index(max(numbers))

numbers[min_index], numbers[max_index] = numbers[max_index], numbers[min_index]

print("Изменённый список:", numbers)
