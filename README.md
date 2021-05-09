This is a sample app for django, it fetch data from https://pokeapi.co/ and serves it into a api.

## Usage

* Installation
    ```bash
    python -m pip install -r requirements.txt
    ```

* Read the data and storage it locally.

    ```bash
    python manage.py fetch_evolution_chain 2
    ```

* Run the webserver

    ```bash
    python manage.py runserver 0.0.0.0:8000
    ```

* Watch all pokemons

    http://localhost:8000:api/pokemon/


* Watch a pokemon by name

    http://localhost:8000:api/pokemon/chameleon/