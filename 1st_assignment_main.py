#########################################################################
# Date: 2018/10/02
# file name: 1st_assignment_main.py
# Purpose: this code has been generated for the 4 wheels drive body
# moving object to perform the project with ultra sensor
# this code is used for the student only
#########################################################################

from car import Car
import time
import numpy


class myCar(object):

    def __init__(self, car_name):
        self.car = Car(car_name)
        self.speed = 0

    def drive_parking(self):
        self.car.drive_parking()

    # move front
    def move_front(self, speed=100):
        self.speed = speed
        self.car.accelerator.go_forward(self.speed)
    
    # move back
    def move_back(self, speed=100):
        self.speed = speed
        self.car.accelerator.go_backward(self.car.FASTER)

    # stop
    def stop(self):
        self.speed = 0
        self.car.accelerator.stop()

    # get distance by accpeted error for stable distance
    def get_distance(self):
        count = 0
        accpeted_error = 3
        before = self.car.distance_detector.get_distance()
        while count < 5:
            distance = self.car.distance_detector.get_distance()
            # if changed distance is acceptable
            if abs(distance - before) < accpeted_error:
                return distance
            count += 1
            before = distance
        # distance error
        return -1

    def read_digit(self):
        return numpy.array(self.car.line_detector.read_digital())
    
    def turn(self, degree):
        min_degree = -25
        max_degree = 25
        degree = max(min_degree, min(max_degree, degree))
        self.car.steering.turn(90 + degree)

    # assignment code = move front and back
    def assign(self):
        try:
            rate = 0.05
            before_s = 0
            multi_rate = numpy.array([(i + 1) / 5 for i in range(5)])
            weight = numpy.array([-5, -2, 0, 2, 5])
            past_degree = [0, 0, 0, 0]
            self.move_front()
            start = time.time()
            end = start + 3.5
            while True:
                line = self.read_digit()
                now_time = time.time()
                if 0 < end - now_time < 0.5:
                    self.move_front(int(100 * (end - now_time)))
                if numpy.sum(line) == 5:
                    break
                dot = numpy.dot(weight, line)
                s = dot * (1 + rate * line[2])
                past_degree.append((s - before_s) * (-1 if s == 0 else 1))
                degree = numpy.dot(multi_rate, past_degree)
                self.turn(degree)
                defore_s = s
                past_degree = past_degree[1:]
            self.stop()

        except Exception as e:
            print("Error Occured : " + str(e))
            self.stop()

    # =======================================================================
    # 1ST_ASSIGNMENT_CODE
    # Complete the code to perform First Assignment
    # =======================================================================
    def car_startup(self):
        # Implement the assignment code here.
        self.assign()


if __name__ == "__main__":
    try:
        myCar = myCar("CarName")
        while True:
            input("Press Enter to Start")
            myCar.car_startup()

    except KeyboardInterrupt:
        # when the Ctrl+C key has been pressed,
        # the moving object will be stopped
        myCar.drive_parking()
