# customize a coffee order: "small", " medium", or "large" with an option for "extra shot"of expresso.

extra_shot = True
order_size = "medium"

if(extra_shot == True):
    coffee = order_size + " coffe with an extra shot"
else:
    coffee = order_size + " coffee"
print(coffee)


