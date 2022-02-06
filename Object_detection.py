import cv2
import cvzone


#for Object Detection
classNames = []
classFile = 'Resources/coco.names'
with open(classFile, 'rt') as f:
        classNames = f.read().split('\n')


configPath = 'Resources/ssd_mobilenet_v3_large_coco_2020_01_14.pbtxt'
weightPath = 'Resources/frozen_inference_graph.pb'

thres = 0.6  # for Object Detection
nmsthres = 0.3  # for Object Detection

net = cv2.dnn_DetectionModel(weightPath, configPath)
net.setInputSize(320, 320)
net.setInputScale(1.0 / 127.5)
net.setInputMean((127.5, 127.5, 127.5))
net.setInputSwapRB(True)
#### Object Detection

cap = cv2.VideoCapture(0)
cap.set(3,800)
cap.set(4,600)


def object_detection():
    while True:
        success, img = cap.read()
        classIds, confs, bbox = net.detect(img, confThreshold=thres, nmsThreshold=nmsthres)
        try:
            for classIds, conf, box in zip(classIds.flatten(), confs.flatten(), bbox):
                cvzone.cornerRect(img, box)
                cv2.putText(img, f'{classNames[classIds - 1].upper()} {round(conf * 100, 2)}',
                        (box[0] + 30, box[1] + 10), cv2.FONT_HERSHEY_COMPLEX_SMALL, 1, (0, 255, 0), 2)
        except:
            pass
        cv2.imshow("Image", img)
        cv2.waitKey(1)