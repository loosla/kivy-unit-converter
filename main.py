from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.gridlayout import GridLayout
from kivy.uix.popup import Popup

import math


class TextArea(TextInput):
    input_filter = "float"
    multiline = False
    padding_x = TextInput().width / 2
    padding_y = TextInput().height / 2

    def __init__(self, **kwargs):
        super(TextArea, self).__init__(**kwargs)

class UnitConverterApp(App):
    def build(self):
        main_layout = BoxLayout(orientation="vertical")

        title_layout = BoxLayout(orientation="horizontal")
        title_layout.add_widget(Label())
        title_layout.add_widget(Label(text="KG"))
        title_layout.add_widget(Label(text="LB"))

        weight_layout = BoxLayout(orientation="horizontal")
        weight_layout.add_widget(Label(text="Weight: "))
        self.weight_kg = TextArea()
        self.weight_lb = TextArea()
        weight_layout.add_widget(self.weight_kg)
        weight_layout.add_widget(self.weight_lb)

        price_layout = BoxLayout(orientation="horizontal")
        price_layout.add_widget(Label(text="Price: "))
        self.price_kg = TextArea()
        self.price_lb = TextArea()
        price_layout.add_widget(self.price_kg)
        price_layout.add_widget(self.price_lb)

        calculate_layout = BoxLayout(orientation="horizontal")
        button = Button(text="Get Cost", pos_hint={"center_x": 0.5, "center_y": 0.5})
        button.bind(on_press=self.get_cost)
        calculate_layout.add_widget(button)

        cost_layout = BoxLayout(orientation="horizontal")
        cost_layout.add_widget(Label(text="Total Cost: "))
        self.cost = Label()
        cost_layout.add_widget(self.cost)

        layout = GridLayout(rows=5)
        layout.add_widget(title_layout)
        layout.add_widget(weight_layout)
        layout.add_widget(price_layout)
        layout.add_widget(calculate_layout)
        layout.add_widget(cost_layout)

        main_layout.add_widget(layout)

        return main_layout

    def get_cost(self, btn):
        if not ((self.weight_kg.text or self.weight_lb.text) and \
                (self.price_kg.text or self.price_lb.text)):
            self.show_warning_popup("Weight and Price Should Have a Value!")
        if (self.weight_kg.text and self.weight_lb.text) or \
                (self.price_kg.text and self.price_lb.text):
            self.show_warning_popup("Weight and Price Should Have a Only One Value!")
        else:
            weight_kg = float(self.weight_kg.text) if self.weight_kg.text else lb_to_kg(float(self.weight_lb.text))
            price_kg = float(self.price_kg.text) if self.price_kg.text else lb_to_kg(float(self.price_lb.text))
            total_price = weight_kg * price_kg
            self.cost.text = "$" + str(round_up(total_price, 2))

    def show_warning_popup(self, text):
        message_layout = BoxLayout(orientation="vertical")
        message_layout.add_widget(Label(text=text))
        close_popup = Button(text="OK")
        message_layout.add_widget(close_popup)
        popup = Popup(title="TRY AGAIN", content=message_layout,
                      auto_dismiss=False)
        close_popup.bind(on_press=popup.dismiss)
        popup.open()


def round_up(self, n, decimals=0):
    multiplier = 10 ** decimals
    return math.ceil(n * multiplier) / multiplier

def lb_to_kg(self, value):
    if value.isnumeric():
        return value * 2.20462262
    return 0

if __name__ == "__main__":
    UnitConverterApp().run()

