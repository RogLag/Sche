from pytz import UTC # timezone
from icalendar import Calendar, Event
from datetime import datetime

cal = Calendar.from_ical(open('ADECal.ics', 'rb').read())
for component in cal.walk():
    if component.name == "VEVENT":
        print(component.get('summary'))
        print(component.get('dtstart').dt)
        print(component.get('dtend').dt)
        print(component.get('location'))
        desc = component.get('description')
        desc = desc.split('\n')
        try:
            desc.remove('')
            desc.remove('')
            desc.remove('')
            desc.pop(-1)
        except ValueError:
            continue
        print(f"\n{desc}\n\n")
        print("------------------------------------------------------------------\n")