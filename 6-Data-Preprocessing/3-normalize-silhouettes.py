import os
import cv2 as cv

silhouettes_path = os.path.join(os.getcwd(), '3-Silhouettes')
normalize_silhouettes = os.path.join(os.getcwd(), '4-Normalize-Silhouettes')

i = 0
for person in os.listdir(silhouettes_path):
    os.mkdir(os.path.join(normalize_silhouettes, person))
    categories = os.listdir(os.path.join(silhouettes_path, person))
    for category in categories:
        os.mkdir(os.path.join(normalize_silhouettes, person, category))
        angles = os.listdir(os.path.join(silhouettes_path, person, category))
        for angle in angles:
            i += 1
            print(i, person, category, angle)
            os.mkdir(os.path.join(normalize_silhouettes, person, category, angle))
            frames = os.listdir(os.path.join(
                silhouettes_path, person, category, angle))
            for frame in frames:
                img = cv.imread(os.path.join(
                    silhouettes_path, person, category, angle, frame), 0)
                top_rows = img[:25, :]
                end_rows = img[-25:, :]
                start_cols = img[:, :10]
                last_cols = img[:, -35:]
                if 255 in img:
                    if (255 not in top_rows or 255 in img[:,10:36]) and 255 not in end_rows and 255 not in start_cols and (255 not in last_cols or 255 in img[:,11:-36]):
                        cv.imwrite(
                            f'{os.path.join(normalize_silhouettes,person,category,angle)}/{frame}', img)