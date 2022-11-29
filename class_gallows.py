import random
from typing import Optional


class Gallows:
    def __init__(self, max_errors: Optional[int] = 7):
        self.word = None
        self.letter = None
        self.max_errors = max_errors
        self.all_letters = set()

    def generate(self):
        afile = open('.\WordsStockRus.txt', encoding='utf-8 ')
        try:
            line = next(afile)
            for num, aline in enumerate(afile, 2):
                if random.randrange(num):
                    continue
                line = aline
            self.word = line
            # print(line)
        except StopIteration:
            return
        print(f'Ваше слово сгенерировано! Оно стоит из {len(self.word) - 1} букв!')
        return self.word

    def player_letter(self):
        while True:
            self.letter = input('Ваша буква? ')
            if len(self.letter) != 1:
                print('Введите букву корректно!')
                continue
            else:
                break
        self.all_letters.add(self.letter)