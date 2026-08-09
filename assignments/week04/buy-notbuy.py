prices = []
print("Enter prices of 6 items:")
for i in range(6):
    price = float(input(f"Item {i + 1}: "))
    prices.append(price)


budget = float(input("\nEnter total budget: "))

bought_items = []
current_total = 0

print()

for i in range(6):
    item_price = prices[i]

    if current_total + item_price <= budget:
        current_total += item_price
        bought_items.append(item_price)
        print(f"Item {i + 1} = {item_price:.0f} -> buy")
    else:
        print(f"Item {i + 1} = {item_price:.0f} -> cannot buy")

    print(f"Current total = {current_total:.0f}")

print(f"\nBought items: {[int(p) for p in bought_items]}")
print(f"Total spent: {current_total:.0f}")
print(f"Remaining budget: {budget - current_total:.0f}")