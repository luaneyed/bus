from urllib.request import Request, urlopen
from urllib.parse import urlencode, quote_plus
import xml.etree.ElementTree as Et
from BusArrivalItem import BusArrivalItem
from config import API

url = 'http://openapi.gbis.go.kr/ws/rest/busarrivalservice'

queryParams = '?' \
              + urlencode(
                    {
                        quote_plus('serviceKey'): API['service_key'],
                        quote_plus('stationId'): '218000952',
                        quote_plus('routeId'): '241449005',
                        quote_plus('staOrder'): '16'
                    }
                )

request = Request(url + queryParams)
request.get_method = lambda: 'GET'
response_body = urlopen(request).read().decode('utf-8')
xml_root = Et.fromstring(response_body)

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
