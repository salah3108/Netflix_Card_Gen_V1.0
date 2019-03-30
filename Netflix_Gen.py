if __name__ == "__main__":
    # execute only if run as a script
    main()
    
from colorama import init
init()
import random

random_letter= ['A', 'Z', 'E', 'R', 'T', 'Y', 'U', 'I', 'O', 'P', 'Q', 'S', 'D', 'F', 'G', 'H', 'J', 'K', 'L', 'M', 'W', 'X', 'C', 'V', 'B', 'N']

colorred = "\033[01;31m{0}\033[00m"
x=int(input("Enter How Many Card You Want : "))
counter=0
print(" ")
file=open("Netflix_Card.txt", "w+")
while counter < x :
    numburs = random.randint(0, 9)
    Fixed_Data = ("LEQ")
    Big_number = random.randint(0, 999999)
    value= random.choice(random_letter)
    print(colorred.format( Fixed_Data+str(numburs)+value+str(Big_number)))
    counter+=1
    file.write(Fixed_Data+str(numburs)+value+str(Big_number)+"\n")
file.close()
print("\n")
print(colorred.format("Created By Salah Belaid"))
input("Print Any Key To Exit")







