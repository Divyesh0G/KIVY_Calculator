import kivy
kivy.require("1.9.0")

from kivy.app import App
from kivy.uix.gridlayout import GridLayout

class CalcGridLayout(GridLayout):
    """
    A simple calculator layout class.
    """

    def calculate(self, calculation):
        """
        Function called when equals is pressed to perform the calculation.
        """
        if calculation:
            try:
                self.display.text = str(eval(calculation))
            except Exception:
                self.display.text = "Error"

class CalculatorApp(App):
    """
    The main application class for the calculator app.
    """

    def build(self):
        """
        Build the app by creating an instance of the CalcGridLayout.
        """
        return CalcGridLayout()

calcApp = CalculatorApp()
calcApp.run()
