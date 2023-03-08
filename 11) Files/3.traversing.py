# 1.YÖNTEM

# file = open("reading.txt","r",encoding="utf-8")

# content = file.read()
# print(content)

# file.close()


# 2.YÖNTEM => close() demeden with bloğunun sonuna gelindiğinde dosya kapanır

with open("reading.txt","r",encoding="utf-8") as file:
     content = file.read()
     print(content)
     print(file.tell())  # tell() fonksyonu o anda kürsörün konumunu verir
     file.seek(5)   # kürsörün konuma gitmesini emreder
     print(file.tell())
     content2 = file.read()
     print(content2)

