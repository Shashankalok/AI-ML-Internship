from tools.calculator import calculator_basic

def test_addition():
    assert calculator_basic("2+2") == "4"

def test_invalid_input():
    assert calculator_basic("abc") == "error"