import random

# Sample product database with stock and categories
products = {
    "apple": {"price": 1.0, "description": "A fresh and juicy apple.", "stock": 10, "category": "Fruits"},
    "banana": {"price": 0.5, "description": "A ripe yellow banana.", "stock": 15, "category": "Fruits"},
    "orange": {"price": 0.8, "description": "A sweet and tangy orange.", "stock": 12, "category": "Fruits"},
    "milk": {"price": 1.5, "description": "A bottle of fresh milk.", "stock": 8, "category": "Dairy"},
    "bread": {"price": 2.0, "description": "A loaf of whole grain bread.", "stock": 5, "category": "Bakery"}
}

# Discount codes
discount_codes = {
    "SAVE10": 0.10,  # 10% discount
    "SAVE20": 0.20   # 20% discount
}

cart = []
order_history = []

def show_products(category=None):
    print("\nAvailable products:")
    for item, details in products.items():
        if category is None or details["category"].lower() == category.lower():
            print(f"- {item.title()}: ${details['price']} - {details['description']} (Stock: {details['stock']})")

def check_price(product_name):
    product = products.get(product_name.lower())
    if product:
        return f"The price of {product_name.title()} is ${product['price']}"
    else:
        return "Sorry, we don't have that product."

def add_to_cart(product_name, quantity):
    product = products.get(product_name.lower())
    if product:
        if quantity <= product["stock"]:
            cart.append((product_name, quantity))
            product["stock"] -= quantity  # Reduce stock
            return f"Added {quantity} x {product_name.title()} to your cart."
        else:
            return f"Sorry, we only have {product['stock']} of {product_name.title()} in stock."
    else:
        return "Sorry, we don't have that product."

def show_cart():
    if not cart:
        return "Your cart is empty."
    else:
        cart_summary = "Your cart:\n"
        total = 0
        for item, quantity in cart:
            price = products[item]["price"] * quantity
            cart_summary += f"- {quantity} x {item.title()} - ${price}\n"
            total += price
        cart_summary += f"Total: ${total:.2f}"
        return cart_summary

def apply_discount(total, code):
    discount = discount_codes.get(code.upper())
    if discount:
        total -= total * discount
        return total, f"Discount code '{code}' applied successfully! You saved {discount * 100}%."
    else:
        return total, "Invalid discount code."

def checkout():
    if not cart:
        return "Your cart is empty. Add some products to proceed to checkout."
    else:
        total = sum(products[item]["price"] * quantity for item, quantity in cart)
        
        # Apply discount if the user has a code
        discount_code = input("Enter a discount code if you have one, or press Enter to skip: ").upper()
        total, discount_message = apply_discount(total, discount_code)
        print(discount_message)
        
        # Record order history and clear cart
        order_history.append(cart.copy())
        cart.clear()
        
        return f"Thank you for your purchase! Your total is ${total:.2f}."

def show_order_history():
    if not order_history:
        return "No previous orders found."
    else:
        history = "Order history:\n"
        for order_num, order in enumerate(order_history, 1):
            history += f"\nOrder {order_num}:\n"
            for item, quantity in order:
                history += f"- {quantity} x {item.title()} at ${products[item]['price']} each\n"
        return history

# Main chatbot loop
def shop_chatbot():
    print("Welcome to the enhanced online shop! How can I assist you today?")
    
    while True:
        user_input = input("\nYou: ").lower()  # Normalize user input to lowercase
        
        if "show products" in user_input:
            if "category" in user_input:
                category = user_input.split("category")[-1].strip()
                show_products(category)
            else:
                show_products()
        
        elif "price" in user_input:
            product_name = user_input.split("price of")[-1].strip()
            print("Chatbot:", check_price(product_name))
        
        elif "add to cart" in user_input:
            parts = user_input.split(" ")
            product_name = parts[3]  # Assuming "add X to cart"
            try:
                quantity = int(parts[1])  # Extract quantity
                print("Chatbot:", add_to_cart(product_name, quantity))
            except ValueError:
                print("Chatbot: Please specify a valid quantity to add.")
        
        elif "show cart" in user_input:
            print("Chatbot:", show_cart())
        
        elif "checkout" in user_input:
            print("Chatbot:", checkout())
        
        elif "order history" in user_input:
            print("Chatbot:", show_order_history())
        
        elif "quit" in user_input or "exit" in user_input:
            print("Chatbot: Thank you for visiting the shop. Goodbye!")
            break
        
        else:
            print("Chatbot: I didn't understand that. You can ask for 'show products', 'price of [product]', 'add [quantity] [product] to cart', 'show cart', 'checkout', 'order history', or 'quit'.")

# Run the chatbot
shop_chatbot()
