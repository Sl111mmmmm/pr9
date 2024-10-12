numbers = []
while True:
    input_value = input("Введите число (или 'end' для завершения): ")
    if input_value == 'end':
        break
    if input_value.isdigit():
        numbers.append(int(input_value))
    else:
        print("Некорректный ввод. Введите число или 'end'.")

if numbers:
    last_element = numbers.pop() 
    numbers.insert(0, last_element) 
    print("Сдвинутый список:", numbers)
else:
    print("Список пуст.")
