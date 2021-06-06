import time, sys

def print_slow(texto, tiempo=0.04):
    t = list(texto)
    for letter in t:
        sys.stdout.write(letter)
        sys.stdout.flush()
        time.sleep(tiempo)

    print('')

def formato(w, x, y, z):
    global mrgrsd, mrgcct
    print_slow(w.rjust(10, " ") + " | " + x, 0.02)
    print_slow("+".rjust(12, " ") + "------", 0.02)
    print_slow(y.rjust(mrgrsd, " ") + "|".rjust(mrgcct + 1, " ") + z, 0.02)


def division(a, b):
    global r, c, i, j, mrgrsd, long_a, cct, rsd, a2, d, mrgcct
    e = b
    if i == 0:
        d = a2[i]
        if d < e:
            time.sleep(1)
            print_slow(
                "\nComo " + d + " es menor que " + e + " tenemos que agarrar otro numero a la derecha")
            mrgrsd = mrgrsd + 1
            mrgcct = mrgcct - 1
            j = j + 1
            d = d + a[j]
    time.sleep(1)
    print_slow("\nNecesitamos un numero que multiplicado por " + e + " sea igual o menor a " + d)
    print_slow("\nCual es ese número?")
    f = input()
    c = int(d) // int(e)
    cct = cct + str(c)
    while int(f) != c:
        time.sleep(1)
        print_slow("\nNo es el número que estamos buscando...\nIntenta nuevamente")
        f = input()
    time.sleep(1)
    print_slow("\nCorrecto!!!\nAhora cuanto nos queda de residuo?")
    h = input()
    r = int(d) % int(e)
    rsd.append(str(r))
    i = i + 1
    while int(h) != r:
        time.sleep(1)
        print_slow("\nNo es el número que estamos buscando...\nIntenta nuevamente")
        h = input()
    time.sleep(1)
    print_slow("\nCorrecto!!!\n")


def bajar_numero(x, y):
    global a2, rsd, i, d, j
    if j < (long_a):
        i = i + 1
        d = y
        d = d + a2[j]
        rsd.append(d)
        time.sleep(1)
        print_slow("\nBajamos el " + a2[j] + " para continuar con la división:\n")

print_slow('Hola Germán!!!')
time.sleep(1)
print_slow('\nEl formato del programa es el siguiente:\n\n"a" dividido entre "b"\n')
time.sleep(1)
print_slow('Por favor introduce el número "a" y presiona ENTER')
a = input()
a2 = a
long_a = len(a)
mrgcct = len(a)
time.sleep(1)
print_slow('\nAhora introduce el número "b" y presiona ENTER')
b = input()
time.sleep(1)
if int(b) == 0:
    print_slow("\nPor favor introduce un número mayor a 0")
    b = input()
c = ""
d = ""
r = ""
cct = ""
rsd = [" "]
i = 0
j = 0
mrgrsd = 11 - long_a
time.sleep(1)
print_slow("\nMuy bien, vamos a hacer la siguiente división:\n")
time.sleep(1)
while j < (long_a):
    formato(a2, b, rsd[i], cct)
    division(a2, b)
    formato(a2, b, rsd[i], cct)
    j = j + 1
    bajar_numero(a2, rsd[i])
    mrgrsd = mrgrsd + 1
    mrgcct = mrgcct - 1
    a = rsd[i]
print_slow("\nEstamos listos Germán...")
