
from src.patterns.fluent_builder import Pizza

def test_fluent_builder():
    pizza = Pizza.PizzaBuilder().add_cheese().add_garlic().build()
    print(pizza)
    assert pizza.garlic
    assert pizza.extra_cheese