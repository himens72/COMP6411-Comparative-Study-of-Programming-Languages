import random
import json

class GUESS:

    def __init__(self, game_information, string_database):
        self.game_information = game_information
        self.string_database = string_database

    def start_game(self):
        print("** The great guessing game **")
        self.string_database.read_word_file()
        self.string_database.calculate_frequency()
        print(self.string_database.words)

    def select_option(self, word_guess, missed_guess, missed_letter):
        print("Initial Guess : ", word_guess)
        print("g = guess, t = tell me, l for a letter, and q to quit")
        option = input()
        if "g" == option:
            self.string_database.guess_option(word_guess, missed_guess, missed_letter)
        elif "t" == option:
            self.string_database.tell_me_option(word_guess, missed_guess, missed_letter)
        elif "l" == option:
            self.string_database.letter_option(word_guess, missed_guess, missed_letter)
        elif "q" == option:
            print("Quit Option selected")
            self.display_ouput()
        else:
            print("Please Select Proper Option")
            self.select_option(word_guess, missed_guess, missed_letter)

    def display_ouput(self):
        template = "{0:7}{1:15}{2:15}{3:15}{4:15}{5:10}"  # column widths: 8, 10, 15, 7, 10
        print("Game\tWord\tStatus\tBad Guesses\tMissed Letter\tScore")
        for i in range(len(self.game_information.data)):
                print('{:<8d}{:>4s}{:^14s}{:<8d}{:>8d}{:>14.2f}'.format(self.game_information.data[i][0], self.game_information.data[i][1], self.game_information.data[i][2], self.game_information.data[i][3], self.game_information.data[i][4], self.game_information.data[i][5]))

class stringDatabase:
    words = []
    letter_used = []
    guess_used = []
    score = 0
    user_guess = ["_", "_", "_", "_"]
    guess_class = ""
    game_class = ""
    characters = []
    character_values = []
    main_line = ""

    def calculate_frequency(self):
        i = 0
        while i < 26:
            self.characters.append(chr(97 + i))
            self.character_values.append(self.main_line.count(self.characters[i]))
            i += 1

    def read_word_file(self):
        initial = 97
        i = 0
        while i < 26:
            self.characters.append(chr(97 + i))
            print(self.characters[i])
            i += 1
        print("Inside Read File Function")
        input_files = open("four_letters.txt", "r+")
        print("Name of the file : ", input_files.name)
        for line in input_files:
            self.main_line += line
            line = line.strip()
            line = line.split(" ")
            for x in line:
                self.words.append(x)
        self.main_line = self.main_line.replace(" ", "")

    def guess_option(self, word_guess, missed_guess, missed_letter):
        print(missed_guess, ", ", missed_letter)
        print("Enter a 4 Character Word :")
        guess = input()
        if guess in self.guess_used:
            print("Guess Word is already used. Try other Word")
            self.guess_option(word_guess, missed_guess, missed_letter)
        else:
            self.guess_used.append(guess)
        current_index = -1
        if guess == word_guess:
            current_index = 0
        if current_index == 0:
            print("Congratulation!! You have Correct Guess ", word_guess)
            self.game_class.add_data(word_guess, "Success",missed_guess, missed_letter)
            self.letter_used = []
            self.guess_used = []
            self.score = 0
            self.user_guess = ["_", "_", "_", "_"]
            self.guess_class.select_option(self.words[random.randint(0, len(self.words))], 0, 0)
        else:
            print("Incorrect Guess")
            new_missed_guess = missed_guess + 1
            self.guess_class.select_option(word_guess, new_missed_guess, missed_letter)

    def tell_me_option(self, word_guess, missed_guess, missed_letter):
        print("Current Guess :", word_guess)
        self.game_class.add_data(word_guess, "Gave Up", missed_guess, missed_letter)
        self.letter_used = []
        self.guess_used = []
        self.score = 0
        self.user_guess = ["_", "_", "_", "_"]
        self.guess_class.select_option(self.words[random.randint(0, len(self.words))], 0, 0)

    def letter_option(self, word_guess, missed_guess, missed_letter):
        print(missed_guess, ", ", missed_letter)
        print("Enter a Letter:")
        letter = input()
        if letter in self.letter_used:
            print("Letter already used. Try other letter")
            self.letter_option(word_guess, missed_guess, missed_letter)
        else:
            self.letter_used.append(letter)
        current_index = -1
        for i in range(0, len(word_guess)):
            if word_guess[i] == letter:
                self.user_guess[i] = letter
                current_index = 0
        if current_index == 0:
            print("You have found 1 letter")
            output = ""
            for i in self.user_guess:
                output += i

            if output == word_guess:
                print("Congratulation!! You have Correct Guess ", word_guess)
                self.game_class.add_data(word_guess, "Success", missed_guess, missed_letter)
                self.letter_used = []
                self.guess_used = []
                self.score = 0
                self.user_guess = ["_", "_", "_", "_"]
                self.guess_class.select_option(self.words[random.randint(0, len(self.words))], 0, 0)
            else:
                output = "Current Guess : "
                for i in self.user_guess:
                    output += i + " "
                print(output)
                self.guess_class.select_option(word_guess, missed_guess, missed_letter)
        else:
            print("No letter found")
            output = "Current Guess : "
            for i in self.user_guess:
                output += i + " "
            print(output)
            new_missed_letter = missed_letter + 1
            self.guess_class.select_option(word_guess, missed_guess, new_missed_letter)


class GAME:
    data = []

    def add_data(self, word_guess,message, missed_guess, missed_letter):
        entries = []
        entries.append(len(self.data) + 1)
        entries.append(word_guess)
        entries.append(message)
        entries.append(missed_guess)
        entries.append(missed_letter)
        entries.append(missed_letter)
        self.data.append(entries)

def main():
    game = GAME()
    database = stringDatabase()
    guess = GUESS(game, database)
    stringDatabase.guess_class = guess
    stringDatabase.game_class = game
    guess.start_game()
    guess.select_option(stringDatabase.words[random.randint(0, len(stringDatabase.words))], 0, 0)


if __name__ == "__main__":
    main()
