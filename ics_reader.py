from pytz import UTC # timezone
from icalendar import Calendar, Event
import datetime
from PIL import Image, ImageDraw, ImageFont
import requests
import time


def updateTimetable():
    calendarFile = open('./ADECal.ics', 'w', encoding='utf-8', newline='\n')

    res = requests.get('http://ade.univ-tours.fr/jsp/custom/modules/plannings/anonymous_cal.jsp?data=d1121bb188fd0e63b198fd6403ea11fbc49a74fae5535d80911af2f48666394e57d58ab4c63f8fe92968762d8416ed8d6aad19fe006b760288bd644fb363dc02,1')
    for line in res.text:
        calendarFile.writelines(line)
    calendarFile.close()

def getTimetable(year, month, day):
    cal = Calendar.from_ical(open('ADECal.ics', 'rb').read())
    today = datetime.datetime(year, month, day)
    image = Image.new(mode='RGBA',size=(700, 1660),color=(22,22,22,255))
    draw = ImageDraw.Draw(image)
    fnt = ImageFont.truetype("arial.ttf", 20)

    for component in cal.walk():
        if component.name == "VEVENT":
            if(datetime.datetime.date(component.get('dtstart').dt) >= datetime.datetime.date(today) and datetime.datetime.date(component.get('dtstart').dt) <= datetime.datetime.date(today)):
                color = (100,100,100,255)
                if('Raisonnement' in component.get('summary')):
                    color = (50,50,255,255)
                elif('Calculus' in component.get('summary')):
                    color = (0,200,200,255)
                elif('Electrostatique' in component.get('summary')):
                    color = (255,128,128,255)
                elif('Mécanique' in component.get('summary')):
                    color = (255,0,128,255)
                elif('Informatique'):
                    color = (0,128,64,255)
                
                print("Found it!")
                print(component.get('summary'))

                draw.rectangle((50, 50+138*(component.get('dtstart').dt.timetuple().tm_hour-6)+35*(component.get('dtstart').dt.timetuple().tm_min//15), 650, 50+138*(component.get('dtend').dt.timetuple().tm_hour-6)+35*(component.get('dtend').dt.timetuple().tm_min//15)), fill=color)

                if(len(component.get('summary')) > 60):
                    draw.text((70, 70+138*(component.get('dtstart').dt.timetuple().tm_hour-6)+35*(component.get('dtstart').dt.timetuple().tm_min//15)),component.get('summary')[:60]+'...',font=fnt,fill=(255,255,255,255))
                else:
                    draw.text((70, 70+138*(component.get('dtstart').dt.timetuple().tm_hour-6)+35*(component.get('dtstart').dt.timetuple().tm_min//15)),component.get('summary'),font=fnt,fill=(255,255,255,255))
                
                if(len(component.get('location')) > 60):
                    draw.text((70, 110+138*(component.get('dtstart').dt.timetuple().tm_hour-6)+35*(component.get('dtstart').dt.timetuple().tm_min//15)),component.get('location')[:60]+'...',font=fnt,fill=(255,255,255,255))
                else:
                    draw.text((70, 110+138*(component.get('dtstart').dt.timetuple().tm_hour-6)+35*(component.get('dtstart').dt.timetuple().tm_min//15)),component.get('location'),font=fnt,fill=(255,255,255,255))
                
                draw.text((70, 150+138*(component.get('dtstart').dt.timetuple().tm_hour-6)+35*(component.get('dtstart').dt.timetuple().tm_min//15)),component.get('description').split('\n')[-3],font=fnt,fill=(255,255,255,255))

                draw.text((70, 50+138*(component.get('dtend').dt.timetuple().tm_hour-6)+35*(component.get('dtend').dt.timetuple().tm_min//15)-40),str(component.get('dtstart').dt.timetuple().tm_hour+2)+':'+str(component.get('dtstart').dt.timetuple().tm_min)+' - '+str(component.get('dtend').dt.timetuple().tm_hour+2)+':'+str(component.get('dtend').dt.timetuple().tm_min),font=fnt,fill=(255,255,255,255))

    image.show('./calendar.png')

if __name__ == "__main__":
    while True:
        updateTimetable()
        time.sleep(21600)
