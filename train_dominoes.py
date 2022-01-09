from train_dominoes_class import DominoGame

def main():
    domino_list = []
    highest_num = 3
    
    for i in range(highest_num+1): # +1 to include blanks
        for j in range(i,highest_num+1):
            domino_list.append((i,j))

    Game = DominoGame(domino_list)
    Game.solve()
    
    
main()
    
