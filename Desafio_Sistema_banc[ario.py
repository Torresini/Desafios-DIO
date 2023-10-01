menu = """

[d] Depositar
[s] Sacar
[e] Extrato
[q] sair

=> """

saldo = 1000
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:

    opcao = input(menu)

    if opcao == "d":
        print("Depósito")

        valor_deposito_str = input("Digite o valor de depósito: ")
        valor_deposito_float = float(valor_deposito_str)
        saldo += valor_deposito_float
        extrato += f"Depósito: R$ {valor_deposito_float: .2f}\n"
        

    elif opcao == "s":
        if numero_saques < LIMITE_SAQUES:
            print("Saque")
            valor_saque_str = input("Digite o valor de saque: ")
            valor_saque_float = float(valor_saque_str)
        
            if valor_saque_float <= limite:
                if  valor_saque_float <= saldo:
                    saldo -= valor_saque_float
                    extrato += f"Saque: R$ {valor_saque_float}\n"
                    numero_saques += 1
                else:
                    print("Você só pode sacar no máximo R$500,00 por vez.")
            else:
                print("Saldo insuficiente.")
        
        else:
            print("Número de saques diários excedidos, contate o gerente.")

    elif opcao == "e":
        print("Extrato")
        if extrato:
            print(extrato)
        else:
            print("Não foram realizadas operações")
        print(f"Saldo atual: R$ {saldo:.2f}\n")

    elif opcao == "q":
        break

    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.")