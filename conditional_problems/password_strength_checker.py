# check if a password is 'weak' , 'medium' or 'strong'. criteria < 6 chars (weak), 6-10 chars (medium), > 10 chars (strong)
password = input("enter your password")
password_length = len(password)

if(password_length < 6):
    strength = "weak"
elif(password_length <= 10):
    strength = "medium"
else:
    strength = "strong"

print("your password strength is ", strength)    
