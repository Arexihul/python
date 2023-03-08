import pandas as pd

df = pd.read_csv("datasets/youtube-ing.csv")
# print(df.columns)

# 1- İlk 10 kaydı getiriniz.
result = df.head(10)

# 2- İkinci 5 kaydı getiriniz.  
result = df[5:10]

# 3- Dataset' de bulunan kolon isimleri ve sayısını bulunuz.
result = df.columns,len(df.columns)

# 4- Aşağıda bulunan bazı kolonları silin ve kalan kolonları listeleyiniz.
# (thumbnail_link,comments_disabled,ratings_disabled,video_error_or_removed,description)
result = df.drop(["thumbnail_link","comments_disabled","ratings_disabled","video_error_or_removed","description"],axis=1,inplace=True)

# 5- Beğenme (like) ve beğenmeme (dislike) sayılarının ortalamasını bulunuz.
result = df["likes"].mean(),df["dislikes"].mean()

# 6- ilk 50 videonun like ve dislike kolonlarını getiriniz.
result = df[["likes","dislikes"]].head(50)

# 7- En çok görüntülenen video hangisidir ?
# result = df["views"].max()    # => 424538912
result = df.sort_values("views",ascending=False).head(1)["title"].iloc[0]
# result = df[df["views"].max() == df["views"]]["title"].iloc[0]

# 8- En düşük görüntülenen video hangisidir?
result = df.sort_values("views").head(1)["title"].iloc[0]
# result = df[df["views"].min() == df["views"]]["title"].iloc[0]

# 9- En fazla görüntülenen ilk 10 video hangisidir ?
result = df.sort_values("views",ascending=False).head(10)["title"]

# 10- Kategoriye göre beğeni ortalamalarını sıralı şekilde getiriniz.
# result = df.groupby("category_id")["likes"].mean()
result = df.groupby("category_id").mean().sort_values("likes", ascending = False)["likes"]

# 11- Kategoriye göre yorum sayılarını yukarıdan aşağıya sıralayınız.
# result = df.groupby("category_id")["comment_count"].mean()
result = df.groupby("category_id").sum().sort_values("comment_count", ascending = False)["comment_count"]

# 12- Her kategoride kaç video vardır ?
# result = df.groupby("category_id")["video_id"].count()
result = df["category_id"].value_counts()

# 13- Her videonun title uzunluğu bilgisini yeni bir kolonda gösteriniz.
df["title_lenght"] = df["title"].apply(len)
result = df[["title","title_lenght"]]

# 14- Her video için kullanılan tag sayısını yeni kolonda gösteriniz.
df["tag_count"] = df["tags"].str.split("|").apply(len)
result = df[["tags","tag_count"]]

# def tagCount(tag):
#     return len(tag.split('|'))

# df["tag_count"] = df["tags"].apply(tagCount)

# 15- En popüler videoları listeleyiniz.(like/dislike oranına göre)
df["likes/dislikes"] = df["likes"] / df["dislikes"]

result = df[df["dislikes"] != 0].sort_values("likes/dislikes",ascending=False)[["title","likes","dislikes","likes/dislikes"]]

print(result)

"""
15. Soru- Sadık Turan
def likedislikeoranhesapla(dataset):
    likesList = list(dataset["likes"])
    dislikesList = list(dataset["dislikes"])

    liste = list(zip(likesList,dislikesList))

    oranListesi = []

    for like,dislike  in liste: 
        if (like + dislike) == 0:
            oranListesi.append(0)
        else:
            oranListesi.append(like/(like+dislike))

    return oranListesi

df["beğeni_orani"] = likedislikeoranhesapla(df)

print(df.sort_values("beğeni_orani",ascending=False)[["title","likes","dislikes","beğeni_orani"]])
"""