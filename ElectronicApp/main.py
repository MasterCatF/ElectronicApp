from kivy.lang import Builder
from kivymd.app import MDApp
from kivymd.uix.dialog import MDDialog
from kivymd.uix.button import MDFlatButton, MDRaisedButton
from kivy.core.window import Window
from kivy.uix.screenmanager import ScreenManager, Screen, SlideTransition
from kivy.utils import get_color_from_hex
from kivy.core.clipboard import Clipboard
from kivymd.toast import toast
import sqlite3
from hashlib import sha256
from datetime import datetime
from kivy.uix.boxlayout import BoxLayout
from kivymd.uix.label import MDLabel
import random

KV = '''
#:import SlideTransition kivy.uix.screenmanager.SlideTransition
#:import utils kivy.utils

ScreenManager:
    transition: SlideTransition()
    LoginScreen:
    RegisterScreen:
    WelcomeScreen:
    ComponentsScreen:
    ElectroWikiScreen:
    ResistanceIdealScreen:
    NotesScreen:
    MenuScreen:
    DificultadScreen:
    QuizScreen:
    ResultadoScreen:

<CyberButton@MDRaisedButton>:
    md_bg_color: utils.get_color_from_hex("#666666")
    text_color: 1, 1, 1, 1
    elevation: 5

<New@MDRaisedButton>:
    md_bg_color: utils.get_color_from_hex("#FF3333")
    text_color: 1, 1, 1, 1
    elevation: 5    

<Pantalla@Screen>:
    canvas.before:
        Color:
            rgba: utils.get_color_from_hex("#440000")
        Rectangle:
            pos: self.pos
            size: self.size
        Color:
            rgba: utils.get_color_from_hex("#DDDDDD")
        Line:
            points: [self.x, self.y, self.right, self.top]
            width: 2
        Line:
            points: [self.x, self.top, self.right, self.y]
            width: 2
        Line:
            points: [self.x, self.y, self.x, self.top]
            width: 6
        Line:
            points: [self.right, self.y, self.right, self.top]
            width: 6
        Line:
            points: [self.x, self.top, self.right, self.top]
            width: 6
        Line:
            points: [self.x, self.y, self.right, self.y]
            width: 6
        Line:
            points: [self.x + self.width / 2, self.y, self.x + self.width / 2, self.top]
            width: 2
        Line:
            points: [self.x, self.y + self.height / 2, self.right, self.y + self.height / 2]
            width: 2

<LoginScreen>:
    name: 'login'
    Pantalla:
        MDCard:
            size_hint: None, None
            size: dp(400), dp(500)
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
            elevation: 10
            padding: dp(25)
            spacing: dp(30)
            md_bg_color: utils.get_color_from_hex("#9999FF")
            orientation: 'vertical'

            Image:
                source: 'fiee.png'
                size_hint: None, None
                size: dp(160), dp(100)
                allow_stretch: True
                keep_ratio: True
                pos_hint: {'center_x': 0.5, 'center_y': 0.5}

            MDTextField:
                id: user
                icon_right: "account"
                hint_text: "Username"
                text_color: 1, 1, 1, 1
                hint_text_color: 0.8, 0.8, 0.8, 1 
                size_hint_x: None
                width: dp(220)
                font_size: dp(18)
                pos_hint: {"center_x": 0.5}

            MDTextField:
                id: password
                icon_right: "eye-off"
                hint_text: "Password"
                text_color: 1, 1, 1, 1
                hint_text_color: 0.8, 0.8, 0.8, 1 
                size_hint_x: None
                width: dp(220)
                font_size: dp(18)
                pos_hint: {"center_x": 0.5}
                password: True

            CyberButton:
                text: "ENTRAR"
                font_size: dp(15)
                pos_hint: {"center_x": 0.5}
                on_release: app.login()

            CyberButton:
                text: "REGISTRARSE"
                font_size: dp(15)
                pos_hint: {"center_x": 0.5}
                on_release: app.root.current = 'register'

<RegisterScreen>:
    name: 'register'
    Pantalla:
        MDCard:
            size_hint: None, None
            size: dp(380), dp(500)
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
            elevation: 10
            padding: dp(25)
            spacing: dp(25)
            md_bg_color: utils.get_color_from_hex("#9999FF")
            orientation: 'vertical'

            MDIcon:
                icon: 'account-plus'
                font_size: dp(80)
                halign: 'center'
                theme_text_color: "Custom"
                text_color: utils.get_color_from_hex("#000011")

            MDTextField:
                id: new_username
                icon_right: "account-plus"
                hint_text: "Usuario"
                text_color: 1, 1, 1, 1
                hint_text_color: 0.8, 0.8, 0.8, 1 
                size_hint_x: None
                width: dp(220)
                font_size: dp(18)
                pos_hint: {"center_x": 0.5}

            MDTextField:
                id: new_password
                icon_right: "key-variant"
                hint_text: "Contraseña"
                text_color: 1, 1, 1, 1
                hint_text_color: 0.8, 0.8, 0.8, 1 
                size_hint_x: None
                width: dp(220)
                font_size: dp(18)
                pos_hint: {"center_x": 0.5}
                password: True

            CyberButton:
                text: "REGISTRARSE"
                font_size: dp(15)
                pos_hint: {"center_x": 0.5}
                on_release: app.register_user()

            CyberButton:
                text: "VOLVER"
                font_size: dp(15)
                pos_hint: {"center_x": 0.5}
                on_release: app.root.current = 'login'

<WelcomeScreen>:
    name: 'welcome'
    Pantalla:
        MDCard:
            size_hint: None, None
            size: dp(330), dp(540)
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
            elevation: 10
            padding: dp(25)
            spacing: dp(20)
            md_bg_color: utils.get_color_from_hex("#1DDDDD")
            orientation: 'vertical'
            
            MDLabel:
                id: welcome_label
                text: "!Bienvenido!"
                halign: 'center'
                font_style: 'H4'
                theme_text_color: "Custom"
                text_color: utils.get_color_from_hex("#990033")
                bold: True
            
            New:
                text: "ElectroWiki"
                font_size: dp(20)
                pos_hint: {"center_x": 0.5}
                on_release: app.root.current = 'electro_wiki'
            
            New:
                text: "Calculo de Resistencia"
                font_size: dp(20)
                pos_hint: {"center_x": 0.5}
                on_release: app.root.current = 'resistance_ideal'

            New:
                text: "Guardar Apuntes"
                font_size: dp(20)
                pos_hint: {"center_x": 0.5}
                on_release: app.root.current = 'notes'
            
            New:
                text: "Prueba tus conocimientos"
                font_size: dp(20)
                pos_hint: {"center_x": 0.5}
                on_release: app.root.current = 'menu'

            New:
                text: "VOLVER"
                font_size: dp(20)
                pos_hint: {"center_x": 0.5}
                on_release: app.root.current = 'login'

<NotesScreen>:
    name: 'notes'
    Pantalla:
        MDCard:
            size_hint: None, None
            size: dp(350), dp(500)
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
            elevation: 10
            padding: dp(25)
            spacing: dp(15)
            md_bg_color: utils.get_color_from_hex("#6699FF")
            orientation: 'vertical'

            MDLabel:
                text: "Notas de Resistencias"
                halign: 'center'
                font_style: 'H5'
                theme_text_color: "Custom"
                text_color: utils.get_color_from_hex("#000000")
                bold: True

            MDTextField:
                id: note_input
                hint_text: "Escribe tu nota aquí..."
                size_hint_x: None
                width: dp(300)
                pos_hint: {"center_x": 0.5}

            CyberButton:
                text: "GUARDAR NOTA"
                font_size: dp(15)
                pos_hint: {"center_x": 0.5}
                on_release: app.save_note()

            ScrollView:
                BoxLayout:
                    id: notes_label
                    orientation: 'vertical'
                    size_hint_y: None
                    height: self.minimum_height

            CyberButton:
                text: "PEGAR"
                font_size: dp(15)
                pos_hint: {"center_x": 0.5}
                on_release: app.paste_note()

            CyberButton:
                text: "VOLVER"
                font_size: dp(15)
                pos_hint: {"center_x": 0.5}
                on_release: app.root.current = 'welcome'

<ElectroWikiScreen>:
    name: 'electro_wiki'
    canvas.before:
        Color:
            rgba: utils.get_color_from_hex("#111111")
        Rectangle:
            pos: self.pos
            size: self.size
    ScrollView:
        MDGridLayout:
            cols: 1
            padding: dp(10)
            spacing: dp(10)
            size_hint_y: None
            height: self.minimum_height

            MDCard:
                size_hint_y: None
                height: dp(150)
                orientation: 'horizontal'
                padding: dp(10)
                spacing: dp(10)
                
                Image:
                    source: 'resistor.png'
                    size_hint_x: None
                    width: dp(100)

                MDLabel:
                    text: "Resistor: Limita la corriente en un circuito."
                    halign: 'left'
                    theme_text_color: "Custom"
                    text_color: utils.get_color_from_hex("#111111")

            MDCard:
                size_hint_y: None
                height: dp(150)
                orientation: 'horizontal'
                padding: dp(10)
                spacing: dp(10)

                Image:
                    source: 'capacitor.png'
                    size_hint_x: None
                    width: dp(100)

                MDLabel:
                    text: "Capacitor: Almacena energía en un campo eléctrico."
                    halign: 'left'
                    theme_text_color: "Custom"
                    text_color: utils.get_color_from_hex("#111111")

            MDCard:
                size_hint_y: None
                height: dp(150)
                orientation: 'horizontal'
                padding: dp(10)
                spacing: dp(10)

                Image:
                    source: 'diode.jpg'
                    size_hint_x: None
                    width: dp(100)

                MDLabel:
                    text: "Diodo: Permite el flujo de corriente en una sola dirección."
                    halign: 'left'
                    theme_text_color: "Custom"
                    text_color: utils.get_color_from_hex("#111111")

            MDCard:
                size_hint_y: None
                height: dp(150)
                orientation: 'horizontal'
                padding: dp(10)
                spacing: dp(10)

                Image:
                    source: 'transistor.png'
                    size_hint_x: None
                    width: dp(100)

                MDLabel:
                    text: "Transistor: Actúa como interruptor o amplificador."
                    halign: 'left'
                    theme_text_color: "Custom"
                    text_color: utils.get_color_from_hex("#111111")

            MDCard:
                size_hint_y: None
                height: dp(150)
                orientation: 'horizontal'
                padding: dp(10)
                spacing: dp(10)

                Image:
                    source: 'led.jpg'
                    size_hint_x: None
                    width: dp(100)

                MDLabel:
                    text: "LED: Emite luz al pasar corriente."
                    halign: 'left'
                    theme_text_color: "Custom"
                    text_color: utils.get_color_from_hex("#111111")

            MDCard:
                size_hint_y: None
                height: dp(150)
                orientation: 'horizontal'
                padding: dp(10)
                spacing: dp(10)

                Image:
                    source: 'ic.png'
                    size_hint_x: None
                    width: dp(100)

                MDLabel:
                    text: "Circuito Integrado: Conjunto de circuitos en un chip."
                    halign: 'left'
                    theme_text_color: "Custom"
                    text_color: utils.get_color_from_hex("#111111")

            MDCard:
                size_hint_y: None
                height: dp(150)
                orientation: 'horizontal'
                padding: dp(10)
                spacing: dp(10)

                Image:
                    source: 'SensorT.png'
                    size_hint_x: None
                    width: dp(100)

                MDLabel:
                    text: "Sensor de Temperatura: Mide la temperatura."
                    halign: 'left'
                    theme_text_color: "Custom"
                    text_color: utils.get_color_from_hex("#111111")

            MDCard:
                size_hint_y: None
                height: dp(150)
                orientation: 'horizontal'
                padding: dp(10)
                spacing: dp(10)

                Image:
                    source: 'rele.jpeg'
                    size_hint_x: None
                    width: dp(100)

                MDLabel:
                    text: "Relé: Interruptor controlado eléctricamente."
                    halign: 'left'
                    theme_text_color: "Custom"
                    text_color: utils.get_color_from_hex("#111111")

            MDCard:
                size_hint_y: None
                height: dp(150)
                orientation: 'horizontal'
                padding: dp(10)
                spacing: dp(10)

                Image:
                    source: 'motor.jpg'
                    size_hint_x: None
                    width: dp(100)

                MDLabel:
                    text: "Motor DC: Convierte energía eléctrica en mecánica."
                    halign: 'left'
                    theme_text_color: "Custom"
                    text_color: utils.get_color_from_hex("#111111")

            MDCard:
                size_hint_y: None
                height: dp(150)
                orientation: 'horizontal'
                padding: dp(10)
                spacing: dp(10)

                Image:
                    source: 'bateria.png'
                    size_hint_x: None
                    width: dp(100)

                MDLabel:
                    text: "Batería: Almacena energía química."
                    halign: 'left'
                    theme_text_color: "Custom"
                    text_color: utils.get_color_from_hex("#111111")

            MDCard:
                size_hint_y: None
                height: dp(150)
                orientation: 'horizontal'
                padding: dp(10)
                spacing: dp(10)

                Image:
                    source: 'Fotodiodo.png'
                    size_hint_x: None
                    width: dp(100)

                MDLabel:
                    text: "Fotodiodo: Convierte la luz en corriente eléctrica."
                    halign: 'left'
                    theme_text_color: "Custom"
                    text_color: utils.get_color_from_hex("#111111")

            MDCard:
                size_hint_y: None
                height: dp(150)
                orientation: 'horizontal'
                padding: dp(10)
                spacing: dp(10)

                Image:
                    source: 'Microcontrolador.jpg'
                    size_hint_x: None
                    width: dp(100)

                MDLabel:
                    text: "Microcontrolador: Pequeño computador en un solo chip."
                    halign: 'left'
                    theme_text_color: "Custom"
                    text_color: utils.get_color_from_hex("#111111")                    

            MDCard:
                size_hint_y: None
                height: dp(150)
                orientation: 'horizontal'
                padding: dp(10)
                spacing: dp(10)

                Image:
                    source: 'Optoacoplador.jpg'
                    size_hint_x: None
                    width: dp(100)

                MDLabel:
                    text: "Optoacoplador: Aísla eléctricamente dos circuitos."
                    halign: 'left'
                    theme_text_color: "Custom"
                    text_color: utils.get_color_from_hex("#111111")   

            MDCard:
                size_hint_y: None
                height: dp(150)
                orientation: 'horizontal'
                padding: dp(10)
                spacing: dp(10)

                Image:
                    source: 'Potenciómetro.jpg'
                    size_hint_x: None
                    width: dp(100)

                MDLabel:
                    text: "Potenciometro: Resistencia variable utilizada para ajustar niveles de voltaje."
                    halign: 'left'
                    theme_text_color: "Custom"
                    text_color: utils.get_color_from_hex("#111111")   

            MDCard:
                size_hint_y: None
                height: dp(150)
                orientation: 'horizontal'
                padding: dp(10)
                spacing: dp(10)

                Image:
                    source: 'Pulsador.png'
                    size_hint_x: None
                    width: dp(100)

                MDLabel:
                    text: "Pulsador: Interruptor momentáneo que activa o desactiva un circuito."
                    halign: 'left'
                    theme_text_color: "Custom"
                    text_color: utils.get_color_from_hex("#111111") 

            MDCard:
                size_hint_y: None
                height: dp(150)
                orientation: 'horizontal'
                padding: dp(10)
                spacing: dp(10)

                Image:
                    source: 'Sensor_Hall.png'
                    size_hint_x: None
                    width: dp(100)

                MDLabel:
                    text: "Sensor Hall: Detecta campos magnéticos."
                    halign: 'left'
                    theme_text_color: "Custom"
                    text_color: utils.get_color_from_hex("#111111") 

            MDCard:
                size_hint_y: None
                height: dp(150)
                orientation: 'horizontal'
                padding: dp(10)
                spacing: dp(10)

                Image:
                    source: 'Termistor.png'
                    size_hint_x: None
                    width: dp(100)

                MDLabel:
                    text: "Termistor: Resistencia dependiente de la temperatura."
                    halign: 'left'
                    theme_text_color: "Custom"
                    text_color: utils.get_color_from_hex("#111111") 

            MDCard:
                size_hint_y: None
                height: dp(150)
                orientation: 'horizontal'
                padding: dp(10)
                spacing: dp(10)

                Image:
                    source: 'Varistor.jpg'
                    size_hint_x: None
                    width: dp(100)

                MDLabel:
                    text: "Varistor (VDR): Protege contra picos de voltaje."
                    halign: 'left'
                    theme_text_color: "Custom"
                    text_color: utils.get_color_from_hex("#111111") 
            New:
                text: "VOLVER"
                font_size: dp(15)
                pos_hint: {"center_x": 0.5}
                on_release: app.root.current = 'welcome'

<ResistanceIdealScreen>:
    name: 'resistance_ideal'
    Pantalla:
        MDCard:
            size_hint: None, None
            size: dp(350), dp(500)
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
            elevation: 10
            padding: dp(25)
            spacing: dp(20)
            md_bg_color: utils.get_color_from_hex("#777777")
            orientation: 'vertical'

            MDLabel:
                text: "Calculo de Resistencia Ideal"
                halign: 'center'
                font_style: 'H5'
                theme_text_color: "Custom"
                text_color: utils.get_color_from_hex("#000000")
                bold: True

            MDTextField:
                id: voltage
                hint_text: "Voltaje (V)"
                size_hint_x: None
                width: dp(220)
                font_size: dp(18)
                pos_hint: {"center_x": 0.5}

            MDTextField:
                id: current
                hint_text: "Corriente (A)"
                size_hint_x: None
                width: dp(220)
                font_size: dp(18)
                pos_hint: {"center_x": 0.5}

            New:
                text: "CALCULAR"
                font_size: dp(15)
                pos_hint: {"center_x": 0.5}
                on_release: app.calculate_resistance()

            MDLabel:
                id: result_label
                text: ""
                halign: 'center'
                theme_text_color: "Custom"
                text_color: utils.get_color_from_hex("#000000")
                font_style: 'H6'
                bold: True

            MDLabel:
                id: component_label
                text: ""    
                halign: 'center'
                theme_text_color: "Custom"
                text_color: utils.get_color_from_hex("#000000")
                font_style: 'Subtitle1'
                bold: True

            New:
                text: "VOLVER"
                font_size: dp(15)
                pos_hint: {"center_x": 0.5}
                on_release: app.root.current = 'welcome'

<MenuScreen>:
    name: "menu"
    Pantalla:
        MDCard:
            size_hint: None, None
            size: dp(350), dp(500)
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
            elevation: 10
            padding: dp(25)
            spacing: dp(30)
            md_bg_color: utils.get_color_from_hex("#66CC66")
            orientation: 'vertical'
            
            MDBoxLayout:
                orientation: "vertical"
                spacing: dp(20)
                padding: dp(50)
                MDLabel:
                    text: "Prueba tus conocimientos"
                    halign: "center"
                    theme_text_color: "Custom"
                    text_color: utils.get_color_from_hex("#111111")
                    font_size: "25sp"
                MDRaisedButton:
                    text: "Prueba tus conocimientos"
                    on_release: app.root.current = "dificultad"
                    pos_hint: {"center_x": .5}
                New:
                    text: "VOLVER"
                    font_size: dp(15)
                    pos_hint: {"center_x": 0.5}
                    on_release: app.root.current = 'welcome'   

<DificultadScreen>:
    name: "dificultad"
    MDBoxLayout:
        orientation: "vertical"
        spacing: dp(20)
        padding: dp(50)
        canvas.before:
            Color:
                rgba: 0.5, 0.5, 0.5, 1
            Rectangle:
                pos: self.pos
                size: self.size
        MDLabel:
            text: "Elija la dificultad"
            halign: "center"
            font_size: "25sp"
        MDRaisedButton:
            text: "Básico"
            on_release: app.iniciar_quiz("basico.txt")
            pos_hint: {"center_x": .5}
        MDRaisedButton:
            text: "Intermedio"
            on_release: app.iniciar_quiz("intermedio.txt")
            pos_hint: {"center_x": .5}
        MDRaisedButton:
            text: "Avanzado"
            on_release: app.iniciar_quiz("avanzado.txt")
            pos_hint: {"center_x": .5}

<QuizScreen>:
    name: "quiz"
    Pantalla:
        MDBoxLayout:
            orientation: "vertical"
            spacing: dp(20)
            padding: dp(50)
            MDLabel:
                id: pregunta
                text: "Pregunta"
                halign: "center"
                font_size: "25sp"
            MDRaisedButton:
                id: opcion1
                text: "Opción 1"
                on_release: app.responder(0)
                pos_hint: {"center_x": .5}
            MDRaisedButton:
                id: opcion2
                text: "Opción 2"
                on_release: app.responder(1)
                pos_hint: {"center_x": .5}
            MDRaisedButton:
                id: opcion3
                text: "Opción 3"
                on_release: app.responder(2)
                pos_hint: {"center_x": .5}

<ResultadoScreen>:
    name: "resultado"
    Pantalla:
        MDBoxLayout:
            orientation: "vertical"
            spacing: dp(20)
            padding: dp(50)
            MDLabel:
                id: resultado_label
                text: "Tu puntaje es: "
                halign: "center"
                font_size: "25sp"
            MDRaisedButton:
                text: "Volver al inicio"
                on_release: app.root.current = "menu"
                pos_hint: {"center_x": .5}

'''

