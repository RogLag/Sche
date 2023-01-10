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

    res = requests.get('http://ade.univ-tours.fr/jsp/custom/modules/plannings/anonymous_cal.jsp?data=7c86f0965396a2da9a0467f1506a11b215dcab0f24b8913b5d144e852a5d9fe58a209302a3a57afb3553857383c37db83b35a62046be8482c8e9a74d112f972a,1')
    for line in res.text:
        calendarFile.writelines(line)
    calendarFile.close()

    calendarFile = open('./ADECal5B.ics', 'w', encoding='utf-8', newline='\n')

    res = requests.get('http://ade.univ-tours.fr/jsp/custom/modules/plannings/anonymous_cal.jsp?data=247bd40e9e927cdcd5372a49fb7bf28015dcab0f24b8913b5d144e852a5d9fe58a209302a3a57afb3553857383c37db83b35a62046be8482c8e9a74d112f972a,1')
    for line in res.text:
        calendarFile.writelines(line)
    calendarFile.close()
    
    calendarFile = open('./ADECal6A.ics', 'w', encoding='utf-8', newline='\n')

    res = requests.get('http://ade.univ-tours.fr/jsp/custom/modules/plannings/anonymous_cal.jsp?data=799faf6bf0b6a9fce5a794983d0c862d15dcab0f24b8913b5d144e852a5d9fe58a209302a3a57afb3553857383c37db83b35a62046be8482c8e9a74d112f972a,1')
    for line in res.text:
        calendarFile.writelines(line)
    calendarFile.close()

    calendarFile = open('./ADECal6B.ics', 'w', encoding='utf-8', newline='\n')

    res = requests.get('http://ade.univ-tours.fr/jsp/custom/modules/plannings/anonymous_cal.jsp?data=8c2507aaccec7d4b83b7529ede7d522215dcab0f24b8913b5d144e852a5d9fe58a209302a3a57afb3553857383c37db83b35a62046be8482c8e9a74d112f972a,1')
    for line in res.text:
        calendarFile.writelines(line)
    calendarFile.close()
    
    calendarFile = open('./ADECalDAE.ics', 'w', encoding='utf-8', newline='\n')

    res = requests.get('http://ade.univ-tours.fr/jsp/custom/modules/plannings/anonymous_cal.jsp?data=e7e9e0536b5040797fe67c4a1c2cc9e115dcab0f24b8913b5d144e852a5d9fe58a209302a3a57afb3553857383c37db83b35a62046be8482c8e9a74d112f972a,1')
    for line in res.text:
        calendarFile.writelines(line)
    calendarFile.close()
    
    calendarFile = open('./ADECalDEE.ics', 'w', encoding='utf-8', newline='\n')

    res = requests.get('http://ade.univ-tours.fr/jsp/custom/modules/plannings/anonymous_cal.jsp?data=97e60766391b2d15771814d85f3acab915dcab0f24b8913b5d144e852a5d9fe58a209302a3a57afb3553857383c37db83b35a62046be8482c8e9a74d112f972a,1')
    for line in res.text:
        calendarFile.writelines(line)
    calendarFile.close()
    
    calendarFile = open('./ADECalDI.ics', 'w', encoding='utf-8', newline='\n')

    res = requests.get('http://ade.univ-tours.fr/jsp/custom/modules/plannings/anonymous_cal.jsp?data=4278910e58b1740d7851b03949135d2c15dcab0f24b8913b5d144e852a5d9fe58a209302a3a57afb3553857383c37db83b35a62046be8482c8e9a74d112f972a,1')
    for line in res.text:
        calendarFile.writelines(line)
    calendarFile.close()
    
    calendarFile = open('./ADECalDMS.ics', 'w', encoding='utf-8', newline='\n')

    res = requests.get('http://ade.univ-tours.fr/jsp/custom/modules/plannings/anonymous_cal.jsp?data=2db25ab0c708b0450cf9e4f4893d593215dcab0f24b8913b5d144e852a5d9fe58a209302a3a57afb3553857383c37db83b35a62046be8482c8e9a74d112f972a,1')
    for line in res.text:
        calendarFile.writelines(line)
    calendarFile.close()
    
    calendarFile = open('./ADECalA1.ics', 'w', encoding='utf-8', newline='\n')

    res = requests.get('http://ade.univ-tours.fr/jsp/custom/modules/plannings/anonymous_cal.jsp?data=6ab8ee8dd6e73e709fc5a321bce36bd9c49a74fae5535d80911af2f48666394e57d58ab4c63f8fe92968762d8416ed8d6aad19fe006b760288bd644fb363dc02,1')
    for line in res.text:
        calendarFile.writelines(line)
    calendarFile.close()
    
    calendarFile = open('./ADECalA2.ics', 'w', encoding='utf-8', newline='\n')

    res = requests.get('http://ade.univ-tours.fr/jsp/custom/modules/plannings/anonymous_cal.jsp?data=a11203656d8a08ed5e0a76b66cd29a96c49a74fae5535d80911af2f48666394e57d58ab4c63f8fe92968762d8416ed8d6aad19fe006b760288bd644fb363dc02,1')
    for line in res.text:
        calendarFile.writelines(line)
    calendarFile.close()
    
    calendarFile = open('./ADECalA3.ics', 'w', encoding='utf-8', newline='\n')

    res = requests.get('http://ade.univ-tours.fr/jsp/custom/modules/plannings/anonymous_cal.jsp?data=c3949d0351b8f2003244c6c11caa32b5c49a74fae5535d80911af2f48666394e57d58ab4c63f8fe92968762d8416ed8d6aad19fe006b760288bd644fb363dc02,1')
    for line in res.text:
        calendarFile.writelines(line)
    calendarFile.close()
    
    calendarFile = open('./ADECalA4.ics', 'w', encoding='utf-8', newline='\n')

    res = requests.get('http://ade.univ-tours.fr/jsp/custom/modules/plannings/anonymous_cal.jsp?data=5c56167aacaabb42a12a5ed40eee07bfc49a74fae5535d80911af2f48666394e57d58ab4c63f8fe92968762d8416ed8d6aad19fe006b760288bd644fb363dc02,1')
    for line in res.text:
        calendarFile.writelines(line)
    calendarFile.close()
    
    calendarFile = open('./ADECalA5.ics', 'w', encoding='utf-8', newline='\n')

    res = requests.get('http://ade.univ-tours.fr/jsp/custom/modules/plannings/anonymous_cal.jsp?data=c993bbc34b8277f1dafbc82596051837c49a74fae5535d80911af2f48666394e57d58ab4c63f8fe92968762d8416ed8d6aad19fe006b760288bd644fb363dc02,1')
    for line in res.text:
        calendarFile.writelines(line)
    calendarFile.close()
    
    calendarFile = open('./ADECalA6.ics', 'w', encoding='utf-8', newline='\n')

    res = requests.get('http://ade.univ-tours.fr/jsp/custom/modules/plannings/anonymous_cal.jsp?data=367bae18e7673ba7ec4e8a137c2d077b15dcab0f24b8913b5d144e852a5d9fe58a209302a3a57afb3553857383c37db83b35a62046be8482c8e9a74d112f972a,1')
    for line in res.text:
        calendarFile.writelines(line)
    calendarFile.close()
    
    calendarFile = open('./ADECalA7.ics', 'w', encoding='utf-8', newline='\n')

    res = requests.get('http://ade.univ-tours.fr/jsp/custom/modules/plannings/anonymous_cal.jsp?data=73681931add2acc6afdf10ebfb15b2e115dcab0f24b8913b5d144e852a5d9fe58a209302a3a57afb3553857383c37db83b35a62046be8482c8e9a74d112f972a,1')
    for line in res.text:
        calendarFile.writelines(line)
    calendarFile.close()

