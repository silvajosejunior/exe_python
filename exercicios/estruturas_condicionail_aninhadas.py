conta_normal = False
conta_universitaria = False

saldo = 1500
saque = 4000
cheque_especial = 450


if conta_normal:
    if saldo >= saque:
        print('saque realizado com sucesso!')
    elif saque <= (saldo + cheque_especial):
        print('saque realizado com cheque especial')
    else:
            print('nao  foi possivel realizar o saque')
elif conta_universitaria:
    if saldo >= saque:
        print('Saque realizado com Sucesso!')
    else:
        print('saldo Insuficiente!')  
else:
    print ('entre em contato com seu gerente')