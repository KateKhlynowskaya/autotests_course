# Напишите 5 тестов на функцию all_division. Обязательно должен быть тест деления на ноль.
# Промаркируйте часть тестов. Например, smoke.
# В консоли с помощью pytest сделайте вызов:
# 1) Всех тестов
# 2) Только с маркером smoke
# 3) По маске. Выберите такую маску, чтобы под неё подпадали не все тесты, но больше одного
# Пришлите на проверку файл с тестами и скрины с вызовами и их результаты

import pytest


def all_division(*arg1):

    division = arg1[0]
    for i in arg1[1:]:
        division /= i
    return division


@pytest.mark.smoke
def test_two_nums():
    result = all_division(100, 2)
    assert result == 50


@pytest.mark.smoke
def test_multiple_nums():
    result = all_division(2, 2, 2, 2, 2, 50, 100, 20)
    assert result == 1.25e-06


@pytest.mark.smoke
def test_negative_nums():
    result = all_division(-10, -20)
    assert result == 0.5


@pytest.mark.custom
def test_nums_and_letter():
    try:
        all_division(20, 30, 20, 23, 234234, 234, 234234, "2")
    except Exception as e:
        assert isinstance(e, TypeError)


@pytest.mark.custom
def test_zero():
    try:
        all_division(2, 0)
    except Exception as e:
        assert isinstance(e, ZeroDivisionError)

