#här så gör vi att koden vet vilket datum det är
import datetime, time

dt = datetime.datetime.now()
persnum = input("Skriv in ditt personnummer(yyyymmdd-xxxx)") #vi säger till användaren att skriva in deras personnummer
persSplit = persnum.split("-")
dtpers = dt.strptime(persSplit[0], '%Y%m%d')

if (dt.month == dtpers.month and dt.day == dtpers.day): #om man skriver in sitt personnummer och det är samma datum så skriver programmet grattis.
    print("Grattis du fyller år idag! ", dtpers.date())
if int(persSplit[1][-2]) % 2 == 0: #här gör koden en uträkning om du är man eller kvinna efter ditt person nummer
    print("Du är en kvinna")
else:
    print("Du är en man")