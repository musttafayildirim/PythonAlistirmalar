import sys

# sys.exit()  kullanıldığı yerde program aniden çalışmayı durdurur.


##sys.stderr.write("Bu bir hata mesajıdır...\n")
##sys.stderr.flush()

#sys.stdout.write("normal bir yazıdır...\n")

#print(sys.argv)


#for i in sys.argv:
 #   print(i)


def kokBulma(a, b, c):
    delta = b ** 2 - 4 * a * c

    if(delta < 0 ):
        print("Reel kök yoktur...")

    else:
        x1 = (-b - delta ** 0.5) / (2 * a)
        x2 = (-b + delta ** 0.5) / (2 * a)
        return (x1, x2)



if len(sys.argv) == 4:
    print("Kök bulma", kokBulma(int(sys.argv[1]), int(sys.argv[2]), int(sys.argv[3])))
else:
    sys.stderr.write("Lütfen doğru değerler girin....")
    sys.stderr.flush()

