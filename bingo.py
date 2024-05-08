import random

class bingo:
    def __init__(self):
        self.player1 = []
        p1=[]
    def funplayer(self):
        ranges = range(1, 26)
        self.player1 = random.sample(ranges, 25)
        self.player2 = random.sample(ranges, 25)
        print(self.player1)
        print(self.player2)
        
    def funcut(self):
        if self.inp in self.player1:
            index = self.player1.index(self.inp)
            self.player1[index] = 0
        if self.inp in self.player2:
            index = self.player2.index(self.inp)
            self.player2[index] = 0
    def display(self,s):
        count=0
        for i in s:
            count=count+1
            print(i,end=" ")
            if(count%5==0):
                print()

    def choose(self, inp):
        self.inp = inp
        for i in range(1, 26):
            if i % 2 == 0:
                self.inp = int(input("player 2 please choose one number: "))
                self.funcut()
                print(self.player1)
                print(self.player2)
                if self.funwin():
                    return
            else:
                self.inp = int(input("player 1 please choose one number: "))
                self.funcut()
                print(self.player1)
                print(self.player2)
                if self.funwin():
                    return
    def printbingo1(self):
        p1=[]
        if len(p1)==0:
            p1.append('b')
            print("player one got ",p1)
        elif len(p1)==1:
            p1.append('bi')
            print("player one got ",p1)
        elif len(p1)==2:
            p1.append('binn')
            print("player one got ",p1)
        elif len(p1)==3:
            p1.append('bing')
            print("player one got ",p1)
        elif len(p1)==4:
            p1.append('bingo')
            print("player one got ",p1)
            print("Player 1 wins!")
            return True
    def printbingo2(self):
        p2=[]
        if len(p2)==0:
            p2.append('b')
            print("p2 two got ",p2)
        elif len(p2)==1:
            p2.append('i')
            print("p2 two got ",p2)
        elif len(p2)==2:
            p2.append('n')
            print("p2 two got ",p2)
        elif len(p2)==3:
            p2.append('g')
            print("p2 two got ",p2)
        elif len(p2)==4:
            p2.append('o')
            print("p2 two got ",p2)
            print("Player 2 wins!")
            return True

    def funwin(self):
        # Check rows
        for row in range(5):
            if all(num == 0 for num in self.player1[row * 5:row * 5 + 5]):
                bingo.printbingo1(self)
            if all(num == 0 for num in self.player2[row * 5:row * 5 + 5]):
                bingo.printbingo2(self)
        # Check columns
        for col in range(5):
            if all(self.player1[i * 5 + col] == 0 for i in range(5)):
                bingo.printbingo1(self)
            if all(self.player2[i * 5 + col] == 0 for i in range(5)):
                bingo.printbingo2(self)
    
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
    a1 = bingo()
    a1.funplayer()
    while True:
        a1.choose(0)
        break

main()
