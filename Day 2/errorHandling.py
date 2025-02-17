
# This Python code prompts the user to enter the price of a product and prints the entered price.
# If the user enters a non-numeric value, an error message is displayed.

# Prompt the user to enter the product price.
try:
	product_price = float(input("Enter product price: "))
	# Print the entered product price.
	print(product_price)
# Handle the case where the user enters a non-numeric value.
except ValueError:
	print("Invalid input. Please enter a numeric value for product price.")

# This code will not raise an error because the user will enter a numeric value for the product price