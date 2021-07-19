# PokeAPI


## Instalar


### Crear entorno virtual
```
$ pyenv virtualenv pokeapi
```

### Instalar dependencias

```
$ pyenv activate pokeapi
$ pip install -r requirements.txt
```

### Correr las migraciones
```
$ ./manage.py migrate
```

### Correr tests
```
$ pytest
```


### Precargar informacion de los pokemons de la cadena de evolucion con id=10

```
$ ./manage.py save_pokemon 10
```


### Iniciar servidor
```
$ ./manage.py runserver
```

### Leer informacion sobre `pichu`
```
Entrar a la URL

http://localhost:8000/api/pokemon/pichu
```


