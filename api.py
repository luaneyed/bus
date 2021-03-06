import xml.etree.ElementTree as Et
from urllib.parse import urlencode
from urllib.request import Request, urlopen

from config import API
from slack import log


def call(service: str, params: dict):
    params['serviceKey'] = API['service_key']

    request = Request('http://openapi.gbis.go.kr/ws/rest/' + service + '?' + urlencode(params))
    request.get_method = lambda: 'GET'
    response_body = urlopen(request).read().decode('utf-8')
    xml_root = Et.fromstring(response_body)

    com_msg_header = xml_root.find('comMsgHeader')
    msg_header = xml_root.find('msgHeader')

    return_code = msg_header.find('resultCode').text
    if return_code == '4':
        return None

    if return_code != '0':
        error_message = 'Error occurred! {}'.format(com_msg_header.find('errMsg').text)
        print(error_message)
        log(error_message)
        exit(0)

    return xml_root.find('msgBody')
