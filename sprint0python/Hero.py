# Hero.py
class Hero:
    def __init__(self, name):
        self.name = name
        self.attack_power = 30  # Cambiado de attack a attack_power
        self.defense = 20
        self.hp = 100
        self.hp_max = 100

    def attack(self, monster):
        damage = self.attack_power - monster.defense
        if damage <= 0:
            damage = 0  # Evita que el daño sea negativo
            print(f"The enemy has blocked the attack.")
        print(f"{self.name} attacks {monster.name} and deals {damage} damage.")
        monster.take_damage(damage)

    def take_damage(self, damage):
        self.hp -= damage
        if self.hp < 0:
            self.hp = 0  # No puede tener menos de 0 HP
        print(f"{self.name} takes {damage} damage. Remaining health: {self.hp}")

    def heal(self):
        heal_amount = 20
        self.hp += heal_amount
        if self.hp > self.hp_max:
            self.hp = self.hp_max
        print(f"The hero has healed. Current health: {self.hp}")

    def defend(self):
        self.defense += 5
        print(f"{self.name} is defending. Defense increased to {self.defense}.")

    def reset_defense(self):
        self.defense = 20
        print(f"{self.name}'s defense has returned to normal.")

    def is_alive(self):
        return self.hp > 0
