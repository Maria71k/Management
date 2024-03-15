class Inventory:
    def __init__(self):
        self.inventory = {}

    def add_product_stock(self, product, quantity):
        self.inventory[product.id] = {"product": product, "quantity": quantity}

    def display_inventory(self):
        print("Inventory:")
        for product_id, item in self.inventory.items():
            print(f"{item['product'].name} - Quantity: {item['quantity']}")

# Example usage:
inventory = Inventory()
inventory.add_product_stock(Product(1, "T-shirt", 20, "Comfortable cotton T-shirt"), 50)
inventory.add_product_stock(Product(2, "Jeans", 40, "Classic denim jeans"), 30)
inventory.display_inventory()
