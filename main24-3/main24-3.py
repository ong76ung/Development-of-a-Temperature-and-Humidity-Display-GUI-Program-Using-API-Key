import urllib.request  # 웹 요청을 보내기 위한 표준 라이브러리
import json            # JSON 데이터를 파싱하기 위한 라이브러리
import tkinter         # GUI 창을 만들기 위한 라이브러리
import tkinter.font    # tkinter 폰트 설정을 위한 라이브러리

# OpenWeatherMap에서 발급받은 API 키 입력
API_KEY = "여기에_본인_API_키_입력"

def tick1Min():
    """
    OpenWeatherMap API에 요청을 보내 서울의 온도와 습도를 가져오고
    tkinter 레이블에 표시하는 함수. 1분마다 자동으로 재호출됨.
    """
    # 서울 날씨 요청 URL 구성 (units=metric: 섭씨 온도)
    url = f"https://api.openweathermap.org/data/2.5/weather?q=Seoul&appid={API_KEY}&units=metric"
    
    # API 서버에 GET 요청 전송 및 응답 수신
    with urllib.request.urlopen(url) as r:
        data = json.loads(r.read())  # JSON 응답을 파이썬 딕셔너리로 변환
    
    temp = data["main"]["temp"]      # 온도 값 추출 (단위: °C)
    humi = data["main"]["humidity"]  # 습도 값 추출 (단위: %)
    
    # 레이블 텍스트 업데이트 (소수점 1자리로 온도 표시)
    label.config(text=f"{temp:.1f}C  {humi}%")
    
    # 60,000ms(1분) 후 tick1Min 함수 재호출 (자동 갱신)
    window.after(60000, tick1Min)

# GUI 창 생성
window = tkinter.Tk()
window.title("TEMP HUMI DISPLAY")   # 창 제목 설정
window.geometry("400x100")          # 창 크기 설정 (가로 400 x 세로 100)
window.resizable(False, False)       # 창 크기 조절 불가 설정

# 폰트 크기 30으로 설정
font = tkinter.font.Font(size=30)

# 텍스트 레이블 생성 및 창에 배치
label = tkinter.Label(window, text="불러오는 중...", font=font)
label.pack(expand=True)  # 창 중앙에 배치

# 프로그램 시작 시 날씨 데이터 첫 호출
tick1Min()

# GUI 이벤트 루프 시작 (창 유지)
window.mainloop()
