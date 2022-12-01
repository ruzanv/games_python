from true_or_false_game.game_t_or_f import game_true_or_false
from gallows_game.game_gallows import game_gallows


def run_games():
    while True:
        want_play = input('Do you want to play? y/n ')
        if want_play == 'y':
            while True:
                choose_game = input('Choose a game:\n'
                                    '0 enter for "True or false"\n'
                                    '1 enter for "Gallows"\n')
                if choose_game == '0':
                    game_true_or_false('./true_or_false_game/Questions.csv', 5)
                    break
                elif choose_game == '1':
                    game_gallows('./gallows_game/WordsStockRus.txt',10)
                    break
                else:
                    print('You entered an invalid value')
                    continue
        elif want_play == 'n':
            break
        else:
            print('You entered an invalid value')
            continue