# SHOPPING RECEIPT

def calculate_subtotal(items):
    subtotal = 0
    for item in items:
        subtotal += item["price"] * item["quantity"]

    return subtotal

def calculate_discount(subtotal):
    amount = subtotal

    if 1000 < subtotal < 2999:
        discount = 5
        amount = amount - amount*0.05
    elif subtotal > 3000:
        discount = 10
        amount = amount - amount*0.1
    else:
        discount = 0

    return [f"{discount}", amount]

def calculate_tax(amount, tax_rate):
    amount = amount + amount*tax_rate

    return amount

def genenrate_receipt(items, tax_rate):
    subtotal = calculate_subtotal(items)
    [discount, amount] = calculate_discount(subtotal)
    final_amount = calculate_tax(amount, tax_rate)

    return f"Subtotal: {subtotal}\ndiscount: {discount}%\ntax: {tax_rate}\nFinal Amount: {final_amount}"


items = [
    {"name": "Notebook", "price": 880, "quantity": 3},
    {"name": "Pen", "price": 150, "quantity": 5},
    {"name": "Belete", "price": 800, "quantity": 3},
    {"name": "Belayneh", "price": 50, "quantity": 5},
    {"name": "OMG", "price": 810, "quantity": 3},
    {"name": "Ohh", "price": 125, "quantity": 5},
    {"name": "whatup", "price": 830, "quantity": 3},
    {"name": "hey", "price": 115, "quantity": 5}
]
tax_rate = 0.15

print(genenrate_receipt(items, tax_rate))