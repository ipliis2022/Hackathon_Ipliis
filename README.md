# Hackathon_Ipliis
- 기간: 2022.4.11-6.09
- 구성
  - YOLO : 윤영준, 서현동
  - OCR  : 황지은, 고건호
  - Jetson nano  : 김다혜 
- - -

# Discription
**시각 장애인을 위한 알약 구분 시스템 개발**
알약 구분이 어려운 시각 장애인을 위해 알약의 종류를 구별해내서 용법 등의 안내사항을 음성으로 알려주는 시스템을 통해 그들의 삶의 질을 향상시키는 것을 목표로 한다.

기존에 알약을 구분해주는 어플리케이션이 출시되어 사용되고 있지만 시각 장애인에게 스마트폰을 이용해서 알약을 구별해내는 것은
어려움이 있기 때문에 자체 하드웨어 제작을 통해 더 직관적으로 사용할 수 있는 차별점을 두고 있다. 

![20220609_161334](https://user-images.githubusercontent.com/97012327/172787537-aaa017eb-49b7-4bc4-833a-f9f2c5d9f460.png)


> ## 1. Function list
> 구분|기능|구현|
> |---|---|---|
> S/W|알약 Dectection & 구분|YOLOv5|
> S/W|알약 각인 인식|Google OCR|
> S/W|구별된 알약에 대한 정보를 음성으로 출력|Kakao_TTS|
> H/W|알약을 올려놓고 버튼을 통해 조작|젯슨나노|

> ## 2. Detailed function
> Software
> ![image](https://user-images.githubusercontent.com/97325633/172170402-b59a6cc8-f0e7-4149-a8ac-cb0c099470d0.png)
> - YOLOv5를 통해 예상되는 결과를 4순위까지 추출하고 바운딩박스 좌표에 해당하는 사진을 Crop하는 프로그램
> - OCR을 통해 각인을 인식해낸 후 YOLO에서 받은 RANK에 해당하는 각인과 비교하여 가장 높은 확률에 해당하는 알약을 판별
> - 가장 유력한 알약에 대한 복약법, 주의사항, 부작용등을 스위치를 통해 원하는 정보를 출력
> Hardware
> (하드웨어 제작 후 사진 추가 예정)
> - 스위치를 통해 조명 및 사진 촬영
> - 필요한 정보에 대해 1,2,3번 중 골라서 나올 수 있게 구성
- - -

# Environment 
colab Python 3.7.13  
잿슨 버전 확인 후 추가 예정
- - -

# Dataset 구성
- 클래스별 train set은 핸드폰 카메라로 찍은 사진은 250장씩, 실제 하드웨어 상의 환경에서 찍은 사진들은 100여장씩 해서 
10개의 클래스에 각각 350여장씩 확보
- train/valid 데이터셋 비율은 9:1 로 설정
- labeling 작업은 roboflow를 이용하여 진행
- roboflow 안에 resize기능을 통해 img_size는 640 x 640으로 설정
- roboflow 안에 agumentation 기능을 통해 기존의 3500여장의 데이터셋을 10596장으로 늘린 후 진행 
![image](https://user-images.githubusercontent.com/97325633/172219026-f74d09a9-2108-41ad-acec-f277430e48f9.png)
- - - 

# 코드

>  ## 전체 소스 코드 
>  - [전체 소스 코드](https://github.com/HyundongSeo/Hackathon_Ipliis/blob/9ec86ac71bc95667acbba370f1e5aa68a7ca5d9b/ipills.py)
>  - yolov5에 weight는 pretrained된 값을 미리 저장해 놓음
> - yolo에서 예상한 것들과 ocr에서 인식한 값이 얼마나 일치하는지 확인하기 위해 문자를 한글자씩 나눠서 저장
> - 버튼(1,2,3)에 따라 필요한 정보만 출력
> - TTS, OCR, YOLO 다 포함

> ## YOLOv5 소스 코드
> - [detect.py](https://github.com/Yoon0527/AIFFEL_Project/blob/3c82e88570bdd02d449861d6c0cba2a94811a3ae/detect.py), [general.py](https://github.com/Yoon0527/AIFFEL_Project/blob/3c82e88570bdd02d449861d6c0cba2a94811a3ae/general%20(1).py)
> - 기본적으로는 ultralyrics yolov5의 깃클론을 통해 이루어져 있음
> - 우리는 크롭한 이미지를 ocr로 넘겨줘야하고 욜로가 정답을 맞추지 못했을 경우 ocr에게 확인해봐야하는 후순위를 전달하기 위해 rank출력이 필요했음
> - 위 링크의 코드 수정을 통해 아래와 같은 결과를 도출
> ![image](https://user-images.githubusercontent.com/97325633/172222343-50850db8-63b9-4554-86e7-a6c4347b343f.png)
> ![image](https://user-images.githubusercontent.com/97325633/172222983-657f4116-92ac-4f01-a989-aed0fedf67f3.png)

> ## Google OCR 소스 코드
> - [Google OCR 코드](https://river-butterfly-5b4.notion.site/G_OCR-3753b3a89e1b4a17a4d80872d429dd81)
> - google ocr api 사용
> - 잿슨에 하는 방법까지 포함
> - 여러 api 중 google을 선택한 이유![image](https://user-images.githubusercontent.com/97325633/172307542-cc942261-21c7-442f-9981-400c29b0dbad.png)

- - - 

# Contributor
> ## Open source
> [YOLOv5](https://github.com/ultralytics/yolov5.git)


> ## Team GitHub  
> [dahyekim](https://github.com/dahyekim1oo2/Aiffel.git)  
> [youngjoonyoon](https://github.com/Yoon0527/AIFFEL_Project.git)  
> [jieunhwang](https://github.com/LumiHunter/Hackathon_Ipliis.git)  
> [keonhoko](https://github.com/GeonHoKo/AIFFEL-HACKATHON.git)  
> [hyundongseo](https://github.com/HyundongSeo/Hackathon_Ipliis.git)


> <details> 
> <summary>references</summary>
> [딥러닝을 이용한 자동 알약 인식, 성균관대학교 일반대학원(2021)](http://www.riss.kr/search/detail/DetailView.do?p_mat_type=be54d9b8bc7cdb09&control_no=b5c082324cf3b892ffe0bdc3ef48d419&outLink=K)  
> [딥러닝을 활용한 알약 인식 모델 연구, 국립 강릉원주대학교 컴퓨터공학과(2020)](https://manuscriptlink-society-file.s3-ap-northeast-1.amazonaws.com/kips/conference/2020fall/presentation/KIPS_C2020B0146.pdf)  
> [딥러닝을 활용한 알약 분석 어플리케이션, 인천대학교 정보통신공학과(2020)](https://manuscriptlink-society-file.s3-ap-northeast-1.amazonaws.com/kips/conference/2020fall/presentation/KIPS_C2020B0152.pdf)  
> [스마트폰으로 촬영된 알약 영상의 글자 및 형상 인식 방법, 서울대학교 대학원(2017)](https://s-space.snu.ac.kr/handle/10371/137361)  
> [알약 자동 인식을 위한 딥러닝 모델간 비교 및 검증, 멀티미디어학회(2019)](https://scienceon.kisti.re.kr/srch/selectPORSrchArticle.do?cn=JAKO201913747257285&dbt=NART)  
