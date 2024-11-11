import requests

url = 'https://magicloops.dev/api/loop/run/c2403195-1385-4493-a1f5-3bfd83b79ff1'
payload = { 'input': 'I love Magic Loops!' }

response = requests.get(url, json=payload)
responseJson = response.json()
print(f"STATUS: {responseJson['status']}")
print(f"OUTPUT: {responseJson['loopOutput']}")