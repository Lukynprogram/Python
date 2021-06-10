import os
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
    print(f'PRICHOD: Dnesni datum je: {today} a cas je {current_time}')

def odchod():
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    today = date.today()
    print(f'ODCHOD:  Dnesni datum je: {today} a cas je {current_time}')
    print("///////////////////////////////////////////////////////////////////////////////")

vyber()
