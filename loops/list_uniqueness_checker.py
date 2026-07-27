# check if all elements in a list are unique. if duplicate is found exit the loop and print the duplicate

items = ['apple', 'banana', 'mango', 'orange', 'apple', 'grapes']

unique_item = set()

for item in items:
    if(item in unique_item):
        print("duplicate item: ", item)
        break
    unique_item.add(item)
    print(unique_item)