from pytz import UTC # timezone
from icalendar import Calendar, Event
import datetime
from PIL import Image, ImageDraw, ImageFont
import requests
import time


def get_wrapped_text(text: str, font: ImageFont.ImageFont, line_length: int):
        lines = ['']
        for word in text.split():
            line = f'{lines[-1]} {word}'.strip()
            if font.getlength(line) <= line_length:
                lines[-1] = line
            else:
                lines.append(word)
        return '\n'.join(lines)

def updateTimetable():
    calendarFile = open('./ADECal5A.ics', 'w', encoding='utf-8', newline='\n')

    res = requests.get('http://ade.univ-tours.fr/jsp/custom/modules/plannings/anonymous_cal.jsp?data=3b46878b11fa7c3d580ecb5f6648a9c295c381511cc76ec8bdffe48ddf108006a56b9d48cf60d89aad5fb9b261bdf14bc23fc73e40a62f8cea315d7ede6c0137,1')
    for line in res.text:
        calendarFile.writelines(line)
    calendarFile.close()

    calendarFile = open('./ADECal5B.ics', 'w', encoding='utf-8', newline='\n')

    res = requests.get('http://ade.univ-tours.fr/jsp/custom/modules/plannings/anonymous_cal.jsp?data=0244767deedd65be3ee51f7470b1cb71c11996846e88763bd0db20b9ce4a14ada56b9d48cf60d89aad5fb9b261bdf14bc23fc73e40a62f8cea315d7ede6c0137,1')
    for line in res.text:
        calendarFile.writelines(line)
    calendarFile.close()
    
    calendarFile = open('./ADECal6A.ics', 'w', encoding='utf-8', newline='\n')

    res = requests.get('http://ade.univ-tours.fr/jsp/custom/modules/plannings/anonymous_cal.jsp?data=5895f33e2f963a3010802e36bbb12558afcee9e49fc2e84b5e5c68df6d2263e5a56b9d48cf60d89aad5fb9b261bdf14bc23fc73e40a62f8cea315d7ede6c0137,1')
    for line in res.text:
        calendarFile.writelines(line)
    calendarFile.close()

    calendarFile = open('./ADECal6B.ics', 'w', encoding='utf-8', newline='\n')

    res = requests.get('http://ade.univ-tours.fr/jsp/custom/modules/plannings/anonymous_cal.jsp?data=503b6f75818e7019255a4e96b4e2e65b95c381511cc76ec8bdffe48ddf108006a56b9d48cf60d89aad5fb9b261bdf14bc23fc73e40a62f8cea315d7ede6c0137,1')
    for line in res.text:
        calendarFile.writelines(line)
    calendarFile.close()

