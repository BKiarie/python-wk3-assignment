def calculate_discount(price, discount_percent):
    if discount_percent >= 35:
        final_price = price - (price * discount_percent / 100)
        return final_price
    return price


original_price = 1000
discount = 35
final_price = calculate_discount(original_price, discount)
print(f"Final price: ${final_price:.2f}")

# the final price is $650.00
