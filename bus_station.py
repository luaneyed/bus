from api import call


def fetch(route_id: str):
    response = call('busrouteservice/station', {'routeId': route_id})

    if response is None:
        return None

    stations = {station.find('stationId').text: station.find('stationName').text for station in response}

    return stations


if __name__ == '__main__':
    print(fetch('235000080'))