def getTimetable(year, month, day, classGroup, englishGroup=1, siGroup=1):
    hour_delta = -7
    cal = Calendar.from_ical(open('ADECal5A.ics', 'rb').read())
    today = datetime.datetime(year, month, day)
    image = Image.new(mode='RGBA',size=(700, 1660),color=(22,22,22,255))
    draw = ImageDraw.Draw(image)
    fnt = ImageFont.truetype("./ayar.ttf", 30, encoding="unic")

    if(classGroup == "5A"):
        cal = Calendar.from_ical(open('ADECal5A.ics', 'rb').read())
    elif(classGroup == "5B"):
        cal = Calendar.from_ical(open('ADECal5B.ics', 'rb').read())
    elif(classGroup == "6A"):
        cal = Calendar.from_ical(open('ADECal6A.ics', 'rb').read())
    elif(classGroup == "6B"):
        cal = Calendar.from_ical(open('ADECal6B.ics', 'rb').read())

    for component in cal.walk():
        if component.name == "VEVENT":
            if(datetime.datetime.date(component.get('dtstart').dt) >= datetime.datetime.date(today) and datetime.datetime.date(component.get('dtstart').dt) <= datetime.datetime.date(today)):
                if(datetime.datetime.weekday(component.get('dtstart').dt) == 0):
                    if(classGroup == '0'):
                        draw.text((225, 100), "Jour non-supporté", font=fnt, fill=(255,255,255,255))
                        continue

                    color = (100,100,100,255)
                    if('Anglais' in component.get('summary')):
                        color = (100,100,255,255)
                    elif('Projets'):
                        color = (255,100,100,255)


                    draw.rectangle((50, 50+138*(component.get('dtstart').dt.timetuple().tm_hour+hour_delta)+35*(component.get('dtstart').dt.timetuple().tm_min//15), 650, 50+138*(component.get('dtend').dt.timetuple().tm_hour+hour_delta)+35*(component.get('dtend').dt.timetuple().tm_min//15)), fill=color)

                    if(len(component.get('summary')) > 35):
                        draw.text((70, 70+138*(component.get('dtstart').dt.timetuple().tm_hour+hour_delta)+35*(component.get('dtstart').dt.timetuple().tm_min//15)),component.get('summary')[:35]+'...',font=fnt,fill=(255,255,255,255))
                    else:
                        draw.text((70, 70+138*(component.get('dtstart').dt.timetuple().tm_hour+hour_delta)+35*(component.get('dtstart').dt.timetuple().tm_min//15)),component.get('summary'),font=fnt,fill=(255,255,255,255))
                    
                    if(len(component.get('location')) > 35):
                        draw.text((70, 110+138*(component.get('dtstart').dt.timetuple().tm_hour+hour_delta)+35*(component.get('dtstart').dt.timetuple().tm_min//15)),component.get('location')[:35]+'...',font=fnt,fill=(255,255,255,255))
                    else:
                        draw.text((70, 110+138*(component.get('dtstart').dt.timetuple().tm_hour+hour_delta)+35*(component.get('dtstart').dt.timetuple().tm_min//15)),component.get('location'),font=fnt,fill=(255,255,255,255))
                    
                    draw.text((70, 150+138*(component.get('dtstart').dt.timetuple().tm_hour+hour_delta)+35*(component.get('dtstart').dt.timetuple().tm_min//15)),component.get('description').split('\n')[-3],font=fnt,fill=(255,255,255,255))

                    draw.text((70, 50+138*(component.get('dtend').dt.timetuple().tm_hour+hour_delta)+35*(component.get('dtend').dt.timetuple().tm_min//15)-40),str(component.get('dtstart').dt.timetuple().tm_hour+1)+':'+str(component.get('dtstart').dt.timetuple().tm_min)+' - '+str(component.get('dtend').dt.timetuple().tm_hour+1)+':'+str(component.get('dtend').dt.timetuple().tm_min),font=fnt,fill=(255,255,255,255))

                else:
                    
                    color = (100,100,100,255)
                    if('Bases de données' in component.get('summary') or 'BD' in component.get('summary')):
                        color = (128,128,0,255)
                    elif('Algèbre' in component.get('summary')):
                        color = (0,128,128,255)
                    elif('Analyse' in component.get('summary')):
                        color = (64,128,64,255)
                    

                    draw.rectangle((50, 50+138*(component.get('dtstart').dt.timetuple().tm_hour+hour_delta)+35*(component.get('dtstart').dt.timetuple().tm_min//15), 650, 50+138*(component.get('dtend').dt.timetuple().tm_hour+hour_delta)+35*(component.get('dtend').dt.timetuple().tm_min//15)), fill=color)

                    if(len(component.get('summary')) > 35):
                        draw.text((70, 70+138*(component.get('dtstart').dt.timetuple().tm_hour+hour_delta)+35*(component.get('dtstart').dt.timetuple().tm_min//15)),component.get('summary')[:35]+'...',font=fnt,fill=(255,255,255,255))
                    else:
                        draw.text((70, 70+138*(component.get('dtstart').dt.timetuple().tm_hour+hour_delta)+35*(component.get('dtstart').dt.timetuple().tm_min//15)),component.get('summary'),font=fnt,fill=(255,255,255,255))
                    
                    if(len(component.get('location')) > 35):
                        draw.text((70, 110+138*(component.get('dtstart').dt.timetuple().tm_hour+hour_delta)+35*(component.get('dtstart').dt.timetuple().tm_min//15)),component.get('location')[:35]+'...',font=fnt,fill=(255,255,255,255))
                    else:
                        draw.text((70, 110+138*(component.get('dtstart').dt.timetuple().tm_hour+hour_delta)+35*(component.get('dtstart').dt.timetuple().tm_min//15)),component.get('location'),font=fnt,fill=(255,255,255,255))
                    
                    draw.text((70, 150+138*(component.get('dtstart').dt.timetuple().tm_hour+hour_delta)+35*(component.get('dtstart').dt.timetuple().tm_min//15)),component.get('description').split('\n')[-3],font=fnt,fill=(255,255,255,255))

                    draw.text((70, 50+138*(component.get('dtend').dt.timetuple().tm_hour+hour_delta)+35*(component.get('dtend').dt.timetuple().tm_min//15)-40),str(component.get('dtstart').dt.timetuple().tm_hour+1)+':'+str(component.get('dtstart').dt.timetuple().tm_min)+' - '+str(component.get('dtend').dt.timetuple().tm_hour+1)+':'+str(component.get('dtend').dt.timetuple().tm_min),font=fnt,fill=(255,255,255,255))

    image.save(f'./calendar{classGroup}.png')

if __name__ == "__main__":
    while True:
        updateTimetable()
        time.sleep(21600)