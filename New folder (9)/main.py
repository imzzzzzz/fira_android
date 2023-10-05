import kivy
from kivy.app import App
from kivy.uix.label import Label
from kivy.clock import Clock
from datetime import datetime
from dateutil.relativedelta import relativedelta

kivy.require("2.2.1")  # Replace with your Kivy version

class TimePassedApp(App):
    def build(self):
        self.start_time = datetime(2003, 9, 30, 9, 0, 0)  # Replace with your desired start date and time
        self.label = Label(text=self.get_time_passed(), font_size='20sp')
        Clock.schedule_interval(self.update_time, 0.5)  # Update every 1 second
        return self.label

    def get_time_passed(self):
        current_time = datetime.now()
        time_difference = relativedelta(current_time, self.start_time)

        years = time_difference.years
        months = time_difference.months
        days = time_difference.days
        hours = time_difference.hours
        minutes = time_difference.minutes
        seconds = time_difference.seconds

        return f"{years} years, {months} months, {days} days, {hours} hours, {minutes} minutes, {seconds} seconds"

    def update_time(self, dt):
        self.label.text = self.get_time_passed()

if __name__ == "__main__":
    TimePassedApp().run()
