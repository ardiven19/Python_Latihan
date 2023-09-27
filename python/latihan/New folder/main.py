from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout

class MyApp(App):
    def build(self):
        main_layout = BoxLayout(orientation='vertical')

        self.label = Label(text="", font_size=30)
        main_layout.add_widget(self.label)

        grid_layout = GridLayout(cols=4, rows=5)
        main_layout.add_widget(grid_layout)

        buttons = [
            '**', '//', '%', 'del',
            '7', '8', '9', '/',
            '4', '5', '6', '*',
            '1', '2', '3', '-',
            '0', '.', '=', '+'
        ]
        for button in buttons:
            grid_layout.add_widget(Button(text=button, on_press=self.on_button_press))

        return main_layout
    
    def on_button_press(self, button):
        hasil = button.text
        if hasil != '=' and hasil != 'del':
            self.label.text = self.label.text + button.text
        elif hasil == 'del':
            self.label.text = ''
        else:
            Hasil = eval(self.label.text)
            self.label.text = str(Hasil)
if __name__ == '__main__':
    MyApp().run()

        

