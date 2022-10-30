from Order import Order
from PaymentProcessor import DebitPaymentProcessor, PaypalPaymentProcessor
from Authorizer import SMSAuthorizer, NotARobotAuthorizer

security_code = 1234
email = "email@example.com"

order = Order()
order.add_item("item 1", 1, 5)
order.add_item("item 2", 1, 3)
order.add_item("item 3", 1, 20)

print(order.total_price())

authorizer = SMSAuthorizer()
paymentProcessor = DebitPaymentProcessor(security_code, authorizer)
authorizer.verify_code(security_code)
paymentProcessor.pay(order)

authorizer = NotARobotAuthorizer()
paymentProcessor = PaypalPaymentProcessor(email, authorizer)
authorizer.not_a_robot()
paymentProcessor.pay(order)
