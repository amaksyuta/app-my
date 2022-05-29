import app

def test_fibonacci():
    assert app.fib(10) == 55 # It was 54 before


def test_summ():
    assert app.summ(2, 5) == 7
    assert app.summ(3, 4) == 7
    assert app.summ(2, 4) == 6