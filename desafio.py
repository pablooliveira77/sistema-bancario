import textwrap


def menu():
    menu = """\n
    ============= MENU =============
    [d]\tDepositar
    [s]\tSacar
    [e]\tExtrato
    [nc]\tNova Conta
    [lc]\tListar Contas
    [nu]\tNova Usuário
    [q]\tSair
    => """

    return input(textwrap.dedent(menu))


def depositar(valor, saldo, extrato, /):
    if valor <= 0:
        print("\nValor inválido para deposito")
    else:
        saldo += valor
        extrato += f"Depósito: R$ {valor:.2f}\n"
        print("\nDepósito realizado com sucesso!")
    
    return saldo, extrato


def sacar(*, saldo, valor, extrato, limite, numero_saque, limite_saque):
    excedeu_valor = valor > saldo
    excedeu_limite = valor > limite
    excedeu_saque = numero_saque >= limite_saque

    if excedeu_valor:
        print("\nOperação inválida: Saldo insuficiente")
    elif excedeu_limite:
        print("\nOperação inválida: Limite de saque excedido")
    elif excedeu_saque:
        print("\nOperação inválida: Limite de saque diário excedido")
    elif valor > 0:
        saldo -= valor
        extrato += f"Saque: R$ {valor:.2f}\n"
        numero_saque += 1
        print("\nSaque realizado com sucesso!")
    else:
        print("\nOperação inválida: Valor inválido para saque")
    
    return saldo, extrato


def exibir_extrato(saldo, extrato):
    print("======================== Extrato ========================")
    print("Não foi realizadas movimentações na conta" if not extrato else extrato)
    print(f"Saldo atual: R$ {saldo:.2f}")


def criar_usuario(usuarios):
    cpf = input("Digite o CPF do usuário: ")
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
        print("Usuário já existe com esse CPF")
        return
    
    nome = input("Digite o nome do usuário: ")
    data_nascimento = input("Digite a data de nascimento do usuário: ")

    usuarios.append({
        "cpf": cpf,
        "nome": nome,
        "data_nascimento": data_nascimento,
    })

    print("Usuário criado com sucesso!")


def filtrar_usuario(cpf, usuarios):
    usuario_filtrado = [usuario for usuario in usuarios if usuario["cpf"] == cpf]
    return usuario_filtrado[0] if usuario_filtrado else None


def criar_conta(agencia, numero_conta, usuarios):
    cpf = input("Digite o CPF do usuário: ")
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
        print("Conta criada com sucesso")
        return {"agencia": agencia, "numero_conta": numero_conta, "usuario": usuario}
    
    print("Usuário não encontrado")


def listar_conta(contas):
    print("======================== Contas ========================")
    for conta in contas:
        print(f"Agência: {conta['agencia']}")
        print(f"Conta: {conta['numero_conta']}")
        print(f"Usuário: {conta['usuario']['nome']}")
        print("------------------------------------------------------")


def main():
    LIMITE_SAQUE = 3
    AGENCIA = "0001"

    saldo = 0
    limite = 500
    extrato = ""
    numero_saque = 0
    usuario = []
    contas = []

    while True:
        opcao = menu()

        if opcao == 'd':
            deposito = float(input("Digite o valor do depósito: "))
            saldo, extrato = depositar(deposito, saldo, extrato)
            

        elif opcao == 's':
            saque = float(input("Digite o valor do saque: "))

            saldo, extrato = sacar(saldo=saldo, valor=saque, extrato=extrato, limite=limite, numero_saque=numero_saque, limite_saque=LIMITE_SAQUE)
            
            
        elif opcao == 'e':
            exibir_extrato(saldo, extrato=extrato)

        elif opcao == 'nu':
            criar_usuario(usuario)    
        
        elif opcao == 'nc':
            numero_conta = len(contas) + 1
            conta = criar_conta(AGENCIA, numero_conta, usuario)

            if conta:
                contas.append(conta)
        
        elif opcao == 'lc':
            listar_conta(contas)

        elif opcao == 'q':
            break
        else:
            print("Opção inválida")


main()