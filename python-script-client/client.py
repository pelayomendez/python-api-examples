import requests
from requests.exceptions import RequestException

# Prompt the user to enter the names of two Pokémon
pokemon_a = input("Enter the name of the first Pokémon: ")
pokemon_b = input("Enter the name of the second Pokémon: ")

# Build the URL with the entered Pokémon names
url = f"http://127.0.0.1:5000/pokemon?pokemona={pokemon_a}&pokemonb={pokemon_b}"

# Make the cURL request
response = requests.get(url)

# Check if the request was successful
if response.status_code == 200:
    # Print the response content
    print(response.content.decode())
else:
    print("Error: Failed to make the request")

# Make the request to the server
def make_request(url):
    try:
        response = requests.get(url)
        response.raise_for_status()  # Raises a HTTPError if the status is 4xx, 5xx
    except RequestException as err:
        print(f"An error occurred: {err}")
        return None
    else:
        return response.json()  # or response.text, response.content, etc.

