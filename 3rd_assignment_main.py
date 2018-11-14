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

    def speed_check(self, *speeds):
        for speed in speeds:
            if int(speed) not in range(0, 101):
                return False
        return True

    def move(self, *speeds):
        if not self.speed_check(*speeds):
            raise ValueError('speed ranges from 0 to 100, speeds is {}' .format(speeds))
        speedL, speedR = speeds
        self.car.accelerator.left_wheel.speed = int(speedL)
        self.car.accelerator.right_wheel.speed = int(speedR)

        self.car.accelerator.left_wheel.forward()
        self.car.accelerator.right_wheel.forward()

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
        turn_left_angle = -35
        turn_right_angle = 35

        self.turn(turn_left_angle)
        while True:
            distance = self.get_distance()
            if self.obstacle_detected_distance < distance:
                break
        self.turn(turn_right_angle)

    # assignment code = move front and back
    def assign(self):
        speed = 72
        self.move_front(speed)

        vector = numpy.array([-3, -1, 0, 1, 3])
        line_out_mul = 1.3
        angle_mul = 12

        now_dot = 0
        before_dot = 0

        count = 0
        stop_condition = 3

        before_turning_angle = -123

        while True:
            lines = self.read_digit()
            lines_sum = numpy.sum(lines)
            if lines_sum == 5:
                count += 1
                if count >= stop_condition:
                    break
            else:
                count = 0
            
            distance = self.get_distance()
            if 0 < distance and distance < self.obstacle_detected_distance:
                self.evading()
            
            if lines_sum:
                now_dot = numpy.dot(lines, vector) / lines_sum
            else:
                now_dot = before_dot * line_out_mul
            before_dot = now_dot

            turning_angle = max(min(now_dot * angle_mul, 45), -45)
            if before_turning_angle == turning_angle:
                continue
            before_turning_angle = turning_angle
            print(turning_angle)
            self.turn(turning_angle)
            
            slow_speed = max(0, speed - 2 * abs(turning_angle))
            if turning_angle < 0:
                self.move(slow_speed, speed)
            else:
                self.move(speed, slow_speed)
        
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
