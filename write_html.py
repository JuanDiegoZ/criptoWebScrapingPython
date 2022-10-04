import requests
html_file = requests.get('https://www.binance.com/en/price/bitcoin').text


with open('home.html','w') as file:
    try:
        file.write(html_file)
    finally: 
        file.close()