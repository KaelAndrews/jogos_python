class Weapon:
    def __init__(self, name, damage, range, fire_rate, ammo_capacity):
        self.name = name
        self.damage = damage
        self.range = range
        self.fire_rate = fire_rate
        self.ammo_capacity = ammo_capacity
        self.current_ammo = ammo_capacity

    def reload(self):
        self.current_ammo = self.ammo_capacity
        print(f"{self.name} reloaded!")

    def fire(self):
        if self.current_ammo > 0:
            self.current_ammo -= 1
            print(f"Firing {self.name}! Damage dealt: {self.damage}")
        else:
            print(f"{self.name} is out of ammo! Reload to continue.")

    def is_empty(self):
        return self.current_ammo <= 0

    def get_info(self):
        return {
            "name": self.name,
            "damage": self.damage,
            "range": self.range,
            "fire_rate": self.fire_rate,
            "current_ammo": self.current_ammo,
            "ammo_capacity": self.ammo_capacity
        }