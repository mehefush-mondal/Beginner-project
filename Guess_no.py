import random

def num():
    guess = random.randint(1, 100)
    count = 0
    while True:
        try:
            number=int(input("Guess a Number between 1 and 100="))
            count+=1
            if (number==guess):
                print("Congratulations!\nYou guessed correctly.")
                print("Number of attempts taken to guess =",count)
                if (count<=5):
                    print("Excellent")
                elif(count<=10):
                    print("Good")
                elif(count<=20):
                    print("Average")
                elif(count>20):
                    print("Keep Practicing")
                break
            elif (number>guess):
                print(" Too High, Try again!")
            else:
                print(" Too Low, Try again!")
        except ValueError:
            print("Enter a valid Number")
while True:
    num()
    again = input("Do another guess? (y/n): ").lower()
    while again not in ("y", "n"):
        again = input("Please enter y or n: ").lower()
    if again == "n":
        print("Thanks for playing!")
        break