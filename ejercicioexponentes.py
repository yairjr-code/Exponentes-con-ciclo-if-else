## Exponentes
'''Python también puede realizar exponenciaciones como 2³ o 10².
En matemáticas escritas, podemos ver un exponente como un número superíndice
(como el anterior), pero escribir superíndices no siempre es fácil en los teclados modernos.
Como la exponenciación es muy similar a la multiplicación, Python usa la notación **.
Así que 2 ** 3es 2³ y 10 ** 2es 10².'''
#< 18.5	Peso inferior al normal
#18.5 - 24.9	Peso normal
'''25-29.9	Sobrepeso
30-34.9	Obesidad I
35-39.9	Obesidad II
> 40	Obesidad III
'''

masa = float(input("Digita la masa en kg :"))

altura = float(input("Digita la altura en metro:"))

imc = masa // altura**2

if imc <= 18.5:
    print(f"Este seria el indice masa muscular: {imc}  Peso inferior al normal")
elif imc > 18.5 and imc <= 24.9:
    print(f"Este seria el indice masa muscular: {imc} Peso normal  ")
elif imc > 24.9 and imc <= 29.9:
    print(f"Este seria el indice masa muscular: {imc} Sobrepeso  ")
elif imc > 29.9  and imc <= 34.9:
    print(f"Este seria el indice masa muscular: {imc} obesidad I  ")
elif imc > 34.9 and imc <= 39.9:
    print(f"Este seria el indice masa muscular: {imc} obesidad II  ")
elif imc > 39.9:
    print(f"Este seria el indice masa muscular: {imc} eres un choncho")



#print (f"Este seria el indice masa muscular: {imc}"