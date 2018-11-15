#########################################################################
# Date: 2018/11/07
# file name: 3st_assignment_main.py
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
        self.obstacle_detected_distance = 35

    def drive_parking(self):
        self.car.drive_parking()

    # move front as same speed of each motor
    def move_front(self, speed=100):
        self.speed = int(speed)
        self.car.accelerator.go_forward(self.speed)
    
    # move back as same speed of each motor
    def move_back(self, speed=100):
        self.speed = int(speed)
        self.car.accelerator.go_backward(self.car.FASTER)

    # stop
    def stop(self):
        self.speed = 0
        self.car.accelerator.stop()

    # get distance by accpeted error for stable distance
    def get_distance(self):
        distances = [self.car.distance_detector.get_distance() for i in range(5)]
        return sorted(distances)[2]

    def read_digit(self):
        return numpy.array(self.car.line_detector.read_digital())
    
    def turn(self, degree):
        min_degree = -35
        max_degree = 35
        degree = max(min_degree, min(max_degree, degree))
        self.car.steering.turn(90 + degree)

    def evading(self):
        turn_left_angle = -35
        turn_right_angle = 35

        self.turn(turn_left_angle)
        while numpy.sum(self.read_digit()) > 0:
            time.sleep(0.01)
        while numpy.sum(self.read_digit()) == 0:
            time.sleep(0.01)

        self.turn(turn_right_angle)
        while numpy.sum(self.read_digit()) > 0:
            time.sleep(0.01)
        while numpy.sum(self.read_digit()) == 0:
            time.sleep(0.01)

        self.turn(turn_left_angle)

    # assignment code = move front and back
    def assign(self):
        count = 0
        stop_condition = 3
        vector = numpy.array([-3, -1, 0, 1, 3])
        turning_rate = 12
        before_turning_angle = 0
        before_lines_sum = 0
        while True:
            lines = self.read_digit()
            lines_sum = numpy.sum(lines)
            if lines_sum == 5:
                count += 1
                if count >= stop_condition:
                    break
            else:
                count = 0
                if lines_sum == 0 and lines_sum != before_lines_sum:
                    self.turn(before_turning_angle)
                    self.move_back()
                    before_lines_sum = lines_sum
                    continue
                before_lines_sum = lines_sum
            if before_lines_sum == 0:
                self.move_front()

            distance = self.get_distance()
            if 0 < distance and distance < self.obstacle_detected_distance:
                self.evading()
            
            dot = numpy.dot(vector, lines)
            turning_angle = dot * turning_rate / lines_sum
            if before_turning_angle == turning_angle:
                continue
            before_turning_angle = turning_angle
            print(time.time(), turning_angle)
            self.turn(turning_angle)
            
        
        self.stop()


    # =======================================================================
    # 3RD_ASSIGNMENT_CODE
    # Complete the code to perform First Assignment
    # =======================================================================
    def car_startup(self):
        # Implement the assignment code here.
        try:
            self.assign()
        except Exception as e:
            print(e)
            self.stop()


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
