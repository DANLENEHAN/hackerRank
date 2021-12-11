"""
    RANDOM STUFF
"""

import sys

if __name__ == '__main__':
    args = sys.argv[1:]


class VendingMachine:

    num_items = 0
    item_cost = 0

    def __init__(self, num_items, item_cost) -> None:
        self.num_items = num_items
        self.item_cost = item_cost


    def reduce_stock(self, items_bought):
        self.num_items -= items_bought


    def buy_items(self, requested_amount, money):

        cost_purchase = requested_amount*self.item_cost

        if cost_purchase > money:
            raise ValueError("Not enough cash to complete purchase")
        elif requested_amount > self.num_items:
            raise ValueError("Not enough items in machine")

        change = money-cost_purchase

        self.reduce_stock(requested_amount)

        return change


def test_vending_machine():
    machine  = VendingMachine(10, 2)
    change  = machine.buy_items(1, 5)

    print(
        "Items bought is {}, change is {} and number items left in machine are {}".format(
            1,
            change,
            machine.num_items
        )
    )

    change  = machine.buy_items(3, 6)

    print(
        "Items bought is {}, change is {} and number items left in machine are {}".format(
            3,
            change,
            machine.num_items
        )
    )

test_vending_machine()