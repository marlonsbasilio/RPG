from typing import List, Tuple
from abc import ABC, abstractmethod

from model.classe import Classe

class ClasseInterface(ABC):
    
    @abstractmethod
    def insertClasse(self,classe: Classe):
        raise NotImplementedError
    
    @abstractmethod
    def deleteClasse(self,classe: Classe):
        raise NotImplementedError

    @abstractmethod
    def getAllowedClasses(self):
        raise NotImplementedError
    
    @abstractmethod
    def getClasse(self,name):
        raise NotImplementedError