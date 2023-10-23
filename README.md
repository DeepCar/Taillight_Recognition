# Nighttime Driver Behavior Prediction 

* Introducing a novel patent based on deep learning to improve defensive driving at night and in adverse weather conditions for Ford vehicles

![image](https://github.com/DeepCar/Taillight_Recognition/assets/96300226/9f9de87d-6822-4a37-bb6f-b1cc1c960301)

# Image-to-Image Translation
* Convert day-time images to nighttime images
  
![image](https://github.com/DeepCar/Taillight_Recognition/assets/96300226/d2c80c30-e93b-4b8d-ad92-e69dcf8bdcf1)

* simulate different adverse weather models


# Single-stage Detector

Using [You Only Learn One Representation (YOLOR)](https://github.com/WongKinYiu/yolor) algorithm  to determines the smallest possible bounding box where the taillights and brake lights of the vehicles are located
``` yolor_dataset -----train
                  |
                   --- test

Before run models, unzip single-detector.rar

```
python train.py --batch-size 8 --img 640 640 --data coco.yaml --cfg cfg/yolor_p6.cfg --weights runs/train/yolor_p62/weights --device 0 --name yolor_p6 --hyp hyp.finetune.1280 --epochs 110
```

Test the detector:
```
python detect.py --source inference/example.mp4 --cfg cfg/yolor_p6.cfg --weights yolor_p6.pt --conf 0.25 --img-size 1280 --device 0
```
Change "source" value to "0" to use camera: i.e. 
```
python detect.py --source 0
```

# Dataset


* Collecting Large-scale dataset from the rear view of vehicles along with labeling Region of Interest (ROIs) of taillights and brake lights
* Supporting two types of Dash-cam ang Insta-360 Camerras
* Including four classes: a) running  b) braking c) left turn  d) right turn
* 
![image](https://github.com/DeepCar/Taillight_Recognition/assets/96300226/1cc51b41-9a7a-47ee-b6ed-c6b594467322)
