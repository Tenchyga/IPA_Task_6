from ..intersection import intersection
from ..union import union
import pytest

@pytest.fixture
def test_data():
    return 10

def test_with_test_data(test_data):
    """
    Проверка на ввод значений фикстуры.
    """
    assert intersection(test_data, test_data, test_data, test_data, test_data, test_data, test_data,
                        test_data) == 0
    assert union(test_data, test_data, test_data, test_data, test_data, test_data, test_data,
                        test_data) == 0

def test1():
    """
    Проверка на ввод значений, который выдают положительный результат.
    """
    assert intersection(2,3,5,1,3,4,7,2) == 2
    assert union(2,3,5,1,3,4,7,2) == 12

def test2():
    """
    Проверка на ввод случайных чисел.
    """
    assert intersection(2, 3, 5, 6, 3, 4, 2, 1) == 0
    assert union(2, 3, 5, 1, 5, 4, 3, 12) == 0

def test3():
    """
    Проверка на ввод случайных чисел.
    """
    assert intersection(2,3,5,6,3,4,2,1) == 0
    assert union(2,3,5,1,5,4,3,12) == 0

def test4():
    """
    Проверка на ввод случайных чисел.
    """
    assert intersection(12, 14, 12, 14, 25, 36, 12, 15) == 0
    assert union(5, 4, 3, 5, 2, 5, 3, 3) == 0

def test5():
    """
    Проверка на ввод значений, при которых объект находится в одной точке,
    не имея какой либо территории для соприкосновения или пересечения.
    """
    assert intersection(8, 8, 8, 8, 8, 8, 8, 8) == 0
    assert union(8, 8, 8, 8, 8, 8, 8, 8) == 0