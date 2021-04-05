# -*- coding: utf-8 -*-
"""
Created on Sun Apr  4 09:06:32 2021

@author: mwtichen
"""

import random
from matplotlib import pyplot as plt

class Tree():
    def __init__(self, color = "red"):
        self._color = color
        self._bucket = 0
            
    def add(self, cherries):
        self._bucket += cherries
        self._bucket = min(self._bucket, 10)
        
    def subtract(self, cherries):
        self._bucket -= cherries
        self._bucket = max(self._bucket, 0)
        
    def get_count(self):
        return self._bucket
    
class Spinner():
    def __init__(self, seed = None):
        self._seed = seed 
        if seed is not None:
            random.seed(seed)
            
    def spin(self):
        return random.randint(1, 7)
    
class Player():
    def __init__(self, color = 'red'):
        self._tree = Tree(color)
        
    def take_turn(self, spinner):
        number = spinner.spin()
        if number == 1:
            self._tree.add(1)
        elif number == 2:
            self._tree.add(2)
        elif number == 3:
            self._tree.add(3)
        elif number == 4:
            self._tree.add(4)
        elif number == 5:
            self._tree.subtract(2)
        elif number == 6:
            self._tree.subtract(2)
        else:
            self._tree.subtract(10)
        
    def check_bucket(self):
        count = self._tree.get_count()
        if count >= 10:
            # print("Hi Ho Cherry O!")
            return True
        else:
            return False
        
class Game():
    def __init__(self, seed = None):
        self._spinner = Spinner(seed)
        self._player1 = Player('red')
        self._player2 = Player('green')
        self._player3 = Player('blue')
        
    def play(self):
        winner = None
        while winner is None:
            self._player1.take_turn(self._spinner)
            if self._player1.check_bucket():
                winner = 1
                break
            self._player2.take_turn(self._spinner)
            if self._player2.check_bucket():
                winner = 2
                break
            self._player3.take_turn(self._spinner)
            if self._player3.check_bucket():
                winner = 3
                break
        return winner
                
        
if __name__ == '__main__':
    N = 50000
    
    player1_wins = [0] * N
    player2_wins = [0] * N
    player3_wins = [0] * N
    
    player1_prob = [0] * N
    player2_prob = [0] * N
    player3_prob = [0] * N
    
    
    for i in range(N):
        game = Game(i)
        outcome = game.play()
        if outcome == 1:
            player1_wins[i] = 1
        elif outcome == 2:
            player2_wins[i] = 1
        else:
            player3_wins[i] = 1
        
        player1_prob[i] = sum(player1_wins) / (i + 1.0) 
        player2_prob[i] = sum(player2_wins) / (i + 1.0) 
        player3_prob[i] = sum(player3_wins) / (i + 1.0)
        
    print(player1_prob[-1])
    print(player2_prob[-1])
    print(player3_prob[-1])
        
    plt.plot(list(range(N)), player1_prob)
    plt.plot(list(range(N)), player2_prob)
    plt.plot(list(range(N)), player3_prob)
    plt.legend(['Player 1', 'Player 2', 'Player 3'])
    plt.title('Probability of Winning Hi Ho Cherry O')
    plt.tight_layout()
    plt.savefig('cherry_o_simulation.png')
    plt.show()
        
    
    