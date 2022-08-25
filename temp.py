from enum import auto
from itertools import tee

import kivy

from datetime import datetime, date

from kivy.app import App 
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.pagelayout import PageLayout
from kivy.uix.button import Button

from kivy.uix.textinput import TextInput

class LoginScreen(GridLayout):

    def __init__(self, **kwargs):
        super(LoginScreen, self).__init__(**kwargs)
        self.cols = 2
        self.add_widget(Label(text="User Name"))
        self.username = TextInput(multiline=False)
        self.add_widget(self.username)
        self.add_widget(Label(text="password"))
        self.password = TextInput(password=True, multiline=False)
        self.add_widget(self.password)

class PageOne(GridLayout):
    
    def __init__(self, **kwargs):
        super(PageOne, self).__init__(**kwargs)

        self.rows = 2
        self.date_now = self.get_date()
        self.time_now = self.get_time()
        self.add_widget(Button(text=self.date_now + " " + self.time_now))
    def get_date(self):
        today = date.today()
        current_date = today.strftime("%m/%d/%y")
        return current_date
    def get_time(self):
        now = datetime.now()
        current_time = now.strftime("%H:%M:%S")
        return current_time

class PageTwo(GridLayout):
    
    def __init__(self, **kwargs):
        super(PageTwo, self).__init__(**kwargs)
        self.rows = 2

        self.add_widget(Button(text="Rate your mood out of 10. If it is more complex than a mental rating, specify on the next step."))
        self.mood = TextInput()
        self.add_widget(self.mood)

class PageThree(GridLayout):
    
    def __init__(self, **kwargs):
        super(PageThree, self).__init__(**kwargs)
        self.rows = 2

        self.add_widget(Button(text="Please choose one to three emotions out of the selection:"))
        self.mood = TextInput()
        self.add_widget(self.mood)

class RecordEvent(PageLayout):
    
    def __init__(self, **kwargs):
        super(RecordEvent, self).__init__(**kwargs)
        page_one = PageOne()
        page_two = PageTwo()
        page_three = PageThree()

        self.add_widget(page_one)
        self.add_widget(page_two)
        self.add_widget(page_three)


class MyApp(App):

    def build(self):
        return RecordEvent()

if __name__ == '__main__':
    MyApp().run()