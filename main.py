import os

class Dialogue:
    def __init__(self, text, options, events = []):
        self.text = text
        self.options = options
        self.events = events

    def display_text(self):
        print(self.text)

    def display_options(self):
        if (self.options == []):
            return

        print("")
        for i, (key, value) in enumerate(self.options.items()):
                    print(f"{i + 1}. {key}")


class Event:
    def __init__(self, text, type, amount):
        self.text = text
        self.type = type
        self.amount = amount

    def display(self):
        print(f"*{self.text}*")


class Player:
    def __init__(self):
        self.name = "Jonáš Bořivoj Harvát"
        self.health = 100

    def lose_health(self, amount):
        self.health -= amount

    def is_alive(self):
        return self.health > 0

    def display_stats(self):
        for i in range(50):
            print("-", end="")

        print("\nJonáš Bořivoj Harvát")
        print(f"Bodíky zdraví:\t{self.health} HP")

        for i in range(50):
            print("-", end="")
        print("\n")


class Game:
    def __init__(self):
        self.player = Player()
        self.dialogue = [
            Dialogue("Vítej, Jonáši Bořivoji Harváte.\nNacházíš se uprostřed temného lesa. Zabloudil jsi?", {"Ano": 1, "Ne": 2}),
            Dialogue("Blbý píčo.", []),
            Dialogue("Skvěle! Budeš muset zachránit princeznu, kterou unesl drak.", {"Jdu na to!": 3, "Nechci": 1}),
            Dialogue("Vydal ses na cestu, ale kousl tě do koulí had.", {":(": 4, "Auuu": 4}, [Event("Ztrácíš 10 HP.", "damage", 10)]),
            Dialogue("To nevadí. Cesta pravého hrdiny zahrnuje i překážky ve formě nepatřičných nehod, náhod, různorodých nestvůr, nebezpečenství, zrady, lásky, slz a potu.\nJsi připraven? Máš to? Cítíš se jako někdo, kdo je opravdu hoden takové výzvy, jako je záchrana líbezné princezny ze spárů zrůdné bestie?", {"Ano": 5, "*krátká odmlka* Ano": 5}),
            Dialogue("Fajn", [], [Event("Ztrácíš 50 HP.", "damage", 50), Event("Ztrácíš 40 HP.", "damage", 40)])
        ]
        self.current_dialogue = 0

    def play(self):
        # dialogue index is out of range of array
        if (self.current_dialogue > len(self.dialogue) - 1):
            print("Je potřeba doprogramovat zbytek hry.")
            return


        # set current dialogue from array based on index
        dialogue = self.dialogue[self.current_dialogue]

        # realize events
        for event in dialogue.events:
            if event.type == "damage":
                self.player.lose_health(event.amount)
        
        self.player.display_stats()

        # display dialogue text
        dialogue.display_text()

        # display event texts
        for event in dialogue.events:
            event.display()

        # if player is dead, end the game
        if not self.player.is_alive():
            print("*Zemřel jsi. Zkus to znovu.*")
            return

        # if there are no options, end the game
        if dialogue.options == []:
            print("*Konec hry.*")
            return

        # display options for progressing dialogue
        dialogue.display_options()

        # next dialogue selection loop: runs until valid choice is made
        while True:
            choice = input("\nVyber číslo možnosti >")

            # check is input is valid: is a number and is in range of options
            if not choice.isdigit() or int(choice) < 1 or int(choice) > len(dialogue.options):
                print(">Neplatná volba.")
                # jump back to the start of the loop
                continue
            break
        
        # set next dialogue based on player choice
        next_dialogue_index = list(dialogue.options.keys())[int(choice) - 1]
        self.current_dialogue = dialogue.options[next_dialogue_index]

        # if using windows terminal, use 'cls' instead of 'clear'
        os.system('clear')
        self.play()

game = Game()
os.system('clear')
game.play()
