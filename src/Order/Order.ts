import OrderItem from "./OrderItem"
import OrderStatus from "./OrderStatus"

export default class Order {
  private items: Array<OrderItem> = []
  public status: OrderStatus = OrderStatus.INITIATED

  public add_item(title: string, qty: number, price: number): void {
    const item = new OrderItem()
    item.title = title
    item.qty = qty
    item.price = price

    this.items.push(item)
  }

  public total_price(): Number {
    return this.items.reduce((accumulator: number, item: OrderItem) => {
      return accumulator + item.price
    }, 0)
  }
}
