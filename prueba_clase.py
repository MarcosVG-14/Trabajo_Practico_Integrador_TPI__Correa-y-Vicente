def calculo_estadisticas(lista):
    """promedio_poblacion = sum(p["poblacion"] for p in lista) / len(lista)
    promedio_superficie = sum(p["superficie"] for p in lista) / len(lista)"""
    menor_poblacion = lista[0] # {"pais":"Argentina","poblacion":"45000000"}
    mayor_poblacion = lista[0] # {"pais":"Argentina","poblacion":"45000000"}
    for p in lista:
        if p["poblacion"] > mayor_poblacion["poblacion"]:
            mayor_poblacion = p
        if p["poblacion"] < menor_poblacion["poblacion"]:
            menor_poblacion = p
    print(f"""El pais {menor_poblacion["pais"]} tiene {menor_poblacion["poblacion"]} habitantes
El pais {mayor_poblacion["pais"]} tiene {mayor_poblacion["poblacion"]} habitantes""")

if __name__=="__main__":
    paises_total=[{"pais":"Argentina","poblacion":"45000000"},
                  {"pais":"Chile","poblacion":"28962431"},
                  {"pais":"Peru","poblacion":"486413278315"},
                  {"pais":"Colombia","poblacion":"2"}]
    calculo_estadisticas(paises_total)