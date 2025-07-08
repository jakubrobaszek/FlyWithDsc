import requests
import json
from datetime import datetime
# Ryanair (Taryfa Basic: To nasza najtańsza taryfa, która obejmuje 🎒 1 małą torbę kabinową (40 x 20 x 25 cm), która musi zmieścić się pod siedzeniem pasażera z przodu, bez dodatkowego limitu bagażu. Odprawa rozpoczyna się 24 godziny przed odlotem, a w tym czasie miejsce zostanie przydzielone Ci losowo.)
# Odprawy można dokonać tylko 24 godziny przed każdym lotem, bez wyboru miejsc, kara za za duzy bagaz(75 EUR)

def scrape_flights(departureCode: str, arrivalCode: str) -> tuple:
    params = {
        'departureAirportIataCode': departureCode,
        'outboundDepartureDateFrom': '2025-07-01',
        'market': 'pl-pl',
        'adultPaxCount': '1',
        'arrivalAirportIataCode': arrivalCode,
        'searchMode': 'ALL',
        'outboundDepartureDateTo': '2026-06-30',
        'outboundDepartureDaysOfWeek': 'MONDAY,TUESDAY,WEDNESDAY,THURSDAY,FRIDAY,SATURDAY,SUNDAY',
        'outboundDepartureTimeFrom': '00:00',
        'outboundDepartureTimeTo': '23:59'
    }

    resp = requests.get('https://www.ryanair.com/api/farfnd/v4/oneWayFares', params=params)

    if resp.ok:
        json_formatted = json.loads(resp.text)
        flights = []
        for flight in json_formatted['fares']:
            outbound = flight['outbound']
            # single.append((
            #     str(datetime.fromtimestamp(int(outbound['priceUpdated']) / 1000))[:19],
            #     "Ryanair",
            #     departureCode,
            #     arrivalCode,
            #     datetime.strptime(outbound['departureDate'], "%Y-%m-%dT%H:%M:%S"),
            #     datetime.strptime(outbound['arrivalDate'], "%Y-%m-%dT%H:%M:%S"),
            #     outbound['price']['value']
            # ))
            curCode = outbound['price']['currencyCode']
            flights.append(str(datetime.fromtimestamp(int(outbound['priceUpdated']) / 1000))[:19])
            flights.append("Ryanair")
            flights.append(departureCode)
            flights.append(arrivalCode)
            flights.append(str(datetime.strptime(outbound['departureDate'], "%Y-%m-%dT%H:%M:%S")))
            flights.append(str(datetime.strptime(outbound['arrivalDate'], "%Y-%m-%dT%H:%M:%S")))
            flights.append(outbound['price']['value'] if curCode == 'PLN' else outbound['price']['value'] * 4)
            
            #download_date, airline, from_airport, to_airport, from_date, to_date, price
            # print(f'-----{outbound['flightNumber']}-----')
            # print(datetime.strptime(outbound['departureDate'], "%Y-%m-%dT%H:%M:%S"))
            # print(datetime.strptime(outbound['arrivalDate'], "%Y-%m-%dT%H:%M:%S"))
            # print(f"{outbound['price']['value']} zl")
            # print(str(datetime.fromtimestamp(int(outbound['priceUpdated']) / 1000))[:19])

        return flights
    else:
        print(f"ERROR: Flights couldn't be scraped, code: {resp.status_code}, json: {resp.text}")
        return 1