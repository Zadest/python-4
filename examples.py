import os

# ----------------------------------------------------------

# Bisher
liste = []
for x in range(20):
    liste.append(x**2)

# list comprehensions mit 'range'
quadrat_liste = [x**2 for x in range(20)]
print(quadrat_liste)

# ----------------------------------------------------------
# Bisher
liste = []
for x in quadrat_liste:
    if x % 2 == 0:
        liste.append(x)

# list comprehension mit 'item in list'
quadrat_liste_even = [x for x in quadrat_liste if x % 2 == 0]
print(quadrat_liste_even)


# ----------------------------------------------------------
# Bisher
text_dateien = []
for datei_Name in os.listdir():
    if datei_Name.endswith(".txt"):
        text_dateien.append(datei_Name)

# Beispiel
text_dateien = [dateiName for dateiName in os.listdir() if dateiName.endswith(".txt")]
print(text_dateien)