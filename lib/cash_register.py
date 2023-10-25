#!/usr/bin/env python3

class CashRegister:
  def __init__(self,discount=0,f=1):
    self._discount = discount
    self._total = 0.0
    self._items = []

  def add_item(self,itemname,price,quantity=1):
    self._total += price * quantity
    self._last_transaction_amount = price * quantity
    for i in range(quantity):
      self._items.append(itemname)
  
  def apply_discount(self):
    if(self._discount > 0):
      self._total = (self._total - (self._discount) * 10)
      print(f"After the discount, the total comes to ${int(self._total)}.")
    else:
      print("There is no discount to apply.")

  def void_last_transaction(self):
    self._total = self._total - self._last_transaction_amount

  @property
  def discount(self):
    return self._discount
  
  @property
  def total(self):
    return self._total or 0
  
  @property
  def items(self):
    return self._items

  @discount.setter
  def discount(self,discount):
    self._discount = discount
  
  @total.setter
  def total(self,total):
    if((type(total) == int or float) and total > -1):
      self._total = total
  

f = CashRegister(20,0)
print(f.total)