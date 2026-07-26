# classify a person age's group: child(<13), Teenager(13-19), Adult(20-59), Senior(60+)

age = int(input("Enter Your age:"))

if(age < 13):
    print("child")
elif(age < 20):
    print("Teenager")
elif(age < 60):
    print("Adult")
else:
    print("Senior")    