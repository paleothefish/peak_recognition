import os
import shutil
from PIL import Image
import matplotlib.pyplot as plt

# Define the directories
src_dir = r"D:\UCD_Fiehn_Lab\EIC_output_plots"
good_dir = r"D:\UCD_Fiehn_Lab\EIC_output_plots\good"
bad_dir = r"D:\UCD_Fiehn_Lab\EIC_output_plots\bad"
unsure_dir = r"D:\UCD_Fiehn_Lab\EIC_output_plots\unsure"

# Create the directories if they don't exist
os.makedirs(good_dir, exist_ok=True)
os.makedirs(bad_dir, exist_ok=True)
os.makedirs(unsure_dir, exist_ok=True)

# Loop through each file in the source directory
for filename in os.listdir(src_dir):
    if filename.endswith(".png"):
        # Open the image file
        img = Image.open(os.path.join(src_dir, filename))
        # Display the image
        plt.imshow(img)
        plt.show()
        # Prompt the user to categorize the image
        category = input("Is this image 'good', 'bad', or 'unsure'? ")
        # Move the image to the appropriate directory
        if category.lower() == "good":
            shutil.move(os.path.join(src_dir, filename), os.path.join(good_dir, filename))
        elif category.lower() == "bad":
            shutil.move(os.path.join(src_dir, filename), os.path.join(bad_dir, filename))
        elif category.lower() == "unsure":
            shutil.move(os.path.join(src_dir, filename), os.path.join(unsure_dir, filename))
