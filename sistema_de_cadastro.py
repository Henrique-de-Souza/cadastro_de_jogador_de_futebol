"""
Crie um programa que gerencie o aproveitamento de um jogador de futebol.
O programa irá ler o nome e a quantidade de partidas que ele jogou.
Depois, vai ler a quantidade de gols em cada partida.
No final, tudo isso será guardado em um dicionário, incluindo o total
de gols.
"""
from time import sleep
dados_do_jogador = {}
soma = 0
gols = 0

while True:
    # Guardando nome e quantidade de partidas de um jogador de futebol ----------------------------------------------------
    dados_do_jogador['nome'] = str(input('Nome do jogador:'))
    dados_do_jogador['partidas'] = int(input(f'Quantas partida {dados_do_jogador["nome"]} jogou?'))

    # Iniciando uma lista da quantidade de gols por partidas e guardando dentro do dicionário ------------------------------
    dados_do_jogador['Gols por partidas'] = []


    for partida in range(dados_do_jogador['partidas']):
        gols = int(input(f'Na {partida + 1}ª partida {dados_do_jogador["nome"]} fez quantos gols:'))
        dados_do_jogador['Gols por partidas'].append(gols)
        soma += gols

    print('Gerando um relatório....')
    sleep(2)

    print('=' * 60)
    print(dados_do_jogador)
    sleep(1)
    print('=' * 60)
    sleep(1)

    for k, v in dados_do_jogador.items():
        print(f'{k}: {v}.')
        sleep(1)

    print('=' * 60)
    sleep(1)

    if dados_do_jogador['partidas'] >= 1:

        # 1ª condição: Se jogou ou não mais de uma partida -----------------------------------------------------------------
        print('QUANTIDADE DE PARTIDAS:')
        if dados_do_jogador['partidas'] > 1:
            print(f'O jogador {dados_do_jogador["nome"]} jogou {dados_do_jogador["partidas"]} partidas')
        elif dados_do_jogador['partidas'] == 1:
            print(f'O jogador {dados_do_jogador["nome"]} jogou apenas {dados_do_jogador["partidas"]} partida')

        print('=' * 60)
        sleep(1)

        # 2ª condição: Se teve ou não gols por patidas ---------------------------------------------------------------------
        print('QUANTIDADE DE GOLS POR PARTIDAS:')
        if dados_do_jogador['partidas'] > 1:
            for partida, gols in enumerate(dados_do_jogador["Gols por partidas"]):
                print(f'Na {partida + 1}ª partida: {dados_do_jogador["nome"]} fez {gols} gols')
                sleep(1)

        elif dados_do_jogador['partidas'] == 1 and soma == 1:
            print(f'Nesta única partida: {dados_do_jogador["nome"]} fez somente {gols} gol')

        elif dados_do_jogador['partidas'] == 1 and soma > 1:
            print(f'Nesta única partida: {dados_do_jogador["nome"]} fez {gols} gols')

        print('=' * 60)
        sleep(1)

        # 3ª condição: Total de gols por partidas --------------------------------------------------------------------------
        print('TOTAL DE GOLS POR PARTIDA:')
        if soma and dados_do_jogador['partidas'] > 1:
            print(f'O jogador {dados_do_jogador["nome"] } fez um total de {soma} gols em {dados_do_jogador["partidas"]} partidas.')

        elif soma > 1 and dados_do_jogador['partidas'] == 1:
            print(f'O jogador {dados_do_jogador["nome"] } fez {soma} gols em {dados_do_jogador["partidas"]} única partida.')

        elif soma == 1 and dados_do_jogador['partidas'] == 1:
            print(f'O jogador {dados_do_jogador["nome"] } fez somente {soma} gol em {dados_do_jogador["partidas"]} única partida.')

    else:
        print(f'{dados_do_jogador["nome"]}, não jogou nesse campeonato')

    print('=' * 60)
    sleep(2)

    continuar = str(input('Quer refazer com outro jogador? [S/N]')).strip().upper()[0]
    if continuar == 'N':
        sleep(1)
        print('Finalizando programa.....')
        sleep(1)
        break

    sleep(1)
    print('=' * 20)
    sleep(2)