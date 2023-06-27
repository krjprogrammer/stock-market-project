import requests
import smtplib
user_name = "xyz757363@gmail.com"
password = "rnkpkktajbxsmmim"
STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"
API_KEY_STOCK = "EKTHDYJIRCAJ4BNN"
API_KEY_NEWS = "19f6a0d0bb2f4e299801fa4a8a6e5d43"
STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"
parameters_stock = {
    "function":"TIME_SERIES_DAILY_ADJUSTED",
    "symbol":STOCK,
    "apikey":API_KEY_STOCK
}
parameters_news = {
     "apiKey":API_KEY_NEWS,
     "qInTitle":COMPANY_NAME
 }

response = requests.get(url=STOCK_ENDPOINT, params=parameters_stock)
data = response.json()
date_data_list = [value for(key,value) in data["Time Series (Daily)"].items()]
yesterday_closing_price = float(date_data_list[0]["4. close"])
day_before_yesterday_closing_price = float(date_data_list[1]["4. close"])
difference = yesterday_closing_price-day_before_yesterday_closing_price
state = None
if difference > 0:
    state = "🔺"
elif difference < 0:
    state = "🔻"
if round((abs(yesterday_closing_price-day_before_yesterday_closing_price)/yesterday_closing_price)*100) > 0.1 or round((abs(yesterday_closing_price - day_before_yesterday_closing_price) / yesterday_closing_price) * 100) > 0.1:
    news_response = requests.get(url=NEWS_ENDPOINT, params=parameters_news)
    news_data = news_response.json()["articles"][:3]
    formated_articles = [f"Headline:{data['title']} .\nBrief:{data['description']}" for data in news_data]
    print("hello")
    message = smtplib.SMTP("smtp.gmail.com")
    message.starttls()
    message.login(user=user_name, password=password)
    for article in formated_articles:
        message.sendmail(from_addr=user_name, to_addrs="krishnarajjadhav2003@gmail.com",
                        msg= f"TSLA: {state}5%\n {article}")

