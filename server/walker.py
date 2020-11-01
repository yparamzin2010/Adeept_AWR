# This program makes AWR turn left in case of obstacle ahead

import ultra
import move
import time

DIRECTION_FORWARD = 'forward'
TURN_LEFT='left'
DIRECTION_NO = 'no'
TURN_NO = 'no'

speed_set = 40
rot_speed = 80
rad = 0.0


def move_forward():
    move.move(speed_set, DIRECTION_FORWARD, TURN_NO, rad)


def turn_left():
    # move.move(speed_set, DIRECTION_FORWARD, TURN_LEFT, rad)
    move.motor_left(1, 0, rot_speed)
    move.motor_right(1, 0, rot_speed)

sleep_done = 0
move.setup()
while 1:
    # Measure distance
    distance = ultra.checkdist()
    print("distance="+str(distance))

    if distance >= 0.7:
        sleep_done = 0
        # if there is a way, go
        move_forward()
    else:
        # if there is no way, turn
        if sleep_done == 0:
            move.motorStop()
            time.sleep(1)
            sleep_done = 1
        turn_left()

    time.sleep(0.1)
