'''Criar funções sacar, depositar e visualizar'''



print('--------Menu--------\n1- Depositar\n2- Sacar\n3- Visualizar Extrato\n5- Sair\n')
numero_saques = 0
limite_saque = 3
saque_máximo= 500
saldo= 0
extrato = ""
menu = 0
valor = 0

while True:
    menu = int(input("Digite o número da opção que deseja: "))
    if menu == 1:
        valor = float(input("Digite o valor que quer depositar: "))
        if valor > 0:     
            saldo += valor
            extrato += f"Depósito: R$ {valor:.2f}\n"

        else:
            print("Operação não realizada, tente novamente")

    elif menu == 2:
        if numero_saques < limite_saque:
            valor = float(input("Digite o valor que quer sacar: "))
            if valor < saldo:
                if valor < saque_máximo:
                    saldo -= valor
                    extrato += f"Saque R$ {valor:.2f}\n"
                    numero_saques += 1
                else:
                    print("valor limite de saque de R$ 500,00")
            else:
                print("Saldo insuficiente, tente novamente!")
        else:
            print("Valor de saque diário excedido")
    
    elif menu == 3:
        if extrato == "":
            print("Nenhuma operação realizada")
        else:
            print("----------Extrato----------")
            print(extrato)
    
    elif menu == 5:
        break

    else: 
        print("Escolha  inválida, tente novamente!") 

                



        
    