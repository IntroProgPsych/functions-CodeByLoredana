# Write a function apply_vat(price) that returns the price including 19% VAT.
# Ask the user for a price and print the result.

# Write your code here:
def apply_vat(price):
    return price * 1.19

price = float(input("Enter a price:"))
print("Price includint VAT:", apply_vat(price))