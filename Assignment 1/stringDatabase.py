import random


class stringDatabase:
    """
        This Class is used to a file contains 4030 words and also  identifies whether player has predicted correct word or letter.
        words = This object is used to 4030 words
        letter_used = This object is used to store letters predicted by player
        guess_used =  This object is used to store words predicted by player
        score = This object is used to store score of current game
        user_guess = This object is used to store correct letter predicted by player
        guess_class = This object is used to store GUESS Class object
        game_class = This object is used to Store GAME Class object
        main_line = This object is used to current line of file
    """
    words = []
    letter_used = []
    guess_used = []
    score = 0
    user_guess = ["_", "_", "_", "_"]
    guess_class = ""
    game_class = ""
    main_line = ""

    def read_word_file(self):
        """
         This Function is to read file of  4030 words
        :return:
        """
        input_files = open("four_letters.txt", "r+")
        for line in input_files:
            self.main_line += line
            line = line.strip()
            line = line.split(" ")
            for x in line:
                self.words.append(x)
        self.main_line = self.main_line.replace(" ", "")

    def guess_option(self, word_guess, missed_guess, missed_letter):
        """
        This function is used to identify whether player has predicted correct  word or not
        :param word_guess: Word which need to predicted by player
        :param missed_guess: Number of incorrect words predicted by player
        :param missed_letter: Number of incorrect letter predicted by player
        :return:
        """
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
        """
                This function is used when player gave up the game and want to start next game round.
                :param word_guess: Word which need to predicted by player
                :param missed_guess: Number of incorrect words predicted by player
                :param missed_letter: Number of incorrect letter predicted by player
                :return:
                """
        print("Current Guess :", word_guess)
        self.game_class.add_data(word_guess, "Gave Up", missed_guess, missed_letter, self.user_guess)
        self.letter_used = []
        self.guess_used = []
        self.score = 0
        self.user_guess = ["_", "_", "_", "_"]
        self.guess_class.select_option(self.words[random.randint(0, len(self.words))], 0, 0)

    def letter_option(self, word_guess, missed_guess, missed_letter):
        """
                This function is used to identify whether player has predicted correct  letter or not
                :param word_guess: Word which need to predicted by player
                :param missed_guess: Number of incorrect words predicted by player
                :param missed_letter: Number of incorrect letter predicted by player
                :return:
                """
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