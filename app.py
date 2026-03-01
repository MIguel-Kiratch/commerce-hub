import os

estabelecimentos = [{'nome':'Sakamoto', 'categoria':'Posto de combustível', 'ativo':False},
                    {'nome':'Madero', 'categoria':'Restaurante', 'ativo':True}]

def exibir_nome_do_app():
      print('''                                                                                                                        
    ▄▄▄▄                                                                                   ▄▄    ▄▄            ▄▄       
  ██▀▀▀▀█                                                                                  ██    ██            ██       
 ██▀        ▄████▄   ████▄██▄  ████▄██▄   ▄████▄    ██▄████   ▄█████▄   ▄████▄             ██    ██  ██    ██  ██▄███▄  
 ██        ██▀  ▀██  ██ ██ ██  ██ ██ ██  ██▄▄▄▄██   ██▀      ██▀    ▀  ██▄▄▄▄██            ████████  ██    ██  ██▀  ▀██ 
 ██▄       ██    ██  ██ ██ ██  ██ ██ ██  ██▀▀▀▀▀▀   ██       ██        ██▀▀▀▀▀▀   █████    ██    ██  ██    ██  ██    ██ 
  ██▄▄▄▄█  ▀██▄▄██▀  ██ ██ ██  ██ ██ ██  ▀██▄▄▄▄█   ██       ▀██▄▄▄▄█  ▀██▄▄▄▄█            ██    ██  ██▄▄▄███  ███▄▄██▀ 
    ▀▀▀▀     ▀▀▀▀    ▀▀ ▀▀ ▀▀  ▀▀ ▀▀ ▀▀    ▀▀▀▀▀    ▀▀         ▀▀▀▀▀     ▀▀▀▀▀             ▀▀    ▀▀   ▀▀▀▀ ▀▀  ▀▀ ▀▀▀   
                                                                                                                        
                                                                                                                        ''')

def finalizar_app():
      exibir_subtitulos('Saindo... ')

def exibir_opcoes():
      print('1. Cadastrar Estabelecimento')
      print('2. Listar Estabelecimento')
      print('3. Alterar estado do Estabelecimento')
      print('4. Sair\n')

def voltar_ao_menu():
      input('\nDigite uma tecla para voltar ao menu principal: ')
      main()

def opcao_invalida():
      os.system('cls')
      print('Opção invalida!!!')
      voltar_ao_menu()

def exibir_subtitulos(texto):
      os.system('cls')
      linha = '-' * len(texto)
      print(linha)
      print(texto)
      print(linha)
      print()

def cadastrar_novos_estabelecimentos():
      exibir_subtitulos('Cadastrar novos estabelecimentos...')
      nome_estabelecimento = input('Qual o nome do estabelecimento? ')
      categoria = input(f'Digite o nome da categoria do Estabelcimento {nome_estabelecimento}: ')
      dados_estabelecimento = {'nome': nome_estabelecimento, 'categoria': categoria, 'ativo': False}
      estabelecimentos.append(dados_estabelecimento)
      print(f'O estabelecimento {nome_estabelecimento} foi cadastrado!')
      voltar_ao_menu()

def listando_estabelecimentos():
      exibir_subtitulos('Listando estabelecimentos...')
      print(f'{'Nome do Estabelecimento'.ljust(21)} | {'Categoria'.ljust(22)} | {'Status'}')
      for estabelecimento in estabelecimentos:
            nome_estabelecimento = estabelecimento['nome']
            categoria = estabelecimento['categoria']
            ativo = 'ativado' if estabelecimento['ativo'] else 'desativado'
            print(f'- {nome_estabelecimento.ljust(20)}  |- {categoria.ljust(21)} |- {ativo}')
      voltar_ao_menu()

def alterar_estado_estabelecimento():
      exibir_subtitulos('Alterando estado do estabelecimento')
      nome_estabelecimento = input('Digite o nome do estabelecimento que deseja alterar o estado: ')
      estabelecimento_encontrado = False
      
      for estabelecimento in estabelecimentos:
            if nome_estabelecimento == estabelecimento['nome']:
                  estabelecimento_encontrado = True
                  estabelecimento['ativo'] = not estabelecimento['ativo']
                  mensagem = f'O estabelecimento {nome_estabelecimento} foi ativado com sucesso' if estabelecimento['ativo'] else f'O estabelecimento {nome_estabelecimento} foi desativado com sucesso'
                  print(mensagem)
      
      if not estabelecimento_encontrado:
            print('O estabelecimento não foi encontrado')

      voltar_ao_menu()

def escolher_opcoes():
      try:
            opcao_1 = int(input('Escolha uma opção '))
            print(f'Opção {opcao_1} escolhida')

            if opcao_1 == 1:
                  cadastrar_novos_estabelecimentos()
            elif opcao_1 == 2:
                  listando_estabelecimentos()
            elif opcao_1 == 3:
                  alterar_estado_estabelecimento()
            elif opcao_1 == 4:
                  finalizar_app()
            else:
                  opcao_invalida()
      except ValueError:
            opcao_invalida()

def main():
      os.system('cls')
      exibir_nome_do_app()
      exibir_opcoes()
      escolher_opcoes()

if __name__ == '__main__':
      main()
