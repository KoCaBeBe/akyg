import requests
url="https://api.coinlore.net/api/exchanges/"
response=requests.get(url)
data=response.json()
print(data)
