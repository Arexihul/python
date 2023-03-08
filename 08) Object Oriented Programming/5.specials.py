mylist = [1,2,3]
# mystring = "my string"

# print(len(mylist))
# print(len(mystring))
# print(type(mylist))
# print(type(mystring))

class Movie:
     def __init__(self, title, director, duration):
          self.title = title
          self.director = director
          self.duration = duration
          print("Movie created")

     def __str__(self):
          return f"{self.title} by {self.director}"

     def __len__(self):
          return self.duration

     def __del__(self):
          print("Movie deleted")

m = Movie("Fight Club", "David Fincher", 120)

print(mylist)
print(m)

print(len(mylist))
print(len(m))

# del m
# print(m)

# google => python special methods list

