import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

import time
from ultralytics import YOLO


# SETTING UP PARAMETERS
# Better not to change these parameters
dataset_root = './data/client_test/'
model_path = './models/8sp2_150.pt'
outputs_root = './outputs'
experiment_name = time.strftime("%Y%m%d-%H%M%S")
# Can be changed
imgsz = 640
batch = 16
device = [4]


#  START OF EVALUATION
print("🚀...WELCOME TO EVALUATION DETECTOR MODEL...")

print("🚀...Initializing model...")
model = YOLO(model_path, task='detect')

print("🚀...INFERENCE MODE...🚀")
print("📦...GETTING PREDICTIONS...📦")
metrics = model.val(
    data= dataset_root+'data.yaml',
    imgsz=imgsz,
    batch=batch,
    device=device,
    save=True,
    save_json=True,
    plots=True,
    save_txt=False,      # Text files
    save_conf=False,     # Save confidences
    # save results to project/name relative to script directory or absolute path
    project=outputs_root,
    name=experiment_name,
)
