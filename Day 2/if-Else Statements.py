try:
    product_price = float(input("Product Price enter here."))
    delivery_charges = int(input("Delivery"))

    if product_price < 20:
        total: float = product_price + delivery_charges
        print("Total: ", total)
    elif product_price >= 20 and product_price < 50:
        total: float = product_price + (product_price * 0.1) + delivery_charges
        print("Discounted total: ", total)
except ValueError:
    print("Error: Please enter valid numbers")
