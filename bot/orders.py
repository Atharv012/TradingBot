from binance.enums import *

class OrderManager:
    def __init__(self, binance_client):
        self.client = binance_client

    def place_futures_order(self, symbol, side, order_type, quantity, price=None):
        # Handle placement of Market and Limit orders.

        try:
            # Prepare arguments
            params = {
                "symbol": symbol.upper(),
                "side": side.upper(),
                "type": order_type.upper(),
                "quantity": quantity,
            }

            if order_type.upper() == "LIMIT":
                if not price:
                    raise ValueError("Price is required for LIMIT orders.")
                params["price"] = price
                params["timeInForce"] = TIME_IN_FORCE_GTC  # Good 'Til Canceled

            # Execute the order
            response = self.client.futures_create_order(**params)
            return {"success": True, "data": response}

        except Exception as e:
            return {"success": False, "error": str(e)}