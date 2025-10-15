from kivymd.app import MDApp
from kivymd.uix.screenmanager import MDScreenManager, MDScreen
from kivymd.uix.dialog import MDDialog
from kivymd.uix.button import MDFlatButton
from kivy.lang import Builder
import os
import json


# === Pagini ===

class WelcomeScreen(MDScreen):
    def login(self):
        name = self.ids.name_field.text.strip()
        if not name:
            self.show_dialog("Eroare", "Introdu un nume de utilizator.")
            return

        os.makedirs("data", exist_ok=True)
        with open("data/profile.json", "w") as f:
            json.dump({"username": name}, f)

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


# === Aplicația ===

class KioskApp(MDApp):
    def build(self):
        self.title = "Kiosk LTS"
        self.theme_cls.theme_style = "Dark"
        self.theme_cls.primary_palette = "BlueGray"
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