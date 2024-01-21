#2. Здесь пишу программу для создания таблицы истинности утверждения
# ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат.

print('| x y z |res|')
print ('-----------')
for x in range(2):
    for y in range (2):
        for z in range (2):
            if not(x or y or z) == (not x and not y and not z):
                print ('|', x, y, z, '| 1 |')
                print ('-------------') 
            else:
                print ('|', x, y, z, '| 0 |')
                print ('-------------')