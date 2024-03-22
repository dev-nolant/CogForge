import requests 

#importing the module that will allow me to send HTTP requests

import json

#serialization of data?

url = "https://matchilling-chuck-norris-jokes-v1.p.rapidapi.com/jokes/random"
headers = {
    'accept' : 'application/json',
    'X-RapidAPI-Key' : '45e3a15de5msh8e1bddba2b07657p1adc4bjsn4eedcce2fd56',
    'X-RapidAPI-Host' : 'matchilling-chuck-norris-jokes-v1.p.rapidapi.com'
}

response = requests.get(url, headers=headers, timeout=60)

if response.status_code == 200:
    #print(response.json())
    pretty_output = json.dumps(response.json(), indent=4)
    
    print(pretty_output)
else:
    print(f"It didn't work: {response.status_code}")
