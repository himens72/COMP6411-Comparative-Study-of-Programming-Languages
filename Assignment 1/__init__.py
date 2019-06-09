from game import game
from stringDatabase import stringDatabase
from guess import guess

import  random

def main():
    database = stringDatabase()
    game_object = game()
    game_object.frequency_data()
    guess_object = guess(game_object, database)
    database.guess_class = guess_object
    database.game_class = game_object
    guess_object.start_game()
    guess_object.select_option(stringDatabase.words[random.randint(0, len(stringDatabase.words))], 0, 0)

main()
