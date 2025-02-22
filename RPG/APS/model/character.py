from model.classe import Classe
from model.user import User
import random

class Character:

    
    def __init__(self, name, _class: Classe, user: User, level=1, health=None, exp=0, damage=None):
        self.name = name
        self._class = _class
        self.user = user
        self.level = level
        self.attack_speed = self.calculate_atk_speed()
        self.health = self.calculate_health()
        self.exp = exp
        self.damage = self.calculate_damage()

    def calculate_atk_speed(self):
        return 1.5 - (self.level*0.1)

    def calculate_health(self):
        return 30 + self._class.base_hp + self.level * self._class.percent_lvl_hp

    def calculate_damage(self):
        return self._class.base_dmg + self.level * self._class.percent_lvl_dmg

    def attack(self):
        return random.randint(int(self.damage * 0.8), int(self.damage * 1.2))

    def receive_damage(self, damage):
        self.health -= damage
        if self.health <= 0:
            print(f"{self.name} foi derrotado!")

    def gain_experience(self, exp):
        self.exp += exp
        print(f"{self.name} ganhou {exp} de experiência!")
        if self.exp >= 100 * self.level:
            self.level_up()

    def level_up(self):
        self.level += 1
        self.health = self.calculate_health()
        self.damage = self.calculate_damage()
        print(f"{self.name} subiu para o nível {self.level}!")
        