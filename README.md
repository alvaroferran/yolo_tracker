# YOLO tracker
An object tracker using the YOLO3 algorithm to drive a pan and tilt tracker.

This project uses 
[qqwwee's keras-yolo3 project](https://github.com/qqwweee/keras-yolo3.git) as
its base, and builds on it to send the coordinates of the detected object over
serial port to a microcontroller for tracking.


## Installation

Create a new conda environment with all the required packages. To do so type

    conda env create -f conda/environment.yml -n yolo_env

Activate this environment by typing

    conda activate yolo_env

Once the python environment is created and activated, launch the install.sh file to download and set up all the required project files.

    chmod +x install.sh
    ./install.sh


## Usage

To launch the program be sure to activate the environment you just created,
otherwise OpenCV, Keras and Tensorflow will be missing, among others.

The program uses looks for one of the 80 classes defined in the
COCO dataset, which is specified in the config.yml file.
[Here's](https://raw.githubusercontent.com/qqwweee/keras-yolo3/master/model_data/coco_classes.txt) 
the complete list of possible classes.

Other parameters include the option to show a video stream during detection
(press 'Q' to close the window and exit the program), or to save this stream
into an .mp4 video. In this last case the FPS value may need to be modified
depending on how much time the image processing takes to keep the video 
real-time.
