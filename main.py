userInput = input("Just write some text: ")

file = open("text.txt", 'a')
file.write(userInput + '\n')

file.close()
