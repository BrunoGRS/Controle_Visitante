import flet as ft
from banco import Conexao

def main(page: ft.Page):
    page.horizontal_alignment = 'center'
    page.vertical_alignment = 'center'
    page.window_height = 500
    page.window_width = 500
    
    titulo = ft.Text(value="Cadastro de visitantes", font_family="Cascadia Mono", size=20)

    user = ft.TextField(label="Usuário", border_color="white", width=350)

    senha = ft.TextField(label="Senha", border_color="white", width=350)

    def button_clicked(e):
        if not user.value or len(str(user)) > 15:
            user.error_text="Campo Iválido."
            page.update()
        if not senha.value:
            senha.error_text="Informe a senha!"
            page.update()
        else:
            entrada1 = user.value
            entrada2 = senha.value

            validar = Conexao.validar_usuario(Conexao, entrada1, entrada2)
            if validar == "Validado":
                page.clean()
                titulo = ft.Text(value="Cadastro de visitantes", font_family="Cascadia Mono", size=20)
                page.add(titulo)
            else:
                warning = page.error("Acesso negado")
                warning.remove()

    page.add(titulo, user, senha, ft.FilledButton(text="Entrar", on_click=button_clicked))

ft.app(target=main)
