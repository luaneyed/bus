from BusLocationList import BusLocationList
from api import call

url = 'http://openapi.gbis.go.kr/ws/rest/buslocationservice'


def fetch(route_id: str):
    response = call('buslocationservice', {'routeId': route_id})

    if response is None:
        return None

    return ''.join(
        map(lambda list_element: BusLocationList(list_element).print_simple(), response)
    )
