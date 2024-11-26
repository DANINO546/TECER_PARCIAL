import flet as ft
from flet import AppBar, ElevatedButton, View

def main(page: ft.Page):
    page.title = "La historia de la Informática"
    page.bgcolor = "Black"
    page.window_width = 650
    page.window_height = 800
    
    image_width_Portada = 800
    image_height_Portada = 400
    
    img_height = 100
    img_width = 100
    border_radius = 25  # Ajusta el valor para el radio del borde

    # Audios Padres de la informática
    intro = ft.Audio(src="Intro.mp3", volume=1, balance=0)
    page.overlay.append(intro)
    
    Pascal = ft.Audio(src="Pascal.mp3", volume=1, balance=0)
    page.overlay.append(Pascal)
    
    Leibniz = ft.Audio(src="Leibniz.mp3", volume=1, balance=0)
    page.overlay.append(Leibniz)
    
    Babbage = ft.Audio(src="Babbage.mp3", volume=1, balance=0)
    page.overlay.append(Babbage)
    
    Lovelace = ft.Audio(src="Lovelace.mp3", volume=1, balance=0) 
    page.overlay.append(Lovelace)
    
    Hollerith = ft.Audio(src="Hollerith.mp3", volume=1, balance=0)
    page.overlay.append(Hollerith)
    
    Turing = ft.Audio(src="Turing.mp3", volume=1, balance=0)
    page.overlay.append(Turing)
    
    Neumann = ft.Audio(src="Neumann.mp3", volume=1, balance=0)
    page.overlay.append(Neumann)
    
    Shannon = ft.Audio(src="shannon.mp3", volume=1, balance=0)
    page.overlay.append(Shannon)
    
    Hopper = ft.Audio(src="Hopper.mp3", volume=1, balance=0)
    page.overlay.append(Hopper)
    
    McCarthy = ft.Audio(src="McCarthy.mp3", volume=1, balance=0)
    page.overlay.append(McCarthy)
    
    Berners = ft.Audio(src="Berners.mp3", volume=1, balance=0)
    page.overlay.append(Berners)
    
    Ritchie = ft.Audio(src="Ritchie.mp3", volume=1, balance=0)
    page.overlay.append(Ritchie)
    
    Thompson = ft.Audio(src="Thompson.mp3", volume=1, balance=0)
    page.overlay.append(Thompson)
    
    Gosling = ft.Audio(src="Gosling.mp3", volume=1, balance=0)
    page.overlay.append(Gosling)
    
    Jobs = ft.Audio(src="Jobs.mp3", volume=1, balance=0)
    page.overlay.append(Jobs)
    
    Wozniak= ft.Audio(src="Wozniak.mp3", volume=1, balance=0)
    page.overlay.append(Wozniak)
    
    Gates = ft.Audio(src="Gates.mp3", volume=1, balance=0)
    page.overlay.append(Gates)
    
    Zuckerberg = ft.Audio(src="Zuckerberg.mp3", volume=1, balance=0)
    page.overlay.append(Zuckerberg)
    
    Pages = ft.Audio(src="Pages.mp3", volume=1, balance=0)
    page.overlay.append(Pages)
    
    Brin = ft.Audio(src="Brin.mp3", volume=1, balance=0)
    page.overlay.append(Brin)
    
    def StopAll():
        intro.pause()
        Pascal.pause()
        Leibniz.pause()
        Babbage.pause()
        Lovelace.pause()
        Hollerith.pause()
        Turing.pause()
        Neumann.pause()
        Shannon.pause()
        Hopper.pause()
        McCarthy.pause()
        Berners.pause()
        Ritchie.pause()
        Thompson.pause()
        Gosling.pause()
        Jobs.pause()
        Wozniak.pause()
        Gates.pause()
        Zuckerberg.pause()
        Pages.pause()
        Brin.pause()
    
    def play_intro(e):
        StopAll()
        intro.play()
        
    def play_pascal(e):
        StopAll()
        Pascal.play()
        
    def play_leibniz(e):
        StopAll()
        Leibniz.play()
        
    def play_babbage(e):
        StopAll()
        Babbage.play()
        
    def play_lovelace(e):    
        StopAll()
        Lovelace.play()
        
    def play_hollerith(e):
        StopAll()
        Hollerith.play()
        
    def play_turing(e):
        StopAll()
        Turing.play()
    
    def play_neumann(e):
        StopAll()
        Neumann.play()
        
    def play_shannon(e):
        StopAll()
        Shannon.play()
    
    def play_hopper(e):
        StopAll()
        Hopper.play()
    
    def play_mccarthy(e):
        StopAll()
        McCarthy.play()
    
    def play_berners(e):
        StopAll()
        Berners.play()
    
    def play_ritchie(e):
        StopAll()
        Ritchie.play()
        
    def play_thompson(e):
        StopAll()
        Thompson.play()
        
    def play_gosling(e):
        StopAll()
        Gosling.play()
        
    def play_jobs(e):
        StopAll()
        Jobs.play()
        
    def play_wozniak(e):
        StopAll()
        Wozniak.play()
        
    def play_gates(e):
        StopAll()
        Gates.play()
    
    def play_zuckerberg(e):
        StopAll()
        Zuckerberg.play()
    
    def play_pages(e):
        StopAll()
        Pages.play()
    
    def play_brin(e):
        StopAll()
        Brin.play()
        
    
    # Botones Padres de la informática con imágenes y etiquetas semánticas
    btn1 = ElevatedButton(content=ft.Image(src="Pascal.jpeg", width=img_width, height=img_height, border_radius=border_radius, semantics_label="Blaise Pascal"), on_click=play_pascal)
    btn2 = ElevatedButton(content=ft.Image(src="Leibniz.png", width=img_width, height=img_height, border_radius=border_radius, semantics_label="Gottfried Wilhelm Leibniz"), on_click=play_leibniz)
    btn3 = ElevatedButton(content=ft.Image(src="babbage.png", width=img_width, height=img_height, border_radius=border_radius, semantics_label="Charles Babbage"), on_click=play_babbage)
    btn4 = ElevatedButton(content=ft.Image(src="Lovelace.png", width=img_width, height=img_height, border_radius=border_radius, semantics_label="Ada Lovelace"), on_click=play_lovelace)
    btn5 = ElevatedButton(content=ft.Image(src="Hollerith.png", width=img_width, height=img_height, border_radius=border_radius, semantics_label="Herman Hollerith"), on_click=play_hollerith)
    btn6 = ElevatedButton(content=ft.Image(src="Turing.jpeg", width=img_width, height=img_height, border_radius=border_radius, semantics_label="Alan Turing"), on_click=play_turing)
    btn7 = ElevatedButton(content=ft.Image(src="Neumann.jpeg", width=img_width, height=img_height, border_radius=border_radius, semantics_label="John von Neumann"), on_click=play_neumann)
    btn8 = ElevatedButton(content=ft.Image(src="shannon.png", width=img_width, height=img_height, border_radius=border_radius, semantics_label="Claude Shannon"), on_click=play_shannon)
    btn9 = ElevatedButton(content=ft.Image(src="Hopper.png", width=img_width, height=img_height, border_radius=border_radius, semantics_label="Grace Hopper"), on_click=play_hopper)
    btn10 = ElevatedButton(content=ft.Image(src="McCarthy.jpeg", width=img_width, height=img_height, border_radius=border_radius, semantics_label="John McCarthy"), on_click=play_mccarthy)
    btn11 = ElevatedButton(content=ft.Image(src="Berners.jpeg", width=img_width, height=img_height, border_radius=border_radius, semantics_label="Tim Berners-Lee"), on_click=play_berners)
    btn12 = ElevatedButton(content=ft.Image(src="Ritchie.png", width=img_width, height=img_height, border_radius=border_radius, semantics_label="Dennis Ritchie"), on_click=play_ritchie)
    btn13 = ElevatedButton(content=ft.Image(src="Thompson.jpeg", width=img_width, height=img_height, border_radius=border_radius, semantics_label="Ken Thompson"), on_click=play_thompson)
    btn14= ElevatedButton(content=ft.Image(src="Gosling.jpeg", width=img_width, height=img_height, border_radius=border_radius, semantics_label="James Gosling"), on_click=play_gosling)
    btn15 = ElevatedButton(content=ft.Image(src="Jobs.jpg", width=img_width, height=img_height, border_radius=border_radius, semantics_label="Steve Jobs"), on_click=play_jobs)
    btn16 = ElevatedButton(content=ft.Image(src="Wozniak.jpg", width=img_width, height=img_height, border_radius=border_radius, semantics_label="Steve Wozniak"), on_click=play_wozniak)
    btn17 = ElevatedButton(content=ft.Image(src="Gates.jpeg", width=img_width, height=img_height, border_radius=border_radius, semantics_label="Bill Gates"), on_click=play_gates)
    btn18 = ElevatedButton(content=ft.Image(src="Zuckerberg.webp", width=img_width, height=img_height, border_radius=border_radius, semantics_label="Mark Zuckerberg"), on_click=play_zuckerberg)
    btn19 = ElevatedButton(content=ft.Image(src="Pages.jpg", width=img_width, height=img_height, border_radius=border_radius, semantics_label="Larry Page"), on_click=play_pages)
    btn20 = ElevatedButton(content=ft.Image(src="Brin.webp", width=img_width, height=img_height, border_radius=border_radius, semantics_label="Sergey Brin"), on_click=play_brin)
    # Manejo del cambio de ruta
    def route_change(route):
        # Limpia las vistas anteriores
        page.views.clear()
        
        # Vista de portada
        if page.route == '/':
            page.views.append(
                View(
                    "/",
                    controls=[
                        AppBar(
                            title=ft.Text("La historia de la Informática"),
                            bgcolor="gray"
                        ),
                        ft.Container(
                            ft.Column(
                                controls=[
                                    ElevatedButton(
                                        'Los padres de la informática',
                                        on_click=lambda _: [StopAll(), page.go('/padres')]
                                    ),
                                    ft.Image(
                                        src="Portada.png",
                                        width=image_width_Portada,
                                        height=image_height_Portada,
                                        fit="cover"
                                    ),
                                    ElevatedButton(
                                        "Escucha el intro",
                                        on_click=play_intro
                                    ),
                                    
                                ],
                                alignment=ft.MainAxisAlignment.START
                            ),
                            bgcolor=page.bgcolor,
                            expand=True
                        )
                    ],
                    bgcolor=page.bgcolor
                )
            )
        # Vista de los padres de la informática
        elif page.route == '/padres':
            page.views.append(
                View(
                    "/padres",
                    controls=[
                        AppBar(
                            title=ft.Text("Los padres de la informática"),
                            bgcolor="gray"
                        ),
                        ft.Container(
                            ft.Column(
                                controls=[
                                    ElevatedButton(
                                        'Volver al inicio',
                                        on_click=lambda _: page.go('/')
                                    ),
                                    ft.Row(
                                        alignment="center",
                                        controls=[
                                            btn1, btn2, btn3,btn4
                                        ]
                                    ),
                                    ft.Row(
                                      alignment="center",
                                      controls=[
                                        btn5, btn6, btn7,btn8
                                      ]  
                                    ),
                                    ft.Row(
                                       alignment="center",
                                        controls=[
                                          btn9, btn10, btn11,btn12
                                        ] 
                                    ),
                                    ft.Row(
                                        alignment="center",
                                        controls=[
                                          btn13,btn14,btn15,btn16
                                        ] 
                                    ),
                                    ft.Row(
                                        alignment="center",
                                        controls=[
                                          btn17,btn18,btn19,btn20
                                        ] 
                                    ),
                                     ElevatedButton(
                                        'La evolución de los lenguajes de programación',
                                        on_click=lambda _: page.go('/lenguajes')
                                    ),
                                ],
                                alignment=ft.MainAxisAlignment.CENTER
                            ),
                            bgcolor=page.bgcolor,
                            expand=True
                        )
                    ]
                )
            )
        # Vista de la evolución de los lenguajes de programación
        elif page.route == '/lenguajes':
            page.views.append(
                View(
                    "/lenguajes",
                    controls=[
                        AppBar(
                            title=ft.Text("La evolución de los lenguajes de programación"),
                            bgcolor="gray"
                        ),
                        ft.Container(
                            ft.Column(
                                controls=[
                                    ElevatedButton(
                                        'Volver al inicio',
                                        on_click=lambda _: page.go('/')
                                    ),
                                    ElevatedButton(
                                        'Los padres de la informática',
                                        on_click=lambda _: page.go('/padres')
                                    ),
                                    ft.Text("Los lenguajes de programación han evolucionado a lo largo de la historia, aquí te presentamos algunos de los más importantes:"),
                                    # Aquí puedes agregar el contenido específico para la sección de lenguajes de programación
                                ],
                                alignment=ft.MainAxisAlignment.START
                            ),
                            bgcolor=page.bgcolor,
                            expand=True
                        )
                    ]
                )
            )
            
        page.update()
    
    page.on_route_change = route_change
    page.go(page.route)

