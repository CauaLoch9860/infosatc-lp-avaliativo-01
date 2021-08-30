import math

altura = float(input("digite a altura: "))
comprimento = float(input("digite o comprimento: "))
medida = (altura*comprimento)
litros = (medida / 3)
latas = math.ceil(litros / 3.6)
preco = (latas* 107)

print("Valor:",preco)
print("Quantidades de lata:",latas)
