import kivy
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.popup import Popup
import smtplib
import os

import yaml  # pip install pyyaml


class LoginApp(App):

    # tạo dao diện đăng nhập
    def build(self):

        self.title = "Login form"
        layout = BoxLayout(orientation="vertical", padding=30, spacing=10, size=(800, 400))

        head_label = Label(text="User login", font_size=26, bold=True, height=40)

        name_label = Label(text="Name:", font_size=18)
        self.name_input = TextInput(multiline=False, font_size=18)
        password_label = Label(text="Password:", font_size=18)
        self.password_input = TextInput(multiline=False, font_size=18, password=True)

        login_button = Button(text="Login", font_size=18, on_press=self.login)

        layout.add_widget(head_label)
        layout.add_widget(name_label)
        layout.add_widget(self.name_input)
        layout.add_widget(password_label)
        layout.add_widget(self.password_input)
        layout.add_widget(login_button)

        popup = Popup(title="User Login", content=layout, size_hint=(None, None), size=(800, 400))
        popup.open()

    # phương thức login khi login_button được kích hoạt
    def login(self, instance):
        name = self.name_input.text
        password = self.password_input.text
        filename = name + '.txt'

        if name.strip() == '' or password.strip() == '':
            message = "please fill in all fields"
        else:
            if os.path.exists(filename):
                with open(filename, 'r') as file:
                    data = yaml.safe_load(file)
                    if password != data['Password']:
                        message = "Wrong password!"
                        with open('log.txt', 'w') as file:
                            file.write(str(0))
                    else:
                        message = "Login Success!"
                        self.lock = True
                        with open('log.txt', 'w') as file:
                            file.write(str(1))

            else:
                message = "User name doesn't exit"

        popup_final = Popup(title="Login Status", content=Label(text=message), size_hint=(None, None), size=(400, 200))
        popup_final.open()

if __name__ == '__main__':
    LoginApp().run()
