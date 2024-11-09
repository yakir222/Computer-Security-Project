from typing import Any
from fastapi import APIRouter, HTTPException
from fastapi.types import UnionType
from server.dal.user import UpdatePasswordBody, User, UserCreateBody, \
    UserLoginBody, UserResponse, UserResetPasswordBody
from server.services.user_services import UserService

class UserRouter(APIRouter):
    def __init__(self) -> None:
        super().__init__()
        self._init_router()
        self._user_service: UserService = UserService()

        print("All routes setup")
        print(*self.routes, sep='\n')

    def _init_router(self):
        self.add_api_route(path="/{username}", endpoint=self.read_user, methods=["GET"], responses={"200":{"description":"OK", "model": User}, 404:{"description":"Not Found", "model":{}}}, status_code=200)
        self.add_api_route(path="", endpoint=self.register_user, methods=["POST"])
        self.add_api_route(path="/updatePassword", endpoint=self.update_password, methods=["POST"])
        self.add_api_route(path="/login", endpoint=self.login, methods=["POST"])
        self.add_api_route(path="/resetPassword", endpoint=self.reset_password, methods=["POST"])

    def read_user(self, username: str):
        print(f"Reading user {username}")
        u = self._user_service.search_for_user(username)
        if not u:
            print("Not Found")
            raise HTTPException(status_code=404, detail="Item not found")

        return u

    def register_user(self, user: UserCreateBody) -> UserResponse:
        try:
            self._user_service.register_user(user)
            u = self._user_service.search_for_user(user.username)
            return UserResponse(
                username=u.username, email=u.email, requires_pass_change=bool(u.requires_pass_change)
            )
        except RuntimeError as e:
            if e.args:
                raise HTTPException(409, detail='User with this name already exists')
        except UserService.PasswordComplexityException as e:
            msg = e.args[0]
            raise HTTPException(400, f"You must pass complex passwd. {msg}")
    def update_password(self, body: UpdatePasswordBody):
        try:
            self._user_service.update_user_pass(body.username, body.old_password, body.new_password)
        except UserService.UserNotExistException:
            raise HTTPException(404, detail="User could not be found")
        except UserService.PasswordMismatchException:
            raise HTTPException(500, detail="Internal server error. User could not be updated")
        except UserService.PasswordComplexityException as e:
            msg = e.args[0]
            raise HTTPException(400, f"You must pass complex passwd. {msg}")
        except UserService.RecycledPasswordError:
            raise HTTPException(400, f"Are you NUTS?")
        return "OK"

    def login(self, body: UserLoginBody) -> UserResponse:
        try:
            u = self._user_service.login(body.username, body.password)
            return UserResponse(
                username=u.username, email=u.email, requires_pass_change=bool(u.requires_pass_change)
            )
        except UserService.UserLockedError:
            raise HTTPException(403, detail="Unauthorized. User is locked")
        except UserService.LoginErrorException:
            raise HTTPException(400, detail="Bad Request")

    def reset_password(self, body: UserResetPasswordBody):
        try:
            self._user_service.reset_password(body.email)
        except UserService.MailNotFoundError:
            raise HTTPException(404, detail="User with given email could not be found")
        return "OK"