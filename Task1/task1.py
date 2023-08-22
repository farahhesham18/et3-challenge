# -*- coding: utf-8 -*-
"""
Created on Tue Aug 22 19:25:34 2023

@author: farah hesham
"""

# The imports used in the system 
import os 
import datetime
import csv
from PIL import Image

# defining the main 
def main():
    #change the paths according to your own paths
    
    Images_path = "F:/Et3/dairies" # the path of the images with files and subfiles
    Images_Dataset = "F:/Et3/images_dataset" # the path of the file we will save the images after extracting it 
    csv_file= "F:/Et3/report.csv" # the path of the reposrt csv will be saved in


    #cheching the image dataset file exists or not if not create it
    if not os.path.exists(Images_Dataset): 
        os.makedirs(Images_Dataset)

    image_details = [] #array contains the details of of the image 
    
    
    #for loop to path on the images in the files and sub files and save it in the image dataset file
    
    for root, _, files in os.walk(Images_path):
        for filename in files:
            if filename.lower().endswith(('.png', '.jpg', '.jpeg', '.gif', '.bmp')):
                source_file_path = os.path.join(root, filename)
                destination_file_path = os.path.join(Images_Dataset, filename)

                image = Image.open(source_file_path)
                image.save(destination_file_path)
                #get image size 
                image_size = os.path.getsize(destination_file_path)
                #get the last modification date 
                modification_time = datetime.datetime.fromtimestamp(os.path.getmtime(destination_file_path))
               #remove prefix to save it in he csv without it 
                image_name_without_prefix = filename.split('_')[-1]
                #save image details in the array 
                image_details.append([image_name_without_prefix, image_size, modification_time])

    
                
                
    # Create the CSV file and write image details
    with open(csv_file, 'w', newline='') as csvfile:
        csv_writer = csv.writer(csvfile)
        csv_writer.writerow(['Image ', 'Image Size', 'Image Modification Data'])
        csv_writer.writerows(image_details)

   

if __name__ == "__main__":
    main()







