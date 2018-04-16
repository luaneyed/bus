from BusLocationList import BusLocationList
from api import call
import bus_station


def fetch(route_id: str):
    response = call('buslocationservice', {'routeId': route_id})

    if response is None:
        return None

    station_map = bus_station.fetch(route_id)

    return ''.join(
        map(lambda list_element: BusLocationList(list_element).print_simple(station_map), response)
    )


if __name__ == '__main__':
    print(fetch('219000025'))

