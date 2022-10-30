from .Authorizer import Authorizer

class NotARobotAuthorizer(Authorizer):
  authorized = False
  
  def not_a_robot(self):
    print("Are you a robot ?")
    self.authorized = True

  def is_authorized(self) -> bool:
    return self.authorized == True
