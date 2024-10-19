import os

cafeterias = [{'nome':'Go Coffee', 'categoria' : 'Café Regional', 'ativa': False},
              {'nome':'The Coffee', 'categoria' : 'Café Japonês', 'ativa': True}]

def exibir_nome_do_programa():

    print(
'''
╭╮╱╱╱╱╱╱╱╱╱╱╱╱╱╱╭━╮
┃┃╱╱╱╱╱╱╱╱╱╱╱╱╱╱┃╭╯
┃╰━┳╮╭┳━━┳━━┳━━┳╯╰┳━━╮
┃╭╮┃┃┃┃━━┫╭━┫╭╮┣╮╭┫┃━┫
┃╰╯┃╰╯┣━━┃╰━┫╭╮┃┃┃┃┃━┫
╰━━┻━━┻━━┻━━┻╯╰╯╰╯╰━━╯''')

def exibir_opcoes():
   
    print('1. Cadastrar cafeteria')
    print('2. Listar cafeterias')
    print('3. Alternar estado da cafeteria')
    print('4. Sair do app\n')

def finalizar_app():
    exibir_subtitulo('Finalizando o aplicativo')

def voltar_menu_principal():
    input('\nDigite um tecla para voltar ao menu principal')
    main()

def opcao_invalida():
    print('Opção inválida!\n')
    voltar_menu_principal()

def exibir_subtitulo(texto):
    os.system('cls')
    linha = '*' * (len(texto))
    print(linha)
    print(texto)
    print(linha)
    print()

def cadastrar_nova_cafeteria():
    exibir_subtitulo('Cadastro de novas cafeterias')
    nome_da_cafeteria = input('Digite o nome da cafeteria que deseja cadastrar: ')
    categoria = input(f'Digite o nome da categoria da cafeteria {nome_da_cafeteria}: ')
    dados_da_cafeteria = {'nome': nome_da_cafeteria, 'categoria': categoria, 'ativa': False}
    cafeterias.append(dados_da_cafeteria)
    print(f'A cafeteria {nome_da_cafeteria} foi cadastrada com sucesso!')

    voltar_menu_principal()

def listar_cafeterias():
    exibir_subtitulo('Listando as Cafeterias')

    print(f"{'Nome da cafeteria'.ljust(22)} | {'Categoria'.ljust(20)} | Status")
    for cafeteria in cafeterias:
        nome_cafeteria = cafeteria['nome']
        categoria = cafeteria['categoria']
        ativa = 'ativada' if cafeteria['ativa'] else 'desativada'
        print(f'- {nome_cafeteria.ljust(20)} | {categoria.ljust(20)} | {ativa}')
    voltar_menu_principal()

def alternar_estado_da_cafeteria():
    exibir_subtitulo('Alternando o estado da cafeteria')
    nome_cafeteria = input("Digite o nome da cafeteria que deseja alternar o estado: ")
    cafeteria_encontrada = False

    for cafeteria in cafeterias:
        if nome_cafeteria == cafeteria['nome']:
            cafeteria_encontrada = True
            cafeteria['ativa'] = not cafeteria['ativa']
            mensagem = f'A cafeteria {nome_cafeteria} foi ativada com sucesso' if cafeteria['ativa'] else f'A cafeteria {nome_cafeteria} foi desativada com sucesso'
            print(mensagem)

    if not cafeteria_encontrada:
        print('A cafeteria não foi encontrada')

    voltar_menu_principal()

def escolher_opcao():
    try:
        opcao_escolhida = int(input('Escolha uma opção: '))

        if opcao_escolhida == 1:
            cadastrar_nova_cafeteria()

        elif opcao_escolhida == 2:
            listar_cafeterias()

        elif opcao_escolhida == 3:
            alternar_estado_da_cafeteria()

        elif opcao_escolhida == 4:
            finalizar_app()

        else:
            opcao_invalida()
    except ValueError:
        opcao_invalida()

def main():
    os.system('cls')
    exibir_nome_do_programa()
    exibir_opcoes()
    escolher_opcao()

if __name__ == '__main__':
    main()
