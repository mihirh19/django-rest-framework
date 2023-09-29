import requests

# URL for the web
endpoints  = "http://localhost:8000/api"

get_response  = requests.get(endpoints)
print(get_response.json())