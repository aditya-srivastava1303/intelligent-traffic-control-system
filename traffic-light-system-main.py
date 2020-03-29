import numpy as np
import cv2
import imutils as im
import time

count = 1


def change(Time):
    if Time > 5:

        return True
    else:
        return False


def inc():
    global count
    count += 1
    if count > 3:
        count = 1
    return count


# #==========start the videos==================
cap1 = cv2.VideoCapture('video3.mp4')
cap2 = cv2.VideoCapture('video3 2.mp4')
cap3 = cv2.VideoCapture('video2.mp4')
cap4 = cv2.VideoCapture('traffic.mp4')

# #============== create cascade objects========
fgbg = cv2.createBackgroundSubtractorMOG2()
car_cascade = cv2.CascadeClassifier('/Users/shreysingh/Library/Containers/com.apple.mail/Data/Library'
                                    '/Mail Downloads/271F36CC-06E1-454A-A702-247638CF2FE6/cars.xml')

# #===========start timer=========
initTime = time.time()
initialTime = initTime
print("reference time value: ", initialTime)

# #==============get continuous frames=============================
while True:

    ret1, lane1 = cap1.read()
    ret2, lane2 = cap2.read()
    ret3, lane3 = cap3.read()
    ret4, lane4 = cap4.read()

    lane1 = im.resize(lane1, 360, 240, cv2.INTER_AREA)
    lane2 = im.resize(lane2, 360, 240, cv2.INTER_AREA)
    lane3 = im.resize(lane3, 360, 240, cv2.INTER_AREA)
    lane4 = im.resize(lane4, 360, 240, cv2.INTER_AREA)

    output1 = lane1.copy()
    output2 = lane2.copy()
    output3 = lane3.copy()
    output4 = lane4.copy()

    lane1_gray = cv2.cvtColor(lane1, cv2.COLOR_BGR2GRAY)
    lane2_gray = cv2.cvtColor(lane2, cv2.COLOR_BGR2GRAY)
    lane3_gray = cv2.cvtColor(lane3, cv2.COLOR_BGR2GRAY)
    lane4_gray = cv2.cvtColor(lane4, cv2.COLOR_BGR2GRAY)

    cars_lane1 = car_cascade.detectMultiScale(lane1_gray, 1.1, 1)
    cars_lane2 = car_cascade.detectMultiScale(lane2_gray, 1.1, 1)
    cars_lane3 = car_cascade.detectMultiScale(lane3_gray, 1.1, 1)
    cars_lane4 = car_cascade.detectMultiScale(lane4_gray, 1.1, 1)
    # create list to count cars in each lane
    l1x = []
    l2x = []
    l3x = []
    l4x = []
    # draw rectangle around cars
    for (x, y, w, h) in cars_lane1:
        cv2.rectangle(output1, (x, y), (x + w, y + h), (0, 0, 255), 2)
        l1x.append(x)
    for (x, y, w, h) in cars_lane2:
        cv2.rectangle(output2, (x, y), (x + w, y + h), (0, 0, 255), 2)
        l2x.append(x)
    for (x, y, w, h) in cars_lane3:
        cv2.rectangle(output3, (x, y), (x + w, y + h), (0, 0, 255), 2)
        l3x.append(x)
    for (x, y, w, h) in cars_lane4:
        cv2.rectangle(output4, (x, y), (x + w, y + h), (0, 0, 255), 2)
        l4x.append(x)

    # ##--control flow code block---
    currentTime = time.time() - initialTime
    # print "current timer:", int(currentTime)
    if change(currentTime):

        initialTime = time.time()
        # print currentTime

        print("lane %d GO, rest stop" % (inc()))
        print("lane1:", len(l1x), "lane2:", len(l2x), "lane3:", len(l3x), "lane4:", len(l4x))
    elif not change(currentTime):
        # -----check and compare the number of cars in next lane
        if count == 1:
            if len(l2x) > len(l1x):
                dif = len(l2x) - len(l1x)
                if dif > 5:
                    initialTime = time.time()
                    # print currentTime

                    print("lane %d GO, rest stop" % (inc()))
                    print("lane1:", len(l1x), "lane2:", len(l2x), "lane3:", len(l3x), "lane4:", len(l4x))

    # to display the traffic lights
    if len(l2x) >= len(l1x) & len(l2x) >= len(l3x) & len(l2x) >= len(l4x):
        cv2.circle(output2, (330, 20), 15, (0, 0, 0), -1)
        cv2.circle(output2, (330, 50), 15, (0, 0, 0), -1)
        cv2.circle(output2, (330, 80), 15, (0, 255, 0), -1)
        cv2.circle(output1, (330, 20), 15, (0, 0, 255), -1)
        cv2.circle(output1, (330, 50), 15, (0, 0, 0), -1)
        cv2.circle(output1, (330, 80), 15, (0, 0, 0), -1)
        cv2.circle(output3, (330, 20), 15, (0, 0, 0), -1)
        cv2.circle(output3, (330, 50), 15, (0, 255, 255), -1)
        cv2.circle(output3, (330, 80), 15, (0, 0, 0), -1)
        cv2.circle(output4, (330, 20), 15, (0, 0, 255), -1)
        cv2.circle(output4, (330, 50), 15, (0, 0, 0), -1)
        cv2.circle(output4, (330, 80), 15, (0, 0, 0), -1)
        cv2.waitKey(2000)
    elif len(l3x) >= len(l1x) & len(l3x) >= len(l2x) & len(l3x) >= len(l4x):
        cv2.circle(output2, (330, 20), 15, (0, 0, 255), -1)
        cv2.circle(output2, (330, 50), 15, (0, 0, 0), -1)
        cv2.circle(output2, (330, 80), 15, (0, 0, 0), -1)
        cv2.circle(output1, (330, 20), 15, (0, 0, 255), -1)
        cv2.circle(output1, (330, 50), 15, (0, 0, 0), -1)
        cv2.circle(output1, (330, 80), 15, (0, 0, 0), -1)
        cv2.circle(output3, (330, 20), 15, (0, 0, 0), -1)
        cv2.circle(output3, (330, 50), 15, (0, 0, 0), -1)
        cv2.circle(output3, (330, 80), 15, (0, 255, 0), -1)
        cv2.circle(output4, (330, 20), 15, (0, 0, 0), -1)
        cv2.circle(output4, (330, 50), 15, (0, 255, 255), -1)
        cv2.circle(output4, (330, 80), 15, (0, 0, 0), -1)
        cv2.waitKey(2000)
    elif len(l4x) >= len(l1x) & len(l4x) >= len(l2x) & len(l4x) >= len(l3x):
        cv2.circle(output2, (330, 20), 15, (0, 0, 255), -1)
        cv2.circle(output2, (330, 50), 15, (0, 0, 0), -1)
        cv2.circle(output2, (330, 80), 15, (0, 0, 0), -1)
        cv2.circle(output1, (330, 20), 15, (0, 0, 0), -1)
        cv2.circle(output1, (330, 50), 15, (0, 255, 255), -1)
        cv2.circle(output1, (330, 80), 15, (0, 0, 0), -1)
        cv2.circle(output3, (330, 20), 15, (0, 0, 255), -1)
        cv2.circle(output3, (330, 50), 15, (0, 0, 0), -1)
        cv2.circle(output3, (330, 80), 15, (0, 0, 0), -1)
        cv2.circle(output4, (330, 20), 15, (0, 0, 0), -1)
        cv2.circle(output4, (330, 50), 15, (0, 0, 0), -1)
        cv2.circle(output4, (330, 80), 15, (0, 255, 0), -1)
        cv2.waitKey(2000)
    else:
        cv2.circle(output2, (330, 20), 15, (0, 0, 0), -1)
        cv2.circle(output2, (330, 50), 15, (0, 255, 255), -1)
        cv2.circle(output2, (330, 80), 15, (0, 0, 0), -1)
        cv2.circle(output1, (330, 20), 15, (0, 0, 0), -1)
        cv2.circle(output1, (330, 50), 15, (0, 0, 0), -1)
        cv2.circle(output1, (330, 80), 15, (0, 255, 0), -1)
        cv2.circle(output3, (330, 20), 15, (0, 0, 255), -1)
        cv2.circle(output3, (330, 50), 15, (0, 0, 0), -1)
        cv2.circle(output3, (330, 80), 15, (0, 0, 0), -1)
        cv2.circle(output4, (330, 20), 15, (0, 0, 255), -1)
        cv2.circle(output4, (330, 50), 15, (0, 0, 0), -1)
        cv2.circle(output4, (330, 80), 15, (0, 0, 0), -1)
        cv2.waitKey(2000)

    cv2.imshow("lane1", output1)
    cv2.imshow("lane2", output2)
    cv2.imshow("lane3", output3)
    cv2.imshow("lane4", output4)
    k = cv2.waitKey(30) & 0xff
    if k == 27:
        break

cap1.release()
cap2.release()
cap3.release()
cap4.release()
cv2.destroyAllWindows()
