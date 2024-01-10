import json
import matplotlib.pyplot as plt
import numpy as np
import os

class EICPlotter:
    def __init__(self, dir_path, width, height):
        #Store the path directory
        self.dir_path = dir_path
        #Set the width and height of the plot
        self.width = width
        self.height = height
        #Initialize the plot counter
        self.i = 0

    def plot(self):
        #Iterate through the files in the directory
        for file_name in os.listdir(self.dir_path):
            #When file is a json file
            if file_name.endswith('.json'):
                #Open the file and load the content
                file_path = os.path.join(self.dir_path, file_name)
                with open(file_path, 'r') as f:
                    content_dict = json.load(f)

                #Get the retention index and intensities from the json file
                intensities = content_dict.get('intensities', [])
                min_ri = content_dict.get('begin_ri', 0)
                max_ri = content_dict.get('end_ri', 0)
                #Create an array of retention indexes
                retention_index = np.linspace(min_ri, max_ri, len(intensities))

                #Create a plot
                fig, ax = plt.subplots(figsize=(1.28, 1.28))
                #fig, ax = plt.subplots(figsize=(self.width, self.height))
                #Plot the retention index and intensities
                ax.plot(retention_index, intensities, linewidth=2.0, color='black')
                ax.axis('off')

                #Set the y-axis limit to the min and max intensities
                if min(intensities) != max(intensities):
                    plt.ylim(min(intensities), max(intensities))

                #Set the x-axis limit to the min and max retention indexes
                plt.xlim(min_ri, max_ri)

                #Adjust the plot
                plt.subplots_adjust(left=0, right=1, top=1, bottom=0)

                #Keep track of the number of plots
                self.i += 1

                #Shrink the plot to fit the figure
                plt.tight_layout()

                # Calculate the dpi for the desired resolution
                dpi = 128 / min(self.width, self.height)

                # Save the figure with the calculated dpi
                plt.savefig('plot_{}.png'.format(self.i), dpi=dpi)

                #Show the plot
                plt.show()


# Usage of the EICPlotter class
dir_path = r'D:\UCD_Fiehn_Lab\peaks_from_LCB'
#Create an instance of the EICPlotter class
plotter = EICPlotter(dir_path, 1, 1)
#Call the plot method
plotter.plot()
