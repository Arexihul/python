# with open("reading.txt","r+",encoding="utf-8") as file:     # "r+" hem okuma hem yazma
#      file.seek(20)
#      file.write("deneme")

# with open("reading.txt","r+",encoding="utf-8") as file:
#      print(file.read())

# *** SAYFA SONUNDA GÜNCELLEME ***

# with open("reading.txt","a",encoding="utf-8") as file:
#      file.write("\nMahmut Tuncer")

# with open("reading.txt","r+",encoding="utf-8") as file:
#      print(file.read())

# *** SAYFA BAŞINDA GÜNCELLEME ***

# with open("reading.txt","r+",encoding="utf-8") as file:
#      content = file.read()
#      content = "Ciguli\n" + content
#      file.seek(0)
#      file.write(content)

# with open("reading.txt","r+",encoding="utf-8") as file:
#      print(file.read())

# *** SAYFA ORTASINDA GÜNCELLEME ***

# with open("reading.txt","r+",encoding="utf-8") as file:
#      liste = file.readlines()   # ['Eyüp Ülgen\n', 'Nihal Ülgen\n', 'Selami Ülgen\n', 'Zehra Ülgen']
#      liste.insert(1,"Sadık Turan\n")   # ['Eyüp Ülgen\n', 'Sadık Turan\n', 'Nihal Ülgen\n', 'Selami Ülgen\n', 'Zehra Ülgen']
#      file.seek(0)

#      # for i in liste:
#      #      file.write(i)

#      file.writelines(liste)

# with open("reading.txt","r",encoding="utf-8") as file:
#      print(file.read())

