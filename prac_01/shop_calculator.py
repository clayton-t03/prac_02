total_price = 0
number_of_items = int(input("How many Items are there: "))
while number_of_items < 1:
    number_of_items = int(input("INVALID INPUT; How many Items are there: "))
for i in range(0, number_of_items, 1):
    item_price = float(input("Item price $"))
    total_price += item_price
if total_price > 100:
    total_price = total_price * 0.9
print(f"Your total price is ${total_price:.2f}")