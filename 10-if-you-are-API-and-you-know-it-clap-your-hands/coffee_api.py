import requests
import subprocess


url = 'https://coffee.alexflipnote.dev/random.json'

r = requests.get(url)
print(r)
obj = r.json()
print(obj)
print(obj['file'])
image = obj['file']

subprocess.run(['firefox', image])