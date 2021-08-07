from hello import add, sayHello

def test_sayHello():
    assert "Hello" == sayHello()

def test_add():
    assert 2 == add(1, 1)
