import random
print("Heads: 1")
print("Tails: 0")
comp=random.randint(0,1)
dict={1 : "Head", 0 : "Tails" }
ch=int(input("Enter your choice: "))
if ch!=1 and ch!=0:
        print("Invalid input")
else:
        print(f"your choice : {dict[ch]}")
        print(f"comp choice : {dict[comp]}")
        if ch==comp:
            print("You Won")
        else:
            print("you Lose")
        

