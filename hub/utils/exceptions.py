from hub.exceptions import BaseException

class LoginExceptions(BaseException):
    default_code=400
    default_detail="Invalid email or password"
    
class AccountExistsException(BaseException):
    default_code=400
    default_detail="Account already exists"

class UserDoesNotExistException(BaseException):
    default_code=400
    default_detail="Account does not exist"

class InvalidEmailException(BaseException):
    default_code=400
    default_detail="Invalid email address"

class InvalidSchoolEmailException(BaseException):
    default_code=400
    default_detail="email  is not a valid KNUST email address"
    

class AccountAlreadyVerifiedException(BaseException):
    status_code = 400
    default_code = 108
    default_detail = "Account already verified or active"
    
class AccountDoesNotExistException(BaseException):
    default_code=400
    default_detail="Account does not exist"
    
class EmailRequiredException(BaseException):
    status_code = 400
    default_code = 113
    default_detail = "At least email or username is required"
    
class UsernameException(BaseException):
    status_code=400
    default_detail="Account with this username already exists"