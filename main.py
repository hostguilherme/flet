import flet as ft
def main(page: ft.Page):
    # configuração da pagina
    page.title = 'Login Screen'
    page.window_width = 600
    page.window_height = 600
    page.window_resizable = False
    page.padding = 100
    page.theme_mode = 'dark'
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    
    # Função que é chamada quando o botão é clicado
    def btn_click(e):
        # Verifica se ambos os campos (Nome e Senha) estão preenchidos.
        if all([name_input.value, pass_input.value]):
            dlg = ft.AlertDialog(
                title=ft.Text('Bem Vindo ' + name_input.value))
            page.dialog = dlg
            dlg.open = True
            page.update()  # Correção: Adicionado parênteses

    # Componetes da interface do usuário
    page.appbar = ft.AppBar(title=ft.Text('Login Screen'))
    name_input = ft.TextField(
        label='Nome', autofocus=True, hint_text='Digite seu nome')
    pass_input = ft.TextField(
        label='Senha', password=True, can_reveal_password=True)
    submit_btn = ft.ElevatedButton(
        text='Enviar', width=600, on_click=btn_click)
    
    page.add(name_input, pass_input, submit_btn)
ft.app(target=main)
