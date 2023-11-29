import csv
import json
import matplotlib.pyplot as plt
import pymzml

# Read the CSV file
with open(r'D:\UCD_Fiehn_Lab\EIC_data.csv', 'r') as f:
    # Create a DictReader object
    reader = csv.DictReader(f)
    # Grab the 'content' column
    content_column = [row['content'] for row in reader]

# Convert the 'content' column to a list of dictionaries
content_dicts = [json.loads(content) for content in content_column]

i = 0

# Iterate over the dictionaries
for content_dict in content_dicts:
    # Grab the 'intensities' values
    intensities = content_dict.get('intensities', [])
    max_rt = 227.674286
    # Create a list with the lower bound 0 and upper bound of 227.67428588867188 with increment of 0.1
    time = [(x / len(intensities)) * max_rt for x in range(0, len(intensities))]

    # Generate the EICs using matplotlib
    plt.plot(time, intensities, linewidth=2.0, color='red')

    # Add labels to the axes
    plt.xlabel('Time [s]')
    plt.ylabel('Abundance')

    # Add grid lines
    plt.grid(True)

    # Adjust the scale of the y-axis
    if min(intensities) != max(intensities):
        plt.ylim(min(intensities), max(intensities))

    plt.xlim(0, max_rt)

    plt.ylim(0, 20E6)

    i = i + 1
    title = "plot #" + str(i)
    plt.title(title)

    plt.show()
