import flet as ft

def main(page: ft.page):
    page.padding = 0
    page.bgcolor = ft.colors.BLACK
    page.vertical_alignment = "center"
    page.horizontal_alignment = "center"
    
    def animate(e):
        c.content = c2 if c.content == c1 else c1
        c.update()
       
    c1= ft.Container(
        ft.Row([
            ft.Container(
                ft.Column([
                    ft.Text(
                        "Iniciar Sesion",
                        width=360,
                        size=30,
                        weight="W900",
                        color='BLACK',
                        text_align="center",
                        font_family='Times New Roman'
                        
                    ),
                    ft.Container(
                        ft.TextField(
                            width=280,
                            height=40,
                            hint_text="Correo electronico",
                            border="underline",
                            color="white",
                            prefix_icon=ft.icons.EMAIL
                        ),
                        padding=ft.padding.only(20,10)
                    ),
                    ft.Container(
                        ft.TextField(
                            width=280,
                            height=40,
                            hint_text="Contraseña",
                            border="underline",
                            color="white",
                            prefix_icon=ft.icons.LOCK,
                            password=True,
                        ),
                        padding=ft.padding.only(20,10)
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
                              color = "white",
                              weight="w500",                
                            ),
                           width=280,
                           bgcolor="black",
                        ),
                        padding=ft.padding.only(25,10)
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
                bgcolor=ft.colors.GREEN_400,
                expand=True,
            ),
            ft.Container(
                ft.Column([
                    ft.Text(
                        "COMPANY",
                        size=40,
                        color='BLACK',
                        font_family="Times new Roman"
                    ),
                    ft.Container(
                        ft.Image(
                            src="190914.png",
                            width=340,
                        ),
                        padding=ft.padding.only(20,20)
                    ),
                ],
                alignment=ft.MainAxisAlignment.SPACE_EVENLY,
                horizontal_alignment=ft.CrossAxisAlignment.CENTER
                ),
                bgcolor=ft.colors.WHITE70,
                expand=True,
                border_radius=ft.BorderRadius(
                    topLeft=15,
                    topRight=0,
                    bottomLeft=15,
                    bottomRight=0,
                )
            ),   
        ],
        alignment=ft.MainAxisAlignment.SPACE_EVENLY,
        ),
        
        alignment=ft.alignment.center,
        width=900,
        height=600,
        bgcolor=ft.colors.GREEN_400,
        border_radius=40
    )

    
    c2 = ft.Container(
        ft.Row([
            ft.Container(
                ft.Column([
                    ft.Text(
                        "Bienvenido",
                        size=40,
                        font_family="Times new Roman",
                        color="black"
                    ),
                    ft.Container(
                        ft.Image(
                            src='3200751.png',
                            width=300
                        ),
                        padding=ft.padding.only(20,20)
                    ),
                ],
                alignment=ft.MainAxisAlignment.SPACE_EVENLY,
                horizontal_alignment=ft.CrossAxisAlignment.CENTER
                ),
                bgcolor=ft.colors.WHITE70,
                expand=True,
                border_radius=ft.BorderRadius(
                    topLeft=0,
                    topRight=15,
                    bottomLeft=0,
                    bottomRight=15,
                )
            ),
            
            ft.Container(
                ft.Column([
                    ft.Text(
                        "Crear cuenta ",
                        width=360,
                        size=30,
                        weight="w900",
                        color='BLACK',
                        text_align="center",
                        font_family='Times New Roman'
                    ),
                    ft.Container(
                        ft.TextField(
                            width=280,
                            height=40,
                            hint_text="Nombre",
                            border="underline",
                            color="black",
                            prefix_icon= ft.icons.PERM_CONTACT_CAL,
                        ),
                        padding=ft.padding.only(20,10)
                    ),
                    ft.Container(
                        ft.TextField(
                            width=280,
                            height=40,
                            hint_text="Correo elctronico",
                            border="underline",
                            color="black",
                            prefix_icon= ft.icons.EMAIL,
                        ),
                        padding=ft.padding.only(20,10)                        
                    ),
                    ft.Container(
                        ft.TextField(
                            width=280,
                            height=40,
                            hint_text="Contraseña",
                            border="underline",
                            color="black",
                            prefix_icon= ft.icons.LOCK,
                            password=True,
                        ),
                        padding=ft.padding.only(20,10)
                    ),
                    
                       ft.Container(
                        ft.TextField(
                            width=280,
                            height=40,
                            hint_text="Confirmar contraseña",
                            border="underline",
                            color="black",
                            prefix_icon= ft.icons.LOCK,
                            password=True,
                        ),
                        padding=ft.padding.only(20,10)
                    ),
                    
                    ft.Container(
                        ft.ElevatedButton(
                            content=ft.Text(
                                "REGISTRARSE",
                                color="white",
                                weight="w500",
                            ),
                            width=200,
                            bgcolor="black",
                        ),
                        padding=ft.padding.only(25,10)
                    ),
                    
                    ft.Container(
                        ft.Row([
                            ft.Text(
                                "¿Ya tienes cuenta?"
                            ),
                            ft.TextButton(
                                "Iniciar sesion",
                                on_click=animate
                            ),
                        ], spacing=8),
                        padding=ft.padding.only(40)
                    ),
                ],
                alignment=ft.MainAxisAlignment.SPACE_EVENLY,
                horizontal_alignment=ft.CrossAxisAlignment.CENTER
                ),
                bgcolor=ft.colors.GREEN_400,
                expand=True,
            ),
        ],
        alignment=ft.MainAxisAlignment.SPACE_EVENLY,
        ),
        
        alignment=ft.alignment.center,
        width=900,
        height=600,
        bgcolor=ft.colors.GREEN_400,
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