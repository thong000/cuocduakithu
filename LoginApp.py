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
        if not os.path.exists("account/" + str(self.name_input.text)):
            os.makedirs("account/" + str(self.name_input.text))
        name = self.name_input.text
        password = self.password_input.text
        filename = "account/" + str(name) + '/info.txt'

        if name.strip() == '' or password.strip() == '':
            message = "please fill in all fields"
        else:
            if os.path.exists(filename):
                with open(filename, 'r') as file:
                    data = yaml.safe_load(file)
                    if str(password) != str(data['Password']):
                        message = "Wrong password!"
                        with open('log.txt', 'w') as file:
                            file.write(str(0))
                    else:

                        # Tạo mới folder mang tên của tài khoản nếu chưa có
                        if not os.path.exists("account/" + str(name)):
                            os.makedirs("account/" + str(name))

                        #######tạo mới các file lưu thông tin người chơi nếu chưa có

                        # information
                        if not os.path.exists("account/" + str(name) + "/info.txt"):
                            with open("account/" + str(name) + "/info.txt", 'w') as file:
                                file.write("")
                        # coin
                        if not os.path.exists("account/" + str(name) + "/coin.txt"):
                            with open("account/" + str(name) + "/coin.txt", 'w') as file:
                                file.write("100")
                        # History
                        if not os.path.exists("account/" + str(name) + "/history.txt"):
                            with open("account/" + str(name) + "/history.txt", 'w') as file:
                                file.write("Stt,Nhan vat,Ket qua,Tien cuoc,Tien nhan duoc,Thoi gian,Nguon goc")
                                file.write('/n')

                        # Kiem tra dang nhap
                        message = "Login Success!"
                        self.lock = True

                        # Lưu tình trạng đăng nhập
                        with open('log.txt', 'w') as file:
                            file.write(str(1))

                        # Xác định user
                        with open('user.txt', 'w') as file:
                            file.write(name)

                        #Stt của lịch sử
                        if not os.path.exists("account/" + str(name) + "/stt.txt"):
                            with open("account/" + str(name) + "/stt.txt", 'w') as file:
                                file.write("1")

                        # screenshot
                        if not os.path.exists("account/" + str(name) + "/screenshot.docx"):
                            with open("account/" + str(name) + "/screenshot.docx", 'w') as file:
                                file.write("")
                            # Xem có phải lần đầu đăng nhập không
                            with open('first_log.txt', 'w') as file:
                                file.write("1")




            else:
                message = "User name doesn't exit"

        popup_final = Popup(title="Login Status", content=Label(text=message), size_hint=(None, None), size=(400, 200))
        popup_final.open()


if __name__ == '__main__':
    LoginApp().run()
