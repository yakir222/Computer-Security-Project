from typing import Union
import server.crypto.crypto as crypto
from server.services import validator_services
import server.services.db_services as db_services
import server.dal.user as user
from server.services.email_service import send_email

class UserService:
    class UserNotExistException(Exception):
        pass
    class PasswordMismatchException(Exception):
        pass
    class PasswordComplexityException(Exception):
        pass
    class LoginErrorException(Exception):
        pass
    class RecycledPasswordError(Exception):
        pass
    class UserLockedError(Exception):
        pass
    class MailNotFoundError(Exception):
        pass

    @staticmethod
    def _validation_wrapper(password):
        res, msg = validator_services.check_password_complexity(password)
        if not res:
            raise UserService.PasswordComplexityException(msg)

    def register_user(self, _u: user.UserCreateBody):
        u = self.search_for_user(_u.username)
        if u:
            raise RuntimeError("User already exists. Can't register")

        self._validation_wrapper(_u.password)
        _u.password = self.get_hashed_pass(_u.password)
        model = user.User(**_u.model_dump())
        db_services.create_user(model)
        db_services.add_password_history(_u.username, _u.password)
        return self.search_for_user(model.username)

    def search_for_user(self, username) -> user.User:
        print(f"Searching for user {username}")
        res = db_services.search_user(username)
        if not res:
            return
        u = user.User(**res)
        return u

    def find_user_by_email(self, email) -> user.User:
        print(f"Searching for user with email {email}")
        res = db_services.search_user_by_email(email)
        if not res:
            print("Didn't find user with email provided")
            raise UserService.MailNotFoundError()
        u = user.User(**res)    
        return u

    def reset_password(self, email) -> bool:
        user = self.find_user_by_email(email)
        randomPass = crypto.generate_random_password()
        user.password = self.get_hashed_pass(randomPass)
        user.requires_pass_change = True
        db_services.update_user(user)
        print(f"new password is {randomPass}")
        send_email(user.email, randomPass)
        return True
        

    def get_hashed_pass(self, password: str) -> str:
        salt = crypto.get_salt()
        return crypto.hash_password(password, salt)

    def update_user_pass(self, username: str, old_password: str, new_password: str):
        u = self.search_for_user(username)
        if not u:
            print("Didn't find user")
            raise UserService.UserNotExistException()
        print("User found, hashing old")
        old_password_hashed = self.get_hashed_pass(old_password)
        if old_password_hashed != u.password:
            print("old pwd doesn't match user pwd")
            raise UserService.PasswordMismatchException()

        self._validation_wrapper(new_password)
        u.password = self.get_hashed_pass(new_password)
        if not validator_services.validate_history(u.username, u.password):
            raise UserService.RecycledPasswordError()
        u.requires_pass_change = False
        db_services.update_user(u)
        db_services.add_password_history(u.username, u.password)


    def login(self, username: str, password: str) -> user.User:
        u = self.search_for_user(username)
        if not u:
            print(f"User Login failed - No such user {username=}. Don't tell the user why!")
            raise UserService.LoginErrorException()

        res, msg = validator_services.validate_attempts(username)
        if not res:
            raise UserService.UserLockedError(f"Too many attempts. {msg}")
        pass_hashed = self.get_hashed_pass(password)
        if pass_hashed != u.password:
            print("User Login failed - password incorrect. Don't tell the user why!")
            db_services.add_login_attempt(username)
            raise UserService.LoginErrorException()
        return u
