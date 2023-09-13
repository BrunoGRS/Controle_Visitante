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

        cpf = int(input("Digite os 5 primeiros digitos do cpf -> "))
        nome = input("Digite teu nome -> ")
        user = input("Digite seu nome de login (máximo 15 letras) -> ")
        senha = input("Digite sua senha -> ")   

        cursor.execute(f"INSERT INTO usuarios(cpf_user,nome_user,user_user,user_senha) VALUES ({cpf},'{nome}','{user}','{senha}')")
        connect.commit()

        return cursor
    
    def cadastrar_visitante(self):
        connect = self.conectar(self)
        cursor = connect.cursor()

        cpf = int(input("Digite os 5 primeiros digitos do CPF do visitante -> "))
        nome = input("Digite o nome completo do visitante -> ")

        escolha = input("Confirmar cadastro?\n S - Sim N -Não\n -> ").upper()

        if escolha == 'S':
            cursor.execute(f"INSERT INTO visitante(cpf_visitante,nome_visitante) VALUES ({cpf}, '{nome}')")
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
    
    def validar_usuario(self, user, senha):
        connect = self.conectar(self)
        cursor = connect.cursor()

        cursor.execute(f"SELECT * FROM usuarios WHERE user_user='{user}' and user_senha='{senha}'")
        user = cursor.fetchall()

        if user:
            return "Validado"
        else: return "Não validado"

    def finalizar_conexao(self):
        if 'conect' in locals():
            conect = self.conectar(self)
            conect.close()