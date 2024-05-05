import flet as ft

registros = []  # Vector para almacenar los registros

def guardar_registro():
    datos_registro = []
    for campo in campos_texto:
        datos_registro.append(campo.value)  # Usar el atributo 'value' en lugar de 'text'
    registros.append(datos_registro)
    print("Registros:", registros)

def main(page: ft.Page):
    global campos_texto
    page.window_width = 450
    page.window_height = 600
    page.padding = 0
    page.vertical_alignment = "center"
    page.horizontal_alignment = "center"

    campo_nombre = ft.TextField(
        width=280,
        height=40,
        hint_text='Nombre',
        border='underline',
        color='black',
        prefix_icon=ft.icons.PERSON,
    )
    campo_correo = ft.TextField(
        width=280,
        height=40,
        hint_text='Correo electrónico',
        border='underline',
        color='black',
        prefix_icon=ft.icons.EMAIL,
    )
    campo_contraseña = ft.TextField(
        width=280,
        height=40,
        hint_text='Contraseña',
        border='underline',
        color='black',
        prefix_icon=ft.icons.LOCK,
        password=True,
    )

    campos_texto = [campo_nombre, campo_correo, campo_contraseña]

    contenedor = ft.Container(
        ft.Column(
            [
                campo_nombre,
                campo_correo,
                campo_contraseña,
                ft.ElevatedButton(
                    content=ft.Text(
                        'Guardar Registro',
                        color='white',
                        weight='w500',
                    ),
                    width=280,
                    bgcolor='black',
                    on_click=lambda e: guardar_registro(),
                ),
            ],
            alignment=ft.MainAxisAlignment.CENTER,
            spacing=20,
        ),
        padding=10,
    )

    page.add(contenedor)

ft.app(target=main)
