import random


class GUESS:

    def __init__(self, game_information, string_database):
        self.game_information = game_information
        self.string_database = string_database

    def start_game(self):
        print("** The great guessing game **")
        self.string_database.read_word_file()
        print(self.string_database.words)

    def select_option(self, word_guess, missed_guess, missed_letter):
        print("Inital Guess : ", word_guess)
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
        else:
            print("Please Select Proper Option")
            self.select_option(word_guess, missed_guess, missed_letter)


class stringDatabase:
    words = []
    letter_used = []
    guess_used = []
    score = 0
    user_guess = ["_", "_", "_", "_"]
    guess_class = ""

    def read_word_file(self):
        print("Inside Read File Function")
        input_files = open("four_letters.txt", "r+")
        print("Name of the file : ", input_files.name)
        for line in input_files:
            line = line.strip()
            line = line.split(" ")
            for x in line:
                self.words.append(x)

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
            self.guess_class.select_option(self.words[random.randint(0, len(self.words))], 0, 0)
        else:
            print("Incorrect Guess")
            new_missed_guess = missed_guess + 1
            self.guess_class.select_option(word_guess, new_missed_guess, missed_letter)

    def tell_me_option(self, word_guess, missed_guess, missed_letter):
        print("Current Guess :", word_guess)
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
    print()


def main():
    game = GAME()
    database = stringDatabase()
    guess = GUESS(game, database)
    stringDatabase.guess_class = guess
    guess.start_game()
    guess.select_option(stringDatabase.words[random.randint(0, len(stringDatabase.words))], 0, 0)


if __name__ == "__main__":
    main()
