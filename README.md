## Required Python Dependency installs: 

 * pip install opencv-python
* pip install xlrd

Weights File required for program to run: 
https://pjreddie.com/media/files/yolov3.weights

## Command to Run: 

python yolo_opencv.py --image *fruits.jpg* --config yolov3.cfg --weights yolov3.weights --classes yolov3.txt

Replace *fruits.jpg* with picture to be ran on.

Can only be jpg, png, or jpeg file extensions. 

## Returned Values: 

object-detection.jpg - original image with boxes drawn around the found objects

Outputs a csv and a JSON file with a list of the found items in the image
