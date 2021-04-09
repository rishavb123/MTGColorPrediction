import json
import os
import progressbar
import time
import urllib.request

if __name__ == "__main__":
    pbar = progressbar.progressbar

    with open("./data/oracle-cards.json", encoding="utf8") as f:
        data = json.load(f)

    urls = [
        (card["id"], card["image_uris"]["art_crop"])
        for card in data
        if "image_uris" in card
        and "art_crop" in card["image_uris"]
        and "legalities" in card
        and "commander" in card["legalities"]
        and card["legalities"]["commander"] == "legal"
    ]

    print("Loaded JSON into memory")
    print("Downloading images . . .")
    folder = f"./data/imgs/{int(time.time())}"
    os.mkdir(folder)
    for id, url in pbar(urls):
        urllib.request.urlretrieve(url, f"{folder}/{id}.jpg")
    print("Finished")