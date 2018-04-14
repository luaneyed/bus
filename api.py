from urllib.request import Request, urlopen
from urllib.parse import urlencode, quote_plus
import xml.etree.ElementTree as Et
from config import API


def call(service: str, params: dict):

    url = 'http://openapi.gbis.go.kr/ws/rest/' + service
    query_params = '?' \
                  + urlencode(
        {
            quote_plus('serviceKey'): API['service_key'],
            quote_plus('routeId'): '241449006'
        }
    )

    request = Request(url + query_params)
    request.get_method = lambda: 'GET'
    response_body = urlopen(request).read().decode('utf-8')
    xml_root = Et.fromstring(response_body)

    print(response_body)
    # com_msg_header = xml_root.find('comMsgHeader')
    msg_header = xml_root.find('msgHeader')

    return_code = msg_header.find('resultCode').text
    if return_code == '4':
        print('결과가 존재하지 않습니다.')
        exit(0)

    # for c in com_msg_header:
    #     print(c)

    bus_arrival_item = BusArrivalItem(xml_root.find('msgBody').find('busArrivalItem'))
    print(bus_arrival_item)
