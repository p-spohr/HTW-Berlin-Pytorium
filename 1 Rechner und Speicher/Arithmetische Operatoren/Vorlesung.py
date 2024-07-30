# %% 

# Addition
4 + 5 

# %%

# Subtraction
1 - 3

# %%

# Multiplikation
3 * 15

# %%

# Division
1 / 3

# Division ergibt immer ein float
10 / 2

# %%

# Exponetial
2**2

# %%

# Operatorrangfolge 
# 1 Arithmetik
# 2 Vergleich
# 3 Logik
# 4 Bitwise
# 5 Initialisierung

# %%

# Klammern > Exponenten > Multiplikation und Division > Addition und Subtraktion
# das Erste ergibt 6, aber das Zweite ergibt 10
1 + 1 * 5
(1 + 1) * 5

# %%

# Arithmetik vor Logik => falsch
1 == 1 + 1

# %%

# ==, ist gleich, funktioniert mit Buchstaben oder Wörter
'abc' == 'abc'

# %%

# != heißt nicht gleich wie
'dog' != 'cat'

# %%

# + kann Liste konkatenieren
[1,2,3,4] + [1]

# %%

# + kann auch Wörter konkatenieren
'Hello' + ' ' + 'World' + '!'
# aber das ist nicht die beste Methode diese Ergebnis zu bekommen
# str.format() oder f'' ist besser und wir lernen das in Daten Strukturen

# %%

# VORSICHTIG!
# [1,2,3,4] + 1 ist ein Fehler, weil Listen nicht vektorisiert sind
# man braucht List-Comprehension, map() oder numpy.array 
# wir besprechen das tiefer in Datenstrukturen

[x + 1 for x in [1,2,3,4]]


# %%

# Konsolenausgabe 
# man braucht print, um etwas im Shell zu zeigen
# hier haben wir die Interactive View und ist es nicht notwendig
print("Hi!")

# %%

# * kann String duplizieren
print("Hi" + "!" * 5)


# %%

# String sind eine Zeichenketten
# [0] ist die erste Kettenglied
# Bemerkung: der Index beginnt mit 0 nicht 1
"12345"[0]

# %%

# minus Index fängt von das Ende an
"12345"[-1]