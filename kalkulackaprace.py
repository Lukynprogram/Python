import os
def main():
  os.system("cls")
  os.system("color a")
  hodiny = int(input("Vložte odpracované hodiny: "))
  minuty = int(input("Vložte zbylé minuty: "))
  mzda = int(input("Vložte kolik máte na hodinu: "))
  datum = input("Vložte datum: ")
  jméno = input("Vložte jméno: ")
  minhod = minuty/60
  koruny = "Kč"
  def log():
      peníze = (hodiny + minhod) * mzda
      print(peníze,"Kč")
      with open('prace.txt', 'a+') as f:
          f.write(f"{jméno, peníze, koruny, datum}\n")
          f.close()
  log()
  exit = input("Chcete pokračovat? Y/N: ")
  if exit == "N":
        exit
  if exit == "Y":
        main()
main()
