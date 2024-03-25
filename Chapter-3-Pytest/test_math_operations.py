# test_math_operations.py
import pytest
from math_operations import MathOperations

class TestMathOperations:
    @pytest.fixture
    def math_ops(self):
        return MathOperations()

    def test_addition(self, math_ops):
        assert math_ops.add(3, 5) == 8
        assert math_ops.add(-1, 1) == 0
        assert math_ops.add(0, 0) == 0

    def test_subtraction(self, math_ops):
        assert math_ops.subtract(5, 3) == 2
        assert math_ops.subtract(-1, -1) == 0
        assert math_ops.subtract(0, 0) == 0

    def test_multiplication(self, math_ops):
        assert math_ops.multiply(2, 3) == 6
        assert math_ops.multiply(-2, 3) == -6
        assert math_ops.multiply(0, 5) == 0

    def test_division(self, math_ops):
        assert math_ops.divide(6, 3) == 2
        assert math_ops.divide(5, 2) == pytest.approx(2.5)
        with pytest.raises(ValueError):
            math_ops.divide(10, 0)
