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

    def drive_parking(self):
        self.car.drive_parking()

    def speed_check(self, *speedList):
        for speed in speedList:
            if speed not in range(0, 101):
                return False
        return True

    def move(self, *speeds):
        if not self.speed_check(speeds):
            raise ValueError('speed ranges from 0 to 100')
        speedL, speedR = speeds
        self.car.accelerator.left_wheel.speed = speedL
        self.car.accelerator.right_wheel.speed = speedR

        self.car.accelerator.left_wheel.forward()
        self.car.accelerator.right_wheel.forward()

    # move front as same speed of each motor
    def move_front(self, speed=100):
        self.speed = speed
        self.car.accelerator.go_forward(self.speed)
    
    # move back as same speed of each motor
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
        min_degree = -35
        max_degree = 35
        degree = max(min_degree, min(max_degree, degree))
        self.car.steering.turn(90 + degree)

    def evading(self):
        pass

    # assignment code = move front and back
    def assign(self):
        obstacle_detected_distance = 35

        self.turn(40)

        while True:
            pass

        """
        self.move_front()

        while True:
            lines = self.read_digit()
            lines_sum = numpy.sum(lines)
            if lines_sum == 5:
                break
            
            if self.get_distance() and self.get_distance() < obstacle_detected_distance:
                self.evading()
        
        self.stop()
        """

    # =======================================================================
    # 3RD_ASSIGNMENT_CODE
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
