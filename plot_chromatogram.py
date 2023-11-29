import json
import matplotlib.pyplot as plt
import numpy as np

# Read the CSV file
with open(r'D:\UCD_Fiehn_Lab\Untitled (1)', 'r') as f:
    # Create a json reader
    single_eic = json.load(open(r'D:\UCD_Fiehn_Lab\Untitled (1)', 'r'))

# Convert the 'content' column to a list of dictionaries
content_dicts = [single_eic]
i = 0

# Iterate over the dictionaries
for content_dict in content_dicts:
    # Grab the 'intensities' values
    intensities = content_dict.get('intensities', [])
    # Set the x min to be begin_ri and set the x max to be end_ri
    min_ri = content_dict.get('begin_ri', 0)
    max_ri = content_dict.get('end_ri', 0)

    # Create a list with the lower bound min_ri and upper bound of max_ri with len(intensities)
    retention_index = np.linspace(min_ri, max_ri, len(intensities))

    # Generate the EICs using tplotlib
    plt.plot(retention_index, intensities, linewidth=2.0, color='red')

    # Add labels to the axes
    plt.xlabel('Time [s]')
    plt.ylabel('Abundance')

    # Add grid lines
    plt.grid(True)

    # Adjust the scale of the y-axis
    if min(intensities) != max(intensities):
        plt.ylim(min(intensities), max(intensities))

    plt.xlim(min_ri, max_ri)

    i = i + 1
    title = "plot #" + str(i)
    plt.title(title)

    plt.show()
