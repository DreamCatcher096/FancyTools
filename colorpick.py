import cv2
import os
import numpy as np

path = r"/home/alan/traindatas"
images = os.listdir(path)
result = []

ROI_img = []
for i in range(0, 3):
    ROI_img.append(np.zeros((10, 10), np.uint8))

def draw(event, x, y, flags, param):
    if event == cv2.EVENT_MOUSEMOVE:
        img_temp = img.copy()
        cv2.line(img_temp, (x, 0), (x, height), (0, 255, 0))
        cv2.line(img_temp, (0, y), (width, y), (0, 255, 0))
        cv2.imshow('label', img_temp)
        ROI = [max(x - 5, 0), max(y - 5, 0), max(x + 5, width), max(y + 5, height)]
        for i in range(0, 10):
            for j in range(0, 10):
                ROI_img[0][j][i] = img[ROI[1]+j][ROI[0]+i][0]
                ROI_img[1][j][i] = img[ROI[1]+j][ROI[0]+i][1]
                ROI_img[2][j][i] = img[ROI[1]+j][ROI[0]+i][2]

        big = cv2.merge(ROI_img)
        big = cv2.resize(big, None, fx=10, fy=10)
        cv2.circle(big, (10 * 10 / 2, 10 * 10 / 2), 1, (0, 255, 0))
        cv2.imshow('bigger', big)
    if event == cv2.EVENT_LBUTTONUP:
        print (x, y)
        print img[y][x]
    #     result.append(img[y][x])

cv2.namedWindow('label')
cv2.setMouseCallback('label', draw)
kernel = cv2.getStructuringElement(cv2.MORPH_RECT,(5, 5))
def nothing(*arg):
    pass
def update(hmax, smax, vmax, hmin, smin, vmin):
    red = cv2.inRange(img, (hmin, smin, vmin), (hmax, smax, vmax))
    cv2.imshow('red', red)

hmax = 146
smax = 215
vmax = 221
hmin = 123
smin = 93
vmin = 43

for image in images:
    img = cv2.imread(os.path.join(path, image))
    img = cv2.cvtColor(img, cv2.COLOR_RGB2HSV_FULL)
    img = cv2.resize(img, None, fx=0.6, fy=0.6)
    (width, height) = cv2.cv.GetSize(cv2.cv.fromarray(img))
    cv2.resizeWindow('label', width, height)
    cv2.imshow('label', img)
    # # channels = cv2.split(img)
    # red = cv2.inRange(img, (0, 0, 118), (130, 110, 255))
    # cv2.imshow('red', red)
    # contours0, hierarchy = cv2.findContours(red, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)(62, 59, 140)(69, 65, 147)(90, 84, 165)

    update(hmax, smax, vmax, hmin, smin, vmin)
    cv2.createTrackbar('hmax', 'red', hmax, 255, nothing)
    cv2.createTrackbar('smax', 'red', smax, 255, nothing)
    cv2.createTrackbar('vmax', 'red', vmax, 255, nothing)
    cv2.createTrackbar('hmin', 'red', hmin, 255, nothing)
    cv2.createTrackbar('smin', 'red', smin, 255, nothing)
    cv2.createTrackbar('vmin', 'red', vmin, 255, nothing)
    while True:
        hmax = cv2.getTrackbarPos('hmax', 'red')
        smax = cv2.getTrackbarPos('smax', 'red')
        vmax = cv2.getTrackbarPos('vmax', 'red')
        hmin = cv2.getTrackbarPos('hmin', 'red')
        smin = cv2.getTrackbarPos('smin', 'red')
        vmin = cv2.getTrackbarPos('vmin', 'red')
        update(hmax, smax, vmax, hmin, smin, vmin)
        if cv2.waitKey(5) == 1048675:
            break
    # morg = cv2.morphologyEx(img, cv2.MORPH_BLACKHAT, kernel)
    # gus = cv2.GaussianBlur(img, (5, 5), 0)
    # edged = cv2.Canny(gus, 75, 200)
    # cv2.imshow('canny', edged)
    key = cv2.waitKey(0)
    if key == 1048603:
        # cnt_b = 0
        # cnt_g = 0
        # cnt_r = 0
        # for i in result:
        #     cnt_b += i[0]
        #     cnt_g += i[1]
        #     cnt_r += i[2]
        # print (cnt_b / len(result), cnt_g / len(result), cnt_r / len(result))
        break
