#nutrition, sleep, discipline, spirituality/philospohy/religion
#rate mood, record date, time

#organized data, future features of voice memos, journaling, drawing, and other forms of expression
#date cleaning and analyzation, ie times where common moods occured etc

from datetime import datetime, date

class Record():
    def __init__(self):
        self.date_now = self.get_date()
        self.time_now = self.get_time()
        self.mood = self.get_mood()
        self.emotion = self.get_emotion()
    def get_date(self):
        today = date.today()
        current_date = today.strftime("%m/%d/%y")
        print("Date =", current_date)
        return current_date
    def get_time(self):
        now = datetime.now()
        current_time = now.strftime("%H:%M:%S")
        print("Current Time =", current_time)
        return current_time
    def get_mood(self):
        mood = input("Rate your mood out of 10. If it is more complex than a mental rating, specify on the next step.")
        return mood
        #need a prevailing list of common emotion
    def get_emotion(self):
        choose_emotion = input("Please choose one to three emotions out of the selection:")
        #choose_emotion will be a list of 1 to 3 emotion names
        #------code here------
        return choose_emotion
        

new_entry = Record()
