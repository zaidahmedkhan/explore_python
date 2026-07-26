# Movie tickets are priced based on age: $12 for adults (18 and over), $8 for children. Everyone gets a $2 discount on wednesday.
from datetime import date

age = int(input("Enter your age: "))
day = date.today().strftime("%A")
price = 12 if age >= 18 else 8

if(day == "Wednesday"):
    price -= 2

print("Ticket for you is $",price)    

