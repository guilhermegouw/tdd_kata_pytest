
class Checkout:
    class Discount:
        def __init__(self, number_of_items, price):
            self.number_of_items = number_of_items
            self.price = price

    def __init__(self):
        self.prices = {}
        self.discounts = {}
        self.items = {}

    def add_discount(self, item, number_of_items, price):
        discount = self.Discount(number_of_items, price)
        self.discounts[item] = discount

    def add_item_price(self, item, price):
        self.prices[item] = price

    def add_item(self, item):
        if item in self.items:
            self.items[item] += 1
        else:
            self.items[item] = 1

    def calculate_total(self):
        total = 0
        for item, cnt in self.items.items():
            total += self.can_calculate_item_total(item, cnt)
        return total

    def can_calculate_item_total(self, item, cnt):
        total = 0
        if item in self.discounts:
            discount = self.discounts[item]
            if cnt >= discount.number_of_items:
                total += self.can_calculate_item_discounted_total(item, cnt, discount)
            else:
                total += self.prices[item] * cnt
        else:
            total += self.prices[item] * cnt
        return total

    def can_calculate_item_discounted_total(self, item, cnt, discount):
        total = 0
        number_of_discounts = cnt / discount.number_of_items
        total += number_of_discounts * discount.price
        remaining = cnt % discount.number_of_items
        total += remaining * self.prices[item]
        return total