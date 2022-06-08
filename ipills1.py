
import RPi.GPIO as GPIO
import time
import os
import playsound as ps
import numpy as np
import matplotlib.pyplot as plt
import glob
import time

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

    print("Starting demo now! Press CTRL+C to exit")
    curr_value = GPIO.LOW
#안내멘트
    #ps.playsound('guide.wav')
    try:
        while True:
#버튼 선택 while 
            value1 = GPIO.input(in1)
            value2 = GPIO.input(in2)
            value3 = GPIO.input(in3)
            if value1 == 1:
              return int(1)
            elif value2 == 1:
              return int(2)
            elif value3 == 1:
              return int(3)
                
    finally:
        GPIO.cleanup()

def save_img():

  GPIO.setmode(GPIO.BOARD)
  #setup
  GPIO.setup(led1, GPIO.OUT)
  GPIO.setup(led2, GPIO.OUT)
  #cam1 = cv2.VideoCapture(0)
  #cam2 = cv2.VideoCapture(1)

  #1번 cam&조명 
  #...
  GPIO.output(led1, GPIO.HIGH)
  time.sleep(3)
  #ret, frame = cam1.read()
  #cv2.imwrite('data/image/img1', frame)
  GPIO.output(led1, GPIO.LOW)
  #2번
  GPIO.output(led2, GPIO.HIGH) 
  time.sleep(3)
  #ret, frame = cam2.read()
  #cv2.imwrite('data/image/img2', frame)
  GPIO.output(led2, GPIO.LOW)
  GPIO.cleanup()


# 글자 단위로 읽은 결과들 리스트화

def gathering_chars(path):
    client = vision.ImageAnnotatorClient()

    with io.open(path, 'rb') as image_file:
        content = image_file.read()
        
    image = vision.Image(content=content)

    response = client.text_detection(image=image)
    symbols = response.full_text_annotation.pages[0].blocks[0].paragraphs[0].words[0].symbols
    
    result = []

    for symbol in symbols:
        result.append(symbol.text)

    if response.error.message:
        raise Exception(
            '{}\nFor more info on error messages, check: '
            'https://cloud.google.com/apis/design/errors'.format(response.error.message))
        
    return result

pills_arr = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]


while True:
  but= button()
  print(but)
  if but>0:
    save_img()
    # yolov5
    os.system('python3 ./yolov5/detect.py  --weights ./yolov5/v5n_300_best.pt --data ./yolov5/data.yaml --img 320 --conf 0.5 --source ./yolov5/data/images --save-txt --save-conf')
    

   # 랭크 텍스트 경로
    text_file_list = glob.glob('./yolov5/runs/detect/exp/labels/img*.txt') 
    print(text_file_list)

    # txt 파일 to ocr 
    pills_rank = []
    for j in text_file_list:
     with open( j, 'r') as f:
      data = f.readlines()[1:5]
      for i in data:
       pills_rank.append(int(i.split()[0]))
    print(pills_rank)
    
    os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = "./my_google_api_key.json"
    loc=glob.glob('./yolov5/run/detect/exp*.jpg')    # front, back image reading
    chars = []
    for path in loc:
      try:
        chars.append(gathering_chars(path))
      except: IndexError    # 문자 검출을 못할 경우에 대비
   

#TTS

    predic_name='azp'
    # 이름과 사용법? 출력
    ps.playsound('K_TTS/'+predic_name+'_name.wav')
#   ps.playsound('pills/guide.wav')
    os.system('rm -rf yolov5/runs/detect/exp')

    
    but= button()
    
    #효과 효능
    if but==1:
      ps.playsound('K_TTS/'+predic_name+'_efficacy.wav')
    #복용량
    elif but==2:
      ps.playsound('K_TTS/'+predic_name+'_dosage.wav')
    #주의사항
    elif but==3:
      ps.playsound('K_TTS/'+predic_name+'_caution.wav')


