from model.character import Character
from model.monster import Monster
import random
import time
import tkinter as tk
import threading
from persistence.repository.character_repository import CharacterRepository
from control.use_case.character_usecase import characterUseCase

def character_factory():
	character_repository = CharacterRepository()
	character_usercase = characterUseCase(character_repository)

	return character_usercase

class Battle:
    def __init__(self, monster: Monster, char: Character, battle_log):
        self.monster = monster
        self.char = char
        self.battle_log = battle_log


    def attacks(self, attacker, target):
        
        while attacker.health > 0 and target.health > 0:

            time.sleep(attacker.attack_speed)

            damage = attacker.attack()
            target.receive_damage(damage)

            self.update_battle_log(f"\n{attacker.name} atacou {target.name} causando {damage} de dano.\n")
            self.update_battle_log(f"{target.name} VIDA: {target.health}\n")

            if target.health <= 0:
                self.update_battle_log(f"{attacker.name} venceu!\n")
                if not isinstance (attacker, Monster):
                    attacker.gain_experience(50 * target.level)
                    self.update_battle_log(f"{attacker.name} Nível: {attacker.level} Experiencia: {attacker.exp}\n")
                return
            
    def start_battle(self):
                
        self.char.health = self.char.calculate_health()
        self.monster.health = self.monster.calculate_health()

        self.update_battle_log(f"{self.char.name} NIVEL: {self.char.level} VIDA: {self.char.health}\n")
        self.update_battle_log(f"{self.monster.name} NIVEL: {self.monster.level} VIDA: {self.monster.health}\n")
        self.update_battle_log(f"Iniciando Batalha!\n\n")
        
        thread1 = threading.Thread(target=self.attacks, args=(self.char, self.monster))
        thread2 = threading.Thread(target=self.attacks, args=(self.monster, self.char))

        thread1.start()
        thread2.start()

        thread1.join()
        thread2.join()

        char_usecase = character_factory()
        char_usecase.charUpdating(self.char)



    def update_battle_log(self, message):
        self.battle_log.config(state='normal')
        self.battle_log.insert(tk.END, message)
        self.battle_log.yview(tk.END)
        self.battle_log.config(state='disabled')
    
    def __str__(self):
        return f"User: {self.user}, Name: {self.name}, Classe: {self._class}, Level: {self.level}, Health: {self.health}, Damage: {self.damage}, Exp: {self.exp}"
        