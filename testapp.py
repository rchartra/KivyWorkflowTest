from kivy.uix.label import Label
from kivy.app import App


class TestApp(App):

    def build(self):
        return Label(text="Hello world")


if __name__ == '__main__':
    TestApp().run()
