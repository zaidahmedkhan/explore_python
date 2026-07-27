# Recommend a type of pet food based on the pets species and age. (eg dog <2 years - puppy food, cat >5 years - senior cat food )

petName = input("Enter pet food: ")
petAge = int(input("Enter pet age: "))

if(petName == "dog" and petAge < 2):
    print("puppy food ")
elif(petName == "dog" and petAge >= 2):
    print("senior dog food ")
elif(petName == "cat" and petAge <= 5):
    print("kitten food ")
elif(petName == "cat" and petAge > 5):
    print("senior cat food ")        