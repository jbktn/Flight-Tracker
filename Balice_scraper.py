import urllib.request
from bs4 import BeautifulSoup
import ssl
import csv

IATA_small_database = {
    "FR": "Ryanair",
    "W6": "Wizz Air",
    "LO": "LOT",
    "LH": "Lufthansa",
    "TK": "Turkish Airlines",
    "U2": "easyJet",
    "KL": "KLM",
    "BA": "British Airways",
    "DY": "Norwegian",   
    "EA": "European Air Express",
    "EF": "EasyFly",
    "D8": "Norwegian Air International",
}

def get_operator(code):
    airline = code[:2]
    if airline in IATA_small_database:
        airline = IATA_small_database[airline]
    else:
        with open("IATA_airline_codes.csv", mode='r') as infile:
            reader = csv.reader(infile, delimiter='^')
            for row in reader:
                if row[0] == airline:
                    airline = row[2]
                    break
    return airline

context = ssl._create_unverified_context()

url_incoming = "https://www.krakowairport.pl/pl/pasazer/loty/polaczenia/przyloty/"
get_incoming = urllib.request.urlopen(url_incoming, context=context)
html_incoming = get_incoming.read()

url_outgoing = "https://www.krakowairport.pl/pl/pasazer/loty/polaczenia/wyloty/"
get_outgoing = urllib.request.urlopen(url_outgoing, context=context)
html_outgoing = get_outgoing.read()

soup_incoming = BeautifulSoup(html_incoming, 'html.parser')
soup_outgoing = BeautifulSoup(html_outgoing, 'html.parser')

table_incoming = soup_incoming.find('table')
table_outgoing = soup_outgoing.find('table')

incoming_unclear = table_incoming.find_all('tr')[1:]
outgoing_unclear = table_outgoing.find_all('tr')[1:]

incoming = []
outgoing = []

for flight in incoming_unclear:
    time = str(flight.find("th").text)
    destination = str(flight.find_all("td")[0].text).replace("\n", "").replace("\t", "").replace(" ", "")
    code = str(flight.find_all("td")[1].text).replace("\n", "").replace("\t", "").replace(" ", "")
    status = str(flight.find("span").text).replace("\n", "").replace("\t", "").replace(" ", "")
    link = "https://www.krakowairport.pl" + str(flight.find("a").get('href'))

    airline = get_operator(code)

    incoming.append({'Time': time, 'Destination': destination, 'Airline': airline,'Code': code,'Status': status, "Link": link})

for flight in outgoing_unclear:
    time = str(flight.find("th").text)
    destination = str(flight.find_all("td")[0].text).replace("\n", "").replace("\t", "").replace(" ", "")
    code = str(flight.find_all("td")[1].text).replace("\n", "").replace("\t", "").replace(" ", "")
    status = str(flight.find("span").text).replace("\n", "").replace("\t", "").replace(" ", "")
    link = "https://www.krakowairport.pl" + str(flight.find("a").get('href'))

    airline = get_operator(code)

    outgoing.append({'Time': time, 'Destination': destination, 'Airline': airline,'Code': code,'Status': status, "Link": link})
    
print("Incoming flights:")
for flight in incoming:
    print(flight)
print("Outgoing flights:")
for flight in outgoing:
    print(flight)

f = open("c:/Users/delve/WebstormProjects/flight-tracker/Balice_data.txt", "w")
f.write("Incoming:\n")
for flight in incoming:
    f.write(str(flight) + "\n")
f.write("Outgoing:\n")
for flight in outgoing:
    f.write(str(flight) + "\n")