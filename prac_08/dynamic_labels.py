from kivy.app import App
from kivy.lang import Builder
from kivy.uix.label import Label
from kivy.properties import StringProperty
from kivy.core.window import Window


class DisplayNamesAsLabelsApp(App):
    status_text = StringProperty()

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.names = {"ethan", "tyler", "clayton", "will", "phil"}

    def build(self):
        self.title = "Names as Labels"
        self.root = Builder.load_file('dynamic_labels.kv')
        self.create_labels()
        Window.size = (400, 200)
        return self.root

    def create_labels(self):
        for name in self.names:
            temp_label = Label(text=name)
            self.root.ids.name_box.add_widget(temp_label)


DisplayNamesAsLabelsApp().run()
