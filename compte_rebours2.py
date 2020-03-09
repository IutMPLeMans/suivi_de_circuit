##compte à rebours sans bouton
import time

time_left = 60
while time_left > 0:
    print('compté à rebours(s):',time_left)
    time.sleep(1)
    time_left = time_left - 1
