import random


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

    def read_word_file(self):
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
            self.game_class.add_data(word_guess, "Success", missed_guess, missed_letter, self.user_guess)
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
        self.game_class.add_data(word_guess, "Gave Up", missed_guess, missed_letter, self.user_guess)
        self.letter_used = []
        self.guess_used = []
        self.score = 0
        self.user_guess = ["_", "_", "_", "_"]
        self.guess_class.select_option(self.words[random.randint(0, len(self.words))], 0, 0)

    def letter_option(self, word_guess, missed_guess, missed_letter):
        if len(self.letter_used) >= 27:
            self.guess_class.select_option(word_guess, missed_guess, missed_letter)
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
                self.game_class.add_data(word_guess, "Success", missed_guess, missed_letter, self.user_guess)
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