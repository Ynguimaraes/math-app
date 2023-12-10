def adicao(a, b):
    return a + b

def subtracao(a, b):
    return a - b

def multiplicacao(a, b):
    return a * b

def divisao(a, b):
    if b == 0:
        return "Não é possível dividir por zero."
    return a / b

print("Calculadora Simples")
print("Escolha a operação:")
print("1 - subtração")
print("2 - adição")
print("3 - Multiplicação")
print("4 - Divisão")

opcao = input("Digite o número da operação desejada: ")

num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))

if opcao == '1':
    print("Resultado da adição:", adicao(num1, num2))
elif opcao == '2':
    print("Resultado da subtração:", subtracao(num1, num2))
elif opcao == '3':
    print("Resultado da multiplicação:", multiplicacao(num1, num2))
elif opcao == '4':
    print("Resultado da divisão:", divisao(num1, num2))
else:
    print("Opção inválida.")
