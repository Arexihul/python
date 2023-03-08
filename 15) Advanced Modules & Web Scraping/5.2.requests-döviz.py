import requests
import json

bozulan = input("Bozulan döviz türü: ")
alınan = input("Alınacak döviz türü: ")
miktar = int(input(f"Ne kadar {bozulan} bozdurmak istiyorsunuz: "))

result = requests.get(f"https://api.exchangeratesapi.io/latest?base={bozulan}")
result = json.loads(result.text)

print(f'1 {bozulan} = {result["rates"][alınan]} {alınan}')

print(f"{miktar} {bozulan} = {result['rates'][alınan]*miktar} {alınan}")

