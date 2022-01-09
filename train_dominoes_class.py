import math
from random import randint

class DominoGame:
    def __init__(self, dominoes):
        ''' initializer '''
        self.dominoes = dominoes
        self.domino_pool = dominoes
        self.highest_domino = 0
        self.start_number_dominoes = 15
        self.round_num = 0
        
        self.hand = []
        self.error_check()
        
    def error_check(self):
        ''' Does the error checking for the given dominoes set '''
        if(not self.is_valid()):
            raise Exception("Please provide a valid set of dominoes")
        
        print("Highest Domino is",self.highest_domino)
        self.get_hand()
        print("Your Hand:",self.hand)
        
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
        max_length, train = self.recursive_solve(self.current_tile, self.hand)
        print("Maximum Train Length is:",max_length)
        print("The best train is",train)
       
    def recursive_solve(self, domino, pool, score=0, train=[]):
        ''' Recurisve helper function to solve() '''
        next_dominoes = self.get_next_dominoes(domino, pool)
        
        #print("Hand:",pool)
        #print(next_dominoes)        
        
        if(len(next_dominoes) == 0):
            return score, train
        
        best_score = score
        best_train = train
        
        for path in next_dominoes:
            #print("Current Path:",path)
            new_hand = list(set(pool) - {path,self.flipped_domino(path)})
            
            new_score, new_train = self.recursive_solve(path, new_hand, score+1, train+[path])
            
            if new_score > best_score:
                best_score = new_score
                best_train = new_train
            
            #best_score = max(best_score, self.recursive_solve(path, new_hand, score+1))
        
        return best_score, best_train
            
    
    def get_next_dominoes(self, current_num, pool):
        ''' Gets a set of the next available tiles given current_tile'''
        next_dominoes = []
        
        for domino in pool:
            if domino[0] == current_num[1]:
                next_dominoes.append(domino)
            elif domino[1] == current_num[1]:
                next_dominoes.append(self.flipped_domino(domino))
                
        return next_dominoes

        