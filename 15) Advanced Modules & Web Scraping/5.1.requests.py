# Bir modülün bilgisayardaki konumunu bulalım. 
# import json
# print(json.__file__)

# requests modülü pythonda yüklü değildir. Konsola pip install requests yazarak indirebiliriz.

import requests
import json

result = requests.get("https://jsonplaceholder.typicode.com/todos")
# result = result.text     # str üretir
result = json.loads(result.text)   # list üretir

print(result)       # => <Response [200]> çıktısı işlem başarılı anlamında
print(type(result))
print(result[0])
print(result[0]["title"])

for i in result:
     print(i)
     if i["userId"] == 1:
          print(i["title"])

