import requests

r = requests.get('https://api.isevenapi.xyz/api/iseven/6/')
obj = r.json()
print(obj['iseven'])

number_of_facts = input("How many cat facts do you want to know? : ")
url = "https://meowfacts.herokuapp.com/"
arguments = {'count': number_of_facts}
r = requests.get(url, params=arguments)
obj = r.json()
for fact in obj['data']:
    print(fact)
