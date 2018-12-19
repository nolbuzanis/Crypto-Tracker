import requests
bitcoin_api_url = 'https://api.coinmarketcap.com/v1/ticker/'
response = requests.request('GET', bitcoin_api_url)
data = response.json()
print(data[0:2])