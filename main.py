import random
print("===== WELCOME TO ROLL DICE APP =====\n")
while 1:
    print("Hi, you can either;")
    print("1. Roll the dice")
    print("2. Exit")
    entry = int(input("Enter preference:- "))
    if entry == 1:
        print(f"Roll no. generated is, {random.choice([1, 2, 3, 4, 5, 6])}")
        break
    elif entry == 2:
        break
    else:
        print("Error!")
        break

