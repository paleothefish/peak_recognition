import csv
import json
import matplotlib.pyplot as plt
import pymzml

# Read the CSV file
with open(r'D:\UCD_Fiehn_Lab\EIC_data.csv', 'r') as f:
    reader = csv.DictReader(f)
    content_column = [row['content'] for row in reader]

# Convert the 'content' column to a list of dictionaries
content_dicts = [json.loads(content) for content in content_column]

# Iterate over the dictionaries
for content_dict in content_dicts:
    # Grab the 'intensities' values
    intensities = content_dict.get('intensities', [])

    # **Remove zeros from the intensities list**
    intensities = [i for i in intensities if i != 0]

    # Generate the EICs using matplotlib
    plt.plot(intensities, linewidth=2.0, color='red')

    # Add labels to the axes
    plt.xlabel('Time')
    plt.ylabel('Abundance')

    # Add grid lines
    plt.grid(True)

    # Adjust the scale of the y-axis
    if min(intensities) != max(intensities):
        plt.ylim(min(intensities), max(intensities))

    plt.show()
