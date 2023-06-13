current_price = float(input("Enter the current price: "))
last_month_price = float(input("Enter the last month price: "))

mortgage = current_price * 0.051 / 12
change_value = last_month_price - mortgage

print("This house is $", current_price, ". The change is $", change_value, " since last month.")
print("The estimated monthly mortgage is $", mortgage)
