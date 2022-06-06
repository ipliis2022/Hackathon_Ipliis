# Hackathon_Ipliis
- 기간: 2022.4.11-5.12
- 구성
  - YOLO : 윤영준, 서현동
  - OCR  : 황지은, 고건호
  - Jetson nano  : 김다혜 

> # Discription
**시각 장애인을 위한 알약 구분 시스템 개발**
알약 구분이 어려운 시각 장애인을 위해 알약의 종류를 구별해내서 용법 등의 안내사항을 음성으로 알려주는 시스템이다. 

기존에 알약을 구분해주는 어플리케이션이 출시되어 사용되고 있지만 시각 장애인에게 스마트폰을 이용해서 알약을 구별해내는 것은
어려움이 있기 때문에 자체 하드웨어 제작을 통해 더 직관적으로 사용할 수 있는 차별점을 두고 있다. 
![image](https://user-images.githubusercontent.com/97325633/172160610-50b52fe1-f850-4917-b1e2-cc9c44446f4c.png)

> > ## 1. Function list
구분 | 기능 | 구현
S/W | 알약 Dectection & 구분 | YOLOv5
S/W | 알약 각인 인식 | Google OCR
S/W | 구별된 알약에 대한 정보를 음성으로 출력 | Kakao_TTS
H/W | 알약을 올려놓고 버튼을 통해 조작 | 잿슨나노

> > ## 2. Detailed function
Software
![image](https://user-images.githubusercontent.com/97325633/172170402-b59a6cc8-f0e7-4149-a8ac-cb0c099470d0.png)
- YOLOv5를 통해 예상되는 결과를 4순위까지 추출하고 바운딩박스 좌표에 해당하는 사진을 Crop하는 프로그램
- OCR을 통해 각인을 인식해낸 후 YOLO에서 받은 RANK에 해당하는 각인과 비교하여 가장 높은 확률에 해당하는 알약을 판별
- 가장 유력한 알약에 대한 복약법, 주의사항, 부작용등을 스위치를 통해 원하는 정보를 출력

Hardware
(하드웨어 제작 후 사진 추가 예정)
- 스위치를 통해 조명 및 사진 촬영
- 필요한 정보에 대해 1,2,3번 중 골라서 나올 수 있게 구성

> # Environment 
colab Python 3.7.13
잿슨 버전 확인

# 전체 소스 코드 
'''python

'''
