import re

def validate_order_input(symbol, side, order_type, quantity, price=None):
    # Validate CLI inputs before sending to the API.

    # 1. Symbol validation (e.g., BTCUSDT)
    if not re.match(r"^[A-Z0-9]{5,12}$", symbol.upper()):
        return False, f"Invalid symbol format: {symbol}"

    # 2. Side validation
    if side.upper() not in ["BUY", "SELL"]:
        return False, f"Side must be BUY or SELL, got: {side}"

    # 3. Order Type validation
    if order_type.upper() not in ["MARKET", "LIMIT"]:
        return False, f"Type must be MARKET or LIMIT, got: {order_type}"

    # 4. Quantity validation
    try:
        if float(quantity) <= 0:
            return False, "Quantity must be greater than zero."
    except ValueError:
        return False, "Quantity must be a numeric value."

    # 5. Price validation (for LIMIT)
    if order_type.upper() == "LIMIT":
        if not price:
            return False, "Price is required for LIMIT orders."
        try:
            if float(price) <= 0:
                return False, "Price must be greater than zero."
        except ValueError:
            return False, "Price must be a numeric value."

    return True, None