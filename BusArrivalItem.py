import xml.etree.ElementTree as Et


class BusArrivalItem:
    def __init__(self, bus_arrival_item: Et):
        self.flag = bus_arrival_item.find('flag').text
        self.location_no_1 = bus_arrival_item.find('locationNo1').text
        self.location_no_2 = bus_arrival_item.find('locationNo2').text
        self.plate_no_1 = bus_arrival_item.find('plateNo1').text
        self.plate_no_2 = bus_arrival_item.find('plateNo2').text
        self.predict_time_1 = bus_arrival_item.find('predictTime1').text
        self.predict_time_2 = bus_arrival_item.find('predictTime2').text
        self.remain_seat_cnt_1 = bus_arrival_item.find('remainSeatCnt1').text
        self.remain_seat_cnt_2 = bus_arrival_item.find('remainSeatCnt2').text

    def __str__(self):
        return '상태 : {}\n\n' \
               '-- First Bus --\n\n' \
               '{}번째 전 정류소\n' \
               '차량번호 : {}\n' \
               '{}분 후 도착 예정\n' \
               '빈 자리 수 : {}\n\n' \
               '-- Second Bus --\n\n' \
               '{}번째 전 정류소\n' \
               '차량번 : {}\n' \
               '{}분 후 도착 예정\n' \
               '빈 자리 수 : {}\n'\
            .format(
                self.flag,
                self.location_no_1,
                self.plate_no_1,
                self.predict_time_1,
                self.remain_seat_cnt_1,
                self.location_no_2,
                self.plate_no_2,
                self.predict_time_2,
                self.remain_seat_cnt_2
            )
