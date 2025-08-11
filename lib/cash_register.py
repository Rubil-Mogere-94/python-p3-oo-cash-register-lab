# cash_register.py

class CashRegister:
    def __init__(self, discount=0):
        self.discount = discount
        self._total = 0.0
        self.items = []
        self.transactions = []

    @property
    def total(self):
        return self._total

    @total.setter
    def total(self, value):
        if value == 0:
            self._total = 0
            self.items = []
            self.transactions = []

    def add_item(self, title, price, quantity=1):
        amount = price * quantity
        self._total += amount
        for _ in range(quantity):
            self.items.append(title)
        self.transactions.append({'amount': amount, 'quantity': quantity})

    def apply_discount(self):
        if self.discount == 0:
            print("There is no discount to apply.")
        else:
            discount_amount = self._total * self.discount / 100
            self._total -= discount_amount
            print(f"After the discount, the total comes to ${int(self._total)}.")

    def void_last_transaction(self):
        if not self.transactions:
            return
        last_trans = self.transactions.pop()
        self._total -= last_trans['amount']
        for _ in range(last_trans['quantity']):
            if self.items:
                self.items.pop()
