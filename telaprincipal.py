from banco import Conexao

Conexao.conectar(self=Conexao)

while True:
    print("="*50)
    print("Controle de visitante")
    print("="*50)

    escolha = input("1 - logar no sistema\n2 - Cadastrar usuário\n3- Sair\n")

    if int(escolha) == 1:
        user = input("Usuário -> ")
        senha = input("Senha -> ")
        validar = Conexao.validar_usuario(Conexao, user, senha)
        if validar == "Validado":
            while True:
                escolha2 = int(input(f"\nSeja Bem-vindo {user}.\n\nEscolha qual menu deseja acessar.\n\n1- Cadastrar Visitante\n2- Cadastrar visita\n3- Cadastrar saida de Visita\n4- Excluir\n0- Sair\n->"))
                if escolha2 == 1:
                    print("="*50)
                    print("Cadastro de visitante")
                    print("="*50)

                    Conexao.cadastrar_visitante(Conexao)

                elif escolha2 == 2:
                    print("="*50)
                    print("Cadastro de visita")
                    print("="*50)

                    Conexao.cadastro_visita(Conexao)
                elif escolha2 == 3:
                    print("="*50)
                    print("Cadastro de saida de visita")
                    print("="*50)

                    Conexao.cadastro_saidavisita(Conexao)

                elif escolha2 == 4:
                    print("="*50)
                    print("Exclusão de dados")
                    print("="*50)

                    while True:
                        Conexao.exclusao_banco(Conexao)
                        escolha = int(input("\nDeseja sair?\n1- Sim\n2- Não\n->"))

                        if escolha == 1:
                            break
                    
                else: break

        else: print("\nAcesso negado!\n")

    elif int(escolha) == 2:
        cas = Conexao.cadastrar_usuario(Conexao)
        if cas:
            print("\nCadastro feito com sucesso! Favor selecionar a opção de login na próxima tela.\n")
        else: print("\nErro no cadastro de usuário.\n")
    else:
        Conexao.finalizar_conexao(Conexao)
        break