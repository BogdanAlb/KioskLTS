from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.clock import Clock
from kivymd.uix.snackbar import Snackbar
from kivy.core.window import Window
import random, threading, time, requests

Window.fullscreen = True

API_URL = "http://localhost:3000/measure"

class PreloadingApp(MDApp):
    def build(self):
        self.running = False
        self.data = []
        self.theme_cls.theme_style = "Dark"
        self.theme_cls.primary_palette = "DeepOrange"
        return Builder.load_file("kiosk_ui.kv")

    def start_measure(self):
        if not self.running:
            self.running = True
            Snackbar(text="Măsurarea a început!").open()
            threading.Thread(target=self.simulate_measure).start()

    def stop_measure(self):
        self.running = False
        Snackbar(text="Măsurarea a fost oprită.").open()

    def simulate_measure(self):
        while self.running:
            value = round(random.uniform(0.0, 100.0), 2)
            self.root.ids.value_label.text = f"[b]{value} N[/b]"
            try:
                requests.post(API_URL, json={"value": value}, timeout=1)
            except:
                self.root.ids.status_label.text = "[color=ff3333]⚠ Server inactiv[/color]"
            time.sleep(1)

if __name__ == "__main__":
    PreloadingApp().run()