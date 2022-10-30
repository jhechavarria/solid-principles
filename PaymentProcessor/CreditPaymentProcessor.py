from .PaymentProcessor import PaymentProcessor

class CreditPaymentProcessor(PaymentProcessor):
  def __init__(self, security_code):
    self.security_code = security_code

  def pay(self, order):
    print("Processing credit payment")
    print(f"Using security code {self.security_code}")
    order.status = "paid"
