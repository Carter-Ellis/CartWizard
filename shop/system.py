from .models import Cart, CartItem, Inventory

class ShopSystem:

    """Service class that handles cart checkout, inventory updates, payment validation."""

    def purchase_cart(self, cart: Cart) -> bool:
        pass
    
    def is_valid_funds(self, cart: Cart) -> bool:
        pass

    def update_inventory(self, cart: Cart) -> bool:
        pass

    def validate_cart(self, cart: Cart) -> bool:
        pass