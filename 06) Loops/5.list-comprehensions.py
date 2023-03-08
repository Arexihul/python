# for x in range(10):
#      print(x)

# numbers = [x for x in range(10)]

# print(numbers)

# numbers = []
# for x in range(10):
#      numbers.append(x)

# print(numbers)


# for x in range(10):
#      print(x**2)

# numbers = [x**2 for x in range(10)]

# print(numbers)

# numbers = [x*x for x in range(10) if x%3 == 0]

# print(numbers)


# text = "Hello"
# liste = []

# for letter in text:
#      liste.append(letter)

# print(liste)

# liste2= [letter for letter in text]
# print(liste2)

# years = [1983, 1999, 2008, 1956, 1986]

# ages = [2020-year for year in years]
# print(ages)

# # 9
# result = [x if x%2==0 else "Tek" for x in range(1,10)]
# print(result)

# içiçedöngü = []

# for x in range(3):
#      for y in range(3):
#           içiçedöngü.append((x,y))

# print(içiçedöngü)

numbers = [(x,y,z) for x in range(3) for y in range(3) for z in range(3)]
print(numbers)

