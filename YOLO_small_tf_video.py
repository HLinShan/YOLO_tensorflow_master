#coding=utf-8
import cv2
import numpy as np

# capture=cv2.VideoCapture("EP01.mp4")

# if capture.isOpened():
#     while True:
#         ret, prev = capture.read()
#         if ret==True:
#             print "readvideo"
#             cv2.imshow('video', prev)
#         else:
#             print "noread video"
#             break
#         if cv2.waitKey(20)==27:
#             break
# else:
#     print "no open"
# cv2.destroyAllWindows()


import numpy as np
import cv2

cap = cv2.VideoCapture('EP01.mp4')


while(cap.isOpened()):
    ret, frame = cap.read()

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    cv2.imshow('frame',gray)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
print "no read video "

cap.release()
cv2.destroyAllWindows()

# ! /usr/bin/env python
# coding=utf-8
import cv2
import numpy as np
import cv2.cv as cv

videoCapture = cv2.VideoCapture("E://code//test.mp4")  # 从文件读取视频
# 判断视频是否打开
if (videoCapture.isOpened()):
    print 'Open'
else:
    print 'Fail to open!'

fps = videoCapture.get(cv2.cv.CV_CAP_PROP_FPS)  # 获取原视频的帧率

size = (int(600), int(1536))  # 自定义需要截取的画面的大小
# size = (int(videoCapture.get(cv2.cv.CV_CAP_PROP_FRAME_WIDTH)),int(videoCapture.get(cv2.cv.CV_CAP_PROP_FRAME_HEIGHT)))#获取原视频帧的大小
videoWriter = cv2.VideoWriter('E://code//test2.avi', cv2.cv.CV_FOURCC('M', 'J', 'P', 'G'), fps, size)
success, frame = videoCapture.read()  # 读取第一帧

while success:
    frame = frame[0:1536, 1200:1800]  # 截取画面
    videoWriter.write(frame)  # 将截取到的画面写入“新视频”
    success, frame = videoCapture.read()  # 循环读取下一帧
videoCapture.release()