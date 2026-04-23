import streamlit as st
from bot.client import BinanceTestnetClient
from bot.orders import OrderManager
from bot.validators import validate_order_input
from bot.logging_config import setup_logging
import logging

setup_logging()
logger = logging.getLogger(__name__)

# --- Page Config ---
st.set_page_config(page_title="Binance Futures Bot", page_icon="📈")
st.title("🤖 Binance Futures Trader")

# --- Sidebar: API Credentials ---
with st.sidebar:
    st.header("Settings")
    api_key = st.text_input("API Key", type="password")
    api_secret = st.text_input("API Secret", type="password")

# --- Main UI ---
col1, col2 = st.columns(2)

with col1:
    symbol = st.text_input("Symbol", value="BTCUSDT")
    side = st.selectbox("Side", ["BUY", "SELL"])

with col2:
    order_type = st.selectbox("Order Type", ["MARKET", "LIMIT"])
    quantity = st.number_input("Quantity", min_value=0.0, step=0.001, format="%.3f")

price = None
if order_type == "LIMIT":
    price = st.number_input("Limit Price", min_value=0.0, step=0.1)

if st.button("Place Order", use_container_width=True):
    logger.info(f"UI Trigger: Placing {order_type} {side} for {symbol}")
    if not api_key or not api_secret:
        st.error("Please enter your API credentials in the sidebar.")
    else:
        # 1. Validate
        is_valid, error_msg = validate_order_input(symbol, side, order_type, quantity, price)
        
        if not is_valid:
            st.warning(f"Validation Error: {error_msg}")
        else:
            # 2. Execute
            with st.spinner("Executing order..."):
                bot_client = BinanceTestnetClient(api_key, api_secret)
                order_manager = OrderManager(bot_client.get_client())
                
                result = order_manager.place_futures_order(
                    symbol=symbol, side=side, order_type=order_type, quantity=quantity, price=price
                )

            # 3. Display Results
            if result["success"]:
                logger.info(f"Order Successful: {result["data"]['orderId']}")
                st.success(f"Order Placed Successfully!")
                st.json(result["data"])
            else:
                logger.error(f"Order Failed: {result['error']}")
                st.error(f"Order Failed: {result['error']}")