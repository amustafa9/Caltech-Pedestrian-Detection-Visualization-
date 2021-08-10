# Caltech-Pedestrian-Detection-Visualization-
Repository Contains codes to visualize Caltech Pedestrian Detection Dataset with bounding box annotations.



### Package Requirements
1.numpy==1.16.5
2.matplotlib==3.1.1
3.json==2.0.9

### Instructions
Download caltech dataset files [here](http://www.vision.caltech.edu/Image_Datasets/CaltechPedestrians/). You may download all or either of the video sets. Regardless of however many
data subsets you download, make sure you also download the annotations and set up the data directory structure as follows:

```
+-- Data
|   +-- set00.rar
|   +-- set01.rar
|   ...
|   +-- annotations.zip
```

Clone the repository, cd into it, and run the converter program to convert .seq and .vbb files from the original dataset into .jpg and .JSON files respectively. Specifically, 
run the following set of commands (in the given order):

```
git clone https://github.com/amustafa9/Caltech-Pedestrian-Detection-Visualization-.git

cd <path\into\repository>

python converter.py -data_path <path\to\Data> 
```


This should change the original Data directory structure as follows:

```
+-- Data
|   +-- set00.rar
|   +-- set01.rar
|   ...
|   +-- annotations.zip
|   +-- extracted_data
    |   +-- set00
    |   |   +-- V000
            |   +-- annotations
                |   +--I00000.JSON
                |   +--I00001.JSON
                |   ...
            |   +-- images
                |   +-- I00000.jpg
                |   +-- I00001.jpg
                |   ...
        |   +-- V001
        |   ...
    |   +-- set01
    |   ... 
```

Then finally run the following to run the script to visualize the video files along with the pedestrian bounding box annotations:

```
python visualize.m
```

### Disclaimer
The codes are provided as is with no guarantees of maintenance/updates and the author bears no responsibility whatsoever in case of any malfunction. 
