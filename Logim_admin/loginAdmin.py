import flet as ft

def main(page: ft.page):
    page.padding = 20  # Ajustar el espacio alrededor de la página
    page.bgcolor = ft.colors.BLUE_GREY_200
    page.vertical_alignment = "center"
    page.horizontal_alignment = "center"
    
    def animate(e):
        c.content = c2 if c.content == c1 else c1
        c.update()
        
    c1= ft.Container( #contenedor pagina principal Inicio de sesion
        ft.Row([
            ft.Container(
                ft.Column([
                    ft.Text(
                        "Iniciar Sesión",
                        size=50,  # Aumentar el tamaño del texto para computadora
                        weight="W900",
                        text_align="center"
                    ),
                    ft.Container(
                        ft.TextField(
                            width=400,  # Ajustar el ancho del campo de texto
                            height=60,  # Ajustar la altura del campo de texto
                            hint_text="Correo electrónico",
                            border="underline",
                            color="white",
                            prefix_icon=ft.icons.EMAIL
                        ),
                        padding=ft.padding.only(20, 10)
                    ),
                    ft.Container(
                        ft.TextField(
                            width=400,
                            height=60,
                            hint_text="Contraseña",
                            border="underline",
                            color="white",
                            prefix_icon=ft.icons.LOCK,
                            password=True,
                        ),
                        padding=ft.padding.only(20, 10)
                    ),
                    ft.Container(
                        ft.Checkbox(
                            label="Recordar contraseña",
                            check_color="black"
                        ),
                        padding=ft.padding.only(40),
                    ),
                    ft.Container(
                       ft.ElevatedButton(
                          content=ft.Text(
                              "INICIAR",
                              color="white",
                              weight="w500",                
                            ),
                           width=400,
                           height=60,
                           bgcolor="black",
                        ),
                        padding=ft.padding.only(25, 10)
                    ),
                    ft.Container(
                        ft.Row([
                            ft.Text(
                                "¿No tienes una cuenta?"
                            ),
                            ft.TextButton(
                                "Crear una cuenta",
                                on_click=animate
                            ),
                        ], spacing=8),
                        padding=ft.padding.only(40)
                    ),
                    
                ],
                alignment=ft.MainAxisAlignment.SPACE_EVENLY,
                horizontal_alignment=ft.CrossAxisAlignment.CENTER
                ),
                bgcolor=ft.colors.PURPLE,
                expand=True,
            ),
            ft.Container(
                ft.Column([
                    ft.Text(
                        "Administrador",
                        size=50,
                        font_family="Georgia"
                    ),
                    ft.Container(
                        ft.Image(
                            src="logo3.png",
                            width=300,  # Ajustar el ancho de la imagen
                        ),
                        padding=ft.padding.only(20, 20)
                    ),
                ],
                alignment=ft.MainAxisAlignment.SPACE_EVENLY,
                horizontal_alignment=ft.CrossAxisAlignment.CENTER
                ),
                bgcolor=ft.colors.CYAN,
                expand=True,
                border_radius=ft.BorderRadius(
                    top_left=100,
                    top_right=0,
                    bottom_left=100,
                    bottom_right=0,
                )
            ),   
        ],
        alignment=ft.MainAxisAlignment.SPACE_EVENLY,
        ),
        
        alignment=ft.alignment.center,
        width=1000,  # Ajustar el ancho del contenedor principal
        height=600,  # Ajustar la altura del contenedor principal
        bgcolor=ft.colors.PURPLE,
        border_radius=40
    )

    c2 = ft.Container( #contenedor pagina para crear cuenta
        ft.Row([
            ft.Container(
                ft.Column([
                    ft.Text(
                        "Bienvenido",
                        size=50,
                        font_family="georgia",
                    ),
                    ft.Container(
                        ft.Image(
                            src='logo4.png',
                            width=300
                        ),
                        padding=ft.padding.only(20, 20)
                    ),
                ],
                alignment=ft.MainAxisAlignment.SPACE_EVENLY,
                horizontal_alignment=ft.CrossAxisAlignment.CENTER
                ),
                bgcolor=ft.colors.PURPLE,
                expand=True,
                border_radius=ft.BorderRadius(
                    top_left=0,
                    top_right=100,
                    bottom_left=0,
                    bottom_right=100,
                )
            ),
            
            ft.Container(
                ft.Column([
                    ft.Text(
                        "Crear cuenta",
                        size=50,
                        font_family="georgia",
                    ),
                    ft.Container(
                        ft.TextField(
                            width=400,
                            height=60,
                            hint_text="Nombre",
                            border="underline",
                            color="black",
                            prefix_icon= ft.icons.PERM_CONTACT_CAL,
                        ),
                        padding=ft.padding.only(20, 10)
                    ),
                    ft.Container(
                        ft.TextField(
                            width=400,
                            height=60,
                            hint_text="Correo electrónico",
                            border="underline",
                            color="black",
                            prefix_icon= ft.icons.EMAIL,
                            password=True,
                        ),
                        padding=ft.padding.only(20, 10)                        
                    ),
                    ft.Container(
                        ft.TextField(
                            width=400,
                            height=60,
                            hint_text="Contraseña",
                            border="underline",
                            color="black",
                            prefix_icon= ft.icons.LOCK,
                            password=True,
                        ),
                        padding=ft.padding.only(20, 10)
                    ),
                    
                    ft.Container(
                        ft.TextField(
                            width=400,
                            height=60,
                            hint_text="Confirmar contraseña",
                            border="underline",
                            color="black",
                            prefix_icon= ft.icons.LOCK,
                            password=True,
                        ),
                        padding=ft.padding.only(20, 10)
                    ),
                    
                    ft.Container(
                        ft.ElevatedButton(
                            content=ft.Text(
                                "REGISTRARSE",
                                color="white",
                                weight="w500",
                            ),
                            width=300,
                            height=60,
                            bgcolor="black",
                        ),
                        padding=ft.padding.only(25, 10)
                    ),
                    
                    ft.Container(
                        ft.Row([
                            ft.Text(
                                "¿Ya tienes cuenta?"
                            ),
                            ft.TextButton(
                                "Iniciar sesión",
                                on_click=animate
                            ),
                        ], spacing=8),
                        padding=ft.padding.only(40)
                    ),
                ],
                alignment=ft.MainAxisAlignment.SPACE_EVENLY,
                horizontal_alignment=ft.CrossAxisAlignment.CENTER
                ),
                bgcolor=ft.colors.CYAN,
                expand=True,
            ),
        ],
        alignment=ft.MainAxisAlignment.SPACE_EVENLY,
        ),
        
        alignment=ft.alignment.center,
        width=1000,
        height=600,
        bgcolor=ft.colors.CYAN,
        border_radius=40   
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
