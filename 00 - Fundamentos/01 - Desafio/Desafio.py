'''
Objetivo Geral:

* Criar um sistema bancário com as operações: sacar, depositar e visualizar extrato.

Desafio:

* Fomos contratados por um grande banco para desenvolver o seu novo sistema. Esse banco deseja modernizar suas operações e para isso escolheu a linguagem Python. Para a primeira versão do sistema devemos implementar apenas 3 operações: depósito, saque e extrato.

Operação de depósito:

* Deve ser possível depositar valores positivos para a minha conta bancária. A v1 do projeto trabalha apenas com 1 usuário, dessa forma não precisamos nos preocupar em identificar qual é o número da agência e conta bancária. Todos os depósitos devem ser armazenados em uma variável e exibidos na operação de extrato.

Operação de saque:

* O sistema deve permitir realizar 3 saques diários com limite máximo de R$ 500,00 por saque. Caso o usuário não tenha saldo em conta, o sistema deve exibir uma mensagem informando que não será possível sacar o dinheiro por falta de saldo. Todos os saques devem ser armazenados em uma variável e exibidos na operação de extrato.

Operação de extrato:

* Essa operação deve listar todos os depósitos e saques realizados na conta. No fim da listagem deve ser exibido o saldo atual da conta. Se o extrato estiver em branco, exibir a mensagem: Não foram realizadas movimentações.
Os valores devem ser exibidos utilizando o formato R$ xxx.xx, exemplo:
1500.45 = R$ 1500.45

'''

menu = """

[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

=> """

saldo = 0
limite = 500
extrato = ""
numero_depositos = 0
numero_saques = 0
LIMITE_SAQUES = 3
deposito_total = 0
saques_total = 0

while True:

    opcao = input(menu)

    if opcao == "d":
        quantidade_deposito = float(input("Digite a quantia que você deseja depositar: "))
        saldo += quantidade_deposito
        print(f'Deposito de: R$ {quantidade_deposito:.2f} Realizado com sucesso!')
        print(f'Novo saldo de: R$ {saldo:.2f}')
        numero_depositos += 1
        deposito_total += quantidade_deposito
        
    elif opcao == "s":
        if numero_saques < LIMITE_SAQUES:
            saque_solicitado = float(input("Digite quanto você quer sacar da conta: "))
            if saque_solicitado <= limite:
                if saque_solicitado <= saldo:
                    saldo -= saque_solicitado
                    numero_saques +=  1
                    saques_total += saque_solicitado
                    print(f'Foi sacado da sua conta bancária: R$ {saque_solicitado:.2f}')
                    print(f'Novo saldo de: R$ {saldo:.2f}')
                else:
                    print(f'Seu saldo é de: R$ {saldo:.2f}')
                    print(f'Seu saldo é menor que a quantia de: R$ {saque_solicitado:.2f}')
            else:
                print("O limite de saque é R$ 500,00.")    
        else:
            print("Limite diário atingido")
            
    elif opcao == "e":
        opcao_extrato = str(input("Você deseja o extrato de depósito ou de saque? use [d] para depósito e [s] para saque: "))
        if opcao_extrato == "d":
            print(f'Foram feitos {numero_depositos} depósitos de no total R$ {deposito_total:.2f}')
        elif opcao_extrato == "s":
            print(f'Foram feitos {numero_saques} saques de no total R$ {saques_total:.2f}')
        else:
            print("Opção inválida.")
    elif opcao == "q":
        break
    else:
        print("Opção inválida.")