class NewGame:
    def __init__(self):
        self.title = "New Game"
        self.score = 0

    def start(self):
        print(f"Welcome to {self.title}!")
        self.play()

    def play(self):
        # Game logic goes here
        print("Game is now starting...")

    def end(self):
        print(f"Game Over! Your score: {self.score}")

if __name__ == "__main__":
    game = NewGame()
    game.start()