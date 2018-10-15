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
        self.speed = 100

    def drive_parking(self):
        self.car.drive_parking()

    # move front
    def move_front(self):
        self.car.accelerator.go_forward(self.car.FASTER)
    
    # move back
    def move_back(self):
        self.car.accelerator.go_backward(self.car.FASTER)

    # stop
    def stop(self):
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

    # assignment code = move front and back
    def assign(self):
        try:
            goal = 20
            start_pos = self.get_distance() - 10

            # move front
            print("move front!")
            self.move_front()
            while True:
                # if myCar reach goal
                if self.get_distance() < goal:
                    break

            time.sleep(0.2)
            
            # move back
            print("move back!")
            self.move_back()
            while True:
                # if myCar reach start position
                if self.get_distance() > start_pos:
                    break
            
            # stop
            print("stop")
            self.stop()

            print()
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
            input()
            myCar.car_startup()

    except KeyboardInterrupt:
        # when the Ctrl+C key has been pressed,
        # the moving object will be stopped
        myCar.drive_parking()
