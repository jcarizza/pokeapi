



# Implementar comando que recibe un ID que identifica al recurso cadena de evolution

Ahi comenzamos a obtener informacion sobre esa cadena de evolucion y el pokemon al 
que corresponde esa cadena de evolucion

Evolution chain endpint [evolution-chain]
https://pokeapi.co/api/v2/evolution-chain/{id}/

Pokemon info [pokemon]
https://pokeapi.co/api/v2/pokemon/{id or name}/


Valores a guardar:
• Name (Se obviene de evolution-chain)
• Base stats (for the 6 categories) (Se obtiene de pokemon.stats)
• Height (Se obtiene de pokemon)
• Weight (Se obtiene de pokemon)
• Id (Se obtiene de pokemon)
• Evolutions 
  - Pre evolucion o pos evolucion (pichu, pikachu, raichu) (Ej: para pikachu, pichu es pre evolution y raichu es pos)
  - species.name
  - id species.url y leer el ID


# Crear endpoing que reciba el nombre del pikachu y retorne toda esta info
