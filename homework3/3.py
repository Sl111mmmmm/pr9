list = []


while True:
    user_input = input("Введите число (или 'end' для завершения): ")
    if user_input.lower() == 'end':
        break


    if user_input.isdigit() or (user_input.startswith('-') and user_input[1:].isdigit()):
        number = int(user_input)
        list.append(number)
    else:
        print("Пожалуйста, введите корректное целое число.")


odd_numbers = [num for num in list if num % 2 != 0]
print("Нечетные элементы списка:", odd_numbers)
