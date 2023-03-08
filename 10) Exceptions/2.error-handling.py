# error handling => hata yönetimi


# x = int(input("x: "))
# y = int(input("y: "))

# print(x/y)


# try: 
#      x = int(input("x: "))
#      y = int(input("y: "))
#      print(x/y)
# except ZeroDivisionError:
#      print("y için 0 girilemez")
# except ValueError:
#      print("x ve y için sayısal değer girmelisiniz")
     

# try: 
#      x = int(input("x: "))
#      y = int(input("y: "))
#      print(x/y)
# except (ZeroDivisionError, ValueError):
#      print("Yanlış bilgi girdiniz")


# try: 
#      x = int(input("x: "))
#      y = int(input("y: "))
#      print(x/y)
# except (ZeroDivisionError, ValueError) as e:
#      print("Yanlış bilgi girdiniz")
#      print(e)


# while True:
#      try: 
#           x = int(input("x: "))
#           y = int(input("y: "))
#           print(x/y)
#      except:
#           print("Yanlış bilgi girdiniz")
#      else:
#           print("Her şey yolunda")
#           break


while True:
     try: 
          x = int(input("x: "))
          y = int(input("y: "))
          print(x/y)
     except Exception as ex:
          print("Yanlış bilgi girdiniz", ex)
     else:
          break
     finally:
          print("try except sonlandı")

