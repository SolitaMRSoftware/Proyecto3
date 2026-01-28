def registro_de_eventos(lista_datos):

    """Procesa una lista de registros de eventos internos proveniente de distintas áreas y devuele un resumen por área acumulando el total de eventos y la cantidad de registros válidos.
    
    Reglas:
    -Solo se consideran registros cuyo estado sea "valido"
    - Los eventos deben ser mayor a 0
    -La gravedad debe ser "media" o "alta"
    -Los registros con clave faltante se ignoran

    Estructura de salida:

    {
        "Area": {"total_eventos": int, 
                "registros_contados": int},
    }
    
    """

    if not lista_datos:
        return {}
    
    resumen_final = {}
    

    for r in lista_datos:

        if "area" not in r or "eventos" not in r or "gravedad" not in r or "estado" not in r:
            continue

        if r["estado"] == "valido" and r["eventos"] > 0 and (r["gravedad"] == "media" or r["gravedad"] == "alta"):

            area = r["area"]
            eventos = r["eventos"]

            if area not in resumen_final:
                resumen_final[area] = {"total eventos": eventos,
                                        "registros contados": 1}
            else:
                resumen_final[area]["total eventos"] += eventos
                resumen_final[area]["registros contados"] += 1

    return resumen_final


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
print(resumen_final)