# Дан текстовый файл test_file/task1_data.txt
# Он содержит текст, в словах которого есть цифры.
# Необходимо удалить все цифры и записать получившийся текст в файл test_file/task1_answer.txt

with open('test_file/task1_data.txt', mode='r', encoding='utf-8') as old_file:
    new = ''
    f = old_file.read()
    for i in f:
        if not i.isdigit():
            new += i
with open('test_file/task1_answer.txt', mode='w', encoding='utf-8') as new_file:
    new_file.write(new)

# Ниже НИЧЕГО НЕ НАДО ИЗМЕНЯТЬ


with open("test_file/task1_answer.txt", 'r', encoding='utf-8') as file1:
    with open("test_file/task1_ethalon.txt", 'r', encoding='utf-8') as file2:
        answer = file1.readlines()
        ethalon = file2.readlines()
        if answer != ethalon:
            print(answer)
            print(ethalon)
        assert answer == ethalon, "Файл ответа не совпадает с эталонном"
print('Всё ок')