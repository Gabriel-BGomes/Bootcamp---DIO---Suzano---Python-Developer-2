saldo = 0
limite = 500
extrato = ""
numero_depositos = 0
numero_saques = 0
LIMITE_SAQUES = 3
deposito_total = 0
saques_total = 0

# Funções:

def depositar():
        
    quantidade_deposito = float(input("Digite a quantia que você deseja depositar: "))
        
    # Declarando variaveis globais dentro do meu método depositar: 
    global saldo, numero_depositos, extrato

    if quantidade_deposito >0:
        saldo += quantidade_deposito
        print(f'Deposito de: R$ {quantidade_deposito:.2f} Realizado com sucesso!')
        print(f'Novo saldo de: R$ {saldo:.2f}')
        numero_depositos += 1
        extrato += f'Deposito de: R$ {quantidade_deposito:.2f}\n'
    else:
        print("Este valor para depósito não é válido.")
    
def sacar():
        
    # Declarando variaveis globais dentro do meu método sacar: 
    global saldo, numero_saques, extrato, LIMITE_SAQUES, numero_saques
        
    if numero_saques < LIMITE_SAQUES:
        saque_solicitado = float(input("Digite quanto você quer sacar da conta: "))
            
        if saque_solicitado <= limite:
            if saque_solicitado <= saldo:
                saldo -= saque_solicitado
                numero_saques +=  1
                extrato += f'Saque de: R$ {saque_solicitado:.2f}\n'
                print(f'Foi sacado da sua conta bancária: R$ {saque_solicitado:.2f}')
                print(f'Novo saldo de: R$ {saldo:.2f}')
            else:
                print(f'Seu saldo é de: R$ {saldo:.2f}')
                print(f'Seu saldo é menor que a quantia de: R$ {saque_solicitado:.2f}')
        else:
            print("O limite de saque é R$ 500,00.")    
    else:
        print("Limite diário atingido")      
            
def exibir_extrato():
        
    # Declarando variaveis globais dentro do meu método exibir_extrato: 
    global saldo, extrato, numero_depositos, numero_saques
        
    print("O Extrato é: \n")
    print(f'O saldo atual é de: {saldo}\n')
    print(f'Foram feitos {numero_depositos} depósitos')
    print(f'Foram feitos {numero_saques} saques')
    print(extrato)

menu = """

[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

=> """

while True:

    opcao = input(menu)

    if opcao == "d":
        depositar()
        
    elif opcao == "s":
        sacar()
        
    elif opcao == "e":
        exibir_extrato()
        
    elif opcao == "q":
        break
    else:
        print("Opção inválida.")