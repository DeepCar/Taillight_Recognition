# Nighttime Driver Behavior Prediction 

* Introducing a novel patent based on deep learning to improve defensive driving at night and in adverse weather conditions for Ford vehicles

![image](https://github.com/DeepCar/Taillight_Recognition/assets/96300226/9f9de87d-6822-4a37-bb6f-b1cc1c960301)

# Image-to-Image Translation
* Convert day-time images to nighttime images
  
![image](https://github.com/DeepCar/Taillight_Recognition/assets/96300226/d2c80c30-e93b-4b8d-ad92-e69dcf8bdcf1)

* simulate different adverse weather models


# Single-stage Detector

This detector determines the smallest possible bounding box where the taillights and brake lights of the vehicles are located

How to run:
tarin
```
python train.py --batch-size 8 --img 640 640 --data coco.yaml --cfg cfg/yolor_p6.cfg --weights '' --device 0 --name yolor_p6 --hyp hyp.scratch.1280.yaml --epochs 300
```
test

# Dataset


* Collecting Large-scale dataset from the rear view of vehicles along with labeling Region of Interest (ROIs) of taillights and brake lights
* Supporting two types of Dash-cam ang Insta-360 Camerras
* Including four classes: a) running  b) braking c) left turn  d) right turn
* 
![image](https://github.com/DeepCar/Taillight_Recognition/assets/96300226/1cc51b41-9a7a-47ee-b6ed-c6b594467322)
