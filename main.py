import random

class bingo:
    def __init__(self):
        self.player1=[]
        self.player2=[]
        
    def funplayer(self):
        ranges=range(1,26)  # Adjusted range to match typical bingo numbers
        self.player1=random.sample(ranges, 25)
        self.p1=self.player1
        self.player2=random.sample(ranges, 25)
        
    def funcut(self):
        if self.inp in self.player1:
            index=self.player1.index(self.inp)
            self.player1[index]=0
        if self.inp in self.player2:
            index=self.player2.index(self.inp)
            self.player2[index]=0

    def choose(self, inp):
        self.inp=inp
        self.inp=int(input("player 2 please choose one number: "))
        self.funcut()
        print(self.p1)
        print(self.player2)
        if self.funwin():
            return
        else:
            self.inp=int(input("player 1 please choose one number: "))
            self.funcut()
            print(self.p1)
            print(self.player2)
            if self.funwin():
                return

    def funwin(self):
        # Check rows
        for row in range(5):
            if all(num == 0 for num in self.player1[row * 5:row * 5 + 5]):
                print("Player 1 wins!")
                return True
            if all(num == 0 for num in self.player2[row * 5:row * 5 + 5]):
                print("Player 2 wins!")
                return True
    
        # Check columns
        for col in range(5):
            if all(self.player1[i * 5 + col] == 0 for i in range(5)):
                print("Player 1 wins!")
                return True
            if all(self.player2[i * 5 + col] == 0 for i in range(5)):
                print("Player 2 wins!")
                return True
    
        # Check main diagonal
        if all(self.player1[i * 6] == 0 for i in range(5)):
            print("Player 1 wins!")
            return True
        if all(self.player2[i * 6] == 0 for i in range(5)):
            print("Player 2 wins!")
            return True
    
        # Check secondary diagonal
        if all(self.player1[i * 4 + 4] == 0 for i in range(5)):
            print("Player 1 wins!")
            return True
        if all(self.player2[i * 4 + 4] == 0 for i in range(5)):
            print("Player 2 wins!")
            return True
    
        return False

def main():
    a1=bingo()
    a1.funplayer()
    while True:
        a1.choose(0)

main()
