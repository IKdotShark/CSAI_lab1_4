def count_common_elements(lists):
    # Используем множество для нахождения общих элементов
    common_elements = set(lists[0])

    # Проходим по всем остальным спискам и пересекаем с общими элементами
    for lst in lists[1:]:
        common_elements.intersection_update(lst)

    return len(common_elements)


# Ввод количества списков
n = int(input("Введите количество списков: "))

# Ввод списков
lists = []
for i in range(n):
    lst = input(f"Введите элементы списка {i + 1}, разделенные пробелом: ").split()
    lists.append(lst)

# Вызов функции для подсчета общих элементов
result = count_common_elements(lists)

# Вывод результата
print(f"Количество одинаковых элементов во всех списках: {result}")
