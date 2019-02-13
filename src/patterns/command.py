
from abc import ABCMeta, abstractmethod


class Order(metaclass=ABCMeta):

    def __init__(self, stock):
        self.stock = stock

    @abstractmethod
    def execute(self):
        pass


class BuyStockOrder(Order):
    def execute(self):
        self.stock.buy()


class SellStockOrder(Order):
    def execute(self):
        self.stock.sell()


class Stock:
    def buy(self):
        print('You will buy some stock')

    def sell(self):
        print('You will sell some stock')


class Agent:
    def __init__(self):
        self._order_quque = []

    def place_order(self, order):
        self._order_quque.append(order)
        order.execute()
