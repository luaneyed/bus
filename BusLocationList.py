import xml.etree.ElementTree as Et


class BusLocationList:
    def __init__(self, bus_arrival_item: Et):
        self.route_id = bus_arrival_item.find('routeId').text
        self.station_id = bus_arrival_item.find('stationId').text
        self.station_seq = bus_arrival_item.find('stationSeq').text
        self.end_bus = bus_arrival_item.find('endBus').text
        self.plate_no = bus_arrival_item.find('plateNo').text
        self.plate_type = bus_arrival_item.find('plateType').text
        self.remain_seat_cnt = bus_arrival_item.find('remainSeatCnt').text

    def __str__(self):
        return '노선 ID : {}\n' \
               '정류소 ID : {}\n' \
               '정류소 순서 : {}\n' \
               '막차 여부 : {}\n' \
               '차량번호 : {}\n' \
               '차종 : {}\n' \
               '빈 자리 수 : {}\n'\
            .format(
                self.route_id,
                self.station_id,
                self.station_seq,
                self.end_bus,
                self.plate_no,
                self.plate_type,
                self.remain_seat_cnt
            )

    def print_simple(self, station_map: dict):
        return '{:2d}번째 정류소 : {}  (ID : {}){} - {}\n'\
            .format(
                int(self.station_seq),
                station_map[self.station_id],
                self.station_id,
                ' <막차>' if (self.end_bus == '1') else '',
                self.plate_no
            )
