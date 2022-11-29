import re

from class_gallows import Gallows

def game_gallows(max_errors):
    start_game = Gallows(max_errors)
    print('''Привет, мой друг, ты попал в игру под названием "Виселица". 
Игра заключается в том, чтобы ты отгадал побуквенно слово. 
Если ты называешь букву, которой нет в слове, то ты теряешь жизнь.
Если такая буква в слове есть, но стоит не на своем месте, то ты ее не теряешь.
Все ранее введенные буквы ты можешь видеть, чтобы не ошибиться на следующем ходе.
Удачи и победы тебе!''')
    name = input('Как твое имя, друг? ')
    word = start_game.generate()
    words = [i for i in word if i != '\n']
    len_letters = len(words)
    result_value = []
    correct_letters = []
    for i in words:
        if start_game.max_errors < 1:
            break
        elif result_value == [i for i in words]:
            break
        while True:
            print("\n")
            agile = ['_' * len_letters]
            print(f'Оставшееся количество попыток: {start_game.max_errors}')
            print(f'Отгаданные буквы: {"".join(map(str, result_value + agile))}')
            print(f'Осталось угадать букв: {len_letters}')
            print(f'Введенные ранее буквы:{", ".join(map(str, start_game.all_letters))}')
            print(f'Угаданные буквы, которые стоят не на своем месте: {", ".join(map(str, correct_letters))}')
            start_game.player_letter()
            # print([i for i in words])
            if start_game.letter.lower() == i:
                print(f'Да, {name}, ты угадал!')
                result_value.append(start_game.letter.lower())
                len_letters -= 1
                if result_value == [i for i in words]:
                    print(f'Ура, {name}, ты победил, я тебя поздравляю, ты угадал все буквы!')
                    print(f'Конечное слово: {"".join(map(str, result_value))}')
                break
            elif start_game.letter.lower() in words and start_game.letter.lower() != i:
                print('Такая буква есть в слове, но она стоит не тут!')
                if start_game.letter.lower() in correct_letters:
                    pass
                else:
                    correct_letters.append(start_game.letter.lower())
            elif start_game.max_errors < 1:
                print('Игра окончена, ты проиграл и не смог угадать все буквы!')
                break
            elif result_value == [i for i in words]:
                break
            else:
                print(f'Нет, {name}, такой буквы в слове нет!')
                start_game.max_errors -= 1
                continue