from binance.client import Client
import logging

class BinanceTestnetClient:
    def __init__(self, api_key, api_secret):
        self.client = Client(api_key, api_secret, testnet=True)
        self.logger = logging.getLogger(__name__)

    def get_client(self):
        return self.client

    def test_connection(self):
        try:
            account_info = self.client.futures_account()
            self.logger.info("Successfully connected to Binance Futures Testnet.")
            return True
        except Exception as e:
            self.logger.error(f"Connection failed: {e}")
            return False