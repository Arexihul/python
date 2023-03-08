# if 3>2:
#      print("Hoşgeldiniz")

# if True:
#      print("Hoşgeldiniz")

# isLoggedin = True

# if isLoggedin:
#      print("Hoşgeldiniz")

# if isLoggedin == True:
#      print("Hoşgeldiniz")

username = "eyup"
password = "asd123"

if (username == "eyup") and (password == "asd123"):
    print("Giriş Başarılı")
else:
    print("Kullanıcı adı veya şifre hatalı")


if username == "eyup":
    if password == "asd123":
        print("Giriş Başarılı")
    else:
        print("Şifre hatalı")
else:
    print("Kullanıı adı hatalı")
