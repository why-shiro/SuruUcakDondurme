import math


class Triangle:
    def __init__(self, layer, distance):
        global dummy_y, dummy_x
        self.layer = layer
        self.distance = distance
        self.height = (self.layer * self.distance * math.sqrt(3)) / 2

        self.x_arr = []
        self.y_arr = []
        self.infill = []

        print(f'Layer Size: {self.layer}')

        if layer == 0:
            return
        elif layer == 1:
            self.x_arr = [0.0, self.distance, self.distance / 2]
            self.y_arr = [0.0, 0.0, self.height]
        elif layer > 1:
            uav_count = (layer * (layer + 1)) / 2
            for x in range((2 * layer) + 1):
                self.x_arr.append(distance * x / 2)

            for y in range(layer + 1):
                self.y_arr.append((y * distance * math.sqrt(3)) / 2)

            dummy_x = self.x_arr.copy()

            y_adj = -2
            for adjust_y in range(layer):
                self.y_arr.append(self.y_arr[y_adj])
                y_adj = y_adj - 2

            dummy_y = self.y_arr.copy()

            for t in range(layer):
                self.x_arr.append(self.x_arr[-1] - distance)
                self.y_arr.append(0.0)

            stage = 1
            for o in range(layer-2,0,-1):
                for ot in range(1,o+1):
                    self.x_arr.append(dummy_x[stage+ot*2])
                    self.y_arr.append(dummy_y[stage])
                stage = stage + 1

        self.gx= sum(self.x_arr) / len(self.x_arr)
        self.gy = sum(self.y_arr) / len(self.y_arr)

