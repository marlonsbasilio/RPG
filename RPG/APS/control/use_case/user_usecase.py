

from model.user import User
from persistence.interface.user_interface import UserInterface
from persistence.repository.user_repository import UserRepository


class UserUseCase:
    
    def __init__(self,
                 user_repository: UserInterface):
        
        self.user_repository = user_repository

    def userLogin(self, user:User) -> User:
        
        user_get = self.user_repository.getUser(user)
        if not user_get:
            return None
        
        return User(user_get.username,user_get.password)
    
    def userRegister(self, user: User) -> User:
    
        user_insert = self.user_repository.insertUser(user)
        return user_insert
    
    def deleteUser(self, user: User):
        
        self.user_repository.deleteUser(user)
    