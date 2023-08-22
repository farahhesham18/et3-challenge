# -*- coding: utf-8 -*-
"""
Created on Tue Aug 22 20:21:25 2023

@author: farah hesham
"""
#implementing the imports needed 
import os
import json

#function for converting the .txt file to .json file 
def process_system_output(txt_filepath):
    #what will be inside the json file
    json_data = {
        #fisrt line in the json 
        "annotations": [
            {
                #the body of the json file 
                "result": []
            }
        ],
        #  final line in the json line carrying the path of the txtfile that will be input 
        # and naming the file .jpg as it is image.txt
        "data": {
            "image": f"{os.path.splitext(os.path.basename(txt_filepath))[0]}.jpg"
        }
    }
    # now open the txt file and read its components 
    with open(txt_filepath, 'r') as txt_file:
        #read each line 
        lines = txt_file.readlines()
        #for each line split it 
        for line in lines:
            values = line.strip().split()

            json_object = {
                "image_rotation": int(values[0]), #firs part of the line contains the rotation
                "value": { #for the images values 
                    "X": float(values[1]), # X carrying x
                    "Y": float(values[2]), #Y carrying y 
                    "width": float(values[3]), # carrying width 
                    "height": float(values[4]), #carrying height 
                    "rotation": int(values[0]), #carrying rotation 
                    "rectanglelabels": ["object"] 
                }
            }
            #fill the json files with each line on the same format 
            json_data["annotations"][0]["result"].append(json_object)

    return json_data

def main():
    #put your actual path
    txt_filepath = "F:/Et3/Image1.txt" #path of the file .txt 
    
    json_output_filepath = "F:/Et3/Image1.json"  #path of the .json

    json_data = process_system_output(txt_filepath)
    #create the json file if it is not existing 
    with open(json_output_filepath, 'w') as json_file:
        json.dump(json_data, json_file, indent=4)

if __name__ == "__main__":
    main()

