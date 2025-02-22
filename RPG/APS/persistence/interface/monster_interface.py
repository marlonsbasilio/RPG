from typing import List, Tuple
from abc import ABC, abstractmethod

from model.monster import Monster

class MonsterInterface(ABC):
    
    @abstractmethod
    def insertMonster(self, monster: Monster):
        raise NotImplementedError

    @abstractmethod
    def deleteMonster(self, monster : Monster):
        raise NotImplementedError
    
    @abstractmethod
    def getMonsters(self):
        raise NotImplementedError

    

