"""Super awesome couopon deals"""

def calculate_order(price, cash_coupon, percent_coupon):
    subtotal = 0
    total = 0
    shipping = 0
    price = float(price)
    cash_coupon = float(cash_coupon)
    percent_coupon = float(percent_coupon)
    tax = 0.06
    if not price < cash_coupon:
        if cash_coupon is not None:
            if percent_coupon is not None:
                discount_percent = price * (percent_coupon * .01)
                subtotal = (price - cash_coupon) - discount_percent
            else:
                subtotal = (price - cash_coupon)
        else:
            subtotal = price
    else:
        subtotal = 0

    if price <= 10:
        shipping = 5.95
    elif price <= 30:
        shipping = 7.95
    elif price <= 50:
        shipping = 11.95
    elif price > 50:
        shipping = 0

    total = subtotal + shipping
    final_total = total + (total * tax)
    return final_total


if __name__ == "__main__":
    cash = input("How much was your purchase: ")
    cash_coupon = input("How much was your cash coupon: ")
    percent_coupon = input("How much was your percent coupon:")
    print("Your total is " + calculate_order(cash, cash_coupon, percent_coupon).__str__())
