import random

# print(dir(random))
# print(help(random))

result = random.random()      # 0.0-1.0 arasında rastgele sayı üretir
result = random.random() * 100     # 0.0-100.0 arasında rastgele sayı üretir
result = random.uniform(5,50)      # 5.0-50.0 arasında rastgele sayı üretir
result = int(random.uniform(5,50))      # 5-50 arasında rastgele tam sayı üretir
result = random.randint(1,100)      # 1-100 arasında rastgele tam sayı üretir

greeting = "Hello Babba"
greeting = greeting.split(" ")

names = ["ali", "veli", "ayşe", "fatma"]

result = names[random.randint(0,len(names)-1)]
result = random.choice(names)
result = random.choice(greeting)

print(result)

liste = list(range(10))
random.shuffle(liste)

print(liste)

listem = range(100)

x = random.sample(listem, 5)

print(x)

y = random.sample(names, 2)

print(y)

