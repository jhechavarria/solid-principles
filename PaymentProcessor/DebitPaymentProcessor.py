from .PaymentProcessor import PaymentProcessor
from Authorizer import Authorizer

class DebitPaymentProcessor(PaymentProcessor):
  def __init__(self, security_code, authorizer: Authorizer):
    self.security_code = security_code
    self.authorizer = authorizer

  def pay(self, order):
    if not self.authorizer.is_authorized():
      raise Exception("Operation not authorized")
    print("Processing debit payment")
    print(f"Using security code {self.security_code}")
    order.status = "paid"
