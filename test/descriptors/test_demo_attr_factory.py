
import pytest

import src.descriptors.demo_attr_factory as attr_factory


def test_attr_desc():
    class LineItem:
        description = attr_factory.quantity()
        weight = attr_factory.quantity()
        price = attr_factory.quantity()

        def __init__(self, description, weight, price):
            self.description = description
            self.weight = weight
            self.price = price

        def subtotal(self):
            return self.weight * self.price

    apple = LineItem("Apple", 2.4, 3.0)

    assert 2.4 == apple.weight
    assert 3.0 == apple.price
    apple.weight = 7.0
    assert 7.0 == apple.weight

    with pytest.raises(ValueError, match='value must be > 0') as error:
        apple.weight = -5.5

    with pytest.raises(ValueError, match='value cannot be empty or blank') as error:
        apple.description = ''

    with pytest.raises(ValueError, match='unsupported data type') as error:
        apple.weight = []
