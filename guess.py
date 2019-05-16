class guess:

    def __init__(self, game_information, string_database):
        self.game_information = game_information
        self.string_database = string_database

    def start_game(self):
        print("** The great guessing game **")
        self.string_database.read_word_file()

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
        total = 0
        template = "{0:7}{1:15}{2:15}{3:15}{4:15}{5:10}"  # column widths: 8, 10, 15, 7, 10
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
        print("Final Score: " + str(float(total)))