import random 
hidden_number = random.randrange(1,10) #random range bewtween 1-10

num = int(input("Enter a number betweeen 1-10: ")) #enter a number between 1-50
while int(num) != hidden_number:  #loops if the number is lower than the hidden number
        if int(num) > hidden_number:    #loops if the number is lower than the hidden number
            num=(int(input("Please try again. Enter a lower number: "))) #response for entering a lower number and allows user to input another number
        elif int(num) < hidden_number: #if the number is lower than hidden number loop
            num=(int(input("Please try again. Enter a higher number: "))) #response for entering a lower number and allows user to input another number
        #else:  #if the number is guess correctly response is executed and game is over
                #if num == hidden_number:
                    #print("YOU WIN!!!" "You guessed the right number")

if int(num) == hidden_number: #if the number is guess correctly response is executed and game is over
    print("YOU WIN!!!" "You guessed the right number")


