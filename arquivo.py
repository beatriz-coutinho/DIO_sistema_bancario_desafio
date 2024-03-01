def menu():
    print('''
BANCO LIBCONTA
OPERAÇÃO:
[1] Depositar
[2] Sacar
[3] Visualizar extrato
[4] Mostrar menu
[5] Sair
''')
    
menu()

qtdSaque = 3
saldoAtual = 0
extrato = ''

while True:
    print('BANCO LIBCONTA')
    opc = int(input('Opção desejada: '))
    while opc < 1 or opc > 5:
        opc = float(input('Digite uma opção válida (4 para ver o menu): '))
    
    # OPÇÃO 1
    if opc == 1:
        deposito = float(input('Valor do depósito (mínimo de R$100.00): R$'))
        while deposito < 100:
            deposito = float(input('Digite uma quantia válida (mínimo de R$100.00): R$'))
        saldoAtual += deposito
        extrato += f'Depósito: R${deposito:.2f} || Saldo: R${saldoAtual:.2f}'
    # OPÇÃO 2
    elif opc == 2:
        if qtdSaque > 0:
            qtdSaque -= 1
            saque = float(input('Valor do saque (máximo de R$500.00): R$'))
            while saque < 0 or saque > 500:
                saque = float(input('Digite uma quantia válida: '))
            if saque > saldoAtual:
                print(f'Saldo insuficiente. Você tem R${saldoAtual:.2f} depositado.')
            else:
                saldoAtual -= saque
                extrato += f'Saque: R${saque:.2f} || Saldo: R${saldoAtual:.2f}#'
                print(f'Saque de R${saque:.2f} realizado com sucesso!')
        else:
            print('Limite máximo de saques atingido.')
    # OPÇÃO 3
    elif opc == 3:
        if extrato == '':
            print('Nenhuma movimentação realizada.')
        else:
            for operacao in extrato.split('#'):
                print(operacao)
    elif opc == 4:
        menu()
    else:
        break