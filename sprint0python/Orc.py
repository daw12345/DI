# Orc.py
from Monster import Monster

class Orc(Monster):
    def __init__(self):
        super().__init__("Orc", attack_power=35, defense=15, hp=120)
