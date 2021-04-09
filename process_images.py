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
    parser.add_argument("-f", "--folder-id", type=int, default=0, help="The folder timestamp to use; defaults to the last one")

    args = parser.parse_args()
    folder_id = args.folder_id

    if folder_id == 0:
        folder_id = os.listdir("./data/imgs")[-1]

    img_files = os.listdir(f"./data/imgs/{folder_id}")
    
    folder_path = f"./data/processed_images/{folder_id}"
    if not os.path.exists(f"./data/processed_images/{folder_id}"):
        os.mkdir(folder_path)

    print("Loaded file names into memory")
    print("Processing images . . .")
    for img_file in progressbar.progressbar(img_files):
        img = cv2.imread(f"./data/imgs/{folder_id}/{img_file}")
        img = process(img)
        cv2.imwrite(f"{folder_path}/{img_file}", img)
    print("Finished")