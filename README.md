# 오늘의 포춘쿠키 서비스 🥠

- 50개의 포춘쿠키 멘트 중 하루의 1개, 랜덤으로 화면에 표시됩니다.
- 한 번 실행하여 log파일(my_fortunes.txt)에 저장된 경우, 하루가 지나기 전 내용이 바뀌지 않습니다.
- 여담 : chatGPT로 쿠키 내용을 자동 생성하려고 했으나 키를 공유하기 애매하여 미리 fortunes.txt에 저장해두었습니다. 😓

## git hook

- pre-commit : app/test.py 를 실행
- post-commit : 자동으로 도커 이미지 및 서비스 업데이트
- [이미지]

## github action 사용 증명

- [이미지]

## 서비스 실행 방법

### 1. Git clone

```
$ git clone https://github.com/jeongiin/fortune-cookie.git
```

### 2. Docker Build

```
$ docker build -t make:latest -f Dockerfile.make .
$ docker build -t dp:latest -f Dockerfile.display .
```

### 3-1. Docker Run

```
$ docker run -it -v ./data:/data make:latest
$ docker run -it -v ./data:/data -p 5000:5000 dp:latest
```

### 3-2. Docker Service

```
$ docker service create -t --mount type=bind,source=./data,target=/data -p 5000:5000 --replicas=2 --name fortunecookieservice dp
```

### 4. http://127.0.0.1:5000/ 에 접속

### 5. 오늘의 행운 멘트를 확인

### (Option) 오류 해결 과정

- m1에서만 나타나는 문제인지는 모르겠으나 수업에서 가르쳐주신 수정전 명령어로 입력 시 절대 경로 관련 오류가 나서 수정해주었습니다. 아래 예시 외 다른 경로도 모두 절대 경로로 설정하였습니다.

```
# 수정전
$ docker run -it -v ./data:/data -p 5000:5000 dp:latest

# 수정후 : 정확한 절대 경로를 입력
$ docker run -it -v /Users/timdalxx/2023_PROJECT/skt_flyai_etc/fortune-cookie/data:/data -p 5000:5000 dp:latest
```
