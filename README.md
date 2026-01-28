# Proyecto 3 -Procesar registros

Este proyecto está desarrollado en Python. Procesa una lista de registros de eventos internos proveniente de distintas áreas.
    
    
## Funcionalidad principal

- Solo se consideran registros:
  - Cuyo estado sea "válido"
  - Los eventos deben ser mayor a 0
  - La gravedad debe ser "media" o "alta"
  - Los registros con clave faltante se ignoran


- Retorna:

  - Un diccionario con un resumen por área acumulando el total de eventos y la cantidad de registros válidos.


## Estructura de salida:

    {
        "Area": {"total_eventos": int, 
                "registros_contados": int},
    }



## Ejemplo de uso

```python

# Crear un archivo nuevo en la misma carpeta, por ejemplo test.py
from procesar_registros.py import registro_de_eventos


datos_area = [ 

    {"area": "IT", "eventos": 1, "gravedad": "media", "estado": "valido"},
    {"area" : "Soporte", "eventos": 2, "gravedad": "leve", "estado": "invalido"}, 
    {"area" : "IT", "eventos": 1, "gravedad": "leve", "estado": "valido"},
    {"area" : "RRHH", "eventos": 1, "gravedad": "media", "estado": "invalido"},
    {"area" : "Atención al cliente", "eventos": 2, "gravedad": "alta", "estado": "valido"},
    {"area" : "IT", "eventos": 4, "gravedad": "alta", "estado": "valido"},
    {"area" : "Atención al cliente", "eventos": 3, "gravedad": "media", "estado": "valido"},
    {"area": "IT", "eventos": 2, "gravedad": "media", "estado": "valido"}
    ]


resumen_final = registro_de_eventos(datos_area)
print(resumen_final) # Salida esperada  {'IT': {'total eventos': 7, 'registros contados': 3}, 'Atención al cliente': {'total eventos': 5, 'registros contados': 2}}

```