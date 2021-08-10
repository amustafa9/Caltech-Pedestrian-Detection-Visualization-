
%matplotlib qt

#%%
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib.patches import Rectangle
import glob
import json


def drawBoundingBox(ax, boxes):
    "function returns rectangular patch for each pedestrian instance in a given image"
    
    num_boxes = len(boxes)
    for box_id in range(num_boxes):
        ped_data = boxes[box_id]
        bbox = np.array(ped_data['pos']).astype(int)
        rect = Rectangle((bbox[0], bbox[1]), width=bbox[2], height=bbox[3], linewidth=1, edgecolor='r', facecolor='none')
        patch = ax.add_patch(rect)
    
    return ax, patch


fig = plt.figure()

img_root = 'C:/Users/ahmad/OneDrive/Desktop/set00/extracted_data/set00/V009/images/'
label_root = 'C:/Users/ahmad/OneDrive/Desktop/set00/extracted_data/set00/V009/annotations/'

# ims is a list of lists, each row is a list of artists to draw in the
# current frame; here we are just animating one artist, the image, in
# each frame
ims = []
for img_name, label_name in zip(glob.glob(img_root+'*.jpg'), glob.glob(label_root+'*.JSON')):
    
    # open and load image
    img = plt.imread(img_name)
    
    # open and load JSON label file
    label_file = open(label_name)
    data = json.load(label_file)
    
    
    
    # show image
    ax = plt.gca() 
    im = ax.imshow(img, animated=True)
    
    # draw bboxes on current axes
    ax, patch = drawBoundingBox(ax, data) 
    
    ims.append([im, patch])

ani = animation.ArtistAnimation(fig, ims, interval=10, blit=True,
                                repeat_delay=1000)

#ani.save('C:/Users/ahmad/OneDrive/Desktop/caltech_annotated_images.mp4')
plt.show()