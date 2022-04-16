from panel import Panels


class Level:

    def __init__(self):
        self.panel_list = []
        self.x_start = -363
        self.y_start = 280

    def load_panels(self, level):
        panel_count = 0
        first_row = self.x_start
        second_row = self.x_start
        third_row = self.x_start
        fourth_row = self.x_start
        if level == 1:
            for i in range(21):
                if i < 10:
                    panel = Panels(xcor=first_row, ycor=self.y_start)
                    self.panel_list.append(panel)
                    panel_count += 1
                    first_row += 80
                if i > 10:
                    panel = Panels(xcor=second_row, ycor=240)
                    self.panel_list.append(panel)
                    panel_count += 1
                    second_row += 80
        if level == 2:
            for i in range(32):
                if i < 10:
                    panel = Panels(xcor=first_row, ycor=self.y_start)
                    self.panel_list.append(panel)
                    panel_count += 1
                    first_row += 80
                if 10 < i < 21:
                    panel = Panels(xcor=second_row, ycor=240)
                    self.panel_list.append(panel)
                    panel_count += 1
                    second_row += 80
                if i > 21:
                    panel = Panels(xcor=third_row, ycor=200)
                    self.panel_list.append(panel)
                    panel_count += 1
                    third_row += 80
        if level == 3:
            for i in range(42):
                if i < 10:
                    panel = Panels(xcor=first_row, ycor=self.y_start)
                    self.panel_list.append(panel)
                    panel_count += 1
                    first_row += 80
                if 10 < i < 21:
                    panel = Panels(xcor=second_row, ycor=240)
                    self.panel_list.append(panel)
                    panel_count += 1
                    second_row += 80
                if 21 < i < 32:
                    panel = Panels(xcor=third_row, ycor=200)
                    self.panel_list.append(panel)
                    panel_count += 1
                    third_row += 80
                if i > 31:
                    panel = Panels(xcor=fourth_row, ycor=160)
                    self.panel_list.append(panel)
                    panel_count += 1
                    fourth_row += 80
