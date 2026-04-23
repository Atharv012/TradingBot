import argparse
import os
from dotenv import load_dotenv
from bot.client import BinanceTestnetClient
from bot.orders import OrderManager
from bot.validators import validate_order_input
from bot.logging_config import setup_logging
import logging

load_dotenv()

API_KEY = os.getenv("BINANCE_API_KEY") 
API_SECRET = os.getenv("BINANCE_API_SECRET_KEY")

def main():
    setup_logging()
    logger = logging.getLogger(__name__)

    parser = argparse.ArgumentParser(description="Binance Futures Testnet CLI Bot")
    parser.add_argument("--symbol", required=True, help="e.g. BTCUSDT")
    parser.add_argument("--side", required=True, choices=["BUY", "SELL"])
    parser.add_argument("--type", required=True, choices=["MARKET", "LIMIT"])
    parser.add_argument("--qty", required=True, type=float)
    parser.add_argument("--price", type=float, help="Required for LIMIT orders")

    args = parser.parse_args()

    # 1. Validate Input
    is_valid, error_msg = validate_order_input(args.symbol, args.side, args.type, args.qty, args.price)
    if not is_valid:
        print(f"Validation Error: {error_msg}")
        return

    # 2. Initialize Client
    print(f"--- Order Request Summary ---")
    print(f"Symbol: {args.symbol} | Side: {args.side} | Type: {args.type} | Qty: {args.qty}")
    
    bot_client = BinanceTestnetClient(API_KEY, API_SECRET)
    order_manager = OrderManager(bot_client.get_client())

    # 3. Place Order
    logger.info(f"Placing {args.type} {args.side} order for {args.symbol}")
    result = order_manager.place_futures_order(
        symbol=args.symbol,
        side=args.side,
        order_type=args.type,
        quantity=args.qty,
        price=args.price
    )

    # 4. Handle Response
    if result["success"]:
        data = result["data"]
        print("\nSUCCESS")
        print(f"OrderID: {data.get('orderId')}")
        print(f"Status: {data.get('status')}")
        print(f"Executed Qty: {data.get('executedQty')}")
        print(f"Avg Price: {data.get('avgPrice', 'N/A')}")
        logger.info(f"Order Successful: {data['orderId']}")
    else:
        print(f"\nFAILURE: {result['error']}")
        logger.error(f"Order Failed: {result['error']}")

if __name__ == "__main__":
    main()