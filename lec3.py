def square (num):
    return num**2

list = [{i, square(i)} for i in range(1,15) if i%2==0]

print(list)