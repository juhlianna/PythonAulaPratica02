# Execute as seguintes atribuições:
# s1 = "ant"
# s2 = "bat"
# s3 = "cod"
s1 = "ant"
s2 = "bat"
s3 = "cod"

# Agora, utilizando operadores + e *, crie as saídas a seguir:
# a) "ant bat cod"
print(s1 + " " + s2 + " " + s3)

# b) "ant ant ant ant ant ant ant ant ant ant"
print(10 * (s1 + " "))

# c) "ant bat bat cod cod cod"
print(1 * (s1 + " ") + 2 * (s2 + " ") + 3 * (s3 + " "))

# d) "ant bat ant bat ant bat ant bat ant bat ant bat ant bat
print(7 * (s1 + " " + s2 + " "))

# e) "batbatcod batbatcod batbatcod batbatcod batbatcod
print(5 * (s2 + s2 + s3 + " " ))



