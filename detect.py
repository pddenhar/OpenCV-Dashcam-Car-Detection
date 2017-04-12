#!/usr/bin/env python

# Python 2/3 compatibility
from __future__ import print_function

import numpy as np
import cv2


if __name__ == '__main__':
    import sys, getopt
    print(__doc__)

    args, video_src = getopt.getopt(sys.argv[1:], '', ['cascade='])
    try:
        video_src = video_src[0]
    except:
        print("No video source supplied.")
        exit()
    args = dict(args)
    cascade_fn = args.get('--cascade', "cascade_dir/cascade.xml")

    car_cascade = cv2.CascadeClassifier(cascade_fn)
    cap = cv2.VideoCapture(video_src)

    paused = False
    step = True

    while True:
        if not paused or step:
            flag, img = cap.read()
            if img == None: break

            height, width, c = img.shape
            gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            cars = car_cascade.detectMultiScale(gray, 1.2, 5)

            for (x,y,w,h) in cars:
                cv2.rectangle(img,(x,y),(x+w,y+h),(0,0,255),2) 

            cv2.imshow('edge', img)

        step = False
        ch = cv2.waitKey(5)
        if ch == 13:
            step = True
        if ch == 32:
            paused = not paused
        if ch == 27:
            break
    cv2.destroyAllWindows()