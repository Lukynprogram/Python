from datetime import datetime, date

def vyber():
    vyber = int(input("Prejes si Prichod - 1 nebo Odchod - 2?: "))
    if vyber == 1:
        prichod()
    elif vyber == 2:
        odchod()
    else:
        vyber()

def prichod():
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    today = date.today()
    todayformat = today.strftime("%d-%B-%Y")
    with open('pracelog.txt', 'a+') as f:
        f.write(f'PRICHOD: Dnesni datum je: {todayformat} a cas je {current_time} \n')
        f.close()

def odchod():
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    today = date.today()
    todayformat = today.strftime("%d-%B-%Y")
    with open('pracelog.txt', 'a+') as f:
        f.write(f'ODCHOD:  Dnesni datum je: {todayformat} a cas je {current_time}\n')
        f.write(f'/////////////////////////////////////////////////////////////////////////////// \n')
        f.close()
vyber()
