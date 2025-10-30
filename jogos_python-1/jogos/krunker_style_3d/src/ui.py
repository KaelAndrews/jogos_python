from tkinter import Tk, Frame, Button, Label

class UI:
    def __init__(self, master):
        self.master = master
        master.title("Krunker Style 3D Game")

        self.frame = Frame(master)
        self.frame.pack()

        self.label = Label(self.frame, text="Welcome to Krunker Style 3D!")
        self.label.pack()

        self.start_button = Button(self.frame, text="Start Game", command=self.start_game)
        self.start_button.pack()

        self.quit_button = Button(self.frame, text="Quit", command=master.quit)
        self.quit_button.pack()

    def start_game(self):
        self.label.config(text="Game Starting...")
        # Here you would initialize the game logic

if __name__ == "__main__":
    root = Tk()
    ui = UI(root)
    root.mainloop()