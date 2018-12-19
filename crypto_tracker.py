import requests
bitcoin_api_url = 'https://api.coinmarketcap.com/v1/ticker/bitcoin/'
request = requests.request('GET', bitcoin_api_url)
print(request)