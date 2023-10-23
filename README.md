<div align="center">
  
# DeepCar Team
![ezgif com-crop](https://github.com/DeepCar/Taillight_Recognition/assets/96300226/25e0a88f-427f-4019-9876-27166256cada)

</div>


# Nighttime Driver Behavior Prediction 


* Introducing a novel patent based on deep learning to improve defensive driving at night and in adverse weather conditions for Ford vehicles

![image](https://github.com/DeepCar/Taillight_Recognition/assets/96300226/f8ec26d3-e08c-440f-9cdb-d2b26864b15d)


# Image-to-Image Translation
* Convert day-time images to nighttime images
  
![image](https://github.com/DeepCar/Taillight_Recognition/assets/96300226/814f22d8-f0a7-4928-8ff0-ab9d0c7bcea3)


* Simulate different adverse weather models

![image](https://github.com/DeepCar/Taillight_Recognition/assets/96300226/d7420b41-73ea-4c27-960b-12ee4828f98f)


# Single-stage Detector

Using [You Only Learn One Representation (YOLOR)](https://github.com/WongKinYiu/yolor) algorithm  to determines the smallest possible bounding box where the taillights and brake lights of the vehicles are located

``` yolor_dataset -----train
                  |
                   --- test
```

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
* Supporting two types of Dash-cam and Insta-360 Camerras
* Including four classes: a) running  b) braking c) left turn  d) right turn
* All model are selected from the products of [Ford Motor Company](https://www.ford.com/)

![image](https://github.com/DeepCar/Taillight_Recognition/assets/96300226/ea37ea5e-3f1c-4332-bad4-72799f289599)

