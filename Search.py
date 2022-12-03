from googlesearch import search

query = 'India vs New Zeland todays match'

for url in search(query):
    print(url)
