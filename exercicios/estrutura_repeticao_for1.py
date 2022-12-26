opcao = -1
while opcao != 0:
    opcao = int(input("[1] Sacar \n[2] Extrato \n[3]Ajuda \n[0] Sair \n "))
    if opcao == 1:
        print("Sacando...")
    elif opcao == 2:
       print("Exibindo o extrato...")

    elif opcao == 3:
        print('Ajuda... ')

print("Obrigado por usar nosso sistema bancário, até logo!")