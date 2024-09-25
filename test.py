import unittest


def count_common_elements(lists):
    # Используем множество для нахождения общих элементов
    common_elements = set(lists[0])

    # Проходим по всем остальным спискам и пересекаем с общими элементами
    for lst in lists[1:]:
        common_elements.intersection_update(lst)

    return len(common_elements)


class TestCountCommonElements(unittest.TestCase):

    def test_common_elements(self):
        self.assertEqual(count_common_elements([['a', 'b', 'c'], ['b', 'c', 'd'], ['b', 'c']]), 2)  # Общие: 'b', 'c'
        self.assertEqual(count_common_elements([['1', '2', '3'], ['4', '5'], ['6', '7']]), 0)  # Нет общих элементов
        self.assertEqual(count_common_elements([['apple', 'banana', 'cherry'], ['banana', 'cherry'], ['banana']]),
                         1)  # Общий: 'banana'
        self.assertEqual(count_common_elements([['cat', 'dog', 'mouse'], ['dog', 'cat'], ['cat', 'dog']]),
                         2)  # Общие: 'dog', 'cat'
        self.assertEqual(count_common_elements([['x', 'y'], ['y', 'z'], ['z', 'x']]), 0)  # Нет общих элементов
        self.assertEqual(count_common_elements([['a', 'b', 'c'], ['c', 'd', 'c'], ['c', 'e']]), 1)  # Общий: 'c'

    def test_single_list(self):
        self.assertEqual(count_common_elements([['x', 'y', 'z']]), 3)  # Все элементы считаются

    def test_empty_lists(self):
        self.assertEqual(count_common_elements([[], []]), 0)  # Пустые списки

    def test_mixed_types(self):
        self.assertEqual(count_common_elements([[1, 2, 3], [2, 3, 4], [3, 4, 5]]), 1)  # Общий: 3
        self.assertEqual(count_common_elements([[1, 'a'], ['a', 2], [2, 3]]), 0)  # Нет общих


if __name__ == '__main__':
    unittest.main()
