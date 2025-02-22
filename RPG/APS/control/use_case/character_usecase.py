
import sys

from control.use_case.classe_usecase import ClasseUseCase
from persistence.repository.classe_repository import ClasseRepository
sys.path.append('.')
from typing import List
from model.character import Character
from model.user import User
from persistence.interface.character_interface import CharacterInterface
from persistence.repository.character_repository import CharacterRepository

def classe_factory():
	classe_repository = ClasseRepository()
	classe_usercase = ClasseUseCase(classe_repository)

	return classe_usercase

class characterUseCase:
    
    def __init__(self,
                 character_repository: CharacterInterface):
        
        self.character_repository = character_repository

    def getAllcharacters(self, user: User) -> List[Character]:
        character_get = self.character_repository.getUserCharacters(user)
        if not character_get:
            return None
        classe_use_case = classe_factory()
        return [Character(character.name,classe_use_case.getClasseByName(character._class), character.user, character.level, character.health, character.exp ) for character in character_get]
        
    def createUserCharacter(self, character: Character) -> Character:
    
        character_insert = self.character_repository.insertCharacter(character)
        return character_insert
    
    def deleteUserCharacter(self, character: Character):
        
        self.character_repository.deleteUserCharacter(character)
    
    def charLevelingUp(self, character: Character):
        
        self.character_repository.charLevelUp(character)
    
    def charUpdating(self, character: Character):
        
        self.character_repository.charUpdate(character)