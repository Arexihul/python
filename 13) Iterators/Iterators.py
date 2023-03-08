liste = [1,2,3,4,5]

# for i in liste:     # liste iterable objedir
#      print(i)

# for döngüsünün arkasında dönen senaryoyu ele alacağız

# print(dir(liste))   # __iter__

iterator = iter(liste)

# print(iterator)

# print(next(iterator))
# print(next(iterator))
# print(next(iterator))
# print(next(iterator))
# print(next(iterator))
# print(next(iterator))    # StopIteration


# ** for döngüsü aslında şu şekilde çalışır **

# while True:
#      try:
#           element = next(iterator)
#           print(element)
#      except StopIteration:
#           break


class MyNumbers:
     def __init__(self, start, stop):
          self.start = start
          self.stop = stop

     def __iter__(self):
          return self

     def __next__(self):
          if self.start <= self.stop:
               x = self.start
               self.start += 1
               return x
          else:
               raise StopIteration

listem = MyNumbers(10,20)

myiter = iter(listem)

# print(next(myiter))
# print(next(myiter))

# while True:
#      try:
#           element = next(myiter)
#           print(element)
#      except StopIteration:
#           break

# for x in listem:
#      print(x)

