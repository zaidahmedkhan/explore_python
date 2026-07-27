# calculate the sum of even numbers upto the given number n

n = int(input("Enter number: "))
even_numbers_count = 0

for i in range(1 , n + 1):
    if(i % 2 == 0):
        even_numbers_count +=1

print("even numbers count is: ",even_numbers_count )        
