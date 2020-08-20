# -*- encoding: utf-8 -*-
import argparse
import base64
import os
import threading
import time
from io import BytesIO

import cv2
import numpy as np
from PIL import Image
from scipy.signal import argrelextrema

import sjh_opencv.crop as crop

class Frame:
    def __init__(self, id, diff_sum_mean):
        self.id = id
        self.diff_sum_mean = diff_sum_mean


def create_dirs(files, destination):
    os.chdir(destination)
    for file in files:
        if not os.path.isdir(file):
            os.mkdir(file)


# 获得视频非黑边大小
def frame_cut(frame):
    BR = crop.BorderRm()
    img = Image.fromarray(frame)
    imgByteArr = BytesIO()
    img.save(imgByteArr, format='PNG')
    imgByteArr = imgByteArr.getvalue()

    image = base64.b64encode(BytesIO(imgByteArr).read())
    print(BR.remove_border_imgs([image]))
    x1, y1, x2, y2 = BR.remove_border_imgs([image])
    return x1, y1, x2, y2


def video_split(root, file, destination):
    despath = os.path.join(destination, file)
    filepath = os.path.join(root, file)
    video = cv2.VideoCapture(filepath)
    cnt = 0
    rval, frame = video.read()
    prev_frame = None
    frame_diffs = []
    frames = []
    keyframe_id_set = set()
    x1, y1, x2, y2 = 0, 0, frame.shape[0], frame.shape[1]
    if rval:
        x1, y1, x2, y2 = frame_cut(frame)
    print(x1, x2, y1, y2)
    while rval:
        frame = frame[y1:y2, x1:x2, :]  # 去黑边
        luv = cv2.cvtColor(frame, cv2.COLOR_BGR2LUV)
        curr_frame = luv
        if curr_frame is not None and prev_frame is not None:
            diff = cv2.absdiff(curr_frame, prev_frame)
            diff_sum = np.sum(diff)
            diff_sum_mean = diff_sum / (
                    diff.shape[0] * diff.shape[1])
            frame_diffs.append(diff_sum_mean)
            frame = Frame(cnt, diff_sum_mean)
            frames.append(frame)
        prev_frame = curr_frame
        cnt += 1
        rval, frame = video.read()
    video.release()
    diff_array = np.array(frame_diffs)
    frame_indexes = np.asarray(argrelextrema(diff_array, np.greater))[0]
    for i in frame_indexes:
        keyframe_id_set.add(frames[i - 1].id)

    cap = cv2.cv2.VideoCapture(filepath)
    rval, frame = cap.read()
    num = 0
    while rval:
        if num in keyframe_id_set:
            cv2.imwrite(despath + "/{:04d}.jpg".format(num), frame)
            keyframe_id_set.remove(num)
        num += 1
        rval, frame = cap.read()
    cap.release()


def main():
    parser = argparse.ArgumentParser(
        description="split videos from origin to frames in destination")
    parser.add_argument("-o", '--origin', required=True)
    parser.add_argument('-d', '--destination', required=True)
    args = parser.parse_args()
    origin = args.origin
    destination = args.destination
    time_start = time.time()
    progress = []
    for root, _, videos in os.walk(origin):
        create_dirs(videos, destination)
        for video in videos:
            progress.append(threading.Thread(target=video_split,
                                             args=[root, video, destination, ]))
    for p in progress:
        p.start()
        p.join()
    print('totally cost: ', time.time() - time_start)


if __name__ == '__main__':
    main()