class Database:
    def __init__(self):
        self.connection = sqlite3.connect('users.db')
        self.cursor = self.connection.cursor()
        self.create_table()

    def create_table(self):
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS users (
                username TEXT PRIMARY KEY,
                password TEXT NOT NULL
            )
        ''')
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS notes (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                username TEXT,
                note TEXT,
                created_at TEXT,
                FOREIGN KEY (username) REFERENCES users (username)
            )
        ''')
        self.connection.commit()

    def hash_password(self, password):
        return sha256(password.encode()).hexdigest()

    def add_user(self, username, password):
        try:
            hashed_password = self.hash_password(password)
            self.cursor.execute('INSERT INTO users (username, password) VALUES (?, ?)',
                              (username, hashed_password))
            self.connection.commit()
            return True
        except sqlite3.IntegrityError:
            return False

    def verify_user(self, username, password):
        hashed_password = self.hash_password(password)
        self.cursor.execute('SELECT * FROM users WHERE username = ? AND password = ?',
                          (username, hashed_password))
        return self.cursor.fetchone() is not None

    def add_note(self, username, note):
        created_at = datetime.now().strftime("%Y-%m-%d")
        self.cursor.execute('INSERT INTO notes (username, note, created_at) VALUES (?, ?, ?)',
                          (username, note, created_at))
        self.connection.commit()

    def get_notes(self, username):
        self.cursor.execute('SELECT * FROM notes WHERE username = ?', (username,))
        return self.cursor.fetchall()

    def delete_note(self, note_id):
        self.cursor.execute('DELETE FROM notes WHERE id = ?', (note_id,))
        self.connection.commit()

    def close(self):
        self.connection.close()

