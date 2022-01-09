import math
from random import randint

class DominoGame:
    def __init__(self, dominoes):
        ''' initializer '''
        self.dominoes = dominoes
        self.domino_pool = dominoes
        self.highest_domino = 0
        self.start_number_dominoes = 4
        self.round_num = 0
        
        self.hand = []
        self.error_check()
        
    def error_check(self):
        ''' Does the error checking for the given dominoes set '''
        if(not self.is_valid()):
            raise Exception("Please provide a valid set of dominoes")
        
        print("Highest Domino is",self.highest_domino)
        self.get_hand()
        
    def is_valid(self):
        ''' Returns a bool depicting whether the given set of 
            dominoes is valid or not for mexican train dominoes.
            We find largest denomination by solving:
            x^2 + 3x + (2-2*self.dominoes) = 0'''
        
        a = 1
        b = 3
        c = 2 - 2*len(self.dominoes)
        
        # Quadratic formula comes from the series sum of dominoes
        x = (((-b + (math.sqrt(b*b - 4*a*c))) / (2*a)),((-b - (math.sqrt(b*b - 4*a*c))) / (2*a)))
        
        if(x[0] < 0):
            if(x[1] < 0 or not x[1].is_integer()):
                return False
            else:
                self.highest_domino = int(x[1])
                return True
        else:
            if(not x[0].is_integer()):
                return False
            else:
                self.highest_domino = int(x[0])
                return True
        
        
    def get_hand(self):
        ''' Temprorary, should be replaced with user input '''
        # Remove the current tile (middle domino)
        tile_val = self.highest_domino - self.round_num
        self.current_tile = (tile_val,tile_val)
        self.domino_pool.remove(self.current_tile)
        
        for _ in range(self.start_number_dominoes):
            random_domino = self.domino_pool[randint(0, len(self.domino_pool)-1)]
            self.hand.append(random_domino)
            self.domino_pool.remove(random_domino)
    
    def flipped_domino(self, domino):
        ''' Returns a flipped domino '''
        return (domino[1],domino[0])

    def solve(self):
        ''' Gets the longest train with the available dominoes in self.hand '''
        self.recursive_solve(self.current_tile, self.hand)
       
    def recursive_solve(self, domino, pool):
        # Current tile domino stored in self.current_tile
        # Uses a pool of dominos to reset back to user sent dominos after each "round"
        # Round starts at zero
        next_dominoes = self.get_next_dominoes(domino, pool)
        
        print("Hand:",pool)
        print(next_dominoes)        
        
        if(len(next_dominoes) == 0):
            print("***RETURNING***")
            return 0
        if len(next_dominoes) == 1:
            return 1
        
        max_length = 0
        for path in next_dominoes:
            print("Current Path:",path)
            new_hand = list(set(pool) - {path,self.flipped_domino(path)})
            max_length = max(max_length, 1 + self.recursive_solve(path, new_hand))
            print(max_length)
    
    def get_next_dominoes(self, current_num, pool):
        ''' Gets a set of the next available tiles given current_tile'''
        next_dominoes = []
        
        for domino in pool:
            if domino[0] == current_num[1]:
                next_dominoes.append(domino)
            elif domino[1] == current_num[1]:
                next_dominoes.append(self.flipped_domino(domino))
                
        return next_dominoes

        