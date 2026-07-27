# choose a mode of transportation based on the distance (e.g, < 3 km: walk, 3- 15km; bike, >15:car)

distance = int(input("Enter distance: "))

if(distance <3):
    transportationMode = "walk"
elif(distance <= 15):
    transportationMode = "bike"
else:
    transportationMode ="car"    


print("Your suitable transportation mode is $", transportationMode)