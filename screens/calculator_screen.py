from kivy.uix.widget import Widget
from kivymd.uix.behaviors import HoverBehavior
from kivymd.uix.button import MDRaisedButton


DIVISION_ZERO_MSG = "Não é possivel dividir por zero."


class HoverButton(HoverBehavior, MDRaisedButton):
    pass


class Calculator(Widget):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.__expression = ""
        self.__last_digited = ""

    def __update_screen(self):
        self.ids.output_label.text = self.__expression

    @staticmethod
    def __normalize_expression(expression: str) -> str:
        expression_parts = expression.split(" ")
        normalized_expression_parts = []

        for parts in expression_parts:
            try:
                parts = str(float(parts))
            except:
                pass

            normalized_expression_parts.append(parts)

        return "".join(normalized_expression_parts)

    def __normalize_value(self, value: str) -> str:
        if not value.isdigit():
            if self.__expression == "":
                value = ""

            elif not self.__last_digited.isdigit():
                value = ""

            elif value != ".":
                value = f" {value} "

        return value

    def __clear_error_message(self):
        if self.__expression == DIVISION_ZERO_MSG:
            self.__expression = ""

    def press_button(self, button_value: str) -> None:
        self.__clear_error_message()
        normalized_value = self.__normalize_value(button_value)
        self.__expression += normalized_value
        self.__last_digited = normalized_value
        self.__update_screen()

    def clear_calculator(self):
        self.__expression = ""
        self.__update_screen()

    def calculate(self):
        if self.__expression:
            try:
                expression = self.__normalize_expression(self.__expression)
                self.__expression = str(float(eval(expression)))
            except ZeroDivisionError:
                self.__expression = DIVISION_ZERO_MSG

        self.__update_screen()
