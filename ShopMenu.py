
hot_brews={
    "Black Tea":299,
    "Latte":395,
    "Cappuccino":370,
    "Americano":375,
    "Espresso":350
}
cravings={
    "Brownie":299,
"Choco Chip Cookies":399,
"Choco Lava Cake":499,
"Blueberry Muffin":599,
}
menu = hot_brews | cravings

print("  __   WELCOME TO RISHU'S BISTRO!!!.......   __")
print("Our special hot serves: ",hot_brews)
print("Your cravings served are : ",cravings)
option1=input("Enter your first item: ")
option2=input("Enter your second item: ")
more=input("Do you want any other items??")
if(more=="yes"):

     option3=input("Enter your third item: ")
     option4=input("Enter your fourth item: ")
     option5=input("Enter your fifth item: ")
     print("Let's do the total...")
     total=menu[option1]+menu[option2]+menu[option3]+menu[option4]+menu[option5]
     print(total)
    
else:
     print("Let's do the total....")
     total=menu[option1]+menu[option2]
     print(total)

   
