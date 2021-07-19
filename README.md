# PokeAPI


## Install


### Create virtualenv
```
$ pyenv virtualenv pokeapi
```

### Install dependencies

```
$ pyenv activate pokeapi
$ pip install -r requirements.txt
```

### Run migrations
```
$ ./manage.py migrate
```

### Run tests
```
$ pytest
```

###


### Retrieve and save pokemons and evolutions from evolution chain with id=10

```
$ ./manage.py save_pokemon 10
```


### Start server
```
$ ./manage.py runserver
```

### Read info about `pichu` pokemon from our API
```
Entrar a la URL

http://localhost:8000/api/pokemon/pichu
```


### Run formater, flake and tests
```
$ chmod +x build.sh
$ ./build.sh
```