def getTimetable(year, month, day, classGroup, englishGroup=None, siGroup=None):
    hour_delta = -7
    calclasse = Calendar.from_ical(open('ADECal5A.ics', 'rb').read())
    calprojet = Calendar.from_ical(open('ADECalDAE.ics', 'rb').read())
    calanglais = Calendar.from_ical(open('ADECalA1.ics', 'rb').read())
    today = datetime.datetime(year, month, day)
    image = Image.new(mode='RGBA',size=(700, 1660),color=(22,22,22,255))
    draw = ImageDraw.Draw(image)
    fnt = ImageFont.truetype("./ayar.ttf", 30, encoding="unic")

    if(classGroup == "5A"):
        calclasse = Calendar.from_ical(open('ADECal5A.ics', 'rb').read())
    elif(classGroup == "5B"):
        calclasse = Calendar.from_ical(open('ADECal5B.ics', 'rb').read())
    elif(classGroup == "6A"):
        calclasse = Calendar.from_ical(open('ADECal6A.ics', 'rb').read())
    elif(classGroup == "6B"):
        calclasse = Calendar.from_ical(open('ADECal6B.ics', 'rb').read())
        
    if(siGroup == "DAE"):
        calprojet = Calendar.from_ical(open('ADECalDAE.ics', 'rb').read())
    elif(siGroup == "DEE"):
        calprojet = Calendar.from_ical(open('ADECalDEE.ics', 'rb').read())
    elif(siGroup == "DI"):
        calprojet = Calendar.from_ical(open('ADECalDI.ics', 'rb').read())
    elif(siGroup == "DMS"):
        calprojet = Calendar.from_ical(open('ADECalDMS.ics', 'rb').read())
        
    if(englishGroup == "1"):
        calanglais = Calendar.from_ical(open('ADECalA1.ics', 'rb').read())
    elif(englishGroup == "2"):
        calanglais = Calendar.from_ical(open('ADECalA2.ics', 'rb').read())
    elif(englishGroup == "3"):
        calanglais = Calendar.from_ical(open('ADECalA3.ics', 'rb').read())
    elif(englishGroup == "4"):
        calanglais = Calendar.from_ical(open('ADECalA4.ics', 'rb').read())
    elif(englishGroup == "5"):
        calanglais = Calendar.from_ical(open('ADECalA5.ics', 'rb').read())
    elif(englishGroup == "6"):
        calanglais = Calendar.from_ical(open('ADECalA6.ics', 'rb').read())
    elif(englishGroup == "7"):
        calanglais = Calendar.from_ical(open('ADECalA7.ics', 'rb').read())

    for component in calclasse.walk():
        if component.name == "VEVENT":
            if(datetime.datetime.date(component.get('dtstart').dt) >= datetime.datetime.date(today) and datetime.datetime.date(component.get('dtstart').dt) <= datetime.datetime.date(today)):
                if(datetime.datetime.weekday(component.get('dtstart').dt) == 0):
                    if(classGroup == '0'):
                        draw.text((225, 100), "Jour non-supporté", font=fnt, fill=(255,255,255,255))
                        continue

                    color = (100,100,100,255)

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
    
    if classGroup != '0' or englishGroup != None or siGroup != None:
        for component in calanglais.walk():
                                if component.name == "VEVENT":
                                    if(datetime.datetime.date(component.get('dtstart').dt) >= datetime.datetime.date(today) and datetime.datetime.date(component.get('dtstart').dt) <= datetime.datetime.date(today)):
                                        if(datetime.datetime.weekday(component.get('dtstart').dt) == 0):
                                            if('Anglais' in component.get('summary')):
                                                color = (100,100,255,255)
                                                
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
        
        for component in calprojet.walk():
                                if  component.name == "VEVENT":
                                    if(datetime.datetime.date( component.get('dtstart').dt) >= datetime.datetime.date(today) and datetime.datetime.date( component.get('dtstart').dt) <= datetime.datetime.date(today)):
                                        if(datetime.datetime.weekday( component.get('dtstart').dt) == 0):
                                            if('Projet' in  component.get('summary')):
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

    image.save(f'./calendar{classGroup}.png')

if __name__ == "__main__":
    while True:
        updateTimetable()
        time.sleep(21600)