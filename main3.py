import pandas as pd
import csv


def analizar_peliculas():
    caracteristicas = [20, 14, 2, 15, 16]
    with open('movies_metadata.csv') as file:
        csv_file = csv.reader(file)
        result = list(csv_file)
    diccionario = {}
    for i in range(1, len(result)):
        if int(result[i][15]) > 2000000 and int(result[i][2]) < 1000000:
            for c in caracteristicas:
                if result[0][c] in diccionario:
                    diccionario[result[0][c]].append(result[i][c])
                else:
                    diccionario[result[0][c]] = [result[i][c]]
    result = pd.DataFrame(diccionario)
    print(result)
    return result


if __name__ == '__main__':
    peliculas_resultantes = analizar_peliculas()
    assert isinstance(peliculas_resultantes, pd.DataFrame), "Tu función aun no devuelve un Dataframe!"
    assert peliculas_resultantes.shape[1] == 5, "Verifica que tu Dataframe solo contenga las columnas mencionadas"
    assert peliculas_resultantes.shape[
               0] == 3, "Creo que debes verificar los filtros, la cantidad de películas que cumple las condiciones no es correcta"
    print("Excelente, has aprendido a leer CSV's con python y como filtrarlos!")