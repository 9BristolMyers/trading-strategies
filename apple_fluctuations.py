import yfinance as yf

#Download Apple stock prices for the year
data = yf.download("AAPL", period="1y")['Close']

#How the prices change every day
data = data.to_frame(name='Close')
data['Daily_Change'] = data['Close'].pct_change()

#My condition – if the price goes down by 5% today, I buy tomorrow at a cheaper price
data['Crash_Happened'] = data['Daily_Change'] < -0.05

# What if I buy after crash?
data['My_Profit'] = data['Crash_Happened'].shift(1) * data['Daily_Change']

print(f"Times Apple crashed >5%: {int(data['Crash_Happened'].sum())}")
print(f"Profit if bought after crash: {data['My_Profit'].sum():.2%}")
