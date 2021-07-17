import ccxt
import config
from ccxt.binance import binance

# print(ccxt.exchanges)  # print a list of all available exchange classes
# for exchange in ccxt.exchanges:
#    print(exchange)


exchange = ccxt.binance(
    {"apiKey": config.BINANCE_API_KEY, "secret": config.BINANCE_SECRET_KEYi}
)


markets = exchange.load_markets()

ticker = exchange.fetch_ticker("FTT/USDT")

print(ticker)

## Open, High, Low,
ohlc = exchange.fetch_ohlcv("ETH/USDT")
print(ohlc)

for candle in ohlc:
    print(candle)
