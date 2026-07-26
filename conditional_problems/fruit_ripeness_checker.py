# Determine if a fruit is ripe, overripe or unripe based on its color. (eg Banana: green - unripe , yellow - ripe , brown -overripe)
fruit = input("Enter fruit name: ")
if (fruit.lower() != "banana"):
    print("No information available for this fruit")
    exit()

color = input("Enter fruit color: ")

if(color == "green"):
    print("unripe")
elif(color == "yellow"):
    print("ripe")
elif(color == "brown"):
    print("overripe")
else:
    print("No data available for this color")




