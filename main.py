from PIL import Image
import os
import subprocess
import pillow_heif

pillow_heif.register_heif_opener()
# set input and output paths
input_folder = "./heics/"
output_folder = "./jpegs/"

# create output folder if it doesn't exist
if not os.path.exists(output_folder):
    print('Output folder not found, creating folder...')
    os.makedirs(output_folder)
    
# print(os.listdir(input_folder))
if not os.path.exists(input_folder):
    print('Input folder not found, please check the path.')
else:
    # get all heic files in input folder
    heic_files = [f for f in os.listdir(input_folder) if f.casefold().endswith(".heic")]
    # print(heic_files)
    # loop through each HEIC file and convert to JPEG
    for heic_file in heic_files:
        
        heif_file = pillow_heif.open_heif(os.path.join(input_folder, heic_file),convert_hdr_to_8bit=False, bgr_mode=True)
        im = Image.open(input_folder + heic_file)
        im.save(output_folder + os.path.splitext(heic_file)[0] + ".jpg")
        
        
