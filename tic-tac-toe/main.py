class tic_tac_toe:

    def __init__(self):
        self.__array=[[0]*3 for _ in range(3)]

    def fill_tic_tac(self,x,y,data):
        self.__array[x][y]=data

    def display(self):
        print("[",end="")
        print()
        for r in self.__array:
            for c in r:
                print(c,end="   ")
            print()
        print("]",end="")
        print()
object1=tic_tac_toe()

while True:

    number =int(input("Enter the number 1 to add ,2 to exit : "))
    if(number==1):
        x=int (input("Enter x coordinate with in range 0 to 2 : "))
        print()
        y=int(input("Enter y coordinate with in range 0 to 2 : "))
        print()
        data=int(input("Enter data : "))
        object1.fill_tic_tac(x,y,data)
        object1.display()
    if(number==2):
        print("Exiting the game ")
        break
    if(number>2 and number<1):
        print("Invalid number ")
    
        

    
    
        
        







