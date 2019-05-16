class game:
    data = []
    frequency = []
    score = 0

    def add_data(self, word_guess, message, missed_guess, missed_letter, user_guess):
        self.calculate_score(word_guess, message, missed_guess, missed_letter, user_guess)
        entries = [len(self.data) + 1, word_guess, message, missed_guess, missed_letter, self.score]
        self.data.append(entries)
        self.score = 0

    def frequency_data(self):
        self.frequency = [8.17, 1.49, 2.78, 4.25, 12.70, 2.23, 2.02, 6.09, 6.97, 0.15,
                          0.77, 4.03, 2.41, 6.75, 7.51, 1.93, 0.10, 5.99, 6.33, 9.06,
                          2.76, 0.98, 2.36, 0.15, 1.97, 0.07]

    def calculate_score(self, word_guess, message, missed_guess, missed_letter, user_guess):
        if message == "Success":
            if missed_letter == 0 and missed_guess == 0:
                if "_" not in user_guess:
                    self.score = 0
                else:
                    for i in range(0, len(word_guess)):
                        x = self.frequency[ord(word_guess[i]) - 97]
                        self.score = self.score + x
                    temp_score = 0
                    count = 0
                    for i in range(0, len(user_guess)):
                        if user_guess[i] == "_":
                            x = self.frequency[ord(word_guess[i]) - 97]
                            y = 1
                            count = count + y
                            temp_score = temp_score + x
                    t = 1
                    temp_score1 = 0
                    while t <= missed_guess:
                        a = self.score * 0.1
                        temp_score1 = temp_score1 + a
                        b = 1
                        t = t + b
                    self.score = (temp_score / (missed_letter + 4 - count)) - temp_score1
            else:
                for i in range(0, len(word_guess)):
                    x = self.frequency[ord(word_guess[i]) - 97]
                    self.score = self.score + x
                temp_score = 0
                count = 0
                for i in range(0, len(user_guess)):
                    if user_guess[i] == "_":
                        x = self.frequency[ord(word_guess[i]) - 97]
                        y = 1
                        count = count + y
                        temp_score = temp_score + x
                t = 1
                temp_score1 = 0
                while t <= missed_guess:
                    a = self.score * 0.1
                    temp_score1 = temp_score1 + a
                    b = 1
                    t = t + b
                self.score = (temp_score / (missed_letter + 4 - count)) - temp_score1
        else:
            temp_score2 = 0
            for i in range(0, len(user_guess)):
                if user_guess[i] == "_":
                    x = self.frequency[ord(word_guess[i]) - 97]
                    temp_score2 = temp_score2 + x
            self.score = -1 * temp_score2
