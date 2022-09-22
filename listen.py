#Um zu bestimmen, wie viele Elemente eine Liste hat, verwenden Sie die len()Funktion:
thislist = ["apple", "banana", "cherry"]
print(len(thislist))



#Sagt dir was dein liste für ein datentyp ist
mylist = ["apple", "banana", "cherry"]
print(type(mylist))

#Es ist auch möglich, den list()- Konstruktor beim Erstellen einer neuen Liste zu verwenden.
hislist = list(("apple", "banana", "cherry")) # note the double round-brackets
print(thislist)

#Hinweis: Das erste Element hat den Index 0.
thislist = ["apple", "banana", "cherry"]
print(thislist[1])

#Sie können einen Bereich von Indizes angeben, indem Sie angeben, wo der Bereich beginnen und wo er enden soll.
#Bei der Angabe eines Bereichs ist der Rückgabewert eine neue Liste mit den angegebenen Elementen.
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[2:5])



#Dieses Beispiel gibt die Elemente vom Anfang an, aber NICHT einschließlich, "kiwi" zurück:

thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[:4])


#Dieses Beispiel gibt die Elemente von "Kirsche" bis zum Ende zurück:

thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[2:])


#Dieses Beispiel gibt die Elemente von "orange" (-4) bis, aber NICHT einschließlich "mango" (-1) zurück:

thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[-4:-1])

#Überprüfen Sie, ob "Apple" in der Liste vorhanden ist:

thislist = ["apple", "banana", "cherry"]
if "apple" in thislist:
  print("Yes, 'apple' is in the fruits list")