message = "Hello there. My name is Eyüp Ülgen"

print(message.upper())
print(message.lower())
print(message.title())
print(message.capitalize())

message2 = " Hello there. My name is Eyüp Ülgen"

print(message2.strip())   # strip baştaki boşluğu siler 

message3 = message.split()   # her boşlukta ayrılır

print(message3)
print(message3[3])

message4 = message.split(".")  # . olunca ayrılır

print(message4)
print(message4[1])

# message3 = " ".join(message3)   # split in tersi tekrar birleştirir / indexler arasına boşluk koyar

print(message3)

message3 = "*".join(message3)    # indexler arasına * koyar

print(message3)

index = message.find("Eyüp")

print(index)

index2 = message.find("Eyyüp")

print(index2)   # yoksa -1 yazar

isFound = message.startswith("H")

print(isFound)

isFound2 = message.startswith("h")

print(isFound2)

isFound3 = message.endswith("n")

print(isFound3)

message5 = message.replace("Eyüp", "Eyyubi")
message5 = message5.replace(" ", "**")
message5 = message5.replace("ı","i").replace("ç","c").replace("ğ","g").replace("ü","u").replace("ş", "s")

print(message5)

message6 = message.center(100,"*")

print(message6)



# Diğer birçok method internette mevcuttur

# https://www.w3schools.com/python/python_ref_string.asp
# https://www.programiz.com/python-programming/methods/string
# https://docs.python.org/2.5/lib/string-methods.html
