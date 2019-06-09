class guess:

    def __init__(self, game_information, string_database):
        """
        This method is used to initialise game and stringDatabase object
        :param game_information: Game Object
        :param string_database: stringDatabase object
        """
        self.game_information = game_information
        self.string_database = string_database

    def start_game(self):
        """
        This Function start the Game
        :return:
        """
        print("** The great guessing game **")
        self.string_database.read_word_file()

    def select_option(self, word_guess, missed_guess, missed_letter):
        """
                This function allow player to select options.
                :param word_guess: Word which need to predicted by player
                :param missed_guess: Number of incorrect words predicted by player
                :param missed_letter: Number of incorrect letter predicted by player
                :return:
                """
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
            print()
            exit(0)
        else:
            print("Please Select Proper Option")
            self.select_option(word_guess, missed_guess, missed_letter)

    def display_ouput(self):
        """
                This function display result of games played by player.
                This function will display result when player quit Game.
                """
        total = 0
        print("Game\tWord\tStatus\tBad Guesses\tMissed Letter\tScore")
        for i in range(len(self.game_information.data)):
            print('{:<8d}{:>4s}{:^14s}{:<8d}{:>8d}{:>14.2f}'.format(self.game_information.data[i][0],
                                                                    self.game_information.data[i][1],
                                                                    self.game_information.data[i][2],
                                                                    self.game_information.data[i][3],
                                                                    self.game_information.data[i][4],
                                                                    self.game_information.data[i][5]))
            x = self.game_information.data[i][5]
            total = total + x
        print()
        print('Final Score: ' + str(float(total)))
