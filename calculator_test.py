import calculator as c
import pytest

# this function performs tests for all the operations
def test_operations():
    assert float(c.parse_input("1 + 2")) == pytest.approx(3)
    assert float(c.parse_input("5 + -2")) == pytest.approx(3)
    assert float(c.parse_input("-1 + 4")) == pytest.approx(3)
    
    assert c.parse_input("1+ 2") == 'input is invalid'
    assert c.parse_input("1 +2") == 'input is invalid'
    assert c.parse_input("1+2") == 'input is invalid'

    assert float(c.parse_input("1 / 2")) == pytest.approx(0.5)
    assert float(c.parse_input("1.0 / 2")) == pytest.approx(0.5)
    assert float(c.parse_input("1 / 2.0")) == pytest.approx(0.5)
    assert float(c.parse_input("100 / 1")) == pytest.approx(100)

    assert float(c.parse_input("1 * 2")) == pytest.approx(2)
    assert float(c.parse_input("2.5 * 2")) == pytest.approx(5)
    assert float(c.parse_input("2.5 * 2.0")) == pytest.approx(5)

    assert float(c.parse_input("2 ^ 4")) == pytest.approx(16)
    assert float(c.parse_input("2.0 ^ 4.0")) == pytest.approx(16)
    assert float(c.parse_input("4 ^ 2")) == pytest.approx(16)

    assert float(c.parse_input("2 log 4")) == pytest.approx(0.5)
    assert float(c.parse_input("10 log 10")) == pytest.approx(1)