saldo = 3000
saque = 2500

status = 'SUCESSO' if saque <=saldo else 'SEM SALDO'
print(' ao realizar o saque:', status)
print(f'{status} ')


status = 'GANHOU' if saque <= saldo else 'PERDEU'
print(' O RSULTADO FOI: \n', status)

nome = input('digite seu nome')