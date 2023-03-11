from funcy import compact, select
import pytest


@pytest.fixture
def coll():  # имя фикстуры выбирается произвольно
    return ["One", True, 3, [1, "hexlet", [0]], "cat", {}, "", [], False]


@pytest.fixture
def predicat():
    return lambda x: x


# Pytest сам прокидывает результат вызова функции там, где функция указана в аргументе
# Имя параметра совпадает с именем фикстуры
def test_compact(coll):
    result = compact(coll)
    assert result == ["One", True, 3, [1, "hexlet", [0]], "cat"]


# Не важно, что предыдущий тест сделал с коллекцией
# Здесь коллекция будет новая, так как pytest вызывает coll() заново
def test_select(predicat, coll):
    result = select(predicat, coll)
    assert result == ["One", True, 3, [1, "hexlet", [0]], "cat"]
