import requests
from bs4 import BeautifulSoup as soup
import smtplib as sm
from twilio.rest import Client
import datetime

date = datetime.datetime.now()
today = date.strftime("%A ,%d ,%B ,%Y")

url = "https://coinmarketcap.com/"

#set your price milestone
chk_amount_bitcoin = #for bitcoin
chk_amount_eth = #for eth

#getting website html data
r= requests.get(url)
content = soup(r.content,"html.parser")
 
#get prices from the url
bitcoin_price = content.find("tr", id="id-bitcoin").find("a", class_="price").text.strip()
ethereum_price = content.find("tr", id="id-ethereum").find("a", class_="price").text.strip()

#compare and send notifications
_bitcoin =  bitcoin_price.split("$")[-1]
_bitcoin = _bitcoin.split(".")[0]
if int(_bitcoin) <= chk_amount_bitcoin:
  #send email
  conn = sm.SMTP("smtp.gmail.com", 587)
  conn.ehlo()
  conn.starttls()
  # set your email and password here
  conn.login(".......@gmail.com", '*******')
  message = '%s\n bitcoin price: %s' % (today,bitcoin_price)
  conn.sendmail('......@gmail.com', '.......@gmail.com',
                'Subject: Cypto Notification\n\n%s' % (message)) #set your emails here
  conn.quit()
  #text
  account_sid = "" #input your twillo account details
  auth_token = ""  # input your twillo account details
  client = Client(account_sid, auth_token)
  message = client.messages.create(
      to="+..........",
      from_="+.......",
      body=message) #set number to send to and twillo number too

_ethereum = ethereum_price.split("$")[-1]
_ethereum = _ethereum.split(".")[0]
if int(_ethereum) <= chk_amount_eth:
  conn = sm.SMTP("smtp.gmail.com", 587)
  conn.ehlo()
  conn.starttls()
  conn.login(".........@gmail.com", '*******')#set your email and password here
  message = '%s\n ethereum price: %s' % (today,ethereum_price)
  conn.sendmail('......@gmail.com', '.......@gmail.com',
                'Subject: Cypto Notification\n\n%s' % (message))  # set your emails here
  conn.quit()
  #text
  account_sid = ""  # input your twillo account details
  auth_token = ""  # input your twillo account details
  client = Client(account_sid, auth_token)
  message = client.messages.create(
      to="+..........",
      from_="+.......",
      body=message)  # set number to send to and twillo number too
exit()
