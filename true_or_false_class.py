from typing import Optional


class TrueOrFalse:
    def __init__(self, file, max_mistake: Optional[int] = 5):
        self.file = file
        self.max_mistake = max_mistake
        self.fileop = open(file, 'r', encoding='utf-8')

    def next(self):
        self.value = self.fileop.readline().split(';')

    def answer_q(self):
        self.answer = input('Yes or no?')

    def in_progress(self):
        if self.value == ['']:
            print('Game is end!')
        else:
            print('Game in progress')