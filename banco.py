import mysql.connector
import datetime

class Conexao:
    def __init__(self) -> None:
        pass

    def conectar(self):
       config = {
        'user':'root',
        'password': 'admin',
        'host':'localhost',
        'database':'banco_controle',
        'raise_on_warnings': True
        }
       
       conect = mysql.connector.connect(**config)
       return conect
    
    def cadastrar_usuario(self):
        connect = self.conectar(self)
        cursor = connect.cursor()

        cpf = input("Digite os 5 primeiros digitos do cpf -> ")
        if len(cpf) > 6:
            print("Número de CPF muito longo, favor colocar só os primeiros 5 digitos.")
            return
        
        nome = input("Digite teu nome -> ")
        user = input("Digite seu nome de login (máximo 15 letras) -> ")
        if len(user) > 15:
            print("Nome de usuário muito grande favor colocar outro.")
            return  
        
        senha = input("Digite sua senha -> ")

        cursor.execute(f"INSERT INTO usuarios(cpf_user,nome_user,user_user,user_senha) VALUES ({int(cpf)},'{nome}','{user}','{senha}')")
        connect.commit()

        return cursor
    
    def cadastrar_visitante(self):
        connect = self.conectar(self)
        cursor = connect.cursor()

        cpf = input("Digite os 5 primeiros digitos do CPF do visitante -> ")
        if len(cpf) > 6:
            print("Número de CPF muito longo, favor colocar só os primeiros 5 digitos.")
            return
        
        nome = input("Digite o nome completo do visitante -> ")

        escolha = input("Confirmar cadastro?\n S - Sim N -Não\n -> ").upper()

        if escolha == 'S':
            cursor.execute(f"INSERT INTO visitante(cpf_visitante,nome_visitante) VALUES ({int(cpf)}, '{nome}')")
            connect.commit()
            return cursor
        else: print("\nCadastro cancelado!\n")

    def cadastro_visita(self):
        connect = self.conectar(self)
        cursor = connect.cursor()

        cpf = int(input("Dgite os 5 primeiros digitos do visitante -> "))
        
        motivo = input("Escreva de forma breve o motivo da visita -> ")

        data = datetime.datetime.now()

        cursor.execute(f"SELECT cpf_visitante FROM visitante WHERE cpf_visitante={cpf};")
        validador = cursor.fetchall()

        if validador:
            cursor.execute(f"INSERT INTO visita(cpf_visitante,motivo_visita,data_hora) VALUES ({cpf},'{motivo}','{data}')")
            connect.commit()
            return cursor
        else: return print("CPF não encontrado, favor cadastrar visitante!")

    def cadastro_saidavisita(self):
        connect = self.conectar(self)
        cursor = connect.cursor()

        cpf = int(input("Dgite os 5 primeiros digitos do CPF do visitante -> "))

        data = datetime.datetime.now()

        cursor.execute(f"SELECT cpf_visitante FROM visitante WHERE cpf_visitante={cpf};")
        validador = cursor.fetchall()

        if validador:
            cursor.execute(f"INSERT INTO saida_visita(cpf_visitante,data_Saida) VALUES ({cpf},'{data}')")
            connect.commit()
            print("\nSaida Cadastrada com sucesso.\n")
            return cursor
        else: return print("CPF não encontrado, favor cadastrar visitante!")

    def exclusao_banco(self):
        connect = self.conectar(self)
        cursor = connect.cursor()

        escolha = int(input("\nSelecione qual dado deseja excluir.\n1- Visitante\n2- Visita\n3- Saida Visita\n-> "))

        if escolha == 1:
            cpf = int(input("\nInforme os 5 primeiros digitos do CPF do visitante -> "))

            cursor.execute(f"SELECT * FROM visitante WHERE cpf_visitante={cpf}")
            resultado = cursor.fetchall()

            for dados in resultado:
                print(f"CPF: {dados[0]}")
                print(f"Nome: {dados[1]}")

            escolha1 = int(input("\n Deseja excluir esses dados?\n 1- Sim\n 2- Não\n->"))

            if escolha1 == 1:
                cursor.execute(f"DELETE FROM saida_visita WHERE cpf_visitante={cpf}")
                connect.commit()
                cursor.execute(f"DELETE FROM visita WHERE cpf_visitante={cpf}")
                connect.commit()
                cursor.execute(f"DELETE FROM visitante WHERE cpf_visitante={cpf}")
                connect.commit()
                print("\nExclusão feita com sucesso!\n")
                return cursor
            else: print("\nExclusão Cancelada!\n")

        elif escolha == 2:
            cpf = int(input("\nInforme os 5 primeiros digitos do CPF do visitante -> "))
            if len(cpf) > 6:
                print("Número de CPF muito longo, favor colocar só os primeiros 5 digitos.")
                return

            cursor.execute(f"SELECT * FROM visita WHERE cpf_visitante={cpf}")
            resultado = cursor.fetchall()


            for dados in resultado:
                print(f"ID: {dados[0]}")
                id = dados[0]
                print(f"CPF: {dados[1]}")
                print(f"Motivo: {dados[2]}")
                print(f"Data\Hora: {dados[3]}")

            escolha1 = int(input("\n Deseja excluir esses dados?\n 1- Sim\n 2- Não\n->"))

            if escolha1 == 1:
                cursor.execute(f"DELETE FROM visita WHERE id_visita={id}")
                connect.commit()
                print("\nExclusão feita com sucesso!\n")
                return cursor
            else: print("\nExclusão Cancelada!\n")
                
        else:
            cpf = int(input("\nInforme os 5 primeiros digitos do CPF do visitante -> "))

            cursor.execute(f"SELECT * FROM saida_visita WHERE cpf_visitante={cpf}")
            resultado = cursor.fetchall()


            for dados in resultado:
                print(f"ID: {dados[0]}")
                id = dados[0]
                print(f"CPF: {dados[1]}")
                print(f"Data\Hora: {dados[2]}")

            escolha1 = int(input("\n Deseja excluir esses dados?\n 1- Sim\n 2- Não\n->"))

            if escolha1 == 1:
                cursor.execute(f"DELETE FROM saida_visita WHERE id_visita={id}")
                connect.commit()
                print("\nExclusão feita com sucesso!\n")
                return cursor
            else: print("\nExclusão Cancelada!\n")

    def validar_usuario(self, user, senha):
        connect = self.conectar(self)
        cursor = connect.cursor()

        cursor.execute(f"SELECT * FROM usuarios WHERE user_user='{user}' and user_senha='{senha}'")
        user = cursor.fetchall()

        if user:
            return "Validado"
        else: return "Não validado"


    def finalizar_conexao(self):
        if 'connect' in locals():
            connect = self.conectar(self)
            connect.close()
