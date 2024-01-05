
# Atividade - Calculadora

# Título
print("[ CALCULADORA ]")

# Operações Matemáticas Básicas
print("[+] -> adição")
print("[-] -> subtração")
print("[*] -> multiplicação")
print("[/] -> divisão\n")

# Entrada de Dados da Operação

# Validação Valor 1
while True:
    valor1 = input("-Digite o valor do 1° número: ")
    if valor1.isnumeric():
        break

    elif valor1.replace('.', '', 1).isdigit():
        break

    else:
        print("! O valor fornecido do 1° número é inválido !")

# Validação Caractere da Operação
while True:
    operacao = input("-Digite o caractere da operação: ")
    if operacao == "+" or operacao == "-" or operacao == "*" or operacao == "/":
        break

    else:
        print("! O caractere da operação digitado é invalido !")

# Validação Valor 2
while True:
    valor2 = input("-Digite o valor do 2°  número: ")
    if valor2.isnumeric():
        break

    elif valor2.replace('.', '', 1).isdigit():
        break

    else:
        print("! O valor fornecido do 2° número é inválido !")

# Definindo as Variáveis
valor1 = float(valor1)
valor2 = float(valor2)

# Resultado da Operação
print("\n[ RESULTADO ]")
if operacao == "+":
    print(f"{valor1} + {valor2} = {valor1 + valor2}")
elif operacao == "-":
    print(f"{valor1} - {valor2} = {valor1 - valor2}")
elif operacao == "*":
    print(f"{valor1} * {valor2} = {valor1 * valor2}")
elif operacao == "/":
    print(f"{valor1} / {valor2} = {valor1 / valor2}")
