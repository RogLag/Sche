from pytz import UTC # timezone
from icalendar import Calendar, Event
import datetime
from PIL import Image, ImageDraw, ImageFont
import requests
import time


def updateTimetable():
    calendarFile = open('./ADECal.ics', 'w', encoding='utf-8', newline='\n')

    res = requests.get('http://ade.univ-tours.fr/jsp/custom/modules/plannings/anonymous_cal.jsp?data=d10d2eee7adfcc1a372dc75a5b67ef2228aab545587a28d07e896f720f6422bca56b9d48cf60d89aad5fb9b261bdf14bc23fc73e40a62f8cea315d7ede6c0137,1')
    for line in res.text:
        calendarFile.writelines(line)
    calendarFile.close()

def getTimetable(year, month, day, englishGroup, siGroup):
    cal = Calendar.from_ical(open('ADECal.ics', 'rb').read())
    today = datetime.datetime(year, month, day)
    image = Image.new(mode='RGBA',size=(700, 1660),color=(22,22,22,255))
    draw = ImageDraw.Draw(image)
    fnt = ImageFont.truetype("arial.ttf", 20)

    for component in cal.walk():
        if component.name == "VEVENT":
            if(datetime.datetime.date(component.get('dtstart').dt) >= datetime.datetime.date(today) and datetime.datetime.date(component.get('dtstart').dt) <= datetime.datetime.date(today)):
                if(datetime.datetime.weekday(component.get('dtstart').dt) == 0):
                    color = (100,100,100,255)
                    if('Anglais' in component.get('summary')):
                        color = (100,100,255,255)
                    elif('Sc_Ingé'):
                        color = (255,100,100,255)

                    if('A'+str(englishGroup) not in component.get('summary') and 'G'+str(siGroup) not in component.get('summary')):
                        continue


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

                else:
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

    image.save('./calendar.png')

if __name__ == "__main__":
    while True:
        updateTimetable()
        time.sleep(21600)
