import random
from rock_paper_scissors import ROCK, PAPER, SCISSORS, BasePlayer


class Player(BasePlayer):

    player_name = 'Monty 2'
    author = 'Leonard B'
    x_beaten_by_y = {SCISSORS: ROCK, ROCK: PAPER, PAPER: SCISSORS}

    def __init__(self):
        self.history = []
        self.counts = {ROCK: 0, PAPER: 0, SCISSORS: 0}
        self.round_number = 1
        self.reflect_count = 0
        self.is_reflected = False
        self.last_choice = None
        self.my_history = []

    def play(self):
        """
        Must return a single var for the decided play:
        either 'ROCK', 'PAPER', 'SCISSORS'
        """
        if self.round_number == 1:
            self.current_choice = random.choice([ROCK, PAPER, SCISSORS])
        else:
            if self.is_reflected:
                self.current_choice = self.beat(self.current_choice)
                self.my_history.append(self.current_choice)
                self.last_choice = self.current_choice
                return self.current_choice
            random_number = random.randint(1, self.round_number)
            if random_number <= self.counts[ROCK]:
                self.current_choice = PAPER
            elif random_number <= self.counts[ROCK] + self.counts[PAPER]:
                self.current_choice = SCISSORS
            else:
                self.current_choice = ROCK
        self.last_choice = self.current_choice
        return self.current_choice

    def result(self, their_play):
        if self.round_number == 6:
            if self.reflect_count >= 4:
                self.is_reflected = True
        if self.round_number > 1 and their_play == self.my_history[-1]:
            self.reflect_count += 1
        self.my_history.append(self.current_choice)
        self.history.append(their_play)
        self.counts[their_play] += 1
        self.round_number += 1

    def beat(self, play):
        return self.x_beaten_by_y[play]
