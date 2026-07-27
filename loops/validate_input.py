# keep asking the user for input until they entered a number between 1 to 10

while True:
    number = int(input("Enter the number b/w 1 to 10: "))

    if(1 <= number <= 10):
        print("Thanks")
        break
    else:
        print("Invalid number. please try again!!")