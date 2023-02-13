import torch
import cv2
import serial
class Serial_Port:
    def __init__(self,port,baudrate,parity,stopbits,bytesize,timeout):
        self.port = port
        self.baurate = baudrate
        self.parity = parity
        self.stopbits = stopbits
        self.bytesize = bytesize
        self.timeout = timeout
        self.ser = None
    def serial_config(self):
        self.ser = serial.Serial(port=self.port ,baudrate=self.baurate,parity=self.parity,stopbits=self.stopbits,bytesize=self.bytesize,timeout=self.timeout)
    def transmit_red_tomato(self):
        self.ser.write(str.encode('0')) 
    def transmit_green_tomato(self):
        self.ser.write(str.encode('1'))
    def recieve_data(self):
        data = self.ser.readline()
        data1 = data.decode()
        data2 = data1.rstrip()
        return data2 
class YOLO:
    def __init__(self,fontScale,font,color,thickness):
        self.fontScale = fontScale
        self.font = font
        self.color = color
        self.thickness = thickness
    def bounding_box(self,image,xmax,ymax,xmin,ymin,clas):
        org = (int(xmin),int(ymin))
        c1 = (int(xmin),int(ymin))
        label = ['Red Tomato','Green Tomato']
        u=label[int(clas)]
        cv2.rectangle(image, c1, (int(((xmax+xmin)/2)+xmax-xmin),int(((ymax+ymin)/2)+ymax-ymin)),color,4)
        image = cv2.putText(image,str(u), org, self.font, self.fontScale, self.color, self.thickness, cv2.LINE_AA)
        cv2.imshow('PubWebcam',image)
    def detect(self,yolo_model):
        cap = cv2.VideoCapture(0)
        while cap.isOpened():
            success, frame = cap.read()
            image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            result = yolo_model(image)
            for (xmin, ymin, xmax,   ymax,  confidence,  clas) in result.xyxy[0].tolist():
                self.bounding_box(image,xmax,ymax,xmin,ymin,clas)
                if cv2.waitKey(1)==ord('q'):
                    break

if __name__ == "__main__":
    fontScale = 1
    font = cv2.FONT_HERSHEY_SIMPLEX
    thickness = 1
    color = (255, 0, 0)
    yolo_model = torch.hub.load('ultralytics/yolov5', 'custom', path='best.pt')
    model=YOLO(fontScale,font,color,thickness)
    model.detect(yolo_model)
 
