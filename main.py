from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput

123455
class CalculatorApp(App):
    def build(self):
        self.operators = ['+', '-', '*', '/']
        self.last_was_operator = None
        self.last_button = None
        self.result = BoxLayout(orientation='vertical')
        
        self.display = TextInput(font_size=32, readonly=True, halign='right', multiline=False)
        self.result.add_widget(self.display)
        
        buttons = [
            ['7', '8', '9', '/'],
            ['4', '5', '6', '*'],
            ['1', '2', '3', '-'],
            ['.', '0', 'C', '+']
        ]
        
        for row in buttons:
            h_layout = BoxLayout()
            for label in row:
                button = Button(text=label, pos_hint={'center_x': 0.5, 'center_y': 0.5})
                button.bind(on_press=self.on_button_press)
                h_layout.add_widget(button)
            self.result.add_widget(h_layout)
        
        equals_button = Button(text='=', pos_hint={'center_x': 0.5, 'center_y': 0.5})
        equals_button.bind(on_press=self.on_solution)
        self.result.add_widget(equals_button)
        
        return self.result

    def on_button_press(self, instance):
        current = self.display.text
        button_text = instance.text

        if button_text == 'C':
            self.display.text = ''
        else:
            if current and (self.last_was_operator and button_text in self.operators):
                return
            elif current == '' and button_text in self.operators:
                return
            else:
                new_text = current + button_text
                self.display.text = new_text

        self.last_button = instance
        self.last_was_operator = button_text in self.operators

    def on_solution(self, instance):
        text = self.display.text
        try:
            solution = str(eval(self.display.text))
            self.display.text = solution
        except:
            self.display.text = 'Error'

if __name__ == '__main__':
    app = CalculatorApp()
    app.run()
