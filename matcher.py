import cv2
import image_slicer
from matplotlib import pyplot as plt
import os
# PATH_TO_BASE_IMAGE = "images/planet.jpg"
NUMBER_OF_TILES = 30

if __name__ == '__main__':
    inp = input("If you want to use your own picture input path, else: 'N'")
    if not (inp == "N" or inp == "n"):
        path = inp
        while not os.path.isfile(path):
            path = input("Input patch to picture")
        NUMBER_OF_TILES = int(input("How many tiles do you want?"))
        tiles = image_slicer.slice(path, NUMBER_OF_TILES)
        temp_path = path
        images = [
            tile.filename
            for tile in tiles
        ]
    else:
        path = ""
        while not os.path.isdir(path):
            path = input("Input patch to folder with puzzles")
        temp_path = ""
        while not os.path.isfile(temp_path):
            temp_path = input("Path to picture")

        images = [
            path + "\\" + im
            for im in os.listdir(path)
        ]

    template = cv2.imread(temp_path, 0)
    tem = cv2.imread(temp_path, 1)

    results = []
    for index, i in enumerate(images):
        img = cv2.imread(i, 0)
        w, h = img.shape[::-1]
        method = eval('cv2.TM_CCOEFF_NORMED')

        res = cv2.matchTemplate(img, template, method)
        results.append(res)
        min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)

        top_left = max_loc
        bottom_right = (top_left[0] + w, top_left[1] + h)
        i = i.split("\\")[1]
        i = i.replace(".png", "")
        i = i.replace(".jpg", "")

        cv2.rectangle(tem, top_left, bottom_right, 255, 2)
        cv2.putText(
            tem, str(i),
            (top_left[0], top_left[1] + h - 20),
            cv2.FONT_HERSHEY_COMPLEX, 1, (255, 255, 255)
        )

    for r in results:
        plt.plot(), plt.imshow(tem)
        plt.title('Solved'), plt.xticks([]), plt.yticks([])

    plt.show()
