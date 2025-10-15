from kivymd.app import MDApp
from kivymd.uix.screenmanager import MDScreenManager, MDScreen
from kivymd.uix.dialog import MDDialog
from kivymd.uix.button import MDFlatButton
from kivy.lang import Builder
import os
import json


class WelcomeScreen(MDScreen):
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
        self.manager.current = "home"

    def show_dialog(self, title, text):
        dialog = MDDialog(
            title=title,
            text=text,
            buttons=[MDFlatButton(text="OK", on_release=lambda x: dialog.dismiss())],
        )
        dialog.open()


class HomeScreen(MDScreen):
    pass


class LiveDataScreen(MDScreen):
    pass


class RecordDataScreen(MDScreen):
    pass


class VerifyScreen(MDScreen):
    pass


class KioskApp(MDApp):
    def build(self):
        self.title = "Kiosk LTS"
        self.theme_cls.theme_style = "Dark"
        self.theme_cls.primary_palette = "Indigo"
        Builder.load_file("kiosk_ui.kv")

        sm = MDScreenManager()
        sm.add_widget(WelcomeScreen(name="welcome"))
        sm.add_widget(HomeScreen(name="home"))
        sm.add_widget(LiveDataScreen(name="live"))
        sm.add_widget(RecordDataScreen(name="record"))
        sm.add_widget(VerifyScreen(name="verify"))
        return sm


if __name__ == "__main__":
    KioskApp().run()