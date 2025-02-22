from typing import List, Tuple
from abc import ABC, abstractmethod

from model.user import User

class UserInterface(ABC):
    
    @abstractmethod
    def insertUser(self,user: User):
        raise NotImplementedError
    
    @abstractmethod
    def deleteUser(self,user: User):
        raise NotImplementedError
    
    @abstractmethod
    def getUser(self,user: User):
        raise NotImplementedError
    
    