import re

# print(dir(re))

""" re module """

string = "Python Kursu: Python Programlama Rehberiniz | 40 Saat"

# ***re.findall()***     => Anahtar kelimeyi bulma
# result = re.findall("Python",string)
# result = len(result)

# ***re.split()***   => Parçalara ayırma
# result = re.split(" ",string)
# result = re.split(":",string)

# ***re.sub()***    => Karakter değiştirme
# result = re.sub(" ","-",string)
# result = re.sub("\s","-",string)   # \s regular expression'da boşluk karakteridir

# ***re.search()***
result = re.search("Python",string)     # match objesi olarak döndürür  # İlk Python'ı alır
# result = result.span()      # match objesinden index aralığını verir
# result = result.start()     # başlangıç indexini verir
# result = result.end()       # bitiş ineksini verir
# result = result.group()     # bulduğu ifadeyi geri gönderir
# result = result.string      # string bilgisini geri döndürür


""" regular expression """

"""

    [] - Köşeli parantezler arasına yazılan bütün karakterler aranır.

         [abc] => a      : 1 match
                  ac     : 2 match 
                  Python : No matches

         [a-e]  => [abcde]
         [1-5]  => [12345]
         [0-39] => [01239]   

         [^abc] => abc dışındaki karakterler.
         [^0-9] => rakam olmayan karakterler.

"""

# result = re.findall("[abc]",string)
# result = re.findall("[sat]",string)
# result = re.findall("[a-e]", string)
# result = re.findall("[a-z]", string)
# result = re.findall("[0-5]", string)
# result = re.findall("[^abc]", string)
# result = re.findall("[^0-9]", string)

"""
    . - Her hangi bir tek karakteri belirtir.

        .. => a    : No match
              ab   : 1 match
              abc  : 1 match
              abcd : 2 matches

    
"""

# result = re.findall("...", string)
# result = re.findall("Py..on", string)

"""
    ^ - Belirtilen string karakterlerle başlıyor mu ?

    ^a => a:    1 match
          abc:  1 match
          bac:  No match

"""

# result = re.findall("^a",string)
# result = re.findall("^P",string) 
# result = re.findall("^Pyt",string) 

"""
    $ - Belirtilen karakterle bitiyor mu ?

    a$ => a      : 1 match
          lamba  : 1 match
          Python : No match 

"""

# result = re.findall("t$",string)
# result = re.findall("Saat$",string)
# result = re.findall("saatt$",string)

"""
     * - Bir karakterin sıfır ya da daha fazla sayıda olmasını 
         kontrol eder.

         ma*n => mn     : 1 match
                 man    : 1 match
                 maaan  : 1 match
                 main   : No match (a' nın arkasına n gelmiyor.) 
"""
# result = re.findall("Sa*t",string)

"""
     + - Bir karakterin bir ya da daha fazla sayıda olmasını 
         kontrol eder.

         ma+n => mn     : No match
                 man    : 1 match
                 maaan  : 1 match
                 main   : No match (a' nın arkasına n gelmiyor.) 
"""

# result = re.findall("Sa+t",string)

"""
    ? - Bir karakterin sıfır ya da bir kez olmasını 
        kontrol eder.

        ma+n => mn     : No match
                man    : 1 match
                maaan  : 1 match
                main   : No match (a' nın arkasına n gelmiyor.) 
"""

# result = re.findall("Sa?t",string)      # a iki kere olduğundan sonuç boş küme

"""
    {} - Karakter sayısını kontrol eder.

        al{2}   => a karakterinin arkasına l karakteri 2 kez tekrarlamalı.
        al{2,3} => a karakterinin arkasına l karakteri en az 2 en fazla 3 kez tekrarlamalı.
        [0-9]{2,4} => en az 2 en çok 4 basamaklı sayılar.
"""
# result = re.findall("a{2}", string)
# result = re.findall("[0-9]{2}", string)

"""
    | - alternatif seçeneklerden birinin gerçekleşmesi gerekir.

        a|b => a ya da b

            cde =>    no match
            ade =>    1 match
            acdbea => 3 match 
"""

# result = re.findall("a|b",string)

"""
    () - gruplamak için kullanılır.

         (a|b|c)xz => a,b,c karakterlerinin arkasına xz gelmelidir.
"""

# result = re.findall("(a|b|c)xz",string)
# result = re.findall("(a|b|c)m",string)


#     \ - Özel karakterleri aramamızı sağlar.
#         \$a => $ karakterinin arkasına a karakterinin arar. Yani
#                $ regular exp. engine tarafından yorumlanmaz.

#     \A - Belirtilen karakter string in başında mı ?
#          \Athe => the string in başındamı

# result = re.findall("\APython", string)

#     \Z - Belirtilen karakter string in sonunda mı ?
#          the\Z => the string in sonunda mı

# result = re.findall("Saat\Z", string)

#     \b - Belirtilen karakter kelimenin en başında ya da sonunda mı ?
#          \bthe => the kelimenin in başında mı?
#          the\b => the kelimenin in sonunda mı?

#     \B - Belirtilen karakter kelimenin en başında ya da sonunda değil mi ?
#          \Bthe => the kelimenin in başında değil mi?
#          the\B => the kelimenin in sonunda değil mi?
    
#     \d - [0-9] ile aynı anlama gelir yani rakamları arar.
#          \d => 12abc34

#     \D - [^0-9] ile aynı anlama gelir yani rakam olmayanları arar.
#          \D => 1ab44_50

#     \s - Boşluk karakterlerini arar.  
#     \S - Boşluk karakterleri dışındakiler.
#     \w - Alfabetik karakterler, rakamlar ve alt çizgi karakteri.
#     \W - \w nin tam tersi


print(result)

# google => regular expressions python
