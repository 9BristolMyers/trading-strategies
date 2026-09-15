import yfinance as yf

# My test: $100 on bank account vs $100 in the Apple stock for 1 year
apple = yf.download("AAPL", period="1y")['Close']

# Bank gives 3% annually
bank_final = 100 * 1.03

# Apple stock: if I bought 1 year ago
apple_start = float(apple.iloc[0])
apple_end = float(apple.iloc[-1])
apple_final = 100 * (apple_end / apple_start)

print(f"Bank after 1 year: ${bank_final:.2f}")
print(f"Apple after 1 year: ${apple_final:.2f}")
print(f"Difference: ${apple_final - bank_final:.2f} more with Apple")
