# Importiere erforderliche Kivy-Klassen
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput

# Definiere die Hauptanwendungsklasse
class CalculatorApp(App):
    def build(self):
        # Liste der mathematischen Operatoren
        self.operators = ['+', '-', '*', '/']
        # Variablen zur Verfolgung des zuletzt gedrückten Buttons und des letzten Operators
        self.last_was_operator = None
        self.last_button = None
        # Erstelle ein vertikales Layout für die Benutzeroberfläche
        self.result = BoxLayout(orientation='vertical')
        
        # Erstelle ein Textfeld zur Anzeige des aktuellen Ausdrucks
        self.display = TextInput(font_size=32, readonly=True, halign='right', multiline=False)
        self.result.add_widget(self.display)
        
        # Definiere die Tasten auf dem Taschenrechner
        buttons = [
            ['7', '8', '9', '/'],
            ['4', '5', '6', '*'],
            ['1', '2', '3', '-'],
            ['.', '0', 'C', '+']
        ]
        
        # Erstelle die Tasten und füge sie zum Layout hinzu
        for row in buttons:
            h_layout = BoxLayout()
            for label in row:
                button = Button(text=label, pos_hint={'center_x': 0.5, 'center_y': 0.5})
                # Verknüpfe die Methode on_button_press mit dem Drücken der Taste
                button.bind(on_press=self.on_button_press)
                h_layout.add_widget(button)
            self.result.add_widget(h_layout)
        
        # Erstelle die Gleichheits-Taste und verknüpfe sie mit der Methode on_solution
        equals_button = Button(text='=', pos_hint={'center_x': 0.5, 'center_y': 0.5})
        equals_button.bind(on_press=self.on_solution)
        self.result.add_widget(equals_button)
        
        # Gib das Layout (die Benutzeroberfläche) zurück
        return self.result

    # Diese Methode wird aufgerufen, wenn eine Taste gedrückt wird
    def on_button_press(self, instance):
        current = self.display.text
        button_text = instance.text

        # Wenn die 'C'-Taste gedrückt wird, lösche den Inhalt des Textfelds
        if button_text == 'C':
            self.display.text = ''
        else:
            # Überprüfe, ob der letzte Button ein Operator war und der aktuelle Button ebenfalls ein Operator ist
            if current and (self.last_was_operator and button_text in self.operators):
                return
            # Überprüfe, ob das Textfeld leer ist und der aktuelle Button ein Operator ist
            elif current == '' and button_text in self.operators:
                return
            else:
                # Füge den Text des aktuellen Buttons zum aktuellen Inhalt hinzu
                new_text = current + button_text
                self.display.text = new_text

        # Aktualisiere die Variablen zur Verfolgung des letzten Buttons und Operators
        self.last_button = instance
        self.last_was_operator = button_text in self.operators

    # Diese Methode wird aufgerufen, wenn die Gleichheits-Taste (=) gedrückt wird
    def on_solution(self, instance):
        text = self.display.text
        try:
            # Berechne das Ergebnis des Ausdrucks und zeige es im Textfeld an
            solution = str(eval(self.display.text))
            self.display.text = solution
        except:
            # Bei einem Fehler zeige 'Error' im Textfeld an
            self.display.text = 'Error'

# Starte die Anwendung, wenn die Datei direkt ausgeführt wird
if __name__ == '__main__':
    app = CalculatorApp()
    app.run()
