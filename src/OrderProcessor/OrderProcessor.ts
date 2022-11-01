import Order from "../Order/Order"

export default interface OrderProcessor {
    pay(order: Order): void
}
