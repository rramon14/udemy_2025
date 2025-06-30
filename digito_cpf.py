print("Primeiro digito do cpf")

multiplicadores = (10, 9, 8, 7, 6, 5, 4, 3, 2)
cpf_gerador = ()

while True:
    cpf = input("\ndigite o número do cpf: ")
    if cpf.isdigit():
        break
    else:
        print("Digite apenas números!")


for digito, multiplicador in zip(cpf, multiplicadores):
    resultado = int(digito) * multiplicador
    cpf_gerador += (resultado,)

soma_tuplas = sum(cpf_gerador)
#print(soma_tuplas)

digito1_cpf = soma_tuplas % 11
#print(digito_do_cpf)

if digito1_cpf < 2:
    print("esse é o primeiro digito do seu cpf: 0")
else:
    if digito1_cpf >= 2:
        digito1_cpf = 11 - digito1_cpf
        print(f"Esse é o primeiro digito do seu cpf: {digito1_cpf}")

cpf_digito = cpf + str(digito1_cpf)
#print(cpf_digito)

print("\nSegundo digito do cpf")

cpf_digito = cpf + str(digito1_cpf)
multiplicadores2 = (11, 10, 9, 8, 7, 6, 5, 4, 3, 2)
cpf_gerador2 = ()

for digito2, multiplicador2 in zip(cpf_digito, multiplicadores2):
    resultado2 = int(digito2) * multiplicador2
    cpf_gerador2 += (resultado2,)

soma_tuplas2 = sum(cpf_gerador2)
#print(soma_tuplas2)

digito2_cpf = soma_tuplas2 % 11
#print(digito2_cpf)

if digito2_cpf < 2:
    print("Esse é o segundo número do seu cpf: 0")
else:
    if digito2_cpf >= 2:
        digito2_cpf  = 11 - digito2_cpf
        print(f"Esse é o segundo número do seu cpf: {digito2_cpf}")
    



cpf_completo = cpf_digito + str(digito2_cpf)
print(f"Esse é seu cpf completo {cpf_completo}")