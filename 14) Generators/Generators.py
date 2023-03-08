# Genel anlamda generator bizim için bellekte yer işgal etmeyen bir iterator üretiyor

def cube():
     result = []

     for i in range(10):
          result.append(i**3)
     return result  

# print(cube())

# Yukarıda result listesi tekrar kullanılmayacağı için bellek içinde gereksiz yer tutuyor

def cube2():
     for i in range(5):
          yield i**3

# generator = cube2()
# iterator = iter(generator)

# veya

iterator = cube2()

# print(next(iterator))
# print(next(iterator))
# print(next(iterator))
# print(next(iterator))

# for i in iterator:
#      print(i)


liste = [i**3 for i in range(5)]
print(liste)

liste = (i**3 for i in range(5))   # => generator
print(liste)

# print(next(liste))
# print(next(liste))
# print(next(liste))

for i in liste:
     print(i)

