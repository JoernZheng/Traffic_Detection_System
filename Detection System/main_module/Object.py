class Object:
    def __init__(self):
        self.id = -1
        self.license = dict()
        self.confidence = -1
        self.type = ''
        self.coordinate = (0, 0, 0, 0)     # (x,y,w,h)
        self.lost_count = 0
        self.break_rule = []            # 1为汽车压线，2为违规停车，3为违规转弯，4为逆向行驶，5为超速行驶，允许有多项违规
        self.drawed_break_rule = []
        self.parking_start_time = 0
        self.speed_detection_start_time = 0
        self.turn_init_ratio = -1                   # 违规转弯检测的初始宽高比
        self.retrograde_detection = []              # 逆行检测过程坐标存放
        self.speeding_detection_coordinates = []    # 速度检测坐标序列
        self.in_retrograde_detection_area = False   # 在逆行检测区中
        self.in_illegal_parking_area = False        # 在违规停车检测区域中
        self.in_speeding_detection_area = False     # 在超速检测区域中
