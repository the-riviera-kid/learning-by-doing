import urllib.request # actually communicates with websites
import json # module to convert to/from json (web data)

# Open a URL 
with urllib.request.urlopen("https://api.isevenapi.xyz/api/iseven/6/") as u:
    obj = json.load(u)
    print(obj['iseven'])


number_of_facts = input("How many cat facts do you want to know? : ")
url = f"https://meowfacts.herokuapp.com/?count={int(number_of_facts)}"
with urllib.request.urlopen(url) as u:
    obj = json.load(u)
    for fact in obj['data']:
        print(fact)
