import mod

# print(help(mod))
# print(help(mod.func))

result = mod.number
result = mod.numbers
result = mod.person["name"]

print(result)

mod.func(123)

p = mod.Person()
p.speak()

# => python

# => import sys

# => sys.path      # python klasörlerinin konumu

# Oluşturduğumuz mod dosyasını python lib'e atarsak da istediğimiz zaman erişebiliriz.

# sys.builtin_module_names    # builtin modüllerini görürüz. DLL şeklinde bulunur. 

