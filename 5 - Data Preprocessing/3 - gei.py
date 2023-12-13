import os
import cv2 as cv
import numpy as np

silhouettes_path = os.path.join(os.getcwd(), "3 - Silhouettes")
gei_path = os.path.join(os.getcwd(), "5 - Gait Energy Images")


def mass_center(img, is_round=True):
    Y = img.mean(axis=1)
    X = img.mean(axis=0)
    Y_ = np.sum(np.arange(Y.shape[0]) * Y) / np.sum(Y)
    X_ = np.sum(np.arange(X.shape[0]) * X) / np.sum(X)
    if is_round:
        return int(round(X_)), int(round(Y_))
    return X_, Y_


def image_extract(img, newsize):
    x_s = np.where(img.mean(axis=0) != 0)[0].min()
    x_e = np.where(img.mean(axis=0) != 0)[0].max()

    y_s = np.where(img.mean(axis=1) != 0)[0].min()
    y_e = np.where(img.mean(axis=1) != 0)[0].max()

    x_c, _ = mass_center(img)
    x_s = x_c - newsize[1] // 2
    x_e = x_c + newsize[1] // 2
    img = img[
        y_s:y_e, x_s if x_s > 0 else 0: x_e if x_e < img.shape[1] else img.shape[1]
    ]
    return cv.resize(img, newsize)


i = 0
for person in os.listdir(silhouettes_path):
    os.mkdir(os.path.join(gei_path, person))
    for category in os.listdir(os.path.join(silhouettes_path, person)):
        for angle in os.listdir(os.path.join(silhouettes_path, person, category)):
            i += 1
            print(i, person, category, angle)
            angle_path = os.path.join(
                silhouettes_path, person, category, angle)
            silhouettes = os.listdir(angle_path)
            if len(silhouettes) == 0:
                break
            frames = [
                cv.imread(os.path.join(angle_path, frame), 0)
                for frame in silhouettes
            ]
            frames = [image_extract(frame, (128, 128)) for frame in frames]
            gei = np.mean(frames, axis=0).astype(np.uint8)
            cv.imwrite(
                f"{os.path.join(gei_path, person)}/{category}-{angle}.png", gei)
