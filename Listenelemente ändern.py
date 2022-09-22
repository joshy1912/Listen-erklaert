 #Um den Wert eines bestimmten Elements zu ändern, beziehen Sie sich auf die Indexnummer:
 
thislist = ["apple", "banana", "cherry"]
thislist[1] = "blackcurrant"
print(thislist)

#Um den Wert von Elementen innerhalb eines bestimmten Bereichs zu ändern, definieren Sie eine Liste mit den neuen Werten und 
# beziehen Sie sich auf den Indexnummernbereich, in den Sie die neuen Werte einfügen möchten:
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "mango"]
thislist[1:3] = ["blackcurrant", "watermelon"]
print(thislist)

#Wenn Sie mehr Elemente einfügen als ersetzen, werden die neuen Elemente dort eingefügt, wo Sie es angegeben haben, und die verbleibenden
#  Elemente werden entsprechend verschoben:
thislist = ["apple", "banana", "cherry"]
thislist[1:2] = ["blackcurrant", "watermelon"]
print(thislist)

#Hinweis: Die Länge der Liste ändert sich, wenn die Anzahl der eingefügten Elemente nicht mit der Anzahl der ersetzten Elemente übereinstimmt.

#Wenn Sie weniger Elemente einfügen, als Sie ersetzen, werden die neuen Elemente dort eingefügt, wo Sie es angegeben haben, 
#und die verbleibenden Elemente werden entsprechend verschoben:
thislist = ["apple", "banana", "cherry"]
thislist[1:3] = ["watermelon"]
print(thislist)

#Um ein neues Listenelement einzufügen, ohne einen der vorhandenen Werte zu ersetzen, können wir die insert()Methode verwenden.
#Die insert()Methode fügt ein Element am angegebenen Index ein:
thislist = ["apple", "banana", "cherry"]
thislist.insert(2, "watermelon")
print(thislist)

#Um ein Element am Ende der Liste hinzuzufügen, verwenden Sie die Methode append() :
thislist = ["apple", "banana", "cherry"]
thislist.append("orange")
print(thislist)

#Verwenden Sie die Methode , um Elemente aus einer anderen Liste an die aktuelle Liste anzuhängen .extend()
thislist = ["apple", "banana", "cherry"]
tropical = ["mango", "pineapple", "papaya"]
thislist.extend(tropical)
print(thislist)

#Die remove()Methode entfernt das angegebene Element.
thislist = ["apple", "banana", "cherry"]
thislist.remove("banana")
print(thislist)

#Die pop()Methode entfernt den angegebenen Index.
thislist = ["apple", "banana", "cherry"]
thislist.pop(1)
print(thislist)

#Wenn Sie den Index nicht angeben, pop()entfernt die Methode das letzte Element.
thislist = ["apple", "banana", "cherry"]
thislist.pop()
print(thislist)

#Das delSchlüsselwort entfernt auch den angegebenen Index:
thislist = ["apple", "banana", "cherry"]
del thislist[0]
print(thislist)

#Das del Schlüsselwort kann die Liste auch komplett löschen.
thislist = ["apple", "banana", "cherry"]
del thislist

#Die clear()Methode leert die Liste.
thislist = ["apple", "banana", "cherry"]
thislist.clear()
print(thislist)