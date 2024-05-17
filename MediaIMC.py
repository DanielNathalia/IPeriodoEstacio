print('Bem vindo á calculadora de IMC!')

peso = float(input('Informe seu peso (em KG):'))
altura = float(input('Informe sua altura (em metros):'))

imc = peso / (altura * altura)

print('Seu IMC é:', imc)
if imc <= 18.5:
    print("Seu estado é de Magreza!")
if imc > 18.5 <= 25:
    print("Você está Saudável!")
if imc > 26:
    print("Seu estado é de Sobrepeso!")

#print('Seu IMC é:', imc)

