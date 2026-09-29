def calculate_order_total(order):
    total = 0

    for item in order["items"]:
        price = item["price"]
        quantity = item["qty"]

        if price > 0:
            if quantity > 0:
                total = total + price * quantity

    if order["member"] == True:
        if total > 100:
            discount = total * 0.2
        else:
            if total > 50:
                discount = total * 0.1
            else:
                discount = 0
    else:
        discount = 0

    total = total - discount

    if order["country"] == "PK":
        shipping = 5
    else:
        if order["country"] == "US":
            shipping = 15
        else:
            shipping = 25

    total = total + shipping
    print("Total: " + str(total))
    return total