STOCK = "RELIANCE.BSE"
COMPANY_NAME = "RELIANCE INDUSTRIES"

## STEP 1: Use https://www.alphavantage.co
# When STOCK price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").

## STEP 2: Use https://newsapi.org
# Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME. 

## STEP 3: Use https://www.twilio.com
# Send a seperate message with the percentage change and each article's title and description to your phone number. 


#Optional: Format the SMS message like this: 
"""
TSLA: 🔺2%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
or
"TSLA: 🔻5%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
"""


from datetime import *
import requests




parameters = {
    "function":"TIME_SERIES_DAILY_ADJUSTED",
    "symbol":STOCK,
    "apikey":"5RJSKWCJEBLO8NF1"
}

response = requests.get(url="https://www.alphavantage.co/query", params=parameters)
data = response.json()['Time Series (Daily)']
response.raise_for_status()
# print(response.status_code)

data_list = [value for (key,value)in data.items()]
yesterday_cp = (data_list[0]["4. close"])
day_before_yesterday_cp = (data_list[1]["4. close"])

change  = ((float(yesterday_cp)-float(day_before_yesterday_cp)))
if change >0:
    up_down = "🔺"
else:
    up_down = "🔻"
print(change)
percentage_change = abs((change/float(day_before_yesterday_cp))*100)
print(percentage_change)

if (percentage_change)> 0:
    parameters = {
        "qinTitle" :COMPANY_NAME,
        "apiKey":"790be82cc6d84e7ba18bc30036ac7c6e",
        "language":"en",    
    }
    response = requests.get(url="https://newsapi.org/v2/everything", params=parameters)

    response.raise_for_status()
    data = response.json()["articles"]
    three_articles = data[:3]

    # print(three_articles )
formatted_articles =  [f"{STOCK} {up_down} {percentage_change} % \nHeadlines: {articles['title']}. \nBrief: {articles['description']}" for articles in three_articles]

for text in formatted_articles:
    print(text)








