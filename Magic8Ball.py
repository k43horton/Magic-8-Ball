import time
import random
import sys

def main():
    possibleAnswers = ["It is certain.", "It is decidedly so.", "Without a doubt.", "Yes, Definitly.", "You may rely on it.", "As I see it, yes.", "Most Likely.", "Outlook Good.", "Yes.", "Signs point to yes.", "Reply hazy, try again.", "Ask again later.", "Better not tell you now.", "Cannot predict now.", "Concentrate and ask again", "Don't count on it.", "My reply is No.", "My sources say no.", "Outlook not so good.", "Very doubtful."]

    answer = random.choice(possibleAnswers)
                   
    print("Welcome to the Magic 8 Ball")
    input("Type Question and Press enter to shake the Magic 8 Ball!!! \n")
    
    print("The Magic 8 Ball is Shaking...")
    time.sleep(4)
    print(answer)

    print("Would you like to ask another question!!!")
    userchoice = (input("1 for yes, 2 for no \n"))

    if userchoice == "1":
        main()
    elif userchoice == "2":
        sys.exit()
    else:
        print("Invaid Answer")
        sys.exit()
                       
main()      
