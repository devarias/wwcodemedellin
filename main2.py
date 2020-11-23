# This is a sample Python script.
import pandas


def generar_dataframe_palabras(text):
    new_text = text.lower().replace(",", "").replace(".", "").strip().split()
    diccionario_ocurrencias = {}
    for word in new_text:
        diccionario_ocurrencias[word] = new_text.count(word)
    dataframe = pandas.DataFrame(diccionario_ocurrencias, index=[0])
    return dataframe


neruda = """Puedo escribir los versos más tristes esta noche.
            Yo la quise, y a veces ella también me quiso.
            En las noches como ésta la tuve entre mis brazos.
            La besé tantas veces bajo el cielo infinito.
            
            Ella me quiso, a veces yo también la quería.
            Cómo no haber amado sus grandes ojos fijos.""".lower()  # lower hace que todas las letras sean minúsculas.

if __name__ == '__main__':
    d = generar_dataframe_palabras(neruda)
    assert isinstance(d, pandas.DataFrame), "Aun no generas un Dataframe, verifica tu algoritmo!"
    print("Excelente, has convertido un poema en un Dataframe para trabajar con el!")