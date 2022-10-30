from abc import ABC, abstractclassmethod

class Authorizer(ABC):
  @abstractclassmethod
  def is_authorized(self) -> bool:
    pass
