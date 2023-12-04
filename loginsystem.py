import kivy

from kivy.app import App

from kivy.uix.boxlayout import BoxLayout

from kivy.uix.label import Label

from kivy.uix.textinput import TextInput

from kivy.uix.button import Button

from kivy.uix.popup import Popup



import subprocess

class Loginsystem(App):
    def build(self):

        self.title = "Login game"

        layout = BoxLayout(orientation='vertical', padding= 30,spacing=10)

        login_button = Button (text='Login', font_size=18, on_press=self.login)

        registration_button = Button (text='Register', font_size=18, on_press=self.register)

        layout.add_widget(login_button)
        layout.add_widget(registration_button)

        popup = Popup(title = "User Login", content = layout, size_hint=(None, None), size=(800, 400))
        popup.open()
    def login(self, instance):
        subprocess.run(['python', 'LoginApp.py'])
    def register(self, instance):
        subprocess.run(['python', 'RegistrationApp.py'])


if __name__=='__main__':
    Loginsystem().run()






        


        

       
        


