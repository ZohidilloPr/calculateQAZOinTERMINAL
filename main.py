from time import sleep
from datetime import date

def now():
    today = date.today()
    return today

def timer():
    timer = sleep(3)


def check_Date(i):
    if i['o'] > 12 or i['k'] > 31:
        oy = i['o']
        kun = i['k']
        print(f'Siz oy yoki kuni xato kiritdingiz ? oy-->{oy}, kun-->{kun}')
        survey()

def survey():
    v = ""
    global a, b
    print('Salom Men Qancha Qazo nomozingiz borligini taxminan hisoblab beraman')
    s = input('Boshlashimiz uchun sizdan bazi bir narsalarni sorashim kerak rozimisiz ? xa/yoq ')
    if s == 'xa':
        name = input('Ismingiz ')
        jins = input('Siz erkak/ayol ? ')
        print('Tug\'ulgan yil oy kuni kiriting!')
        a = {
            'y': int(input('yil ')),
            'o': int(input('oy ')),
            'k': int(input('kun ')),
        } 
        check_Date(a)
        n = input('Nomoz o\'qishni boshlaganmisiz xa/yoq ')
        if n == 'xa':
            print('Nomoz o\'qishni boshlagan taxminiy sanani kiriting!\n(Haqiqatdan 5 mahal o\'qishni boshlagan sanani)')
            b = {
                'y': int(input('yil ')),
                'o': int(input('oy ')),
                'k': int(input('kun ')),
            }
            check_Date(b)
        elif n == 'yoq':
            print('Unday bo\'lsa "bugun" deb yozing !')
            v = input("... ")
        else:
            survey()    
        if jins == 'erkak':    
            a['y'] += 12 
        elif jins == 'ayol':
            a['y'] += 8 
        else:
            print('bunday tanlov yoq')
            survey()
        if v != "":
            if v == 'bugun':
                r1 = a['y'] - now().year
                r2 = a['o'] - now().month
                r3 = a['k'] - now().day
        else:
            r1 = a['y'] - b['y']
            r2 = a['o'] - b['o']
            r3 = a['k'] - b['k']

        qy = r1 * 365
        qo = r2 * 31
        qr = qy + qo + r3

        print(f'Xurmatli {name} siz {r1} yil {r2} oy {r3} kun Nomoz O\'qimagansiz (Bu taxminiy hisob)')
        if qr != 0:
            print(f' Bu {qr} kun nomoz o\'qimagansiz degani :( ')
        if qr != 0:    
            m = input('Maslahat beraymi :) xa/yoq ')
            if m == 'xa':
                print(f'Yaxshi Tanlov {name} Har kuni qolib ketgan bir kunik nomozingizni o\'qing!')
                timer()
                print('Bunga o\'rtacha 20 daqiqa yoki kamroq ham ketishi mumkun. Chunki qolib ketgan nomozni faqat farzni o\'qiysiz:)')
                timer()
                print('Axir kunlik 20 daqiqa nomoz uchun sariflasangiz nima bolibdi :) Tog\'rimi! ')
                timer()
                l = input(f'Nimani Unitganizni aytaymi ? {name} xa/yoq ')
                if l == 'xa':
                    print('Istifforni....')
                elif l == 'yoq':
                    print(f'Mayli Nima ham deya olardik Bilimdon {name.upper()}ga :] ')    
            elif m == 'yoq':
                print(f'O\'zingiz bilasiz {name.upper()}')
        elif qr == 0:
            print('qoyil !')
            timer()
            print('Menimcha men sizga kerak emasman :)')

    elif s == 'yoq':
        print('Ha tushunarli xayr :(')    

survey()
a = input('Dasturdan chiqish uchun enterni bosing :) ')