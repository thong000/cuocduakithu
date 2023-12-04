import kivy

from kivy.app import App

from kivy.uix.boxlayout import BoxLayout

from kivy.uix.label import Label

from kivy.uix.textinput import TextInput

from kivy.uix.button import Button

from kivy.uix.popup import Popup

import smtplib
import random
import os


class RegistrationApp(App):


    def build(self):
        

        self.title = "Registration Form"

        layout = BoxLayout(orientation='vertical', padding= 30,spacing=10)

        layout_otp = BoxLayout(orientation = 'vertical', padding = 30, spacing = 10)


        head_label = Label(text="User Registration", font_size=26, bold=True, height=40)

        head_label_otp = Label(text = "Check user otp", font_size = 26, bold=True, height = 40)


        #create otp

        self.otp = ''.join([str(random.randint(0,9)) for i in range(6)])


        #adding label

        name_label = Label(text="Name:",font_size=18)

        self.name_input = TextInput(multiline=False, font_size=18)


        email_label = Label(text="Email:",font_size=18)

        self.email_input = TextInput(multiline=False, font_size=18)


        password_label = Label(text="Password:",font_size=18)

        self.password_input = TextInput(multiline=False, font_size=18, password=True)


        confirm_label = Label(text="Confirm Password:",font_size=18)

        self.confirm_input = TextInput(multiline=False, font_size=18, password=True)
        

        #button

        submit_button = Button (text='Register', font_size=18, on_press=self.register)


        layout.add_widget(head_label)

        layout.add_widget(name_label)

        layout.add_widget(self.name_input)

        layout.add_widget(email_label)

        layout.add_widget(self.email_input)

        layout.add_widget(password_label)

        layout.add_widget(self.password_input)

        layout.add_widget(confirm_label)

        layout.add_widget(self.confirm_input)

        layout.add_widget(submit_button)


        return layout
        


    def register(self, instance):

        #collect information

        name = self.name_input.text

        email = self.email_input.text

        password = self.password_input.text

        confirm_password = self.confirm_input.text

        filename_username = name + ".txt"
        filename_email = email + ".txt"
       



        #validation

        if name.strip()=='' or email.strip()=='' or password.strip() == '' or confirm_password.strip() =='':

            message = "please fill in all fields"

            popup_final = Popup(title = "Register Status", content = Label(text=message), size_hint=(None, None), size=(400, 200))
            popup_final.open()

        elif password != confirm_password:

            message = "Passwords do not match"

            popup_final = Popup(title = "Register Status", content = Label(text=message), size_hint=(None, None), size=(400, 200))
            popup_final.open()

        elif os.path.exists(filename_username):

            message = "Username existed! Please change other username!"

            popup_final = Popup(title = "Register Status", content = Label(text=message), size_hint=(None, None), size=(700, 200))
            popup_final.open()
        elif os.path.exists(filename_email):
            message = "Email has be used! Please change other email!"

            popup_final = Popup(title = "Register Status", content = Label(text=message), size_hint=(None, None), size=(700, 200))
            popup_final.open()

        else:

            self.title = "Check otp Form"

            layout_otp = BoxLayout(orientation = 'vertical', padding = 20, spacing = 10)

            head_label_otp = Label(text = "Check user otp", font_size = 26, bold=True, height = 40)

            #otp block

            confirm_otp = Label(text="Confirm Otp:", font_size = 16)

            self.otp_input = TextInput(multiline = False, font_size =20, password = True)


            #button otp

            check_otp_button = Button (text = "Check", font_size = 16, on_press = self.checkotp)

            #send email button 

            send_otp_button = Button (text = "Send otp", font_size = 16, on_press = self.sendotp)


            #layout of otp check

            layout_otp.add_widget(head_label_otp)

            layout_otp.add_widget(confirm_otp)

            layout_otp.add_widget(self.otp_input)

            layout_otp.add_widget(send_otp_button)

            layout_otp.add_widget(check_otp_button)
            

            #create layout_otp

            popup = Popup(title = "Otp validation", content = layout_otp, size_hint=(None, None), size=(800, 400))
            popup.open()
            

    #check otp

    def checkotp(self, instance):

        email = self.email_input.text

        name = self.name_input.text

        password = self.password_input.text

        confirm_password = self.confirm_input.text

        otp_i = self.otp_input.text

        if otp_i.strip() != self.otp:

            message = "Wrong otp!"

            popup_final = Popup(title = "Register Status", content = Label(text=message), size_hint=(None, None), size=(400, 200))
            popup_final.open()

        else:

            filename_username = name + '.txt'

            user_dictionary = {

                "Name": name,

                "Email": email,

                "Password": password

            }

            with open(filename_username, 'w') as file:

                for i in user_dictionary:   

                    file.write(i + ": " + user_dictionary[i]+ "\n")

            filename_email = email + ".txt"
            user_email = {

                "Email": email

            }
            with open(filename_email, 'w') as file:

                for i in user_email:   

                    file.write(i + ": " + user_email[i])


            message = "Registration suscessful\nName: {}\nEmail: {}".format(name, email)


            popup_final = Popup(title = "Register Status", content = Label(text=message), size_hint=(None, None), size=(400, 200))
            popup_final.open()

    #send otp

    def sendotp(self, instance):

        email = self.email_input.text

        self.server = smtplib.SMTP('smtp.gmail.com', 587)

        self.server.starttls()

        self.server.login("phungudandaicaa@gmail.com","iahttvkmginujahl")

        self.msg='Hello, Your OTP is '+ self.otp

        self.server.sendmail('phungudandaicaA@gmail.com', email, self.msg)

        self.server.quit()
    

if __name__=='__main__':

    RegistrationApp().run()

