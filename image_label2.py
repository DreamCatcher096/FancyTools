# coding:utf-8
import cv2
import os
import time
import random

class_name = {12: '鼻梁'}  # 1: '左眉毛上', 2: '左眉毛下', 3: '左眼皮上', 4: '右眉毛上',
# 5: '右眉毛下', 6: '右眼皮上', 7: '上嘴唇上', 8: '上嘴唇下'}
path = r"E:\label\img_68_all\img_68_all"
txt_path = r"E:\label\image_names2.txt"
save_path = r"E:\label\results2"
nums = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
image_names = []
# colors = [(0, 255, 255), (255, 0, 255), (255, 255, 0),
#           (0, 0, 255), (0, 255, 0), (255, 0, 0),
#           (255, 255, 255), (0, 0, 0)]

with open(txt_path, 'rb') as txt:
    names = txt.read().split('\r\n')
for name in names:
    image_names.append(os.path.join(path, name))


def draw(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONUP:
        points.append((x, y, 12))


cv2.namedWindow('label')
cv2.setMouseCallback('label', draw)
count = 0
prog = 0

if os.path.exists(os.path.join(save_path, 'progress.txt')):
    with open(os.path.join(save_path, 'progress.txt'), 'rb') as pr:
        prog = pr.read()
prog = int(prog)

elasp_time = 0
total_time = 0
avg_time = 0
hour = 0
minu = 0
sec = 0
last = 0

for image in image_names:
    count += 1
    if count <= prog:
        continue
    print "%s/%s  %s%%" % (count, len(image_names), count * 100 / len(image_names))
    print "Elasped_time: %s:%s:%s" % (hour, minu, sec)
    print "Speed: %s second/img" % int(avg_time)
    print "%s" % last
    points = []
    img = cv2.imread(image)
    img = cv2.resize(img, None, fx=0.6, fy=0.6)
    cv2.imshow('label', img)
    classes = 0
    time1 = time.time()
    # for cl in range(1, 9):
    print class_name[12]
    while True:
        gmi = img.copy()
        for p in points:
            cv2.circle(gmi, (p[0], p[1]), 2, (0, 255, 0), -1)
        cv2.imshow('label', gmi)
        key = cv2.waitKey(5)
        if key == 120:
            break
        if key == 100:
            points.pop()
    print 'finished?'
    while True:
        if cv2.waitKey(0) == 99:
            break
    last = time.time() - time1
    total_time += last
    avg_time = total_time / (count - prog)
    elasp_time = (len(image_names) - count) * avg_time
    sec = int(elasp_time % 60)
    minu = int(elasp_time / 60 % 60)
    hour = int(elasp_time / 60 / 60)
    name = str(count)
    name = name.zfill(4)
    name = 'zhangsiqi' + name + '.txt'
    with open(os.path.join(save_path, name), 'wb') as res:
        res.write("%s\r\n" % image)
        for i in points:
            ix = str(i[0] / 0.6)
            iy = str(i[1] / 0.6)
            ix = ix.split('.')[0] + '.'
            iy = iy.split('.')[0] + '.'
            for co in range(0, 13):
                ix += random.choice(nums)
                iy += random.choice(nums)
            line = ix + ' ' + iy + ' ' + str(i[2])
            res.write("%s\r\n" % line)
    with open(os.path.join(save_path, 'progress.txt'), 'wb') as pro:
        pro.write("%s" % str(count))
