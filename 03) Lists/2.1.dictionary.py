# # key - value

# # 41 => Kocaeli  34 => İstanbul

# # dictionary olmadan listeyle yapalım.

# sehirler = ["kocaeli", "istanbul"]
# plakalar = [41, 34]

# print(plakalar[sehirler.index("kocaeli")])

# # bu şekilde yapınca şehir ve plakaların sıralarının uyması gerekiyor.

# print(plakalar["kocaeli"]) => 41
# print(plakalar["istanbul"]) => 34

# # amacımız bunları yazınca plakaları söylemesi

dictionary = {"key": "value"}

plakalar = {"kocaeli": 41, "istanbul": 34}

print(plakalar)
print(plakalar["kocaeli"])

# # dictionary'ye ekleme veya değişiklik yapılabilir.

plakalar["ankara"] = 6
plakalar["kocaeli"] = "new value"

print(plakalar)

# # başka bi uygulama yapalım

users = {
    "sadikturan": 36,
    "cinarturan": 2
}

print(users)

users = {
    "sadikturan": {
        "age": 36,
        "roles": "user",
        "e-mail": "sadik@gmail.com",
        "address": "kocaeli",
        "phone": 123123123
    },
    "cinarturan": {
        "age": 2,
        "roles": ["admin", "user"],
        "e-mail": "cinar@gmail.com",
        "address": "istanbul",
        "phone": 321321321
    }
}

print(users)
print(users["sadikturan"])
print(users["cinarturan"])
print(users["sadikturan"]["age"])
print(users["cinarturan"]["e-mail"])
print(users["sadikturan"]["roles"])
print(users["cinarturan"]["roles"])
print(users["cinarturan"]["roles"][0])

