lista =[]
while True:
    n2 = float(input(" Introduce el valor (para parar, ponga un 0): "))
    lista.append(n2)
    if n2 == 0:
        break
lista.pop(-1)
resultado = str(tuple(lista))
mul_nums = resultado.replace(',','+')
r=eval(mul_nums)
r = float(r)
notas = len(lista)
promedio= r/notas
print("Tu promedio es: ")
print("{:.1f}".format(r))
