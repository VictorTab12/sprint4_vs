import requests

params = {
    "engine": "google_shopping",
    "q": "Austin Spurs Uniform",
    "location": "Austin, Texas, United States",
    "hl": "en",
    "gl": "us",
    "api_key": "2f2afff318fb54275b1c90320748f68c46177611d91b99c226a4101debd44cd0"
}

response = requests.get("https://serpapi.com/search", params=params)
results = response.json()

print("Status Code:", response.status_code)
print("Response Headers:", response.headers)
print("Response JSON:", results)

# Acessar as categorias nos resultados
categories = results.get("categories", [])
print("Categories:", categories)
