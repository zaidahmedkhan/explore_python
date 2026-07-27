# given a string, find the first non repeated character

inputString = input("Enter the string: ")
for char in inputString:
    if(inputString.count(char) == 1):
        print("non repeated character is", char)
        break
    