class LoginScreen(Screen):
    pass

class RegisterScreen(Screen):
    pass

class WelcomeScreen(Screen):
    pass

class ComponentsScreen(Screen):
    pass

class ElectroWikiScreen(Screen):
    pass

class ResistanceIdealScreen(Screen):
    pass

class MenuScreen(Screen):
    pass

class DificultadScreen(Screen):
    pass

class QuizScreen(Screen):
    pass

class ResultadoScreen(Screen):
    pass



class NotesScreen(Screen):
    def on_enter(self):
        self.ids.notes_label.clear_widgets()  # Limpiar las notas existentes
        username = self.manager.get_screen('login').ids.user.text
        notes = app.db.get_notes(username)
        for note in notes:
            note_box = BoxLayout(size_hint_y=None, height=40)  # Crear un contenedor para la nota
            note_label = MDLabel(text=f"{note[2]} ({note[3]})", halign='left', theme_text_color="Custom", text_color=get_color_from_hex("#000000"))
            delete_button = MDFlatButton(text="Eliminar", on_release=lambda x, note_id=note[0]: self.delete_note(note_id))
            note_box.add_widget(note_label)
            note_box.add_widget(delete_button)
            self.ids.notes_label.add_widget(note_box)  # Agregar el contenedor de la nota a la interfaz

    def delete_note(self, note_id):
        app.db.delete_note(note_id)  # Llamar al método de eliminación en la base de datos
        self.on_enter()  # Actualizar la vista de notas


