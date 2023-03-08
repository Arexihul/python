fruits = {"orange", "apple", "banana"}

print(fruits)

# print(fruits[0])    setler listelerin aksine indexlenemez

for x in fruits:
     print(x)

fruits.add("cherry")
fruits.update(["mango", "grape", "apple"])    # apple zaten sette olduğu için tekrar eklenmez
fruits.remove("mango")
fruits.discard("apple")
fruits.pop()     # listede pop son elemanı siliyodu sette rasgele bir eleman siler 
fruits.clear()    # tüm elemanları siler

print(fruits)

# liste = [1,2,5,4,4,2,1]

# print(liste)
# print(set(liste))

