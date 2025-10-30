class Player:
    def __init__(self, name, character_class):
        self.name = name
        self.character_class = character_class
        self.health = 100
        self.position = (0, 0, 0)
        self.inventory = []

    def move(self, direction):
        if direction == "forward":
            self.position = (self.position[0], self.position[1], self.position[2] + 1)
        elif direction == "backward":
            self.position = (self.position[0], self.position[1], self.position[2] - 1)
        elif direction == "left":
            self.position = (self.position[0] - 1, self.position[1], self.position[2])
        elif direction == "right":
            self.position = (self.position[0] + 1, self.position[1], self.position[2])

    def attack(self, target):
        if target.health > 0:
            target.health -= 10
            print(f"{self.name} attacked {target.name}. {target.name} health is now {target.health}.")
        else:
            print(f"{target.name} is already defeated.")

    def pick_up_item(self, item):
        self.inventory.append(item)
        print(f"{self.name} picked up {item}.")

    def get_status(self):
        return f"Player: {self.name}, Class: {self.character_class}, Health: {self.health}, Position: {self.position}"