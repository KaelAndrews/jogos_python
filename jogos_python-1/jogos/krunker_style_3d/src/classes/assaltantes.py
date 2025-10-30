class Assaltantes:
    def __init__(self, gender):
        self.gender = gender
        self.health = 100
        self.speed = 5
        self.weapon = None
        self.skin = self.load_skin()

    def load_skin(self):
        if self.gender == 'male':
            return "assets/models/characters/assaltantes/male/skin_texture.png"
        elif self.gender == 'female':
            return "assets/models/characters/assaltantes/female/skin_texture.png"
        else:
            raise ValueError("Gender must be 'male' or 'female'.")

    def attack(self, target):
        damage = 10  # Example damage value
        target.take_damage(damage)

    def take_damage(self, amount):
        self.health -= amount
        if self.health <= 0:
            self.die()

    def die(self):
        print(f"{self.gender.capitalize()} Assaltante has died.")

    def equip_weapon(self, weapon):
        self.weapon = weapon
        print(f"{self.gender.capitalize()} Assaltante equipped {self.weapon}.")