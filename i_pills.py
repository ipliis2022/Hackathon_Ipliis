import cv2
import RPi.GPIO as GPIO
import time
import os
import playsound as ps
import numpy as np
import matplotlib.pyplot as plt
import glob
import time
from google.cloud import vision
import pandas as pd
import io

CAM_ID1 = 0
CAM_ID2 = 1



in1 = 18    
in2 = 15
in3 = 16
led1 = 11
led2 = 12


def button():
    # Pin Setup:
    # Board pin-numbering scheme
    GPIO.setmode(GPIO.BOARD) #보이는 데로 꽂은 모드
    # set pin as an output pin with optional initial state of HIGH
    GPIO.setup(in1, GPIO.IN)
    GPIO.setup(in2, GPIO.IN)
    GPIO.setup(in3, GPIO.IN)


    prev_value = None

    print(" Press CTRL+C to exit")
    curr_value = GPIO.LOW
#안내멘트
    #ps.playsound('guide.wav')
    try:
        while True:
#버튼 선택 while 
            a=0
            value1 = GPIO.input(in1)
            value2 = GPIO.input(in2)
            value3 = GPIO.input(in3)
            if value1 == 1:
              return (int(1))

            elif value2== 1:
              return(int(2))

            elif value3 == 1:
              return(int(3))

                
    finally:
        GPIO.cleanup()

def save_img():
   CAM_ID1 = 0
   CAM_ID2 = 1
   cam1 = cv2.VideoCapture(CAM_ID1) #카메라 생성
   cam2 = cv2.VideoCapture(CAM_ID2) #카메라 생성
   GPIO.setmode(GPIO.BOARD)
   GPIO.setup(led1, GPIO.OUT)
   GPIO.setup(led2, GPIO.OUT)

   GPIO.output(led1, GPIO.HIGH)
   time.sleep(3)
   ret, image1 = cam1.read()
#crop
   image1 =image1[:,544:2016]
#resize
   image1 = cv2.resize(image1,(640, 640))
   cv2.imwrite("./yolov5/data/cv_test/img1.jpg", image1)
   GPIO.output(led1, GPIO.LOW)
 
   GPIO.output(led2, GPIO.HIGH) 
   time.sleep(3)
   ret, image2 = cam2.read()
   image2 =image2[:,544:2016]
   image2 = cv2.resize(image2,(640, 640))
   cv2.imwrite("./yolov5/data/cv_test/img2.jpg", image2)
   GPIO.output(led2, GPIO.LOW) 

   GPIO.cleanup()
   cam1.release()
   cam2.release()

# size = [2560.000000, 1472.000000] -crop-> 1472:1472 =>1:1 & 640:640 => 1:1



def gathering_symbols(loc):
  client = vision.ImageAnnotatorClient()
  result = []
  for path in loc:
    with io.open(path, 'rb') as image_file:
      content = image_file.read()
    image = vision.Image(content=content)
    response = client.text_detection(image=image)
    try:
      symbols = response.full_text_annotation.pages[0].blocks[0].paragraphs[0].words[0].symbols
      for symbol in symbols:
        result.append(symbol.text)
    except: IndexError
    
    if response.error.message:
      raise Exception(
          '{}\nFor more info on error messages, check: '
          'https://cloud.google.com/apis/design/errors'.format(response.error.message)) 
  return result

while True:
  pills_arr = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
  but= button()
  print(but)
  if but>0:
    save_img()
 
#yolov5

  os.system('python3 ./yolov5/detect.py  --weights ./yolov5/v5n_300_best.pt --data ./yolov5/data.yaml --img 320 --conf 0.5 --source ./yolov5/data/images --save-txt --save-conf')
    
    # 랭크 텍스트 경로
  print(but)
  text_file_list = glob.glob('./yolov5/runs/detect/exp/labels/*.txt') 
  print(text_file_list)
  pills_rank = []
  for j in text_file_list:
    with open( j, 'r') as f:
      data = f.readlines()[1:5]
      for i in data:
        pills_rank.append(int(i.split()[0]))
      print(pills_rank)

  print(text_file_list)
  os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = "./my_google_api_key.json"
  loc=glob.glob('./yolov5/data/images/*.jpg')    # front, back image reading
  chars = gathering_symbols(loc)
  YOLO = []
  DICT = {}
  Pills_data_sheet = pd.read_csv('./data.csv')
 
  for pill in pills_rank:
    if pill not in YOLO:
      YOLO.append(pill)

  for i in YOLO:
    count = 0
    for char in chars:
      if char in list(Pills_data_sheet['chars'][i]):
        count += 1
        score = count / len(list(Pills_data_sheet['chars'][i]))
        DICT[i] = score
  

  answer=max(DICT, key=DICT.get)
#TTS

  predic_name=Pills_data_sheet['TTS'][answer]
    # 이름과 사용법? 출력
  ps.playsound('K_TTS/'+predic_name+'_name.wav')
  ps.playsound('K_TTS/guide.wav')
  os.system('rm -rf yolov5/runs/detect/exp')

    
  but= button()
  but1=button()
  if but != but1:
    continue
    
    #효과 효능
  elif but==1:
    ps.playsound('K_TTS/'+predic_name+'_efficacy.wav')
    #복용량
  elif but==2:
    ps.playsound('K_TTS/'+predic_name+'_dosage.wav')
    #주의사항
  elif but==3:
    ps.playsound('K_TTS/'+predic_name+'_caution.wav')



