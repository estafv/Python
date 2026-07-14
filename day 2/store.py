#Let's build a robot Barista!!

print("Hello, Welcome to the Robot Barista!")

name = input("What is your name? ")

print("Hello " + name + ", thank you so much for coming in today!")

menu = "Latte"
price = 5

print("Today's menu:")
print(menu)

order = input("What would you like to order? ")

quantity = input("How many Lattes would you like? ")

total = price * int(quantity)

print("Thank you. Your total is: $" + str(total))

print("Thank you for your order of " + str(quantity) + " " + order + ", it will be ready shortly!")