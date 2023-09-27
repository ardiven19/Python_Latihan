from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
from kivy.uix.label import Label

class Kalkulator(App):
    def build(self):
        # Membuat tata letak
        layout = GridLayout(cols=4)

        # Membuat label untuk menampilkan hasil
        self.label = Label(text="0", font_size=30)
        layout.add_widget(self.label)

        # Membuat tombol-tombol angka dan operator
        buttons = [
            '7', '8', '9', '/',
            '4', '5', '6', '*',
            '1', '2', '3', '-',
            '0', '.', '=', '+'
        ]
        for button in buttons:
            layout.add_widget(Button(text=button, on_press=self.on_button_press))

        return layout

    def on_button_press(self, instance):
        current = self.label.text
        button_text = instance.text

        if button_text == '=':
            # Evaluasi dan tampilkan hasil
            try:
                result = str(eval(current))
            except:
                result = 'Error'
            self.label.text = result
        else:
            # Tambahkan teks tombol ke tampilan saat ini
            self.label.text = current + button_text

if __name__ == '__main__':
    Kalkulator().run()
