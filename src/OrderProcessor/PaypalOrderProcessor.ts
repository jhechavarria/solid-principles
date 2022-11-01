import Order from "../Order/Order";
import OrderStatus from "../Order/OrderStatus";
import OrderProcessor from "./OrderProcessor";
import Authorizer from "../Authorizer/Authorizer"

export default class PaypalOrderProcessor implements OrderProcessor {
    private email: string
    private authorizer: Authorizer

    constructor(email: string, authorizer: Authorizer) {
        this.email = email
        this.authorizer = authorizer
    }

    public pay(order: Order): void {
        if (!this.authorizer.is_authorized()) {
            throw "You are not authorized"
        }
        console.log(`Processing to payment with email ${this.email}`)
        order.status = OrderStatus.PAID
    }
}
