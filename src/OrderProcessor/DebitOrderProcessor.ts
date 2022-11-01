import Order from "../Order/Order";
import OrderStatus from "../Order/OrderStatus";
import OrderProcessor from "./OrderProcessor";
import Authorizer from "../Authorizer/Authorizer"

export default class DebitOrderProcessor implements OrderProcessor {
    private security_code: number
    private authorizer: Authorizer

    constructor(security_code: number, authorizer: Authorizer) {
        this.security_code = security_code
        this.authorizer = authorizer
    }    

    public pay(order: Order): void {
        if (!this.authorizer.is_authorized()) {
            throw "You are not authorized"
        }
        console.log(`Processing to payment with code ${this.security_code}`)
        order.status = OrderStatus.PAID
    }
}
