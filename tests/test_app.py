import app


def test_add():
    assert app.add(3, 4) == 7
    assert app.add(3.5, 4) == 7
    assert app.add(3.9, 4) == 7
    assert app.add(3.9, 4.1) == 8
