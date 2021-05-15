# YOLOv3
## link: https://pjreddie.com/darknet/yolo/

### Detection Using A Pre-Trained Model
- git clone https://github.com/pjreddie/darknet
- cd darknet
- make
- wget https://pjreddie.com/media/files/yolov3.weights


### TEST DETECTOR
- ./darknet detect cfg/yolov3.cfg yolov3.weights data/dog.jpg

-_*DOG IMAGE WILL DISPLAY*_


### Real-Time Detection on a Webcam
#### Compiling With CUDA
-INSTALL Nvidia GPU and cuda first 

-After you have Nvidia and cuda open Makefile and change GPU=1

-save the Makefile and go terminal and make


#### Compiling With OpenCV
-open Makefile change openCV=1

-save the Makefile and go terminal and make

-run
- ./darknet imtest data/eagle.jpg

-image eagle will display.

#### RUN real_time detection on a webcam
- ./darknet detector demo cfg/coco.data cfg/yolov3.cfg yolov3.weights
#### RUN real_time detection on a video
- ./darknet detector demo cfg/coco.data cfg/yolov3.cfg yolov3.weights <video file>
