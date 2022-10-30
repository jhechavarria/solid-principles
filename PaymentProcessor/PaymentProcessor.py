from abc import ABC, abstractclassmethod

class PaymentProcessor(ABC):
  @abstractclassmethod
  def pay(self, order):
    pass
