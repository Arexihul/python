import pandas as pd

data = pd.read_csv("datasets/nba.csv")

data.dropna(inplace=True)   # inplace=True işlemi data üzerinde kalıcı yapmak için

# data["Name"] = data["Name"].str.upper()
# data["Name"] = data["Name"].str.lower()
# data["index"] = data["Name"].str.find("a")      # Name kısmında a karakterini arar ve indexini oluşturulan index columna yazar
# data = data[data.Name.str.contains("Jordan")]
# data["Team"] = data["Team"].str.replace(" ","-")
data[["First Name","Last Name"]] = data["Name"].loc[data["Name"].str.split().str.len()==2].str.split(expand=True)   # Burayı tam anlamadım

print(data.columns)

print(data.tail(15))
