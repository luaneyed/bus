from datetime import datetime, timedelta

import bus_location
from slack import log


def run(debug: bool = True):
    routes = {
            '241449005': '15-1 | 고양,양주',
            '241449011': '15-1구파발 | 고양,서울,양주',
            '241449007': '15-1막차 | 고양,서울,양주',
            '241449006': '15-1첫차 | 고양,양주',
            '235000090': '365-2 | 양주,파주',
            '235000080': '19 | 고양,서울,양주',
            '235000081': '19-1 | 고양,서울,양주'
        }

    now = datetime.utcnow() + timedelta(hours=9)

    locations = [
        '({} | {})\n\n'.format(routes[route_id], route_id) + location
        for route_id, location in {route_id: bus_location.fetch(route_id) for route_id in routes}.items()
        if location is not None
    ]

    result = '[버스 위치 정보] ({})'.format(now.strftime('%Y-%m-%d %H:%M:%S'))

    if locations:
        result += '\n\n' + '\n'.join(locations)

        print(result)
        if not debug:
            log(result)
    else:
        result += ' - 결과 없음'

        print(result)


if __name__ == '__main__':
    run()