ft.app(target=main, assets_dir="assets")
#ft.app(target=main,view=ft.WEB_BROWSER, assets_dir="assets")

def main (page: ft.Page):
    page.title ="Aplicaciones"
    page.bgcolor ="Black"
    page.window_width =650
    page.window_height =800

    image_width_Portada =800
    image_height_Portada =400

    img_height =100
    img_width =100
    border_radius =25

    #Audios de las redes sociales 

    Introducción= ft.Audio(src="Introducción.mp3", volume=1, balance=0)
    page.overlay.append(Introducción)

    Calculadora= ft.Audio(src="Calculadora.mp3", volume=1, balance=0)
    page.overlay.append(Calculadora)

    Canva= ft.Audio(src="Canva.mp3", volume=1, balance=0)
    page.overlay.append(Canva)    

    Configuración = ft.Audio(src="Configuración.mp3", volume=1, balance=0)
    page.overlay.append(Configuración)

    Facebook = ft.Audio(src="Facebook.mp3", volume=1, balance=0)
    page.overlay.append(Facebook)

    Gmail = ft.Audio(src="Gmail.mp3", volume=1, balance=0)
    page.overlay.append(Gmail)

    GooglePlay = ft.Audio(src="GooglePlay.mp3", volume=1, balance=0)
    page.overlay.append(GooglePlay)

    Google = ft.Audio(src="Google.mp3", volume=1, balance=0)
    page.overlay.append(Google)

    Instagram = ft.Audio(src="Instagram.mp3", volume=1, balance=0)
    page.overlay.append(Instagram)

    Netflix = ft.Audio(src="Netflix.mp3", volume=1, balance=0)
    page.overlay.append(Netflix)

    Notas = ft.Audio(src="Notas.mp3", volume=1, balance=0)
    page.overlay.append(Notas)

    Visual = ft.Audio(src="Visual.mp3", volume=1, balance=0)
    page.overlay.append(Visual)

    Whatsapp = ft.Audio(src="Whatsapp.mp3", volume=1, balance=0)
    page.overlay.append(Whatsapp)

    Pinterest = ft.Audio(src="Pinterest.mp3", volume=1, balance=0)
    page.overlay.append(Pinterest)

    Tiktok = ft.Audio(src="Tiktok.mp3", volume=1, balance=0)
    page.overlay.append(Tiktok)

    Twitter = ft.Audio(src="Twitter.mp3", volume=1, balance=0)
    page.overlay.append(Twitter)

    Uber = ft.Audio(src="Uber.mp3", volume=1, balance=0)
    page.overlay.append(Uber)

    def StopAll():
        Introducción.pause()
        Calculadora.pause()
        Canva.pause()
        Configuración.pause()
        Facebook.pause()
        Gmail.pause()
        GooglePlay.pause()
        Google.pause()
        Instagram.pause()
        Netflix.pause()
        Notas.pause()
        Pinterest.pause()
        Tiktok.pause()
        Twitter.pause()
        Uber.pause()
        Visual.pause()
        Whatsapp.pause()

    def play_Introducción(e):
        StopAll()
        Introducción.play()
    
        
    def play_Calculadora(e):
        StopAll()
        Calculadora.play()

    def play_Canva(e):
        StopAll()
        Canva.play()

    def play_Configuración(e):
        StopAll()
        Configuración.play()

    def play_Facebook(e):
        StopAll()
        Facebook.play()

    def play_Gmail(e):
        StopAll()
        Gmail.play()

    def play_GooglePlay(e):
        StopAll()
        GooglePlay.play()

    def play_Google(e):
        StopAll()
        Google.play()

    def play_Instagram(e):
        StopAll()
        Instagram.play()

    def play_Netflix(e):
        StopAll()
        Netflix.play()

    def play_Notas(e):
        StopAll()
        Notas.play()

    def play_Pinterest(e):
        StopAll()
        Pinterest.play()

    def play_Tiktok(e):
        StopAll()
        Tiktok.play()

    def play_Twitter(e):
        StopAll()
        Twitter.play()

    def play_Uber(e):
        StopAll()
        Uber.play()

    def play_Visual(e):
        StopAll()
        Visual.play()

    def play_Whatsapp(e):
        StopAll()
        Whatsapp.play()



        # Botones Aplicaciones 
    btn1 = ElevatedButton(content=ft.Image(src="Calculadora.png", width=img_width, height=img_height, border_radius=border_radius, semantics_label="Calculadora"), on_click=play_Calculadora)
    btn2 = ElevatedButton(content=ft.Image(src="Canva.png", width=img_width, height=img_height, border_radius=border_radius, semantics_label="Canva"), on_click=play_Canva)
    btn3 = ElevatedButton(content=ft.Image(src="Configuración.png", width=img_width, height=img_height, border_radius=border_radius, semantics_label="Configuración"), on_click=play_Configuración)
    btn4 = ElevatedButton(content=ft.Image(src="Facebook.png", width=img_width, height=img_height, border_radius=border_radius, semantics_label="Facebook"), on_click=play_Facebook)
    btn5 = ElevatedButton(content=ft.Image(src="Gmail.png", width=img_width, height=img_height, border_radius=border_radius, semantics_label="Gmail"), on_click=play_Gmail)
    btn6= ElevatedButton(content=ft.Image(src="GooglePlay.png", width=img_width, height=img_height, border_radius=border_radius, semantics_label="GooglePlay"), on_click=play_GooglePlay)
    btn7 = ElevatedButton(content=ft.Image(src="Google.png", width=img_width, height=img_height, border_radius=border_radius, semantics_label="Google"), on_click=play_Google)
    btn8 = ElevatedButton(content=ft.Image(src="Instagram.jpeg", width=img_width, height=img_height, border_radius=border_radius, semantics_label="Instagram"), on_click=play_Instagram)
    btn9 = ElevatedButton(content=ft.Image(src="Netflix.png", width=img_width, height=img_height, border_radius=border_radius, semantics_label="Netflix"), on_click=play_Netflix)
    btn10 = ElevatedButton(content=ft.Image(src="Notas.png", width=img_width, height=img_height, border_radius=border_radius, semantics_label="Notas"), on_click=play_Notas)
    btn11 = ElevatedButton(content=ft.Image(src="Pinterest.png", width=img_width, height=img_height, border_radius=border_radius, semantics_label="Pinterest"), on_click=play_Pinterest)
    btn12 = ElevatedButton(content=ft.Image(src="Tiktok.png", width=img_width, height=img_height, border_radius=border_radius, semantics_label="Tiktok"), on_click=play_Tiktok)
    btn13 = ElevatedButton(content=ft.Image(src="Twitter.jpeg", width=img_width, height=img_height, border_radius=border_radius, semantics_label="Twitter"), on_click=play_Twitter)
    btn14 = ElevatedButton(content=ft.Image(src="Uber.jpeg", width=img_width, height=img_height, border_radius=border_radius, semantics_label="Uber"), on_click=play_Uber)
    btn15 = ElevatedButton(content=ft.Image(src="Visual.png", width=img_width, height=img_height, border_radius=border_radius, semantics_label="Visual"), on_click=play_Visual)
    btn16 = ElevatedButton(content=ft.Image(src="Whatsapp.jpeg", width=img_width, height=img_height, border_radius=border_radius, semantics_label="Whatsapp"), on_click=play_Whatsapp)
    




  # Manejo del cambio de ruta
    def route_change(route):
        # Limpia las vistas anteriores
        page.views.clear()
        
        # Vista de portada
        if page.route == '/':
            page.views.append(
                View(
                    "/",
                    controls=[
                        AppBar(
                            title=ft.Text("Las aplicaciones"),
                            bgcolor="gray"
                        ),
                        ft.Container(
                            ft.Column(
                                controls=[
                                    ElevatedButton(
                                        'Las aplicaciones',
                                        on_click=lambda _: [StopAll(), page.go('/aplicaciones')]
                                    ),
                                    ft.Image(
                                        src="Portada.png",
                                        width=image_width_Portada,
                                        height=image_height_Portada,
                                        fit="cover"
                                    ),
                                    ElevatedButton(
                                        "Escucha el intro",
                                        on_click=play_Introducción
                                    ),
                                    
                                ],
                                alignment=ft.MainAxisAlignment.START
                            ),
                            bgcolor=page.bgcolor,
                            expand=True
                        )
                    ],
                    bgcolor=page.bgcolor
                )
            )
        # Vista de las aplicaciones
        elif page.route == '/aplicaciones':
            page.views.append(
                View(
                    "/aplicaciones",
                    controls=[
                        AppBar(
                            title=ft.Text("Las aplicaciones"),
                            bgcolor="gray"
                        ),
                        ft.Container(
                            ft.Column(
                                controls=[
                                    ElevatedButton(
                                        'Volver al inicio',
                                        on_click=lambda _: page.go('/')
                                    ),
                                    ft.Row(
                                        alignment="center",
                                        controls=[
                                            btn1, btn2, btn3,btn4
                                        ]
                                    ),
                                    ft.Row(
                                      alignment="center",
                                      controls=[
                                        btn5, btn6, btn7,btn8
                                      ]  
                                    ),
                                    ft.Row(
                                       alignment="center",
                                        controls=[
                                          btn9, btn10, btn11,btn12
                                        ]
                                    ),
                                    ft.Row(
                                        alignment="center",
                                        controls=[
                                          btn13,btn14,btn15,btn16
                                        ] 
                                    ),
                                     ElevatedButton(
                                        'La evolución de los lenguajes de programación',
                                        on_click=lambda _: page.go('/lenguajes')
                                    ),
                                ],
                                alignment=ft.MainAxisAlignment.CENTER
                            ),
                            bgcolor=page.bgcolor,
                            expand=True
                        )
                    ]
                )
            )
        # Vista de la evolución de los lenguajes de programación
        elif page.route == '/lenguajes':
            page.views.append(
                View(
                    "/lenguajes",
                    controls=[
                        AppBar(
                            title=ft.Text("Las aplicaiones"),
                            bgcolor="gray"
                        ),
                        ft.Container(
                            ft.Column(
                                controls=[
                                    ElevatedButton(
                                        'Volver al inicio',
                                        on_click=lambda _: page.go('/')
                                    ),
                                    ElevatedButton(
                                        'Las aplicaciones',
                                        on_click=lambda _: page.go('/aplicaciones')
                                    ),
                                    ft.Text("Los lenguajes de programación han evolucionado a lo largo de la historia, aquí te presentamos algunos de los más importantes:"),
                                    # Aquí puedes agregar el contenido específico para la sección de lenguajes de programación
                                ],
                                alignment=ft.MainAxisAlignment.START
                            ),
                            bgcolor=page.bgcolor,
                            expand=True
                        )
                    ]
                )
            )
            
        page.update()
    
    page.on_route_change = route_change
    page.go(page.route)

