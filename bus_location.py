from urllib.request import Request, urlopen
from urllib.parse import urlencode, quote_plus
import xml.etree.ElementTree as Et
from BusLocationList import BusLocationList
from config import API

url = 'http://openapi.gbis.go.kr/ws/rest/buslocationservice'


def fetch(route_id: str):
    query_params = '?' \
                  + urlencode(
                        {
                            quote_plus('serviceKey'): API['service_key'],
                            quote_plus('routeId'): route_id
                        }
                    )

    request = Request(url + query_params)
    request.get_method = lambda: 'GET'
    response_body = urlopen(request).read().decode('utf-8')
    xml_root = Et.fromstring(response_body)

    # com_msg_header = xml_root.find('comMsgHeader')
    msg_header = xml_root.find('msgHeader')

    return_code = msg_header.find('resultCode').text
    if return_code == '4':
        return None

    return ''.join(
        map(
            lambda list_element: BusLocationList(list_element).print_simple(),
            xml_root.find('msgBody')
        )
    )
