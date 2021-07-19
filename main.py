from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout
import math
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.config import Config

Config.set("graphics", "resizable", 0)
Config.set("graphics", "width", 400)
Config.set("graphics", "height", 500)


class СalculatorApp(App):
    def update_label(self):
        self.lbl.text = self.formula

    def build(self):
        self.formula = "0"
        gl = GridLayout(spacing=3, cols=4, size_hint=(1, .6))
        bl = BoxLayout(orientation="vertical", padding=25)
        self.lbl = Label(text="0", font_size=40, halign="right", valign="center", size_hint=(1, .4),
                         text_size=(400 - 50, 500 * .4 - 50))

        bl.add_widget(self.lbl)

        gl.add_widget(
            Button(text="(", on_press=self.add_number, background_color=[.16, .42, .30, 1], background_normal=""))
        gl.add_widget(
            Button(text=")", on_press=self.add_number, background_color=[.16, .42, .30, 1], background_normal=""))
        gl.add_widget(
            Button(text="Clear", on_press=self.clear, background_color=[.42, .16, .32, 1], background_normal=""))
        gl.add_widget(
            Button(text="<--", on_press=self.add_operation, background_color=[.42, .16, .32, 1], background_normal=""))

        gl.add_widget(
            Button(text="sin", on_press=self.add_operation, background_color=[.16, .42, .30, 1], background_normal=""))
        gl.add_widget(
            Button(text="cos", on_press=self.add_operation, background_color=[.16, .42, .30, 1], background_normal=""))
        gl.add_widget(
            Button(text="π", on_press=self.add_operation, background_color=[.16, .42, .30, 1], background_normal=""))
        gl.add_widget(
            Button(text="n!", on_press=self.add_operation, background_color=[.16, .42, .30, 1], background_normal=""))

        gl.add_widget(
            Button(text="tan", on_press=self.add_operation, background_color=[.16, .42, .30, 1], background_normal=""))
        gl.add_widget(
            Button(text="√", on_press=self.add_operation, background_color=[.16, .42, .30, 1], background_normal=""))
        gl.add_widget(
            Button(text="^", on_press=self.add_operation, background_color=[.16, .42, .30, 1], background_normal=""))
        gl.add_widget(
            Button(text="÷", on_press=self.add_operation, background_color=[.16, .42, .30, 1], background_normal=""))

        gl.add_widget(
            Button(text="7", on_press=self.add_number, background_color=[.25, .41, .42, 1], background_normal=""))
        gl.add_widget(
            Button(text="8", on_press=self.add_number, background_color=[.25, .41, .42, 1], background_normal=""))
        gl.add_widget(
            Button(text="9", on_press=self.add_number, background_color=[.25, .41, .42, 1], background_normal=""))
        gl.add_widget(
            Button(text="x", on_press=self.add_operation, background_color=[.16, .42, .30, 1], background_normal=""))

        gl.add_widget(
            Button(text="4", on_press=self.add_number, background_color=[.25, .41, .42, 1], background_normal=""))
        gl.add_widget(
            Button(text="5", on_press=self.add_number, background_color=[.25, .41, .42, 1], background_normal=""))
        gl.add_widget(
            Button(text="6", on_press=self.add_number, background_color=[.25, .41, .42, 1], background_normal=""))
        gl.add_widget(
            Button(text="-", on_press=self.add_operation, background_color=[.16, .42, .30, 1], background_normal=""))

        gl.add_widget(
            Button(text="1", on_press=self.add_number, background_color=[.25, .41, .42, 1], background_normal=""))
        gl.add_widget(
            Button(text="2", on_press=self.add_number, background_color=[.25, .41, .42, 1], background_normal=""))
        gl.add_widget(
            Button(text="3", on_press=self.add_number, background_color=[.25, .41, .42, 1], background_normal=""))
        gl.add_widget(
            Button(text="+", on_press=self.add_operation, background_color=[.16, .42, .30, 1], background_normal=""))

        gl.add_widget(Button(text="by Alex_lkv", on_press=self.add_operation, background_color=[.32, .85, .94, 0],
                             background_normal=""))
        gl.add_widget(
            Button(text="0", on_press=self.add_number, background_color=[.25, .41, .42, 1], background_normal=""))
        gl.add_widget(
            Button(text=".", on_press=self.add_operation, background_color=[.16, .42, .30, 1], background_normal=""))
        gl.add_widget(
            Button(text="=", on_press=self.calc_result, background_color=[.42, .16, .16, 1], background_normal=""))

        bl.add_widget(gl)
        return bl

    def add_number(self, instance):
        if self.formula == "0":
            self.formula = ""
        self.formula += str(instance.text)
        self.update_label()

    def add_operation(self, instance):
        if str(instance.text) == "x":
            self.formula += "*"
        elif str(instance.text) == "n!":
            self.formula = str(math.factorial(int(self.formula)))
        elif str(instance.text) == "<--":
            self.formula = self.formula[0:-1]
        elif str(instance.text) == "cos":
            self.formula = str(math.cos(int(self.formula)))
        elif str(instance.text) == "sin":
            self.formula = str(math.sin(int(self.formula)))
        elif str(instance.text) == "π":
            self.formula += "3.14"
        elif str(instance.text) == "tan":
            self.formula = str(math.tan(int(self.formula)))
        elif str(instance.text) == "by Alex_lkv":
            self.formula = self.formula
        elif str(instance.text) == "^":
            self.formula += "**"
        elif str(instance.text) == "√":
            self.formula += "** 0.5"
        else:
            self.formula += str(instance.text)
        self.update_label()

    def calc_result(self, instance):
        self.lbl.text = str(eval(self.lbl.text))
        self.formula = "0"

    def clear(self, instance):
        self.formula = "0"
        self.update_label()


if __name__ == "__main__":
    СalculatorApp().run()
