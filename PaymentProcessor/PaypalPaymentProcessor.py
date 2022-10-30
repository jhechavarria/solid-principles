from .PaymentProcessor import PaymentProcessor
from Authorizer import Authorizer

class PaypalPaymentProcessor(PaymentProcessor):
  def __init__(self, email, authorizer: Authorizer):
    self.email = email
    self.authorizer = authorizer

  def pay(self, order):
    if not self.authorizer.is_authorized():
      raise Exception("Operation not authorized")
    print("Processing paypal payment")
    print(f"Using email {self.email}")
    order.status = "paid"
