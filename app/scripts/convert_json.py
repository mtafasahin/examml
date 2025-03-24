import json
import os
from PIL import Image
from collections import defaultdict

INPUT_JSON = "/app/dataset/annotations/labels.json"
IMAGES_PATH = "/workspaces/examml/app/dataset/images"
OUTPUT_PATH = "/workspaces/examml/app/dataset/labels"

def convert_to_yolo_format(x, y, w, h, img_width, img_height):
    x_center = (x + w / 2) / img_width
    y_center = (y + h / 2) / img_height
    width = w / img_width
    height = h / img_height
    return x_center, y_center, width, height

def convert_json_to_yolo():
    with open(INPUT_JSON, "r") as f:
        data = json.load(f)

    image_annotations = defaultdict(list)

    # Resim bazında annotation'ları grupla
    for item in data["testInstanceQuestions"]:
        question = item["question"]
        image_file = os.path.basename(question["imageUrl"])
        image_annotations[image_file].append(question)

    for image_file, annotations in image_annotations.items():
        image_path = os.path.join(IMAGES_PATH, image_file)

        if not os.path.exists(image_path):
            print(f"Resim bulunamadı: {image_path}")
            continue

        with Image.open(image_path) as img:
            img_width, img_height = img.size

        label_file = os.path.splitext(image_file)[0] + ".txt"
        label_path = os.path.join(OUTPUT_PATH, label_file)

        with open(label_path, "w") as f_out:
            for ann in annotations:
                x, y, w, h = ann["x"], ann["y"], ann["width"], ann["height"]
                x_center, y_center, width, height = convert_to_yolo_format(
                    x, y, w, h, img_width, img_height
                )
                f_out.write(f"0 {x_center} {y_center} {width} {height}\n")

if __name__ == "__main__":
    convert_json_to_yolo()
