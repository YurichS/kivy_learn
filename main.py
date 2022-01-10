from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.popup import Popup


class MainApp(App):
    def build(self):
        main_layout = BoxLayout(orientation="vertical", padding=10, spacing=10)
        self.equation = TextInput(multiline=False, readonly=False, halign="right", font_size=50, input_filter="float")
        main_layout.add_widget(self.equation)
        buttons = [
            ['1/x', 'x^2', 'x^(1/2)', '/'],
            ['7', '8', '9', '*'],
            ['4', '5', '6', '-'],
            ['1', '2', '3', '+'],
            ['C', '0', '.', '='],
        ]
        for line in buttons:
            h_layout = BoxLayout()
            for label in line:
                button = Button(text=label, font_size=30, background_color=[0, 0, 0, 0], on_press=self.button_press)
                h_layout.add_widget(button)
            main_layout.add_widget(h_layout)

        return main_layout

    def show_error(self, error_text):
        popup_layout = GridLayout(cols=1)
        error_name = Label(text=error_text)
        popup_button = Button(text="OK", on_press=lambda *args: self.pop.dismiss())
        popup_layout.add_widget(error_name)
        popup_layout.add_widget(popup_button)
        self.pop = Popup(title='Error',
                         content=popup_layout,
                         size_hint=(None, None), size=(400, 400), auto_dismiss=False)
        self.pop.open()


    def button_press(self, instance):
        if instance.text == 'C':
            print(type(self.equation))
            self.equation.text = ""
        elif instance.text == '1/x':
            if self.equation.text != '' and self.equation.text != '0':
                self.equation.text = str(1 / eval(self.equation.text))
            else:
                error_text = 'Can\'t divide by zero'
                self.show_error(error_text)
        elif instance.text == 'x^2':
            self.equation.text = str(eval(self.equation.text) ** 2)
        elif instance.text == 'x^(1/2)':
            if eval(self.equation.text) >= 0 and self.equation.text != '':
                self.equation.text = str(eval(self.equation.text) ** (1 / 2))
            else:
                error_text = 'No square root of negative number'
                self.show_error(error_text)
        elif instance.text == "=":
            self.equation.text = str(eval(self.equation.text))

        else:
            self.equation.text += instance.text


if __name__ == '__main__':
    MainApp().run()
