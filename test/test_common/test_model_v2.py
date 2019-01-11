import common.model_v2 as model

@model.entity
class LineItem:
    description = model.NonBlank()
    weight = model.Quantity()
    price = model.Quantity()

    def __init__(self, description, weight, price):
        self.description = description
        self.weight = weight
        self.price = price

    def subtotal(self):
        return self.weight * self.price

if __name__ == '__main__':
    apple = LineItem("Apple", 2.4, 3.0)

    print(dir(apple))

    print(apple.subtotal())

    apple.weight = 7.0
    print(apple.subtotal())

    try:
        apple.weight = -5.5
    except ValueError as ve:
        print(ve)

    try:
        apple.description = ""
    except ValueError as ve:
        print(ve)

    for key, attr in apple.__class__.__dict__.items():
        print('{}-{}: {}-{}'.format(key, type(key), attr, type(attr)))

