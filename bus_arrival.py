from BusArrivalItem import BusArrivalItem
from api import call

# bus_arrival_item = BusArrivalItem(xml_root.find('msgBody').find('busArrivalItem'))
# print(bus_arrival_item)


def fetch(station_id: str, route_id: str):
    response = call(
        'busarrivalservice',
        {
            'stationId': station_id,
            'routeId': route_id
        }
    )

    if response is None:
        return None

    return ''.join(
        map(
            lambda list_element: str(BusArrivalItem(list_element)),
            response
        )
    )


if __name__ == '__main__':
    print(fetch('218000952', '241449005'))
