import json
import os
import progressbar
import cv2
import numpy as np

def load_data(stamp=0):

    if stamp == 0:
        stamp = os.listdir("./data/processed_images")[-1]

    pbar = progressbar.progressbar

    with open("./data/oracle-cards.json", encoding="utf8") as f:
        data = json.load(f)

    card_data = [
        (card["id"], set(card["color_identity"]))
        for card in data
        if "image_uris" in card
        and "art_crop" in card["image_uris"]
        and "legalities" in card
        and "commander" in card["legalities"]
        and card["legalities"]["commander"] == "legal"
    ]

    X = []
    Y = []

    for card in pbar(card_data):
        card_id, colors = card
        X.append(cv2.imread(f"./data/processed_images/{stamp}/{card_id}.jpg"))
        Y.append([
            int('W' in colors),
            int('U' in colors),
            int('B' in colors),
            int('R' in colors),
            int('G' in colors),
        ])

    return np.array(X, dtype=np.float32), np.array(Y, dtype=np.float32)
