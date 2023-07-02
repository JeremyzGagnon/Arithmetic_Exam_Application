import random, math


def main():
    # Check if input is 1 or 2
    while(True):
        print("""Which level do you want? Enter a number:
     1 - simple operations with numbers 2-9
     2 - integral squares of 11-29""")
        try:
            userChoice = int(input())
            if userChoice not in [1, 2]:
                print("Incorrect format.")
            else:
                break
        except ValueError:
            print("Incorrect format.")

    # Enter the mode specified by the user adn get his result from the test
    if userChoice == 1:
        description = "simple operations with numbers 2-9"
        result = simpleOperations()
    else:
        description = "integral squares of 11-29"
        result = integralSquaresOperations()

    # Ask the user to save his result to a file. Do nothing if user don't want to save to a file
    saveToFile = input(f"Your mark is {result}/5. Would you like to save the result? Enter yes or no.")
    if saveToFile in ["y", "yes", "YES", "Yes"]:
        usersName = input("What is your name?")
        usersFile = open("results.txt", mode="a")
        print(f"{usersName}: {result}/5 in Level {userChoice} ({description})", file=usersFile)
        print('The results are saved in "results.txt".')
        usersFile.close()



# Integral Squares mode
def integralSquaresOperations():
        correctAnswer = 0
        for i in range(5):
            randNum = random.randint(11, 29)
            result = math.pow(randNum, 2)
            print(randNum)
            # Checking if the user's input is in the wrigth format
            while (True):
                usersGuess = input()
                if usersGuess.__contains__("-"):
                    print("Incorrect format.")
                    continue
                if not usersGuess.isdecimal():
                    print("Incorrect format.")
                    continue
                else:
                    break
            # Check if the user's guess is the rigth answer to the equation
            if int(usersGuess) == result:
                print("Right!")
                correctAnswer += 1
            else:
                print("Wrong!")
        return correctAnswer

# Simple operations mode
def simpleOperations():
    correctAnswer = 0
    for i in range(5):
        # Selects random integer between 2 and 9 inclusive and one operator
        operand1 = random.randint(2, 9)
        operand2 = random.randint(2, 9)
        operands = ["+", "-", "*"]
        operand = operands[random.randint(0, 2)]

        print(str(operand1) + " " + operand + " " + str(operand2))
        # Do the arithmetic told by the operator
        if operand == "+":
            result = (operand1) + (operand2)
        elif operand == "-":
            result = (operand1) - (operand2)
        elif operand == "*":
            result = (operand1) * (operand2)

        # Checking if the user's input is in the wrigth format
        while(True):
            usersGuess = input()
            if usersGuess.__contains__("-"):
                break
            if not usersGuess.isdecimal():
                print("Incorrect format.")
                continue
            else:
                break
        # Check if the user's guess is the rigth answer to the equation
        if int(usersGuess) == result:
            print("Right!")
            correctAnswer += 1
        else:
            print("Wrong!")
    # print(f"Your mark is {correctAnswer}/5. Would you like to save the result? Enter yes or no.")
    return correctAnswer


if __name__ == '__main__':
    main()