import flet as ft

# Función para guardar los registros en un archivo
def guardar_registros(registros):
    with open("registros.txt", "w") as file:
        for registro in registros:
            file.write(",".join(registro) + "\n")


def cargar_registros():
    registros = []
    try:
        with open("registros.txt", "r") as file:
            for line in file:
                registros.append(line.strip().split(","))
    except FileNotFoundError:
        pass  # Si el archivo no existe, no hay registros para cargar
    return registros


def guardar_registro():
    datos_registro = []
    for campo in campos_texto:
        datos_registro.append(campo.value)
    registros.append(datos_registro)
    guardar_registros(registros)
    print("Registro guardado:", datos_registro)

# Función principal
def main(page: ft.Page):
    global campos_texto, registros
    registros = cargar_registros()  # Cargar registros existentes al iniciar la aplicación
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
                campo_nombre  ,
                campo_correo  ,
                campo_contraseña  ,
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
