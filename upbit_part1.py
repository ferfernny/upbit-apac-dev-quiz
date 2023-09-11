import pandas as pd
import requests
url = "https://th-api.upbit.com/v1/candles/days?market=THB-BTC&count=200"
response = requests.get(url)
response.raise_for_status() 
json_data = response.json()  
df = pd.DataFrame(json_data)
print(df)
###############section1##################
timestamps = []
opens = []
highs = []
lows = []
closes = []
for candle in json_data:
	timestamps.append(candle['candle_date_time_utc'])
	opens.append(candle['opening_price'])
	highs.append(candle['high_price'])
	lows.append(candle['low_price'])
	closes.append(candle['trade_price'])
df = pd.DataFrame({'timestamp': timestamps,'open': opens,'high': highs,'low': lows,'close': closes})
print("I am df "+str(df))
###############section2################
#Calculate and display the following statistics from the DataFrame:
max_close_price = df['close'].max()
max_close_date = df[df['close'] == max_close_price]['timestamp'].values[0]
min_close_price = df['close'].min()
min_close_date = df[df['close'] == min_close_price]['timestamp'].values[0]
avg_close_price = df['close'].mean()
print("I am Maximum closing price: "+str(max_close_price)+" on date "+str(max_close_date))
print("I am Minimum closing price: "+str(min_close_price)+" on date "+str(min_close_date))
print("I am Average closing price: "+str(avg_close_price))
###############section 3###############
df['price_change'] = abs(df['close'] - df['open'])
print("I am df with price_change \n"+str(df))
###############section 4###############
filtered_df = df[df['price_change'] > 1000]
print("I am df with filterd price change more than 1000 \n"+str(filtered_df))
###############section 5###############
correlation = df['price_change'].corr(df['high'])
print("Correlation between price_change and high columns:"+str(correlation))
##############section 6################
filtered_df.to_csv('upbit_data.csv', index=False)
print("I am processing dataframe to csv")
##############end of part1#############