import flet as ft

def main(page: ft.Page):
    # Ajustar el tamaño de la ventana para que coincida con el menú y aumentar en 200 píxeles la altura
    page.window_width = 450
    page.window_height = 820 # 520 es el tamaño original del menú
    page.padding = 0
    page.vertical_alignment = "center"
    page.horizontal_alignment = "center"

    def animate(e):
        c.content = c2 if c.content == c1 else c1
        c.update()

    def clear_text_fields():
        # Limpiar los campos de texto
        for container in [c1, c2]:
            for control in container.controls:
                if isinstance(control, ft.Container):
                    for inner_control in control.controls:
                        if isinstance(inner_control, ft.TextField):
                            inner_control.text = ''

    c1 = ft.Container(
        ft.Row([
            ft.Container(
                ft.Column(controls=[
                    ft.Container(
                        ft.Image(
                            src='logo1.png',
                            width=70,
                        ),
                        padding=ft.padding.only(150, 20)
                    ),
                    ft.Text(
                        'Bienvenido',
                        width=360,
                        size=30,
                        weight='w900',
                        text_align='center',
                        font_family='Times New Roman'  # Cambio de tipo de letra
                    ),
                    ft.Container(
                        ft.TextField(
                            width=280,
                            height=40,
                            hint_text='Correo electronico',
                            border='underline',
                            color='black',
                            prefix_icon=ft.icons.EMAIL,
                        ),
                        padding=ft.padding.only(20, 10)
                    ),
                    ft.Container(
                        ft.TextField(
                            width=280,
                            height=40,
                            hint_text='Contraseña',
                            border='underline',
                            color='black',
                            prefix_icon=ft.icons.LOCK,
                            password=True,
                        ),
                        padding=ft.padding.only(20, 10)
                    ),
                    ft.Container(
                        ft.Checkbox(
                            label='Recordar contraseña',
                            check_color='black'
                        ),
                        padding=ft.padding.only(40),
                    ),
                    ft.Container(
                        ft.ElevatedButton(
                            content=ft.Text(
                                'INICIAR',
                                color='white',
                                weight='w500',
                            ),
                            width=280,
                            bgcolor='black',
                            on_click=lambda e: clear_text_fields(),  # Llamar a la función clear_text_fields al hacer clic en el botón "Iniciar"
                        ),
                        padding=ft.padding.only(25, 10)
                    ),
                    ft.Container(
                        ft.Row([
                            ft.Text(
                                '¿No tiene una cuenta?'
                            ),
                            ft.TextButton(
                                'Crear una cuenta',
                                on_click=animate
                            ),
                        ], spacing=8),
                        padding=ft.padding.only(40)
                    ),
                ],
                    alignment=ft.MainAxisAlignment.SPACE_EVENLY,
                ),
                gradient=ft.LinearGradient(['blue', 'black']),
                width=380,
                height=760,
                border_radius=20
            ),
        ],
            alignment=ft.MainAxisAlignment.SPACE_EVENLY,
        ),
        padding=10,
    )

    # Definición de c2, similar a c1 pero con campos adicionales
    c2 = ft.Container(
        ft.Row([
            ft.Container(
                ft.Column(controls=[
                    ft.Container(
                        ft.Image(
                            src='logo2.png',
                            width=70,
                        ),
                        padding=ft.padding.only(150, 20)
                    ),
                    ft.Text(
                        'Crear Cuenta',
                        width=360,
                        size=30,
                        weight='w900',
                        text_align='center'
                    ),
                    ft.Container(
                        ft.TextField(
                            width=280,
                            height=40,
                            hint_text='Nombre',
                            border='underline',
                            color='white',
                            prefix_icon=ft.icons.PERSON,
                        ),
                        padding=ft.padding.only(20, 10)
                    ),
                    ft.Container(
                        ft.TextField(
                            width=280,
                            height=40,
                            hint_text='Correo electronico',
                            border='underline',
                            color='white',
                            prefix_icon=ft.icons.EMAIL,
                        ),
                        padding=ft.padding.only(20, 10)
                    ),
                    ft.Container(
                        ft.TextField(
                            width=280,
                            height=40,
                            hint_text='Usuario',
                            border='underline',
                            color='white',
                            prefix_icon=ft.icons.WEB
                        ),
                        padding=ft.padding.only(20, 10)
                    ),
                    ft.Container(
                        ft.TextField(
                            width=280,
                            height=40,
                            hint_text='Confirmar contraseña',
                            border='underline',
                            color='white',
                            prefix_icon=ft.icons.LOCK,
                            password=True,
                        ),
                        padding=ft.padding.only(20, 10)
                    ),
                    ft.Container(
                        ft.TextField(
                            width=280,
                            height=40,
                            hint_text='Contraseña',
                            border='underline',
                            color='white',
                            prefix_icon=ft.icons.LOCK,
                            password=True,
                        ),
                        padding=ft.padding.only(20, 10)
                    ),
                    ft.Container(
                        ft.Row([
                            ft.Text(
                                'Género:',
                                size=14,
                            ),
                            ft.ElevatedButton(
                                content=ft.Text(
                                    'F',
                                    color='white',
                                    weight='w500',
                                    size=14,
                                    text_align='center'
                                ),
                                width=40,
                                bgcolor='black',
                            ),
                            ft.ElevatedButton(
                                content=ft.Text(
                                    'M',
                                    color='white',
                                    weight='w500',
                                    size=14,
                                    text_align='center',
                                ),
                                width=40,
                                bgcolor='black',
                            ),
                        ], spacing=20),
                        padding=ft.padding.only(20, 10)
                    ),
                    ft.Container(
                        ft.ElevatedButton(
                            content=ft.Text(
                                'REGISTRARSE',
                                color='white',
                                weight='w500',
                            ),
                            width=280,
                            bgcolor='black',
                            on_click=lambda e: clear_text_fields(),  # Llamar a la función clear_text_fields al hacer clic en el botón "Registrarse"
                        ),
                        padding=ft.padding.only(25, 10)
                    ),
                    ft.Container(
                        ft.Row([
                            ft.Text(
                                '¿Ya tiene una cuenta?'
                            ),
                            ft.TextButton(
                                'Iniciar Sesion',
                                on_click=animate
                            ),
                        ], spacing=8),
                        padding=ft.padding.only(40)
                    ),
                ],
                    alignment=ft.MainAxisAlignment.SPACE_EVENLY,
                ),
                gradient=ft.LinearGradient(['black', 'blue']),
                width=380,
                height=760,
                border_radius=20
            ),
        ],
            alignment=ft.MainAxisAlignment.SPACE_EVENLY,
        ),
        padding=10,
    )

    c = ft.AnimatedSwitcher(
        c1,
        transition=ft.AnimatedSwitcher.scale,
        duration=500,
        reverse_duration=100,
        switch_in_curve=ft.AnimationCurve.DECELERATE,
        switch_out_curve=ft.AnimationCurve.EASE,
    )
    page.add(c)

ft.app(target=main)
