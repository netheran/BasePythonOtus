"""
Домашнее задание №1
Функции и структуры данных
"""


def power_numbers(*num_list):
    """
    функция, которая принимает N целых чисел,
    и возвращает список квадратов этих чисел
    >>> power_numbers(1, 2, 5, 7)
    [1, 4, 25, 49]
    """
    result = []
    for item in num_list:
        result.append(item ** 2)
    return result

# filter types
ODD = "odd"
EVEN = "even"
PRIME = "prime"


def filter_numbers(num_list, ftype):
    """
    функция, которая на вход принимает список из целых чисел,
    и возвращает только чётные/нечётные/простые числа
    (выбор производится передачей дополнительного аргумента)

    >>> filter_numbers([1, 2, 3], ODD)
    [1, 3]
    >>> filter_numbers([2, 3, 4, 5], EVEN)
    [2, 4]
    """
    result = []
    if ftype == ODD:
        result = list(filter(lambda x: x % 2, num_list))

    elif ftype == EVEN:
        result = list(filter(lambda x: x % 2 == 0, num_list))

    elif ftype == PRIME:
        result = list(filter(lambda y: (lambda x: all(x % i != 0 for i in range(2, int(x ** 0.5)+1)), num_list)))

    return result



