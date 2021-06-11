from datetime import datetime, date

def vyber():
    vyber = int(input("Prejes si Prichod - 1 nebo Odchod - 2? Nebo vypocitat odpracovany cas? - 3: "))
    if vyber == 1:
        prichod()
    elif vyber == 2:
        odchod()
    elif vyber == 3:
        mzda()
    else:
        vyber()

def mzda():
    timeh1 = int(input("Zadej cas prichodu v hodinach: "))
    timem1 = int(input("Zadej cas prichodu v minutach: "))
    timeh2 = int(input("Zadej cas odchodu v hodinach: "))
    timem2 = int(input("Zadej cas odchodu v minutach: "))
    money = int(input("Zadej kolik dostavas na hodinu: "))
    den = input("Zadej co to bylo za den: ")
    if timeh2 > timeh1:
        finaltimeh = timeh2 - timeh1
    else:
        finaltimeh = timeh1 - timeh2
    if timem2 > timeh1:
        finaltimem = timem2 - timem1
    else:
        finaltimem = timem1 - timem2
    finalmoney = (finaltimeh * money) + (finaltimem/60 * money)
    zaokrouhleno = round(finalmoney, 2)
    print(f'\nOdpracovany cas je: {finaltimeh} hodin/y a {finaltimem} minut.')
    print(f'Za tento den: {den} jsi si vydelal: {zaokrouhleno} Korun')
    with open('vyplata.txt', 'a+') as f:
        f.write(f'Za {den} jsi si vydelal {zaokrouhleno} Korun\n\n')
        f.close()
    pokracovani = input("Prejes si pokracovat? Y/N: ")
    if pokracovani == "Y" or pokracovani == "y":
        mzda()
    elif pokracovani == "N" or pokracovani == "n":
        print("Dekuji za vyuziti tohoto programu... <3")

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
        f.write(f'ODCHOD:  Dnesni datum je: {todayformat} a cas je {current_time}\n\n')
        f.write(f'/////////////////////////////////////////////////////////////////////////////// \n\n')
        f.close()
vyber()
