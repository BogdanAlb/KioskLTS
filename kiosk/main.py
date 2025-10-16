from kivymd.app import MDApp
from kivymd.uix.screenmanager import ScreenManager, Screen
from kivymd.uix.dialog import MDDialog
from kivymd.uix.button import MDFlatButton
from kivy.lang import Builder
import os
import json


class WelcomeScreen(Screen):
    def on_pre_enter(self):
        # Verifică dacă există deja un profil creat
        if os.path.exists("data/profile.json"):
            self.manager.current = "login"

    def create_user(self):
        username = self.ids.name_field.text.strip()
        password = self.ids.password_field.text.strip()

        if not username or not password:
            self.show_dialog("Eroare", "Completează toate câmpurile.")
            return

        os.makedirs("data", exist_ok=True)
        with open("data/profile.json", "w") as f:
            json.dump({"username": username, "password": password}, f, indent=4)

        self.show_dialog("Succes", f"Profilul '{username}' a fost creat!")
        self.manager.current = "login"

    def show_dialog(self, title, text):
        dialog = MDDialog(
            title=title,
            text=text,
            buttons=[MDFlatButton(text="OK", on_release=lambda x: dialog.dismiss())],
        )
        dialog.open()


class LoginScreen(Screen):
    def login(self):
        username = self.ids.login_user.text.strip()
        password = self.ids.login_pass.text.strip()

        if not os.path.exists("data/profile.json"):
            self.show_dialog("Eroare", "Nu există niciun profil. Creează unul mai întâi.")
            self.manager.current = "welcome"
            return

        with open("data/profile.json", "r") as f:
            data = json.load(f)

        if username == data["username"] and password == data["password"]:
            self.show_dialog("Succes", f"Bun venit, {username}!")
            self.manager.current = "home"
        else:
            self.show_dialog("Eroare", "Nume sau parolă incorecte.")

    def show_dialog(self, title, text):
        dialog = MDDialog(
            title=title,
            text=text,
            buttons=[MDFlatButton(text="OK", on_release=lambda x: dialog.dismiss())],
        )
        dialog.open()


class HomeScreen(Screen):
    pass


class LiveDataScreen(Screen):
    pass


class RecordDataScreen(Screen):
    pass


class VerifyScreen(Screen):
    pass


class KioskApp(MDApp):
    def build(self):
        self.title = "PRELOAD MEASURING SYSTEM"
        self.theme_cls.theme_style = "Dark"
        self.theme_cls.primary_palette = "Indigo"
        Builder.load_file("kiosk_ui.kv")

        sm = MDScreenManager()
        sm.add_widget(WelcomeScreen(name="welcome"))
        sm.add_widget(LoginScreen(name="login"))
        sm.add_widget(HomeScreen(name="home"))
        sm.add_widget(LiveDataScreen(name="live"))
        sm.add_widget(RecordDataScreen(name="record"))
        sm.add_widget(VerifyScreen(name="verify"))
        return sm


if __name__ == "__main__":
    KioskApp().run()