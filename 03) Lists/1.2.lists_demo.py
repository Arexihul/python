# 1- "BMW, Mercedes, Opel, Mazda" elemanlarına sahip bir liste oluşturunuz.

print("Cevap 1".center(25,"*"))

list1 = ["BMW", "Mercedes", "Opel", "Mazda"]
print(list1)

# 2- Liste kaç elemanlıdır?

print("Cevap 2".center(25,"*"))

print(len(list1))

# 3- Listenin ilk ve son elemanları nelerdir?

print("Cevap 3".center(25,"*"))

print(list1[0] + " " + list1[-1])

# 4- Mazda değerini Toyota ile değiştirin.

print("Cevap 4".center(25,"*"))

list1[3] = "Toyota"
print(list1)

# 5- Mercedes listenin bir elamanı mıdır?

print("Cevap 5".center(25,"*"))

print(list1.index("Mercedes"))
# veya
print("Mercedes" in list1)

# 6- Listenin -2 indexindeki değer nedir?

print("Cevap 6".center(25,"*"))

print(list1[-2])

# 7- Listenin ilk 3 elemanını alın.

print("Cevap 7".center(25,"*"))

print(list1[0:3])

# 8- Listenin son 2 elemanı yerine "Toyota" ve "Renault" değerleri ekleyin.

print("Cevap 8".center(25,"*"))

list1[-2:] = "Toyota", "Renault"
print(list1)

# 9- Listenin üzerina "Audi" ve "Nissan" değerlerini ekleyin.

print("Cevap 9".center(25,"*"))

# newcars = "Audi", "Nissan"
# list1.extend(newcars)
# print(list1)

print(list1 + ["Audi", "Nissan"])

# 10- Listenin son elemanını silin.

print("Cevap 10".center(25,"*"))

# list1.pop(-1)
# print(list1)

del list1[-1]
print(list1)

# 11- Liste elemanlarını tersten yazdırın.

print("Cevap 11".center(25,"*"))

# list1.reverse()
# print(list1)

print(list1[::-1])

# 12- Aşağıdaki verileri birliste içinde saklayınız.

              #   studentA: Yiğit Bilgi 2010, (70,60,70)
              #   studentB: Sena Turan 1999, (80,80,70)
              #   studentC: Ahmet Turan 1998, (80,70,90)

print("Cevap 12".center(25,"*"))

studentA = ["Yiğit Bilgi", 2010, [70,60,70]]
studentB = ["Sena Turan", 1999, [80,80,70]]
studentC = ["Ahmet Turan", 1998, [80,70,90]]

students = [studentA] + [studentB] + [studentC]

print(students)

# 13- Liste elemanlarını ekrana yazdırınız.

print("Cevap 13".center(25,"*"))

print(students[0])
print(students[1])
print(students[2])
print(students[0][0])
print(students[0][1])
print(students[0][2])
print(students[0][2][0])
print(students[1][0])
print(students[1][1])
print(students[1][2])
print(students[1][2][1])
print(students[2][0])
print(students[2][1])
print(students[2][2])
print(students[2][2][2])


print(f"{students[0][0][:11]} {2020-students[0][1]} yaşında ve not ortalaması {(studentA[2][0] + studentA[2][1] + studentA[2][2])/3}")

