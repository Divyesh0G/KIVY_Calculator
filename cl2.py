from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
from kivy.lang import Builder
from kivy.base import runTouchApp

Builder.load_string('''

<GridLayout>:

    rows: 5
    padding: 10
    spacing: 10
    Button:
        text: 'B1'
        sixe
    Button:
        text: 'B1'
    Button:
        text: 'B1'
    Button:
        text: 'B1'
    Button:
        text: 'B1'
    
    



''')


class  calculator(GridLayout):
    pass


if __name__=='__main__':
    runTouchApp(calculator())