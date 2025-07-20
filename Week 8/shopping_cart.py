# Create a shopping cart program that will continuously ask the user for a food product and the price of the product
# Have an exit clause if the user wishes to stop adding more things to their cart
# At the end show the food items and the total cost to the user

product = []
price = []
total = 0

while True:
    item = input("Enter item name you want to buy or enter 'Q' to quit: ")
    if item.lower() == 'q':
        break
    else:
        itemPrice  = float(input(f"Enter price of the item({item}) you're buying R"))
        product.append(item)
        price.append(itemPrice)

print("------ CART PRODUCTS -------")

for itm in product:
    print(itm, end= " ")

for prc in price:
    total += prc

print("\n")
print(f"Total: R{total}")
        