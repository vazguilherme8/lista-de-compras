from time import sleep
import os
lista = []

def adicionar_produto(produto, quantidade, medida):
    id = len(lista) + 1
    lista.append({'produto': produto, 'quantidade' : quantidade, 'medida' : medida, 'id' : id})

def remover_produto(id):
    for produto in lista:
        if produto['id'] == id:
            lista.remove(produto)
            print(f'{produto['produto'].title()} removido com sucesso.')
            voltar_menu()
        if id > len(lista):
            print('ID inválido, tente novamente.')
            voltar_menu() 

def pesquisar_produto(nome_produto):
    produto_encontrado = False 
    for produto in lista:
        if nome_produto in produto['produto']:
            produto_encontrado = True
            print(f'Produto: {produto['produto']} | Quantidade: {produto['quantidade']} | Medida: {produto['medida']} | ID: {produto['id']}')
            print()
    if not produto_encontrado:
        print('Nenhum produto encontrado.')
        voltar_menu()
    voltar_menu()

def voltar_menu():
    input('Aperte ENTER para voltar ao menu principal')
    main()

def msg_opcao_escolhida(msg):
    os.system('cls')
    print(f'**{msg.upper()}**\n')
    
def listar_produtos():
    print()
    print('**LISTA ATUAL**')
    for produto in lista:
        print(f'Produto: {produto['produto']} | Quantidade: {produto['quantidade']} {produto['medida']} | ID: {produto['id']}')
    print()

def opcoes_menu():
    os.system('cls')
    print('Bem vindo a lista de compras!')
    listar_produtos()
    print('''1 - Adicionar produto
2 - Remover produto
3 - Pesquisar produtos
4 - Sair do programa
          ''')

def menu_principal():
    while True:
        opcoes_menu()
        try:
            opcao = int(input('Escolha uma das opções acima: '))
            match opcao:
                case 1:
                    msg_opcao_escolhida('ADICIONAR PRODUTO')
                    opcao_produto = str(input('Qual produto deseja adicionar a lista?\n'))
                    opcao_quantidade = float(input('Qual a quantidade desejada?\n'))
                    opcao_medida = str(input('Qual a unidade de medida? '))
                    adicionar_produto(opcao_produto, opcao_quantidade, opcao_medida)
                    print('Produto adicionado com sucesso!')
                    sleep(1)
                    main()
                case 2:
                    msg_opcao_escolhida('REMOVER PRODUTO')
                    listar_produtos()
                    opcao_remover = int(input('Digite o ID do produto que deseja remover: '))
                    remover_produto(opcao_remover)
                    main()
                case 3:
                    msg_opcao_escolhida('pesquisar produto')
                    opcao_pesquisa = str(input('Digite qual produto deseja pesquisar: '))
                    pesquisar_produto(opcao_pesquisa)
                    main()
                case 4:
                    print('Saindo do programa...')
                    sleep(1)
                    print('Volte sempre!')
                    sleep(1.5)
                    break
                case _:
                    print('Opção inválida. Tente novamente')
                    sleep(1.5)
                    main()
        except ValueError:
            print('Erro. Digite apenas números.')
            sleep(1.5)
            main()

def main():
    menu_principal()

if __name__ == '__main__':
    main()