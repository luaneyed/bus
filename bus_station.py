from api import call
from config import STATION_DATA


def fetch(route_id: str):
    response = call('busrouteservice/station', {'routeId': route_id})

    if response is None:
        return None

    return {station.find('stationId').text: station.find('stationName').text for station in response}


def get_map(route_id: str):
    if route_id in STATION_DATA:
        return STATION_DATA[route_id]

    return fetch(route_id)


if __name__ == '__main__':
    print(get_map('219000025'))
