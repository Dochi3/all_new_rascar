#########################################################################
# Date: 2018/10/02
# file name: 1st_assignment_main.py
# Purpose: this code has been generated for the 4 wheels drive body
# moving object to perform the project with ultra sensor
# this code is used for the student only
#########################################################################

from car import Car
import time


class myCar(object):

    def __init__(self, car_name):
        self.car = Car(car_name)

    def drive_parking(self):
        self.car.drive_parking()

    def move_front(self):
        self.car.accelerator.go_forward(self.car.FASTER)

    def move_back(self):
        self.car.accelerator.go_backward(self.car.FASTER)

    def stop(self):
        self.car.accelerator.stop()

    def get_distance(self):
        sum = 0
        for i in range(5):
            sum += self.car.distance_detector.get_distance()
        return sum / 5

    def assign(self):
        try:
            goal = 10
            start_pos = self.get_distance()

            # move front
            print("move front!")
            while True:
                if self.get_distance() < goal:
                    break
            
            # move back
            print("move back!")
            while True:
                if self.get_distance() > start_pos:
                    break
            
            # stop
            print("stop")
            self.stop()

            print()
        except Exception e:
            print("Error Occured : " + str(e))
            self.drive_parking()
        

    # =======================================================================
    # 1ST_ASSIGNMENT_CODE
    # Complete the code to perform First Assignment
    # =======================================================================
    def car_startup(self):
        # Implement the assignment code here.
        pass


if __name__ == "__main__":
    try:
        myCar = myCar("CarName")
        myCar.car_startup()
        while True:
            input()
            myCar.assign()

    except KeyboardInterrupt:
        # when the Ctrl+C key has been pressed,
        # the moving object will be stopped
        myCar.drive_parking()