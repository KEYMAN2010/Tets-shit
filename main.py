from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.graphics import Color, Rectangle
import random
import string

class PasswordGenApp(App):
    def build(self):
        # Main layout
        layout = BoxLayout(orientation="vertical", padding=10, spacing=10)

        # Large Textbox for generated passwords
        self.password_box = self.create_outlined_widget(
            TextInput(
                text="Passwords appear here",
                multiline=True,
                background_color=(0, 0, 0, 1),
                foreground_color=(1, 1, 1, 1),
                font_size=18,
                size_hint=(1, 0.7),
            )
        )
        layout.add_widget(self.password_box)

        # Small Textbox for inputting password length
        self.length_box = self.create_outlined_widget(
            TextInput(
                hint_text="Enter password length",
                multiline=False,
                background_color=(0, 0, 0, 1),
                foreground_color=(1, 1, 1, 1),
                size_hint=(1, 0.1),
            )
        )
        layout.add_widget(self.length_box)

        # Generate Button
        generate_button = self.create_outlined_widget(
            Button(
                text="Generate",
                size_hint=(1, 0.2),
                background_color=(0, 0, 0, 1),
                color=(1, 1, 1, 1),
            )
        )
        generate_button.bind(on_press=self.generate_password)
        layout.add_widget(generate_button)

        return layout

    def create_outlined_widget(self, widget):
        """Adds a white outline around the widget."""
        with widget.canvas.before:
            Color(1, 1, 1, 1)  # White color for outline
            widget.rect = Rectangle(size=widget.size, pos=widget.pos)
            widget.bind(size=self.update_rect, pos=self.update_rect)
        return widget

    def update_rect(self, widget, *args):
        """Updates the rectangle outline when widget size/position changes."""
        widget.rect.size = widget.size
        widget.rect.pos = widget.pos

    def generate_password(self, instance):
        try:
            # Get the desired password length
            length = int(self.length_box.text)
            if length < 1:
                self.password_box.text = "Length must be greater than 0!"
                return

            # Generate a random password
            characters = string.ascii_letters + string.digits + string.punctuation
            password = "".join(random.choices(characters, k=length))

            # Display the password in the large textbox
            self.password_box.text = password
        except ValueError:
            self.password_box.text = "Please enter a valid number!"

# Run the app
if __name__ == "__main__":
    PasswordGenApp().run()
