#!/usr/bin/env python3

class CashRegister:
  def __init__(self, discount=0):
    self.discount = discount
    self.total = 0
    self.items = []
    self.last_transaction = 0

  def add_item(self, title, price, quantity=0):
    if quantity == 0:
      self.total += price
      self.items.append(title)
      self.last_transaction = price
    else:
      self.total += price * quantity
      self.last_transaction = price * quantity
      for number in range(quantity):
        self.items.append(title)

  def apply_discount(self):
    if self.discount == 0:
      print("There is no discount to apply.")
    else:
      discount_decimal = self.discount / 100
      discount_amount = discount_decimal * self.total
      new_total = self.total - discount_amount
      self.total = new_total
      print(f"After the discount, the total comes to ${int(new_total)}.")

  def void_last_transaction(self):
    new_total = self.total - self.last_transaction
    self.total = new_total
