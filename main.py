# Import the necessary module
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput


class SimpleCalculatorApp(App):
    def build(self):
        self.operators = ["/", "*", "+", "-", "%", "**"]
        self.was_last_operator = None
        self.last_button = None
        main_layout = BoxLayout(orientation="vertical")
        self.solution = TextInput(
            multiline=False, readonly=True, halign="left", font_size=55
        )
        main_layout.add_widget(self.solution)

        #Create Button Layout
        buttons = [
            ["7", "8", "9", "/"],
            ["4", "5", "6", "*"],
            ["1", "2", "3", "-"],
            [".", "0", "C", "+"],
            ["%", "**"]
        ]
        for row in buttons:
            h_layout = BoxLayout()

            # loop through each item in row, then create a Button for each of them
            for label in row:
                button = Button(
                    text=label,
                    pos_hint={"center_x": 0.5, "center_y": 0.5},
                )

                # using the bind() method, bind the on_button_pressed() to each button.
                button.bind(on_press=self.on_button_press)
                
                h_layout.add_widget(button)
            main_layout.add_widget(h_layout)

        # Handles the equal sign
        equals_button = Button(text="=", pos_hint={"center_x": 0.5, "center_y": 0.5})
        equals_button.bind(on_press=self.on_solution)
        main_layout.add_widget(equals_button)

        return main_layout

    def on_button_press(self, instance):
        current = self.solution.text
        button_text = instance.text
        print(button_text)

        if button_text == "C":
            # Clear the solution widget
            self.solution.text = ""
        else:
            if current and (self.was_last_operator and button_text in self.operators):
                # Don't add two operators right after each other
                
                # print(current)
                # print(self.was_last_operator)
                # print(button_text)
                # print(self.operators)

                return
            elif current == "" and button_text in self.operators:
                # First character cannot be an operator
                return
            else:
                new_text = current + button_text
                self.solution.text = new_text
        self.last_button = button_text
        self.was_last_operator = self.last_button in self.operators

    def on_solution(self, instance):
        text = self.solution.text
        if text:
            solution = str(eval(self.solution.text))
            self.solution.text = solution
            pass


if __name__ == "__main__":
    app = SimpleCalculatorApp()
    app.run()