ft.app(target=main, assets_dir="assets")
#ft.app(target=main,view=ft.WEB_BROWSER, assets_dir="assets")


def main (page: ft.Page):
    page.title ="Las nuevas tecnologías"
    page.bgcolor ="Black"
    page.window_width =650
    page.window_height =800

    image_width_Portada =800
    image_height_Portada =400

    img_height =100
    img_width =100
    border_radius =25

    #Audios de las nuevas tecnololgías
    Intro2= ft.Audio(src="Intro2.mp3", volume=1, balance=0)
    page.overlay.append(Intro2)

    Artificial= ft.Audio(src="Artificial.mp3", volume=1, balance=0)
    page.overlay.append(Artificial)

    Autos= ft.Audio(src="Autos.mp3", volume=1, balance=0)
    page.overlay.append(Autos)

    Blockchain= ft.Audio(src="Blockchain.mp3", volume=1, balance=0)
    page.overlay.append(Blockchain)

    Cadena= ft.Audio(src="Cadena.mp3", volume=1, balance=0)
    page.overlay.append(Cadena)

    Ciberseguridad= ft.Audio(src="Ciberseguridad.mp3", volume=1, balance=0)
    page.overlay.append(Ciberseguridad)

    Cibertecnología= ft.Audio(src="Cibertecnología.mp3", volume=1, balance=0)
    page.overlay.append(Cibertecnología)

    Cookie= ft.Audio(src="Cookie.mp3", volume=1, balance=0)
    page.overlay.append(Cookie)

    Criptomonedas= ft.Audio(src="Criptomonedas.mp3", volume=1, balance=0)
    page.overlay.append(Criptomonedas)

    Cuántica= ft.Audio(src="Cuántica.mp3", volume=1, balance=0)
    page.overlay.append(Cuántica)

    Economía= ft.Audio(src="Economía.mp3", volume=1, balance=0)
    page.overlay.append(Economía)

    Internet= ft.Audio(src="Internet.mp3", volume=1, balance=0)
    page.overlay.append(Internet)

    Metaverso= ft.Audio(src="Metaverso.mp3", volume=1, balance=0)
    page.overlay.append(Metaverso)

    Nube= ft.Audio(src="Nube.mp3", volume=1, balance=0)
    page.overlay.append(Nube)

    Realidad= ft.Audio(src="Realidad.mp3", volume=1, balance=0)
    page.overlay.append(Realidad)

    Redes= ft.Audio(src="Redes.mp3", volume=1, balance=0)
    page.overlay.append(Redes)

    Robótica= ft.Audio(src="Robótica.mp3", volume=1, balance=0)
    page.overlay.append(Robótica)

    def StopAll():
        Intro2.pause()
        Artificial.pause()
        Autos.pause()
        Blockchain.pause()
        Cadena.pause()
        Ciberseguridad.pause()
        Cibertecnología.pause()
        Cookie.pause()
        Criptomonedas.pause()
        Cuántica.pause()
        Economía.pause()
        Internet.pause()
        Metaverso.pause()
        Nube.pause()
        Realidad.pause()
        Redes.pause()
        Robótica.pause()
    

    def play_Intro2(e):
        StopAll()
        Intro2.play()

    def play_Artificial(e):
        StopAll()
        Artificial.play()

    def play_Autos(e):
        StopAll()
        Autos.play()

    def play_Blockchain(e):
        StopAll()
        Blockchain.play()

    def play_Cadena(e):
        StopAll()
        Cadena.play()

    def play_Ciberseguridad(e):
        StopAll()
        Ciberseguridad.play()

    def play_Cibertecnología(e):
        StopAll()
        Cibertecnología.play()

    def play_Cookie(e):
        StopAll()
        Cookie.play()

    def play_Criptomonedas(e):
        StopAll()
        Criptomonedas.play()

    def play_Cuántica(e):
        StopAll()
        Cuántica.play()

    def play_Economía(e):
        StopAll()
        Economía.play()

    def play_Internet(e):
        StopAll()
        Internet.play()

    def play_Metaverso(e):
        StopAll()
        Metaverso.play()

    def play_Nube(e):
        StopAll()
        Nube.play()

    def play_Realidad(e):
        StopAll()
        Realidad.play()

    def play_Redes(e):
        StopAll()
        Redes.play()

    def play_Robótica(e):
        StopAll()
        Robótica.play()

    
    #Botones de las nuevas tecnologías 
    btn1 = ElevatedButton(content=ft.Image(src="Artificial.jpeg", width=img_width, height=img_height, border_radius=border_radius, semantics_label="Artificial"), on_click=play_Artificial)
    btn2 = ElevatedButton(content=ft.Image(src="Autos.jpeg", width=img_width, height=img_height, border_radius=border_radius, semantics_label="Autos"), on_click=play_Autos)
    btn3 = ElevatedButton(content=ft.Image(src="Blockchain.jpeg", width=img_width, height=img_height, border_radius=border_radius, semantics_label="Blockchain"), on_click=play_Blockchain)
    btn4 = ElevatedButton(content=ft.Image(src="Cadena.jpeg", width=img_width, height=img_height, border_radius=border_radius, semantics_label="Cadena"), on_click=play_Cadena)
    btn5 = ElevatedButton(content=ft.Image(src="Ciberseguridad.jpeg", width=img_width, height=img_height, border_radius=border_radius, semantics_label="Ciberseguridad"), on_click=play_Ciberseguridad)
    btn6 = ElevatedButton(content=ft.Image(src="Cibertecnología.jpeg", width=img_width, height=img_height, border_radius=border_radius, semantics_label="Cibertecnología"), on_click=play_Cibertecnología)
    btn7 = ElevatedButton(content=ft.Image(src="Cookie.jpeg", width=img_width, height=img_height, border_radius=border_radius, semantics_label="Cookie"), on_click=play_Cookie)
    btn8 = ElevatedButton(content=ft.Image(src="Criptomonedas.jpeg", width=img_width, height=img_height, border_radius=border_radius, semantics_label="Criptomonedas"), on_click=play_Criptomonedas)
    btn9 = ElevatedButton(content=ft.Image(src="Cuántica.jpeg", width=img_width, height=img_height, border_radius=border_radius, semantics_label="Cuántica"), on_click=play_Cuántica)
    btn10 = ElevatedButton(content=ft.Image(src="Economía.jpeg", width=img_width, height=img_height, border_radius=border_radius, semantics_label="Economía"), on_click=play_Economía)
    btn11 = ElevatedButton(content=ft.Image(src="Internet.jpeg", width=img_width, height=img_height, border_radius=border_radius, semantics_label="Internet"), on_click=play_Internet)
    btn12 = ElevatedButton(content=ft.Image(src="Metaverso.jpeg", width=img_width, height=img_height, border_radius=border_radius, semantics_label="Metaverso"), on_click=play_Metaverso)
    btn13 = ElevatedButton(content=ft.Image(src="Nube.jpeg", width=img_width, height=img_height, border_radius=border_radius, semantics_label="Nube"), on_click=play_Nube)
    btn14 = ElevatedButton(content=ft.Image(src="Realidad.jpeg", width=img_width, height=img_height, border_radius=border_radius, semantics_label="Realidad"), on_click=play_Realidad)
    btn15 = ElevatedButton(content=ft.Image(src="Redes.jpeg", width=img_width, height=img_height, border_radius=border_radius, semantics_label="Redes"), on_click=play_Redes)
    btn16 = ElevatedButton(content=ft.Image(src="Robótica.jpeg", width=img_width, height=img_height, border_radius=border_radius, semantics_label="Robótica"), on_click=play_Robótica)
  

