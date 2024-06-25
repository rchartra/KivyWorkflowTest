from kivy.uix.label import Label
from kivy.app import App


class SimpleApp(App):
    def __init__(self, **kwargs):
        super(SimpleApp, self).__init__(**kwargs)
        self.text = "Hello World"

    def build(self):
        return Label(text=self.text)


if __name__ == '__main__':
    SimpleApp().run()
