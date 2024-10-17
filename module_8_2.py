def personal_sum(*numbers):
    result = 0
    incorrect_data = 0
    correct_data = 0
    for i in numbers:
        if isinstance(i, (int, float)):
            result += i
            correct_data += 1
        elif isinstance(i, (list,tuple)):
            for k in i:
                if isinstance(k,(int, float)):
                    result += k
                    correct_data += 1
                else:
                    incorrect_data += 1
        else:
            incorrect_data += 1
        return result, incorrect_data, correct_data


def calculate_average(*numbers):
    try:
        result, incorrect_data, correct_data = personal_sum(*numbers)
        return result / correct_data
    except ZeroDivisionError:
        print(f'В numbers записан некорректный тип данных')
        return 0



print(f'Результат 1: {calculate_average("1, 2, 3")}') # Строка перебирается, но каждый символ - строковый тип
print(f'Результат 2: {calculate_average([1, "Строка", 3, "Ещё Строка"])}') # Учитываются только 1 и 3
print(f'Результат 3: {calculate_average(567)}') # Передана не коллекция
print(f'Результат 4: {calculate_average([42, 15, 36, 13])}') # Всё должно работать