# Manejo del cambio de ruta
    def route_change(route):
        # Limpia las vistas anteriores
        page.views.clear()
        
        # Vista de portada
        if page.route == '/':
            page.views.append(
                View(
                    "/",
                    controls=[
                        AppBar(
                            title=ft.Text("Las nuevas tecnologías"),
                            bgcolor="gray"
                        ),
                        ft.Container(
                            ft.Column(
                                controls=[
                                    ElevatedButton(
                                        'Las nuevas tecnologías',
                                        on_click=lambda _: [StopAll(), page.go('/tecnologías')]
                                    ),
                                    ft.Image(
                                        src="Portada.png",
                                        width=image_width_Portada,
                                        height=image_height_Portada,
                                        fit="cover"
                                    ),
                                    ElevatedButton(
                                        "Escucha el intro2",
                                        on_click=play_Intro2
                                    ),
                                    
                                ],
                                alignment=ft.MainAxisAlignment.START
                            ),
                            bgcolor=page.bgcolor,
                            expand=True
                        )
                    ],
                    bgcolor=page.bgcolor
                )
            )
        # Vista de las nuevas tecnologías
        elif page.route == '/tecnologías':
            page.views.append(
                View(
                    "/tecnologías",
                    controls=[
                        AppBar(
                            title=ft.Text("Las nuevas tecnologías"),
                            bgcolor="gray"
                        ),
                        ft.Container(
                            ft.Column(
                                controls=[
                                    ElevatedButton(
                                        'Volver al inicio',
                                        on_click=lambda _: page.go('/')
                                    ),
                                    ft.Row(
                                        alignment="center",
                                        controls=[
                                            btn1, btn2, btn3,btn4
                                        ]
                                    ),
                                    ft.Row(
                                      alignment="center",
                                      controls=[
                                        btn5, btn6, btn7,btn8
                                      ]  
                                    ),
                                    ft.Row(
                                       alignment="center",
                                        controls=[
                                          btn9, btn10, btn11,btn12
                                        ] 
                                    ),
                                    ft.Row(
                                        alignment="center",
                                        controls=[
                                          btn13,btn14,btn15,btn16
                                        ] 
                                    ),
                                     ElevatedButton(
                                        'La evolución de los lenguajes de programación',
                                        on_click=lambda _: page.go('/lenguajes')
                                    ),
                                ],
                                alignment=ft.MainAxisAlignment.CENTER
                            ),
                            bgcolor=page.bgcolor,
                            expand=True
                        )
                    ]
                )
            )
        # Vista de la evolución de los lenguajes de programación
        elif page.route == '/lenguajes':
            page.views.append(
                View(
                    "/lenguajes",
                    controls=[
                        AppBar(
                            title=ft.Text("La evolución de los lenguajes de programación"),
                            bgcolor="gray"
                        ),
                        ft.Container(
                            ft.Column(
                                controls=[
                                    ElevatedButton(
                                        'Volver al inicio',
                                        on_click=lambda _: page.go('/')
                                    ),
                                    ElevatedButton(
                                        'Los padres de la informática',
                                        on_click=lambda _: page.go('/padres')
                                    ),
                                    ft.Text("Los lenguajes de programación han evolucionado a lo largo de la historia, aquí te presentamos algunos de los más importantes:"),
                                    # Aquí puedes agregar el contenido específico para la sección de lenguajes de programación
                                ],
                                alignment=ft.MainAxisAlignment.START
                            ),
                            bgcolor=page.bgcolor,
                            expand=True
                        )
                    ]
                )
            )
            
        page.update()
    
    page.on_route_change = route_change
    page.go(page.route)

ft.app(target=main, assets_dir="assets")
#ft.app(target=main,view=ft.WEB_BROWSER, assets_dir="assets")



    









