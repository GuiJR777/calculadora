from kivymd.app import MDApp
from kivy.lang import Builder

from screens.calculator_screen import Calculator

Builder.load_file("screens/calculator_screen.kv")


class CalculatorAPP(MDApp):
    def build(self):
        return Calculator()


if __name__ == "__main__":
    CalculatorAPP().run()
