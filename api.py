#!/usr/bin/env python3.7
import requests
from flask import Flask, request, jsonify

app = Flask(__name__)

OPENAI_API_KEY = 'your-api-key-here'

@app.route("/")
def home():
    return "Flask Vercel Example - Hello World", 200

@app.errorhandler(404)
def page_not_found(e):
    return jsonify({"status": 404, "message": "Not Found"}), 404

@app.route("/pokemon", methods=['GET'])
def get_pokemon():
    pokemona = request.args.get('pokemona')
    pokemonb = request.args.get('pokemonb')

    response_a = requests.get(f'https://pokeapi.co/api/v2/pokemon/{pokemona}')
    response_b = requests.get(f'https://pokeapi.co/api/v2/pokemon/{pokemonb}')

    if response_a.status_code == 200 and response_b.status_code == 200:
        data_a = response_a.json()
        data_b = response_b.json()
        return jsonify({"pokemona": data_a, "pokemonb": data_b}), 200
    else:
        return jsonify({"status": 404, "message": "Pokemon not found"}), 404
    

@app.route("/pokemonfight", methods=['GET'])
def get_pokemon_fight():
    pokemona = request.args.get('pokemona')
    pokemonb = request.args.get('pokemonb')

    response_a = requests.get(f'https://pokeapi.co/api/v2/pokemon/{pokemona}')
    response_b = requests.get(f'https://pokeapi.co/api/v2/pokemon/{pokemonb}')

    if response_a.status_code == 200 and response_b.status_code == 200:
        data_a = response_a.json()
        data_b = response_b.json()

        ability_a = data_a['abilities'][0]['ability']['name']
        ability_b = data_b['abilities'][0]['ability']['name']

        chatgpt_response = requests.post(
            'https://api.openai.com/v1/engines/davinci-codex/completions',
            headers={'Authorization': f'Bearer {OPENAI_API_KEY}'},
            json={
                'prompt': f'Who would win in a fight, a {pokemona} with the ability {ability_a} or a {pokemonb} with the ability {ability_b}?',
                'max_tokens': 60
            }
        )

        if chatgpt_response.status_code == 200:
            chatgpt_data = chatgpt_response.json()
            return jsonify({"pokemona": data_a, "pokemonb": data_b, "fight_result": chatgpt_data['choices'][0]['text'].strip()}), 200
        else:
            return jsonify({"status": 500, "message": "ChatGPT API error"}), 500
    else:
        return jsonify({"status": 404, "message": "Pokemon not found"}), 404