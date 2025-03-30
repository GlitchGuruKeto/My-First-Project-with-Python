# Define the earnings for each item
bubblegum = 202
toffee = 118
ice_cream = 2250
milk_chocolate = 1680
doughnut = 1075
pancake = 80

# Calculate total income
total_income = bubblegum + toffee + ice_cream + milk_chocolate + doughnut + pancake

# Print the earned amounts and the total income
print("Earned amount:")
print("Bubblegum: $" + str(bubblegum))
print("Toffee: $" + str(toffee))
print("Ice cream: $" + str(ice_cream))
print("Milk chocolate: $" + str(milk_chocolate))
print("Doughnut: $" + str(doughnut))
print("Pancake: $" + str(pancake))
print("\nIncome: $" + str(total_income))

# Ask for staff expenses and other expenses
staff = int(input("Staff expenses: "))
other = int(input("Other expenses: "))

# Calculate net income
net_income = total_income - staff - other

# Print the net income
print("Net income: $" + str(net_income))
