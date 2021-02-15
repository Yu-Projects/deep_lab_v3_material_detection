# -*- coding: utf-8 -*-
"""
Created on Fri Dec 11 13:48:39 2020

@author: Eric Bianchi
"""

# import roslib
import os
from show_results__ import*
from tqdm import tqdm
import torch
import rospy


# Load the trained model, you could possibly change the device from cpu to gpu if
# you have your gpu configured.
model = torch.load("../../../../saved_models/var10_weights_ep18.pt", map_location=torch.device('cpu'))

# Set the model to evaluate mode
model.eval()

source_image_dir = '../bridge_images/'
destination_mask = '../predicted_masks/'
destination_overlays = '../combined_overlays/'
print("Kevin was here")
for image_name in tqdm(os.listdir(source_image_dir)):
    print(image_name)
    image_path = source_image_dir + image_name
    generate_images(model, image_path, image_name, destination_mask, destination_overlays)

