from .Authorizer import Authorizer

class SMSAuthorizer(Authorizer):
  authorized = False
  
  def verify_code(self, code):
    print(f"Verifying 2FA code {code}")
    self.authorized = True

  def is_authorized(self) -> bool:
    return self.authorized == True
