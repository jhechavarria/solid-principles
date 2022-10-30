from OrderItem import OrderItem

class Order:
  items = []
  status = "created"

  def add_item(self, title, qty, price):
    orderItem = OrderItem()
    orderItem.title = title
    orderItem.qty = qty
    orderItem.price = price
    self.items.append(orderItem)

  def total_price(self):
    total = 0
    for orderItem in self.items:
      total += orderItem.price
    return total