class LoginApp(MDApp):
    dialog = None

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.db = Database()

    def build(self):
        self.theme_cls.theme_style = 'Dark'
        self.theme_cls.primary_palette = 'Cyan'
        self.theme_cls.accent_palette = 'Teal'
        return Builder.load_string(KV)

    def show_dialog(self, title, text):
        if not self.dialog:
            self.dialog = MDDialog(
                title=title,
                text=text,
                buttons=[
                    MDFlatButton(
                        text="OK",
                        theme_text_color="Custom",
                        text_color=self.theme_cls.primary_color,
                        on_release=lambda x: self.dialog.dismiss()
                    )
                ]
            )
        self.dialog.text = text
        self.dialog.title = title
        self.dialog.open()

    def show_result_dialog(self, title, text):
        result_dialog = MDDialog(
            title=title,
            text=text,
            size_hint=(0.8, None),
            height=200,
            buttons=[
                MDFlatButton(
                    text="OK",
                    on_release=lambda x: result_dialog.dismiss()
                )
            ]
        )
        result_dialog.open()

    def copy_to_clipboard(self):
        password = self.root.get_screen('generate_password').ids.generated_password.text
        if password != "La contraseña aparecera aqui":
            Clipboard.copy(password)
            toast("Contraseña copiada al portapapeles!")

    def login(self):
        username = self.root.get_screen('login').ids.user.text
        password = self.root.get_screen('login').ids.password.text

        if self.db.verify_user(username, password):
            self.root.get_screen('welcome').ids.welcome_label.text = f"!Bienvenido {username}!"
            self.root.current = 'welcome'
            toast(f"Bienvenido, {username}!")
        else:
            self.show_dialog("Error", "Invalido Usuario o Contraseña")

    def register_user(self):
        username = self.root.get_screen('register').ids.new_username.text
        password = self.root.get_screen('register').ids.new_password.text

        if not username or not password:
            self.show_dialog("Error", "Por favor llena todos los campos")
            return

        if self.db.add_user(username, password):
            self.show_dialog("Exito", "Usuario Registrado Satisfactoriamente!")
            self.root.current = 'login'
        else:
            self.show_dialog("Error", "Usuario ya existe")

    def save_note(self):
        username = self.root.get_screen('login').ids.user.text
        note = self.root.get_screen('notes').ids.note_input.text

        if note:
            self.db.add_note(username, note)
            self.root.get_screen('notes').ids.note_input.text = ""
            self.show_dialog("Exito", "Nota guardada exitosamente!")
            self.root.get_screen('notes').on_enter()
        else:
            self.show_dialog("Error", "Por favor escribe una nota.")

    def paste_note(self):
        clipboard_text = Clipboard.paste()
        self.root.get_screen('notes').ids.note_input.text = clipboard_text
    
    def calculate_resistance(self):
        voltage = self.root.get_screen('resistance_ideal').ids.voltage.text
        current = self.root.get_screen('resistance_ideal').ids.current.text

        try:
            voltage = float(voltage)
            current = float(current)
            resistance = voltage / current
            self.root.get_screen('resistance_ideal').ids.result_label.text = f"Resistencia: {resistance:.2f} Ohmios"

            # Determinar el componente comercial apropiado
            if resistance < 10:
                component = "Resistor de 10 Ohmios"
                characteristics = "Resistor de baja potencia, ideal para circuitos simples."
            elif resistance < 100:
                component = "Resistor de 100 Ohmios"
                characteristics = "Resistor de potencia media, adecuado para la mayoría de los circuitos."
            else:
                component = "Resistor de 1k Ohmios"
                characteristics = "Resistor de alta potencia, utilizado en circuitos de alta resistencia."

            self.root.get_screen('resistance_ideal').ids.component_label.text = f"Componente: {component}\nCaracterísticas: {characteristics}"

        except ValueError:
            self.show_dialog("Error", "Por favor ingresa valores válidos para voltaje y corriente.")

    def build(self):
        return Builder.load_string(KV)

    def iniciar_quiz(self, archivo):
        self.preguntas = self.cargar_preguntas(archivo)
        self.pregunta_actual = 0
        self.puntaje = 0
        self.mostrar_pregunta()
        self.root.current = "quiz"

    def cargar_preguntas(self, archivo):
        with open(archivo, "r", encoding="utf-8") as f:
            lineas = f.read().strip().split("\n\n")

        preguntas = []
        for linea in lineas:
            partes = linea.split("\n")
            pregunta = partes[0]
            opciones = [p[3:] for p in partes[1:]]
        
            # Agregar impresión de depuración
            print("Pregunta leída:", pregunta)
            print("Opciones leídas:", opciones)

            # Buscar la opción correcta
            correctas = [o for o in opciones if o.endswith("(*)")]
            if not correctas:
                print(f"Error: No se encontró opción correcta en la pregunta: {pregunta}")
                continue  # Saltar esta pregunta si no hay opción correcta

            correcta = opciones.index(correctas[0])
            opciones = [o.replace(" (*)", "") for o in opciones]
            preguntas.append((pregunta, opciones, correcta))

        random.shuffle(preguntas)
        return preguntas[:10]

    def mostrar_pregunta(self):
        pregunta, opciones, _ = self.preguntas[self.pregunta_actual]
        quiz_screen = self.root.get_screen("quiz")
        quiz_screen.ids.pregunta.text = pregunta
        quiz_screen.ids.opcion1.text = opciones[0]
        quiz_screen.ids.opcion2.text = opciones[1]
        quiz_screen.ids.opcion3.text = opciones[2]

    def responder(self, seleccion):
        _, _, correcta = self.preguntas[self.pregunta_actual]
        if seleccion == correcta:
            self.puntaje += 1
        self.pregunta_actual += 1
        if self.pregunta_actual < len(self.preguntas):
            self.mostrar_pregunta()
        else:
            self.mostrar_resultado()

    def mostrar_resultado(self):
        resultado_screen = self.root.get_screen("resultado")
        resultado_screen.ids.resultado_label.text = f"Tu puntaje es: {self.puntaje} de 10"
        self.root.current = "resultado"




    def on_stop(self):
        """Se llama cuando la aplicación se cierra"""
        self.db.close()

    
if __name__ == '__main__':
    app = LoginApp()
    app.run()