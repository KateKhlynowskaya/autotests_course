# Напишите функцию modification(lst), которая принимает список и меняет местами его первый и последний элемент.
# В исходном списке минимум 2 элемента.

def modification(lst):
    lst[0][-1] = lst[-1][0]
    return lst


# Дан список из 7 различных элементов. Используя функции (не использовать цикл), необходимо найти:
# минимальный и максимальный элементы списка;
# сумму и среднее арифметическое с округлением до 2 знаков после запятой;

def get_list_info(lst):
    min_elem = min(lst)
    max_elem = max(lst)
    sum_list = sum(lst)
    average = round(sum(lst)/len(lst), 2)
    return min_elem, max_elem, sum_list, average


# Дан список. Найдите сумму элементом с четными индексами

def even_sum(lst):
    even_indices = lst[0::2]
    sum_list = sum(even_indices)
    return sum_list
