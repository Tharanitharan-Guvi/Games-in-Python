import random

def computer_play():
    return random.choice([1,2,3])

print("1. Stone     2.Paper     3. Scissor")

while True:
    option = int(input("Select any one from the above:  "))
    comp = computer_play()
    print("Computer has picked", comp)
    if option == comp:
        print("Draw")
    
    elif option == 1 and comp == 2:
        print("Computer Wins")
    
    elif option == 1 and comp == 3:
        print("You have won!")
    
    elif option == 2 and comp == 1:
        print("You have won!")
    
    elif option == 2 and comp == 3:
        print("Computer Wins")
    
    elif option == 3 and comp == 1:
        print("Computer Wins")
    
    elif option == 3 and comp == 2:
        print("You have won!")

    print()
    print("Do you want to continue? 1.Yes   2.No")
    flag = int(input())
    if flag == 2:
        break
