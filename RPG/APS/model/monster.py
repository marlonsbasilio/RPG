from model.classe import Classe
from model.user import User
import random

class Monster:
    
    def __init__(self, name, level):
        self.name = name
        self.level = level
        self.attack_speed = self.calculate_atk_speed()
        self.health = self.calculate_health()
        self.damage = self.calculate_damage()

    def calculate_atk_speed(self):
        return 3 - (self.level*0.05)

    def calculate_health(self):
        return 50 + int(self.level) * 10

    def calculate_damage(self):
        return 5 + int(self.level) * 2

    def attack(self):
        return random.randint(int(self.damage * 0.8), int(self.damage * 1.2))

    def receive_damage(self, damage):
        self.health -= damage
        if self.health <= 0:
            print(f"{self.name} foi derrotado!")
    
    def __str__(self):
        return f"Name: {self.name}, Level: {self.level}, Health: {self.health}, Damage: {self.damage}"
        