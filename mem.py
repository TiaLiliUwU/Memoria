# Codado por Aliyah

import os
import platform
file_name = 'dados.txt'
lista_transf = []
sel1 = None
last_line = None
debug_exit = None
so = platform.system()

# Comando Clear apropriado
def clear():
    if so == 'Windows':
        os.system('clr')
    else:
        os.system('clear')
#
# Cabeçalho
clear()
print('Bem vindo ao Memória! \n\n')
#
# Swap
if os.path.exists('dados.txt'):
    with open(file_name) as dadostxt:
        debug_exit = 'Existia'
        dados = dadostxt.read().splitlines()
        for ln in dados:
            lista_transf.append(ln)
    dadostxt.close()
#
else:
    debug_exit = 'Não existia'
# Seleção
while True:
    print('O que deseja fazer? \n\n1 - Gravar novo dado \n2 - Ver último dado registrado \n3 - Ver todos os dados registrados \n4 - Resetar lista \n5 - Sair')
    sel1 = input('\nSelecione uma opção: ')
    clear()
# Gravar novo dado
    if sel1 == '1':
        print('Digite o dado que deseja ser guardado: ')
        print()
        nvdd = input()
        lista_transf.append(nvdd)
        print('\nDado guardado com sucesso:', nvdd, '\n\n')
        input('Aperte enter para continuar...')
        clear()
#
# Último dado
    elif sel1 == '2':
        print('Este é o último dado registrado: \n')
        verific = len(lista_transf)
        if verific == 0:
            print('Não há nenhum dado registrado')
        else:
            print(lista_transf[-1])
        input('\nAperte enter para continuar...')
        clear()
#
# Todos os dados
    elif sel1 == '3':
        print('Estes são todos os dados armazenados: \n')
        verific = len(lista_transf)
        if verific == 0:
            print('Não há nenhum dado registrado')
        else:
            for dd in lista_transf:
                print(dd)
        input('\nAperte enter para continuar...')
        clear()
#
# Reset
    elif sel1 == '4':
        del lista_transf[0:]
        with open(file_name, 'w+') as dadostxt:
            pass
        dadostxt.close()
        clear()
        print('Lista resetada com sucesso! \n\n')
        input('Aperte enter para continuar...')
        clear()
# Sair
#
    elif sel1 == '5':
        with open(file_name, "w+") as dadostxt:
            for dd in lista_transf:
                dadostxt.write(dd + '\n')
        dadostxt.close()
        print('Bye Bye ;)')
        exit()
# Debug
#
    elif sel1 == '666':
        print('Debug mode: \n')
        print('Sistema operacional' + ' ' + so + '\n')
        print('O documento' + ' ' + debug_exit + '\n')
        print(lista_transf)
        input('\nAperte enter para continuar...')
        clear()
    else:
        print('Por favor, selecione uma opção válida')
#
