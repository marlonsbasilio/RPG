

from typing import List
from model.monster import Monster
from persistence.interface.monster_interface import MonsterInterface
from persistence.repository.monster_repository import MonsterRepository


class monsterUseCase:
    
    def __init__(self,
                 monster_repository: MonsterInterface):
        
        self.monster_repository = monster_repository

    def getAllmonsters(self) -> List[Monster]:
        
        monster_get = self.monster_repository.getMonsters()
        if not monster_get:
            return None
        
        return [Monster(monster.name,monster.level) for monster in monster_get]
        
    def monsterRegister(self, monster: Monster) -> Monster:
    
        monster_insert = self.monster_repository.insertMonster(monster)
        return monster_insert
    
    def monsterDelete(self, monster: Monster):
        
        self.monster_repository.deleteMonster(monster)
    