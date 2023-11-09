#1. a Generieren Sie alle Primzahlen, die kleiner als eine natürliche Zahl n sind.
n = int(input("Enter a number: "))
for i in range(2, n + 1):
    is_prime = 1
    for d in range(2, i // 2 + 1):
        if i % d == 0:
            is_prime = 0
            break  # se opreste daca gaseste un divizor
    if is_prime == 1:
        print(i, end=" ")

#1. b längste ansteigende zusammenhängende Teilfolge

def secventa_cu_lungime_maxima(v):
     if not v:
         return[]

     lung_act = 1
     lung_max = 1
     secv_act = [v[0]]
     secv_max = [v[0]]

     for i in range (1, len(v)):
         if v[i-1] <= v[i]:
             lung_act += 1
             secv_act.append(v[i]) # fals der nexte nummer größer als der nummer ist, man fugt der nummer in der act liste
         else:
             if lung_max < lung_act:
                 lung_max = lung_act
                 secv_max = secv_act
             lung_act = 1
             secv_act = [v[i]] #reluam secventa actuala de la capat
     if lung_max < lung_act:
         secv_max = secv_act
     return secv_max

v = [1, 2, 3, 4, 5, 0, 3, 2, 1] #ich habe zahlen auch ansteigend und auch absteigend genommen
final = secventa_cu_lungime_maxima(v) # apelam functia'secv...', si copiem intr-o lista finala rezultatul functiei
print('Die längste ansteigende zusammenhängende Teilfolge ',v,'ist:', final)

 # wir zeigen die längste ansteigende zusammenhängende Teilfolge  [1, 2, 3, 4, 5, 0, 3, 2, 1]  ist:  [1, 2, 3, 4, 5]

#2.a pascalsche dreieck
def generate_pascals_triangle(n):
    triangle = []
    for i in range(n):
        row = [1] * (i + 1) #jedes Element wird auf den Wert 1 gesetzt, um die erste und letzte 1 in jeder Zeile zu initialisieren
        triangle.append(row) #Die Zeile row wird zur Liste triangle hinzugefügt, um das Pascal'sche Dreieck zu erstellen.
        if i > 1:
            for j in range(1, i):
                triangle[i][j] = triangle[i - 1][j - 1] + triangle[i - 1][j] #In dieser Zeile wird der Wert in der aktuellen Zeile i und Spalte j berechnet, indem er gleich der Summe der Werte in der vorherigen Zeile i-1 und den benachbarten Spalten j-1 und j ist.
    return triangle

def print_pascals_triangle(triangle):
    max_width = len(' '.join(map(str, triangle[-1]))) #Hier wird max_width auf die Breite der längsten Zeile im Dreieck gesetzt. Es verwendet die letzte Zeile des Dreiecks, wandelt sie in einen Zeichenfolge um und berechnet die Länge der Zeichenfolge.
    for row in triangle:
        row_str = ' '.join(map(str, row)) #n jeder Schleifeniteration wird die Zeile row in eine Zeichenfolge row_str umgewandelt, wobei die Werte durch Leerzeichen getrennt werden.
        print(row_str.center(max_width))

n = int(input("Geben Sie die Anzahl der Zeilen für das Pascal'sche Dreieck ein: "))

if n <= 0:
    print("Die Anzahl der Zeilen muss größer als 0 sein.")
else:
    pascals_triangle = generate_pascals_triangle(n)
    print("\nPascal'sches Dreieck:")
    print_pascals_triangle(pascals_triangle)


#2.b längste zusammenhängende Teilfolge von Primzahlen
def ist_primzahl(zahl):
    if zahl <= 1:
        return False
    if zahl <= 3:
        return True
    if zahl % 2 == 0 or zahl % 3 == 0:
        return False
    i = 5
    while i * i <= zahl:
        if zahl % i == 0 or zahl % (i + 2) == 0:
            return False
        i += 6
    return True

def finde_laengste_primzahlen_teilfolge(zahlen):
    aktuelle_teilfolge = []
    laengste_teilfolge = []

    for zahl in zahlen:
        if ist_primzahl(zahl):
            aktuelle_teilfolge.append(zahl)
        else:
            if len(aktuelle_teilfolge) > len(laengste_teilfolge):
                laengste_teilfolge = aktuelle_teilfolge
            aktuelle_teilfolge = []

    if len(aktuelle_teilfolge) > len(laengste_teilfolge):
        laengste_teilfolge = aktuelle_teilfolge

    return laengste_teilfolge

# Beispiel-Vektor von Zahlen
zahlen = [1, 2, 3, 4, 5, 6, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47]

laengste_primzahlen_teilfolge = finde_laengste_primzahlen_teilfolge(zahlen)
print("Die längste zusammenhängende Teilfolge von Primzahlen ist:", laengste_primzahlen_teilfolge)
