
import pytest

import src.descriptors.demo_attr_desc as attr_desc


def test_attr_desc():

    @attr_desc.entity
    class LineItem:
        description = attr_desc.NonBlank()
        weight = attr_desc.Quantity()
        price = attr_desc.Quantity()

        def __init__(self, description, weight, price):
            self.description = description
            self.weight = weight
            self.price = price

        def subtotal(self):
            return self.weight * self.price

    apple = LineItem("Apple", 2.4, 3.0)

    dir_apple = dir(apple)
    assert '_Quantity#weight' in dir_apple
    assert '_NonBlank#description' in dir_apple
    assert '_Quantity#price' in dir_apple

    assert 2.4 == apple.weight
    assert 3.0 == apple.price
    apple.weight = 7.0
    assert 7.0 == apple.weight

    with pytest.raises(ValueError, match='value must be > 0') as error:
        apple.weight = -5.5

    with pytest.raises(ValueError, match='value cannot be empty or blank') as error:
        apple.description = ''
