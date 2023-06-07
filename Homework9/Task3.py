

# Дан файл test_file/task_3.txt можно считать, что это запись покупок в магазине, где указана только цена товара
# В каждой строке файла записана цена товара.
# Покупки (т.е. несколько подряд идущих цен) разделены пустой строкой
# Нужно найти сумму трёх самых дорогих покупок, которые запишутся в переменную three_most_expensive_purchases

# Здесь пишем код
with open("test_file/task_3.txt", "r") as file:
    lines = file.readlines()

sums_purchases = []
curr_p = []

for line in lines:
    num = line.strip()
    if num.isnumeric():
        curr_p.append(int(num))
    else:
        sums_purchases.append(sum(curr_p))
        curr_p = []

three_most_expensive_purchases = sum(sorted(sums_purchases, reverse=True)[:3])

assert three_most_expensive_purchases == 202346