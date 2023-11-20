import os
import cv2 as cv

dataset_path = os.path.join(os.getcwd(), "dataset")
frames_path = os.path.join(os.getcwd(), "frames")

videos = os.listdir(dataset_path)

records = {}
for video in videos:
    person = video[0:3]
    if person not in list(records.keys()):
        records[person] = {}
        os.mkdir(os.path.join(frames_path, person))

    person_dir = os.path.join(frames_path, person)
    category = video[4:9]
    if category not in list(records[person].keys()):
        records[person][category] = []
        os.mkdir(os.path.join(frames_path, person, category))

    category_dir = os.path.join(frames_path, person, category)
    angle = video[10:13]
    if angle not in records[person][category]:
        records[person][category].append(angle)
        os.mkdir(os.path.join(frames_path, person, category, angle))

    angle_dir = os.path.join(frames_path, person, category, angle)
    capture_video = cv.VideoCapture(os.path.join(dataset_path, video))
    i = 1
    while True:
        isTrue, frame = capture_video.read()
        if not isTrue:
            print("Error: Could not read frame.")
            break
        if frame.shape[0] > 0 and frame.shape[1] > 0:
            cv.imwrite(f"{angle_dir}/{i}.jpg", frame)
            i += 1
        else:
            print("Error: Invalid frame size.")
            break
    capture_video.release()

