print("Welcome to the E-Supermarket")
print("What do you wish to buy?")
print("1.Fruits")
print("2.Vegetables")
print("3.Cereals")
print("4.Juice")
print("5.Beans")
print("6.Dairy Items")
f= input("Enter the section you need:")
if f == "fruits":
    print("How many kgs of apple you need?")
    apple = int(input(""))
    print("The apple cost is", apple*2, "euros")
    print("Thank you for purchased",apple, "kgs of apple")
      
elif f == "vegetables":
    print("How many kgs of cabbage you need?")
    cabbage = float(input(""))
    print("The apple cost is", cabbage*2.20, "euros")
    print("Thank you for purchased",cabbage, "kgs of cabbage")

elif f == "cereals": 
    print("How many kgs of packets you need?")
    cereals = float(input(""))
    print("The cereals cost is", cereals*3.10, "euros")
    print("Thank you for purchased",cereals, "packet of cereals")

elif f == "beans": 
    print("How many kgs of kgs you need?")
    beans = float(input(""))
    print("The beans cost is", beans*4.15, "euros")
    print("Thank you for purchased",beans, "kgs of beans")

elif f == "diary products":
    print("How many kgs of packets you need?")
    diary_products = float(input(""))
    print("The milk cost is", diary_products*1.10, "euros")
    print("Thank you for purchased",diary_products, "packet of milk")


