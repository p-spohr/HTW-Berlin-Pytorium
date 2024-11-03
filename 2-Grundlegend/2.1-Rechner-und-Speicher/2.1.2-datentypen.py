# Datatypen

# %%

# int
type(1)

# %%

# float
type(45.0032)

# %%

# str
type('Hi')

# %%

# bool
type(True)


# %%
# not kann das Gegenteil von bool ergeben
# False
not True

# %%

# True
not False


# %%

# rundet ab
int(3.9325)

# %%

# wandelt str in int um und dann Arithmetik
int('99') + 100

# %%

# man muss int umwandeln und dann konkatenieren
'Das Buch ist ' + str(300) + ' Seiten lang.'


# %%

# _ lässt sich als , in Zahlen zeigen.
# Viel einfacher lange Zahlen zu lesen!

2345234000.2345 == 2_345_234_000.2345

# %%

# str handelt int und float
'Der Anteil die Bevölkerung ist ' + str(5_532_000 / 341_040_001)


# %%

# Value Error!
int('0.50')

# float('0.50') ist richtig

