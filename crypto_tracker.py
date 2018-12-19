import requests
bitcoin_api_url = 'https://api.coinmarketcap.com/v1/ticker/'
response = requests.request('GET', bitcoin_api_url)
data = response.json()
data_bitcoin = data[0]
data_ripple = data[1]
data_ethereum = data[2]

print(data_ethereum)