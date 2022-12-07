import random as r 
random_num = r.randint(1, 100)
print(random_num)

guess = input ("Enter a Number :")

while int(guess) != random_num:
    print("Wrong!")
    if int(guess) > random_num:
        print("Too High!")
    else: 
        print ("Too Low!")
        
