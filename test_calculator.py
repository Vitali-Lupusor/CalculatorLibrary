"""Unit tests for the calculator library."""

# Import local modules
import calculator


class TestCalculator:
    """Test `calculator.py` code."""

    def test_addition(self):
        """TODO."""
        assert 4 == calculator.add(2, 2)

    def test_subtraction(self):
        """TODO."""
        assert 2 == calculator.subtract(4, 2)

    def test_multiplication(self):
        """TODO."""
        assert 100 == calculator.multiply(10, 10)

    def test_division(self):
        """TODO."""
        assert 10 == calculator.divide(100, 10)
