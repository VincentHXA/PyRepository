
from src.patterns.command import SellStockOrder, BuyStockOrder, Agent, Stock

def test_command():
    stock = Stock()
    sell_stock_order = SellStockOrder(stock)
    buy_stock_order = BuyStockOrder(stock)

    agent = Agent()
    agent.place_order(sell_stock_order)
    agent.place_order(buy_stock_order)

    assert len(agent._order_quque) == 2