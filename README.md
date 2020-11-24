# **전국 1년치의 주유소 데이터를 분석하고 시각화하는 과정**

***

+ 과정
1. opinet에서 제공하는 전국 주유소 데이터를 수집
2. 수집한 데이터를 분석에 필요한 형식으로 전처리 및 병합
3. 여러가지 분석기법 적용 -> 어떤 기법인지 추가 예정
4. QT를 이용해서 시각화
5. 성능 평가 및 코드 수정

***

## 1. opinet에서 제공하는 전국 주유소 데이터를 수집<br><br>
![1](https://user-images.githubusercontent.com/51322546/99346922-19280700-28d9-11eb-9efb-279074676117.PNG)  
<br>관련 URL
> http://www.opinet.co.kr/user/opdown/opDownload.do  

<br><br><br>
## 2.수집한 데이터를 분석에 필요한 형식으로 전처리<br><br>
![1](https://user-images.githubusercontent.com/51322546/99348995-3c08ea00-28de-11eb-898b-791be542793c.PNG)  
<br>필요없는 주석행 제거<br><br>

![1](https://user-images.githubusercontent.com/51322546/100058814-565a3f00-2e6d-11eb-983e-5fc85a572131.png)  
<br>결측치 처리<br><br><br>

### 코드상으로 적용된 작업
* **데이터 병합**
-한달별로 분리되있는 데이터들을 Merge
* **결측치 처리**
* **데이터 자료형 변환**
* **스케일링 및 필요 컬럼 재정의**







