class Bingo:
    def __init__(self):
        self.__array1=[[0]*5 for _ in range(5)]
        self.__array2=[[0]*5 for _ in range(5)]

    def grid_data(self):
        data=int(input("Enter data in range 1 to 25 :"))
    
    def fill_grid1(self):
        for i in range(5):
            print(" Enter Row",i,"of bingo") 
            for j in range(5):
                print(i,j,": ",end=" ")
                x=int(input())
                self.__array1[i][j]=x
                print(" ",end="")
            print()
        print()
    def fill_grid2(self):
        for i in range(5):
            print(" Enter Row",i,"of bingo") 
            for j in range(5):
                print(i,j,": ",end=" ")
                x=int(input())
                self.__array2[i][j]=x
                print(" ",end="")
            print()
        print()
    
    def display_grid_1(self):
        print("\n Player 1 bingo: ")
        for i in self.__array1:
            for j in i:
                print(j,end=" ")
            print()
    def display_grid_2(self):
        print("\n Player 2 bingo: ")
        for i in self.__array2:
            for j in i:
                print(j,end=" ")
            print()

object1=Bingo()

while True:

    count=0
    while(count%2==0):
        print("PLayer 1: ")
        print('''\n Enter number for operation 
              1 for putting number in your bingo, 
              2 for bingo display,
              3. for exit.,
    ''')
        x=int(input())
        if(x==1):
            object1.fill_grid1()
        if(x==2):
            object1.display_grid_1()
        if(x==3):
            count+=1
        if(x>3 and x<1):
            print("Invalid operation  ")

    while(count%2!=0):
        print("Player 2: ")
        print('''\n Enter number for operation 
              1 for putting number in your bingo, 
              2 for bingo display,
              3. for exit.,
    ''')
        x=int(input())
        if(x==1):
            object1.fill_grid2()
        if(x==2):
            object1.display_grid_2()
        if(x==3):
            count+=1
        if(x>3 and x<1):
            print("Invalid operation  ")


        
