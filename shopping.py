file = open("shoppinglist.txt, w")
file.write("milk")
file.write("fruit")
file.write("nuts")
file.close()


file=open("shoppinglist.txt, r")
print("my shopping list")
print(file.read())

file=open("shopinglist.txt")
file.write("cheese")
file.write("juice")



file = open("shoppinglist.txt")
print("updated shopping list")
for item in file:
    print(item.strip())
