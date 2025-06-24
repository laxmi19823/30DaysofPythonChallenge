from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.core.window import Window

Window.size = (400, 500)
Window.clearcolor = (0.95, 0.95, 0.95, 1)  # Light background

class TempConverterApp(App):
    def build(self):
        self.layout = BoxLayout(orientation='vertical', padding=20, spacing=20)

        self.input = TextInput(
            hint_text="Enter temperature",
            font_size=22,
            size_hint=(1, 0.2),
            multiline=False,
            background_color=(1, 1, 1, 1),
            foreground_color=(0, 0, 0, 1),
            padding=(10, 10)
        )
        self.layout.add_widget(self.input)

        self.result_label = Label(
            text="",
            font_size=24,
            color=(0, 0, 0, 1),
            size_hint=(1, 0.2)
        )
        self.layout.add_widget(self.result_label)

        btn_celsius = Button(
            text="Convert to Celsius",
            size_hint=(1, 0.2),
            font_size=20,
            background_color=(0.2, 0.6, 1, 1)
        )
        btn_celsius.bind(on_press=self.to_celsius)
        self.layout.add_widget(btn_celsius)

        btn_fahrenheit = Button(
            text="Convert to Fahrenheit",
            size_hint=(1, 0.2),
            font_size=20,
            background_color=(1, 0.5, 0.2, 1)
        )
        btn_fahrenheit.bind(on_press=self.to_fahrenheit)
        self.layout.add_widget(btn_fahrenheit)

        return self.layout

    def to_celsius(self, instance):
        try:
            f = float(self.input.text)
            c = (f - 32) * 5 / 9
            self.result_label.text = f"{c:.2f} °C"
        except:
            self.result_label.text = "Invalid input!"

    def to_fahrenheit(self, instance):
        try:
            c = float(self.input.text)
            f = (c * 9 / 5) + 32
            self.result_label.text = f"{f:.2f} °F"
        except:
            self.result_label.text = "Invalid input!"

if __name__ == "__main__":
    TempConverterApp().run()
