# Project Name

This is a sample project showcasing the usage of Flask API.

## Installation

1. Clone the repository.
2. Navigate to the project directory.
3. Install the required dependencies using the following command:

```shell
pip install -r requirements.txt
```

## Usage

To launch the Flask API, use the following command:

```shell
flask --app api --debug run
```
# Project Name

This is a sample project showcasing the usage of Flask API.

## Installation
1. Clone the repository.
2. Navigate to the project directory.
3. Create a virtual environment and activate it.
```shell
python -m venv venv
source .venv/bin/activate
```
4. Install the required dependencies using the following command:
```shell
pip install -r requirements.txt
```

## Usage
To launch the Flask API, use the following command:
```shell
flask --app api --debug run
```

## API Endpoints
- `/`: Hello world.
- `/pokemonfight`: Pokemon fight.
```shell
http://127.0.0.1:5000/pokemon?pokemona=pikachu&pokemonb=bulbasaur
```

## Test
You can call the endpoint from the CLI
```shell
# For iOS and Linux
curl "http://127.0.0.1:5000/pokemon?pokemona=pikachu&pokemonb=bulbasaur"
```

## Contributing
Contributions are welcome! Please follow the guidelines outlined in CONTRIBUTING.md.

## License
This project is licensed under the [MIT License](LICENSE).