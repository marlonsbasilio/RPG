

from typing import List
from model.classe import Classe
from persistence.interface.classe_interface import ClasseInterface
from persistence.repository.classe_repository import ClasseRepository


class ClasseUseCase:
    
    def __init__(self,
                 classe_repository: ClasseInterface):
        
        self.classe_repository = classe_repository

    def getAllClasses(self) -> List[Classe]:
        
        classe_get = self.classe_repository.getAllowedClasses()
        if not classe_get:
            return None
        
        return [Classe(classe.classe,classe.base_dmg, classe.base_hp, classe.percent_lvl_dmg, classe.percent_lvl_hp) for classe in classe_get]
    def getClasseByName(self,name) -> Classe:
        classe_get = self.classe_repository.getClasse(name)
        if not classe_get:
            return None
        return Classe(classe_get.classe,classe_get.base_dmg, classe_get.base_hp, classe_get.percent_lvl_dmg, classe_get.percent_lvl_hp)
    def classeRegister(self, classe: Classe) -> Classe:
    
        classe_insert = self.classe_repository.insertClasse(classe)
        return classe_insert
    
    def classeDelete(self, classe: Classe):
        
        self.classe_repository.deleteClasse(classe)
    