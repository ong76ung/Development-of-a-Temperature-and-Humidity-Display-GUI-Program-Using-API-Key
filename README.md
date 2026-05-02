# 🌡️ API Key 발급받아 온습도 표시 GUI 프로그램 만들기

> 한신대학교 AIoT 설계입문 실습 보고서
> 조성웅 (202378162) | AI·SW학전공

---

## 📌 프로젝트 개요

OpenWeatherMap API를 활용하여 서울의 실시간 온도와 습도를
Python tkinter GUI 창에 표시하는 프로그램입니다.
1분마다 자동으로 데이터를 갱신합니다.

---

## 🎬 데모 영상

https://www.youtube.com/watch?v=XAUOyUqhd0g
---

## 🎯 실험 목적

- OpenWeatherMap API를 통해 외부 서버에서 실시간 기상 데이터 수신
- JSON 응답 파싱 및 원하는 값 추출 방법 학습
- tkinter를 이용한 GUI 프로그램 구성 능력 습득
- AIoT 디바이스에 외부 API를 연동하는 구조 이해

---

## 🛠️ 사용 기술

| 항목 | 내용 |
|------|------|
| 언어 | Python 3.x |
| GUI | tkinter |
| API | OpenWeatherMap Current Weather API |
| 하드웨어 | Raspberry Pi 5 |
| 개발환경 | Thonny IDE / Geany |

---

## 📦 필요 라이브러리

별도 설치 없이 Python 표준 라이브러리만 사용합니다.

```
urllib.request
json
tkinter
```

---

## 🔑 API 키 발급 방법

1. [OpenWeatherMap](https://openweathermap.org/) 접속
2. 회원가입 후 로그인
3. 상단 메뉴 [API Keys] 클릭
4. 발급된 키 복사
5. `main24-3.py`의 `API_KEY` 변수에 붙여넣기

> ⚠️ API 키는 발급 후 활성화까지 약 10분~2시간 소요됩니다.

---

## 💻 주요 코드 설명

| 코드 | 설명 |
|------|------|
| `urllib.request.urlopen(url)` | API 서버에 GET 요청 전송 |
| `json.loads(r.read())` | JSON 응답을 딕셔너리로 변환 |
| `data["main"]["temp"]` | 온도 값 추출 |
| `data["main"]["humidity"]` | 습도 값 추출 |
| `window.after(60000, tick1Min)` | 1분마다 자동 갱신 |

---

## ▶️ 실행 방법

```bash
python3 main24-3.py
```

---

## 📊 실행 결과

GUI 창에 아래와 같이 온도와 습도가 표시됩니다.

```
21.8C  40%
```

---

## ⚠️ 주의사항

- API 키는 외부에 공개하지 마세요
- API 키 발급 후 활성화까지 최대 2시간 소요될 수 있습니다
- 인터넷 연결이 필요합니다
- `API_KEY` 변수에 본인 키를 반드시 입력해야 합니다

---

## 📁 파일 구조

```
📂 프로젝트 폴더
 ┣ 📄 main24-3.py   # 메인 실행 파일
 ┗ 📄 README.md     # 프로젝트 설명
```

---

## 📚 참고문헌

- [OpenWeatherMap API Docs](https://openweathermap.org/current)
- [Python tkinter Docs](https://docs.python.org/3/library/tkinter.html)
- [Raspberry Pi Documentation](https://www.raspberrypi.com/documentation/)
