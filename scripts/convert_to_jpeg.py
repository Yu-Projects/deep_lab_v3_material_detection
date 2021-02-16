# -*- coding: utf-8 -*-
"""
Created on Sat Jan 16 18:24:48 2021

@author: Eric Bianchi
"""

import os 
from tqdm import tqdm   
import cv2

source_image_dir = '/home/klyu/bridgeInspection/trainingImages/bridge4/'

for image_name in tqdm(os.listdir(source_image_dir)):
    print(image_name)
    image_path = source_image_dir + image_name
    
    
    name = os.path.splitext(image_name)[0]
    image_name = source_image_dir + name + '.jpeg'
    # Load .png image
    image = cv2.imread(image_path)
    # dsize
    # dsize = (512, 512)
    
    # resize image
    # image = cv2.resize(image, dsize)
    # Save .jpg image
    cv2.imwrite(image_name, image, [int(cv2.IMWRITE_JPEG_QUALITY), 100])
