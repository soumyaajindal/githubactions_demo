from app import get_weather, add, divide

def test_get_weather():
    result = get_weather.invoke("New York")
    assert "sunny" in result

def test_add():
    result = add(1, 2)
    assert result == 3

def test_divide():
    result = divide(10, 2)
    assert result == 5