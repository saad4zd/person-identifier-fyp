import os
import cv2 as cv

frames_path = os.path.join(os.getcwd(), "frames")
silhouettes_path = os.path.join(os.getcwd(), "silhouettes")

i = 0
for person in os.listdir(frames_path):
    os.mkdir(os.path.join(silhouettes_path, person))
    categories = os.listdir(os.path.join(frames_path, person))
    categories.remove("bkgrd")
    for category in categories:
        os.mkdir(os.path.join(silhouettes_path, person, category))
        angles = os.listdir(os.path.join(frames_path, person, category))
        for angle in angles:
            i += 1
            print(i, person, category, angle)
            os.mkdir(os.path.join(silhouettes_path, person, category, angle))
            frames = os.listdir(os.path.join(frames_path, person, category, angle))
            for frame in frames:
                img = cv.imread(
                    os.path.join(frames_path, person, category, angle, frame)
                )
                bkgrd = cv.imread(
                    os.path.join(frames_path, person, "bkgrd", angle, "5.png")
                )
                img_gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
                img_gray = cv.GaussianBlur(img_gray, (3, 3), 0)
                bkgrd_gray = cv.cvtColor(bkgrd, cv.COLOR_BGR2GRAY)
                bkgrd_gray = cv.GaussianBlur(bkgrd_gray, (3, 3), 0)
                isolated_person = cv.absdiff(img_gray, bkgrd_gray)
                _, binary_img = cv.threshold(
                    isolated_person, 35, 255, cv.THRESH_BINARY + cv.THRESH_OTSU
                )
                binary_img = cv.dilate(binary_img, None, iterations=2)
                cv.imwrite(
                    f"{os.path.join(silhouettes_path, person, category, angle)}/{frame}",
                    binary_img,
                )
