list = [1,2,3]
tuple = (1,"iki",3)
tuple2 = 1,"iki",3

print(list)
print(tuple)
print(tuple2)

print(type(list))
print(type(tuple))
print(type(tuple2))

print(list[2])
print(tuple[1])

print(len(list))
print(len(tuple))

list = ["Ali", "Veli"]
tuple = ("Damla", "Ayşe", "Ayşe")

# list de tuple da tamamen değiştirilebilir.

print(list)
print(tuple)

list[0] = "Ahmet"       # list de eleman değiştirilebilirken
# tuple[0] = "Deniz"    # tuple da değiştirilemez.

print(list)
print(tuple)

print(tuple.count("Ayşe"))
print(tuple.index("Ayşe"))

names = ("Demet", "Emel", "Ayşe") + tuple

print(names)

# tuple'ları tamamen liste ile aynı anlamda algılayabiliriz, tuple'da tek farkımız herhangi
# bir eleman üzerinde güncelleme, silme, eleman ekleme gibi işlemler yapılamaz.

