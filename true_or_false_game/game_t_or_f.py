from true_or_false_class import TrueOrFalse


# a function that calls the game true or false. answer only "yes" or "no"

def game_true_or_false(file, max_mistake):
    game = TrueOrFalse(file, max_mistake)
    print('Hello, my friend, its game with name as "True or false"'
          'Rules in game: you see questions and you should say real this fact or lie.'
          'Good luck!')
    score = 0
    while True:
        game.next()
        if game.value != [''] and game.max_mistake > 0:
            print(game.value[0])
            game.answer_q()
            if game.answer.lower() == game.value[1].lower():
                score += 1
                print(f'Yes, you are right! {game.value[2]}')
            elif game.answer.lower() != game.value[1].lower():
                game.max_mistake -= 1
                print(f'No, man, you are mistake! {game.value[2]}')
        elif game.value == [''] and game.max_mistake > 0:
            print(f'Congratulations, my friend, you are win! You scores: {score}')
            break
        elif game.max_mistake <= 0:
            print(f'Game is over, you lose!')
            break
        else:
            print('Game is over!')
