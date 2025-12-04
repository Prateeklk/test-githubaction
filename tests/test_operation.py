from src.maths_opeartion import add, sub, mul

def test_add():
    assert add(2,3) == 5
    assert add(7,5) == 13

def test_sub():
    assert sub(3,2) == 1
    assert sub(4,6) == -2

def test_mul():
    assert mul(2,6) == 12





