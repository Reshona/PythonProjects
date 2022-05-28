import random # import the random module
list1= random.sample(range(1,11),10)  # create the list for random values
num = random.choice(list1) #guess this number
for i in range(0,5):
    print ("Enter your guess attempt", i+1)
    enterednum = int(input())
    if enterednum == num:
        print ("congratulations, you have guessed the number on attempt", i+1)
        break
    elif enterednum > num:
        print ("your guess is higher than the actual number, guess again\t(Chances left",4-i,")")
    elif enterednum < num:
        print ("your guess is lower than the actual number, guess again\t(Chances left",4-i,")")   
    else:
        print("incorrect guess, please keep guessing\t(Chances left",4-i,")")
