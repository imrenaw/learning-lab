userInput = input("Write anything you want: ")
try:
    userInput = int(userInput)
    print("You entered number:", userInput)
except ValueError:
    print("Error! It's not a number!")
finally:
    print("End of the programm!")