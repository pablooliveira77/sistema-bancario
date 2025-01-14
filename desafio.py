menu = """

[d] - depositar
[s] - sacar
[e] - extrato
[q] - sair

=> """

saldo = 0
limite = 500
extrato = []
numero_saque = 0
LIMITE_SAQUE = 3

while True:
    opcao = input(menu)
    if opcao == 'd':
        deposito = float(input("Digite o valor do depósito: "))
        if deposito <= 0:
            print("Valor inválido para deposito")
        else:
            saldo += deposito
            extrato.append(f"Depósito: R$ {deposito:.2f}")
            print("Depósito realizado com sucesso!")
    elif opcao == 's':
        if numero_saque < LIMITE_SAQUE:
            saque = float(input("Digite o valor do saque: "))
            if saque < 0 or saque > saldo:
                print("Valor inválido para saque")
            elif saque > limite:
                print("Limite de saque: R$ 500")
            else:
                saldo -= saque
                extrato.append(f"Saque: R$ {saque:.2f}")
                numero_saque += 1
                print("Saque realizado com sucesso!")
        else:
            print(f"Limite de saques diários atingido: {numero_saque}")
    elif opcao == 'e':
        mensagem_extrato = """
Extrato
-------------------
{extrato}
-------------------
Saldo: R$ {saldo:.2f}
        """
        print(mensagem_extrato.format(extrato='\n'.join(extrato), saldo=saldo))
    elif opcao == 'q':
        break
    else:
        print("Opção inválida")