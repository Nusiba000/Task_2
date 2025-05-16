#shopping 

food_list = []
price_list = []
total = 0

while True:
    food = input("Enter the food you buy (when you finish enter done): ")
    if food.lower() == "done":
        break
    else:
        price = float(input(f"Enter the price of {food}: OMR"))

    food_list.append(food)
    price_list.append(price)

print("-----YOUR CART-----")
for food in food_list:
    print(food, end=" ")

for price in price_list:
    total += price

print()
print(f"Your total is:{total}OMR")


    
    



