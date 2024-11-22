#!/usr/bin/env python
# coding: utf-8

# 2.1 - 2.2 Aufgaben
# 
# Diese Aufgaben sind länger als Lernzielkontrolle und fassen alle Themen aus 2.1 und 2.2 zusammen.
# Lösen Sie diese Aufgabe in VS Code oder in Jupyter Notebook.

# # Aufgabe 1

# ## 1.1 Initialisieren Sie eine Liste mit fünf Namen

# In[214]:


namen = ['Tim', 'Nina', 'Sara', 'Alexander', 'Katja']


# In[215]:


namen


# ## 1.2 Fügen Sie noch einen Name der Liste hinzu.

# In[216]:


namen.append('John')


# In[217]:


namen


# ## 1.3 Drucken Sie jede Name aus.

# In[218]:


for name in namen:
    print(name)


# ## 1.4 Drucken Sie die erste Buchstabe von jede Name aus.

# In[219]:


for name in namen:
    print(name[0])


# ## 1.5 Speichern Sie jede Name als ungekehrt in einer neuen Liste und drucken Sie gleichzeitig jeden Name aus.
# 

# In[220]:


ungekehrt = []
for name in namen:
    print(name[::-1])
    ungekehrt.append(name[::-1])    


# In[221]:


print(ungekehrt)


# ## 1.6 Löschen Sie alle Elemente in der neuen ungekehrten Liste.

# In[222]:


ungekehrt.clear()
print(ungekehrt)


# # Aufgabe 2

# ## 2.1 Initialisieren Sie eine Liste von 0 bis 50.

# In[223]:


num_liste = list(range(0,51))


# In[224]:


print(num_liste[0:10])
print(num_liste[-10::])
print(len(num_liste))


# ## 2.2 Ordnen Sie die List von absteigend zu.

# In[225]:


num_absteigend = num_liste[::-1]


# In[226]:


print(num_absteigend[0:10])
print(num_absteigend[-10::])


# ## 2.3 Drucken Sie jede gerade Zahl aus, die nicht ein Teiler von zehn ist.

# In[227]:


num_gerade = num_liste[::2] # noch eine Methode, aber es funktioniert nur, wenn die Liste schon zugeordnet ist.


# In[228]:


print(num_gerade[0:10])
print(num_gerade[-10::])


# In[229]:


for num in num_liste:
    if num % 2 == 0 and num % 10 != 0:
        print(num)


# ## 2.4 Drucken Sie jede ungerade Zahl quadriert aus, die nicht ein Teiler von fünf ist.

# In[230]:


for num in num_liste:
    if num % 2 != 0 and num % 5 != 0:
        print(num)


# # Aufgabe 3 

# ## 3.1 Initialisieren Sie eine Liste von 0 bis 1 mit 0.01 Schrittgröße   

# In[231]:


num_init = range(0,101, 1)
schritt_num = []
for i in num_init:
    neu = i / 100
    schritt_num.append(neu)


# In[232]:


print(schritt_num[0:10])
print(schritt_num[-10::])


# In[233]:


len(schritt_num)


# ## 3.2 Drucken Sie ein Liste der kumulative Summe aus.

# In[234]:


# 1. Methode mit geschachtelten Schleifen
summe_1 = []
temp = 0
for i in range(1,len(schritt_num)+1,1):
    for y in schritt_num[0:i]:
        temp += y
    summe_1.append(round(temp,4))
    temp = 0
print(summe_1)


# In[235]:


print(sum(schritt_num))


# In[236]:


# 2. Methode mit Hilfe sum() von die Standardbibliothek
summe_2 = []
x_1 = schritt_num.copy()
j = 1
for i in x_1:
    summe_2.append(round(sum(x_1[0:j]),4))
    j+=1 


# In[237]:


print(summe_2)


# In[238]:


# 3. Methode mit einer while-Schleife
summe_3 = []
x_2 = schritt_num.copy()
temp = 0
while len(x_2) > 0:
    temp += x_2.pop(0)
    summe_3.append(round(temp, 4))


# In[239]:


print(summe_3)


# In[240]:


# 4. Methode ohne eine neue Liste mit Hilfe enumerate()
x_3 = schritt_num.copy()
temp = 0
for index, num in enumerate(x_3):
    temp += num
    x_3[index] = round(temp, 4)


# In[241]:


print(x_3)


# # Aufgabe 4

# ## 4.1 Initialisieren Sie eine Liste von Dict mit 10 Leute: Name, Age und Haustier (Hund oder Katze)

# 1. Benutzen Sie die Namen von früher plus vier mehr. 
# 2. Das Alter ist 5 mal die Anzahl der Buchstaben.
# 3. Alle Leute mit ein 'a' in ihrem Name hat ein Hund, sonst Katze
# 4. Drucken Sie alle Daten in vernünftigen Sätze aus.

# In[242]:


namen


# In[243]:


namen_2 = namen + ['Jose', 'Mei', 'Thor', 'Mary']


# In[244]:


namen_2


# In[245]:


gruppe = []


# In[246]:


for name in namen_2:
    person = {}
    person['name'] = name
    person['alter'] = len(name) * 5
    if 'a' in name:
        person['haustier'] = 'Hund'
    else: 
        person['haustier'] = 'Katze'
    gruppe.append(person)


# In[247]:


for person in gruppe:
    print(person.keys())


# In[248]:


for person in gruppe:
    if person['haustier'] == 'Hund':
        art = 'einen'
    else:
        art = 'eine'
    print(f'{person['name']} ist {person['alter']} Jahre alt und hat {art} {person['haustier']}.')

