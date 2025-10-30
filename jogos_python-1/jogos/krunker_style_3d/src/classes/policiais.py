class Policiais:
    def __init__(self, gender):
        self.gender = gender
        self.skin = self.load_skin()
        self.weapons = []

    def load_skin(self):
        if self.gender == 'male':
            return "assets/models/characters/policiais/male/skin_texture.png"
        elif self.gender == 'female':
            return "assets/models/characters/policiais/female/skin_texture.png"
        else:
            raise ValueError("Gender must be 'male' or 'female'.")

    def equip_weapon(self, weapon):
        self.weapons.append(weapon)

    def attack(self):
        if self.weapons:
            print(f"{self.gender.capitalize()} policial is attacking with {self.weapons[-1]}!")
        else:
            print(f"{self.gender.capitalize()} policial has no weapons to attack with.")

    def defend(self):
        print(f"{self.gender.capitalize()} policial is defending!")