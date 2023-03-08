x = 5

hak = 3
devam = "ok"

result = 5 < x < 10      # False

# and

result = (x > 5) and (x < 10)
result = (hak > 0) and (devam == "ok")
# True, True => True
# True, False => False

# or

result = (x > 0) or (x % 2 == 0)
# True, False => True
# True, True => True
# False, False => False

# not

result = not(x > 0)
# True => False
# False => True

# Example: x, 5-10 arasında olan bir çift sayı mıdır?

result = ((x > 5) and (x < 10)) and (x % 2 == 0)

print(result)

