import argparse
import cv2
import os
import progressbar

def process(img):
    img = cv2.resize(img, (312, 228))
    return img

if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        description="Process the cmd arguments to the script"
    )
    parser.add_argument("-f", "--folder-id", type=int, default=0, help="The folder timestamp to use")

    args = parser.parse_args()
    folder_id = args.folder_id

    if folder_id == 0:
        folder_id = os.listdir("./data/imgs")[-1]

    img_files = os.listdir(f"./data/imgs/{folder_id}")
    os.mkdir(f"./data/processed_images/{folder_id}")

    print("Loaded file names into memory")
    print("Processing images . . .")
    for img_file in progressbar.progressbar(img_files):
        img = process(cv2.imread(img_file))
    print("Finished")