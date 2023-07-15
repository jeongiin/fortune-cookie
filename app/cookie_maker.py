import random
import datetime

def cookie_maker():

    # 포춘쿠키 내용이 담긴 텍스트 파일의 경로
    fortunes_file = "./data/fortunes.txt"

    # 포춘쿠키 문구를 저장할 파일의 이름과 경로
    output_file = "./data/my_fortunes.txt"

    # 텍스트 파일에서 포춘쿠키 문구 읽어오기
    with open(fortunes_file, "r", encoding="utf-8") as file:
        fortunes = file.readlines()

    # 랜덤으로 한 문구 선택
    random_fortune = random.choice(fortunes).strip()

    # 현재 시간과 함께 문구를 추가할 파일에 기록
    current_time = ""
    with open(output_file, "a", encoding="utf-8") as file:
        current_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        file.write(f"[{current_time}] {random_fortune}\n")

    print(current_time + "포춘쿠키 문구가 파일에 추가되었습니다.")
    
if __name__ == "__main__":
    cookie_maker()