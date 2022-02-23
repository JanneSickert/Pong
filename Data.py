class Data:
    def __init__(self):
        self.court = []
        self.x = 1200
        self.y = 750
        self.filed_size = 25
        for i in range(self.x / self.filed_size):
            self.court.append([])
            for k in range(self.y / self.filed_size):
                self.court[i].append(False)