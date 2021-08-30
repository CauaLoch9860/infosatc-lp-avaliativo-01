#Váriaveis e cálculo
premio = float(input("Digite o Valor Total do Premio: "))
premiodesc = premio - premio * 0.07
imposto = premio * 0.07
#cálculo dos ganhadores
ganhador1 = (premiodesc * 0.46)
ganhador2 = (premiodesc * 0.32)
ganhador3 = premiodesc - (ganhador1 + ganhador2)
#Mostrar na tela as informações
print("\nValor Premio Total: ",premio)
print("\nValor Premio Descontado: ",premiodesc)
print("\nValor do imposto Descontado: ",imposto)
print("\n============Ganhadores=====================\n")
print("\nValor Premio primeiro ganhador: ",ganhador1)
print("\nValor Premio segundo  ganhador: ",ganhador2)
print("\nValor Premio terceiro ganhador: ",ganhador3)