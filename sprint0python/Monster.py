# Monster.py
class Monster:
    def __init__(self, name, attack_power, defense, hp):
        self.name = name
        self.attack_power = attack_power
        self.defense = defense
        self.hp = hp
        self.hp_max = hp

    def attack(self, hero):
        damage = self.attack_power - hero.defense
        if damage <= 0:
            damage = 0  # Prevent negative damage
            print(f"The hero has blocked the attack.")
        print(f"{self.name} attacks {hero.name} and deals {damage} damage.")
        hero.take_damage(damage)

    def take_damage(self, damage):
        self.hp -= damage
        if self.hp < 0:
            self.hp = 0  # No puede tener menos de 0 HP
        print(f"{self.name} takes {damage} damage. Remaining health: {self.hp}")

    def is_alive(self):
        return self.hp > 0
