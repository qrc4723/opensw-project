# 오픈소스 프로젝트(로티플)

## 종합게임 플랫폼  제작


> 종합 게임 플랫폼
> > (1) 카드 게임 구현
> >> 블랙잭
> >>
> >> poker
> 
> > (2) 지뢰찾기
>
> > (3) 거북이 팩맨
>
> > (4) 검키우기
>
> > (5) 고군분투
>

## 프로젝트 별 진행상황

-주차마다 진행한만큼 적고 깃허브에 갱신하도록 (코드 또는 스샷)

(1) 카드 게임 구현

(1) - 1 블랙잭

사용 라이브러리 sklearn

기본 모델 뼈대 코드
```py
import pandas as pd

df = pd.read_csv('poker-hand-training.csv')

# 요 사이에 원핫 인코딩 + 데이터 전처리 과정있는데 생략

x = asd.iloc[:, :15] #카드 문양 원핫 인코딩(4) + 카드 숫자(1) = 5개인데 3장 뽑으니까 15개

y = asd.iloc[:, -1]

from sklearn.ensemble import RandomForestClassifier


model = RandomForestClassifier(random_state=32, n_estimators=200)
model.fit(x,y)

import pickle

filename= 'poker-model3.sav'
pickle.dump(model, open(filename, 'wb'))
```
(2) 지뢰찾기

- 기본적인 게임 GUI 구현
- 지뢰 및 깃발 이미지 삽입
- Highscore 구현
- 메인 메뉴 구현(Start, Quit)
- 난이도 설정 메뉴 구현(맵 크기, 지뢰 개수)
- 난이도 설정 메뉴 세부사항 미구현(현재 맵 크기 표시, easy/ normal/ hard 버튼의 이미지화)

(3) 거북이 팩맨

(4) 검키우기

(5) 고군분투
