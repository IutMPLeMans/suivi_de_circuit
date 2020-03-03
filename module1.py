import numpy as np
from matplotlib import pyplot as plt
import cv2 as cv
#ééàù

vid_capture = cv.VideoCapture(0)
vid_cod = cv.VideoWriter_fourcc(*'XVID')
output = cv.VideoWriter("videos/cam_video.mp4", vid_cod, 20.0, (640,480))
