# cal/utils.py

from datetime import datetime, timedelta
from calendar import HTMLCalendar

from django.shortcuts import get_object_or_404

from .models import User, Profile, tutorClasses, Classes, Request, Tutor


class Calendar(HTMLCalendar):
    def __init__(self, year=None, month=None, user=None):
        self.year = year
        self.month = month
        self.user = user
        super(Calendar, self).__init__()

    # formats a day as a td
    # filter events by day
    def formatday(self, day, events):
        if len(str(self.month)) == 1:
            formatted_month = "0" + str(self.month)
        else:
            formatted_month = str(self.month)
        if len(str(day)) == 1:
            formatted_day = "0" + str(day)
        else:
            formatted_day = str(day)
        date = str(self.year) + "-" + formatted_month + "-" + formatted_day
        # print(date)
        events_per_day = events.filter(date__contains=date)
        d = ''
        for event in events_per_day:
            d += f'<li> {event.classname}, {event.startTime} to {event.endTime}, {event.location}, ' \
                 f'{event.student.first_name} {event.student.last_name}, approval status: {event.approved} </li>'

        if day != 0:
            return f"<td><span class='date'>{day}</span><ul> {d} </ul></td>"
        return '<td></td>'

    # formats a week as a tr
    def formatweek(self, theweek, events):
        week = ''
        for d, weekday in theweek:
            week += self.formatday(d, events)
        return f'<tr> {week} </tr>'

    # formats a month as a table
    # filter events by year and month
    def formatmonth(self, withyear=True):
        tutor = Tutor.objects.filter(user=self.user)
        # tutor = get_object_or_404(Tutor, user=self.user)
        # request = Request.objects.get(tutor=tutor)
        # print(request.date)
        events = Request.objects.filter(date__icontains=self.year, date__contains=self.month,
                                        tutor__id__in=tutor).exclude(approved="denied")

        cal = f'<table border="0" cellpadding="0" cellspacing="0" class="calendar">\n'
        cal += f'{self.formatmonthname(self.year, self.month, withyear=withyear)}\n'
        cal += f'{self.formatweekheader()}\n'
        for week in self.monthdays2calendar(self.year, self.month):
            cal += f'{self.formatweek(week, events)}\n'
        return cal
