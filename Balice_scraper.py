import urllib.request
from bs4 import BeautifulSoup
import ssl
import csv
import json

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

def clear_table(table, append_array):
    for flight in table:
        time = str(flight.find("th").text)
        destination = str(flight.find_all("td")[0].text).replace("\n", "").replace("\t", "").replace(" ", "")
        code = str(flight.find_all("td")[1].text).replace("\n", "").replace("\t", "").replace(" ", "")
        status = str(flight.find("span").text).replace("\n", "").replace("\t", "").replace(" ", "")
        link = "https://www.krakowairport.pl" + str(flight.find("a").get('href'))

        airline = get_operator(code)

        append_array.append(json.dumps({"Time": time, "Destination": destination, "Airline": airline,"Code": code,"Status": status, "Link": link}))

def print_flights(array):
    for flight in array:
        print(flight)


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

clear_table(incoming_unclear, incoming)
clear_table(outgoing_unclear, outgoing)
   
print("Incoming flights:")
print_flights(incoming)
print("Outgoing flights:")
print_flights(outgoing)

with open("./src/Mock_Balice_incoming.json", "w") as file:
    json.dump(incoming, file, indent=4)


