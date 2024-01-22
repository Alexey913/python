#6. Напишите программу для проверки истинности утверждения
# ¬(X = Z ⋁ X <= Y ⋀ Z) для всех значений предикат.
print ("x y z")
for x in range(2):
    for y in range(2):
        for z in range(2):
            if not (x == z or x <= y and z):
                print (x, y, z)
