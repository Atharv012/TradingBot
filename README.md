# Binance Futures Testnet Trading Bot

A structured Python application to interact with the Binance Futures Testnet (USDT-M). This project was built as part of the Python Developer Intern assessment for Primetrade.ai.

## 🚀 Features
- **Core Trading**: Place MARKET and LIMIT orders for any USDT-M pair.
- **Validation**: Strict input validation for symbols, quantities, and prices before API calls.
- **Logging**: Full audit trail of API requests, responses, and errors saved to `trading_bot.log`.
- **Dual Interface**: 
    - **CLI**: Professional command-line interface using `argparse`.
    - **UI**: Interactive web dashboard built with **Streamlit**.

## 🛠️ Setup Instructions

1. **Clone the Repository**
   ```bash
   git clone <your-repo-link>
   cd trading_bot

2. **Environment Setup**
    Create a virtual environment and install dependencies:
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows: venv\Scripts\activate
    pip install -r requirements.txt

3. **API Credentials**
    Create a .env file and place the API_KEY and API_SECRET there for running the bot via cli or enter them directly in the Streamlit sidebar. Ensure you are using Binance Futures Testnet keys.

## 📈 How to Run

    **Option 1: Command Line Interface (CLI)**
    ***Market Order:***
    ```bash
    python cli.py --symbol BTCUSDT --side BUY --type MARKET --qty 0.001

    ***Limit Order:***
    ```bash
    python cli.py --symbol BTCUSDT --side SELL --type LIMIT --qty 0.001 --price 75000

    **Option 2: Streamlit UI**
    ```bash
    streamlit run UI.py

## 📝 Assumptions & Notes

    - **Lot Size**: The bot assumes the user provides a quantity that meets the symbol's minimum lot size requirements on the Binance Testnet (e.g., 0.001 for BTC).

    - **Testnet**: The application is hardcoded to use the Binance Futures Testnet environment for safety.

    - **Logging**: JSON-formatted logs are used for API requests and responses to ensure high readability and traceability.

## 📁 Project Structure

    **bot/client.py**: Handles connection and authentication.

    **bot/orders.py**: Core logic for order placement and response handling.

    **bot/validators.py**: Input scrubbing and error prevention.

    **bot/logging_config.py**: Centralized logging configuration.

    **cli.py**: The main entry point for command-line usage.

    **UI.py**: The web UI wrapper.

