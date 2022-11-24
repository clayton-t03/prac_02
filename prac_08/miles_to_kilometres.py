from kivy.app import App
from kivy.lang import Builder
from kivy.core.window import Window

MILES_TO_KM = 1.609


class MilesToKilometersApp(App):
    def build(self):
        """build the kivy app from kv file"""
        Window.size = (400, 200)
        self.title = "Convert Miles to Kilometres"
        self.root = Builder.load_file('miles_to_kilometres.kv')
        return self.root

    def convert_text_to_float(self, text):
        try:
            return float(text)
        except ValueError:
            return 0.0

    def handle_calculate(self, text):
        try:
            kilometres = self.convert_text_to_float(text) * MILES_TO_KM
            self.root.ids.output_label.text = str(kilometres)
        except ValueError:
            pass

    def handle_increment_increase(self, text):
        miles = self.convert_text_to_float(text) + 1
        self.root.ids.input_number.text = str(miles)

    def handle_increment_decrease(self, text):
        miles = self.convert_text_to_float(text) - 1
        self.root.ids.input_number.text = str(miles)


MilesToKilometersApp().run()

