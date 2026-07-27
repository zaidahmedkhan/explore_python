# print the multiplication for a given number upto 10. but skip the fifth iteration.

number = int(input("Enter the number: "))

for i in range(1, 11):
    if(i ==5):
        continue
    print(number, 'x', i , '=', (number * i))