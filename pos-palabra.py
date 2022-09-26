list = ["a", "b", "c", "d"]
word = "abccccda"

# m = aridad n = longitud

# Algoritmo que calcula el numero de palabras min(len(word)) [(m^n - 1 ) / (m - 1)]


def wordsMin(m: int, n: int):
    return int((pow(m, n)-1)/(m-1))

# Algoritmo que calcula el numero de palabras con len(word) [m^n]


def wordsLen(m: int, n: int):
    return pow(m, n)

# Algortimo que calcula el numero de palabras que preseden a la pablbra "word" en el alfabeto "l"


def calcToWord(l: list, word: str):
    # Cálcula las palabras que son min(word)
    # m = aridad [pow(len(l)], n = longitud [len(word)]
    min = (pow(len(l), len(word))-1)/(len(l)-1)

    # Entero que devolverá el número de palabras anteriores
    before = 0
    # Se volea la palabra pues el sistem numerico es posicional e inicia por el final
    wordReverse = word[::-1]
    # Algoritmo que calcula el número de palabras anteriores (Paso 5)
    for i in range(len(word)):
        before += pow(len(l), i) * l.index(wordReverse[i])
    return int(min), before, int(min + before)


print(calcToWord(list, word))
print(wordsLen(4, 6))
print(wordsMin(4, 6))
