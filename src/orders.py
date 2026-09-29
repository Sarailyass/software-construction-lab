def calculate_items_subtotal(order: dict) -> float:
    subtotal = 0.0

    for item in order["items"]:
        price = item["price"]
        quantity = item["qty"]

        if price > 0 and quantity > 0:
            subtotal = subtotal + price * quantity

    return subtotal


def calculate_member_discount(subtotal: float, is_member: bool) -> float:
    if not is_member:
        return 0.0

    if subtotal > 100:
        return subtotal * 0.2

    if subtotal > 50:
        return subtotal * 0.1

    return 0.0


def calculate_shipping_cost(country: str) -> int:
    if country == "PK":
        return 5

    if country == "US":
        return 15

    return 25


def calculate_order_total(order: dict) -> float:
    subtotal = calculate_items_subtotal(order)

    discount = calculate_member_discount(
        subtotal,
        order["member"],
    )

    shipping = calculate_shipping_cost(order["country"])

    total = subtotal - discount + shipping

    return total