class Area:
    def __init__(self, w, h):
        self.type = -1  # 0:计数区,1:压线区,2:违停区,3:违规转弯区,4:逆向行驶区,5:测速区
        self.points = []  # 内部是元组，points= [(1,1),(2,)...]
        self.region = [[False] * w for i in range(h)]
        self.turn = []
        self.direction = ''  # B2T和T2B
        self.turn_boundary = []  # top, down, left, right
        self.parking_threshold_time = -1
        self.maxSpeed = -1
        self.roadLength = -1
