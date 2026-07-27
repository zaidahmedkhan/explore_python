# calculate the factorial of number using a while loop.

number = int(input("Enter the number: "))
factorial = 1

while(number > 0):
    factorial *= number
    number -= 1
print("factorial is", factorial)    