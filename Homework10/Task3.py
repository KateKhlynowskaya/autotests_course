# Из набора тестов задания task_2 создайте один тест с параметрами, используя @pytest.mark.parametrize
# Промаркируйте 1 параметр из выборки как smokе, а 1 набор данных скипните

import pytest


def all_division(*arg1):

    division = arg1[0]
    for i in arg1[1:]:
        division /= i
    return division


@pytest.mark.parametrize("test_input, expected", [([2, 2], 1), ([100, 200], 0.5), pytest.param([100, 2], 50, marks=pytest.mark.smoke)])
def test_two_nums(test_input, expected):
    if test_input[0] == 100 and test_input[1] == 200:
        pytest.skip("invalid parameters")
    assert all_division(test_input[0], test_input[1]) == expected
