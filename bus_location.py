from BusLocation import BusLocation
from api import call
import bus_station
from urllib.request import Request, urlopen
import json


def fetch(route_id: str, by_scrapping: bool = True):
    return fetch_by_scrapping(route_id) if by_scrapping else fetch_by_api(route_id)


def fetch_by_scrapping(route_id: str):
    request = Request('http://m.gbis.go.kr/search/getBusLocationList.do?routeId=' + route_id)
    response_string = urlopen(request).read().decode('utf-8')

    location_list = json.loads(response_string)['busLocationList']['locationList']

    return print_locations(map(lambda location: BusLocation(location), location_list), route_id)\
        if location_list\
        else None


def fetch_by_api(route_id: str):
    response = call('buslocationservice', {'routeId': route_id})

    return print_locations(map(lambda location: BusLocation.from_element_tree(location), response), route_id)\
        if response\
        else None


def print_locations(locations: iter, route_id: str):
    station_map = bus_station.get_map(route_id)

    return ''.join(map(lambda location: location.print_simple(station_map), locations))


if __name__ == '__main__':
    print(fetch('219000025'))
