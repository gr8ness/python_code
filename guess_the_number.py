from random import randint
answer = (randint(1,3))

print("Guess the right number between 1-5")
number = int(input())
if number == answer:
   print("Congrats! You win!")
   exit()
else:
    print("Sorry,try again.")
number = int(input())
if number == answer:
       print("Congrats! You win!")
       exit()

else:
    print("Sorry,try again. This is your last chance.")
    number = int(input())
if number == answer:
       print("Congrats! You win!")

else:
    if number != answer:
        print("Sorry, you lose.")
    else: 
        if number == answer:
            print("Congrats! You win! I knew you could do it!")
        
