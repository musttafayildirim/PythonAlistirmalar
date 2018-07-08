def kareleriAl():
    for i in range(1,21):
        yield i ** 2

generator = kareleriAl()
print(generator)

iterator = iter(generator)


for i in iterator:
    print(i)

