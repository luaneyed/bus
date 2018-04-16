from bus_location import fetch
from slack import log

routes = {
    '241449005': '15-1 | 고양,양주',
    '241449011': '15-1구파발 | 고양,서울,양주',
    '241449007': '15-1막차 | 고양,서울,양주',
    '241449006': '15-1첫차 | 고양,양주',
    '235000090': '365-2 | 양주,파주',
    '235000080': '19 | 고양,서울,양주',
    '235000081': '19-1 | 고양,서울,양주',
    '219000025': '상관 없는 테스트 노선'
}


def run(enable_logging:bool = False):
    result = '\n\n'.join(
        [
            '[버스 위치 정보] ({} | {})\n\n'.format(route_name, route_id) + fetch(route_id)
            for route_id, route_name in routes.items()
        ]
    )

    print(result)
    if enable_logging:
        log(result)


if __name__ == '__main__':
    run()
