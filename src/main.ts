import Order from "./Order/Order"
import DebitOrderProcessor from "./OrderProcessor/DebitOrderProcessor"
import PaypalOrderProcessor from "./OrderProcessor/PaypalOrderProcessor"
import SMSAuthorizer from "./Authorizer/SMSAuthorizer"

const security_code = 1234
const email = " email@example.com"
const order = new Order()

const authorizer = new SMSAuthorizer()

authorizer.check_authorization(security_code)

const debitOrderProcessor = new DebitOrderProcessor(security_code, authorizer)
const paypalOrderProcessor = new PaypalOrderProcessor(email, authorizer)

order.add_item("product 1", 1, 1)
order.add_item("product 2", 5, 13)
order.add_item("product 3", 7, 15)

console.log(order.total_price)

debitOrderProcessor.pay(order)
paypalOrderProcessor.pay(order)
