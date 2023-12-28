from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
import random

class GuessNumberApp(App):
    def build(self):
        return GuessNumberLayout()

class GuessNumberLayout(BoxLayout):
    def __init__(self, **kwargs):
        super(GuessNumberLayout, self).__init__(**kwargs)
        self.orientation = "vertical"
        self.secret_number = random.randint(1, 100)
        self.attempts = 0

        self.label = Label(text="Enter your guess:")
        self.text_input = TextInput(multiline=False)
        self.button = Button(text="Submit", on_press=self.check_guess)

        self.add_widget(self.label)
        self.add_widget(self.text_input)
        self.add_widget(self.button)

    def check_guess(self, instance):
        guess = int(self.text_input.text)
        self.attempts += 1

        if guess == self.secret_number:
            self.label.text = f"Congratulations! You guessed the number in {self.attempts} attempts."
        elif guess < self.secret_number:
            self.label.text = "Too low. Try again."
        else:
            self.label.text = "Too high. Try again."

if __name__ == "__main__":
    GuessNumberApp().run()
