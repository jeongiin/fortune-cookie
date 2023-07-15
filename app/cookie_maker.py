import random
import datetime
import os

def load_fortunes_file_path():
    fortunes_file_folder = os.environ.get('DATAPATH')
    if fortunes_file_folder is None:
        fortunes_file_folder = '../data'
    fortunes_file_path = os.path.join(fortunes_file_folder, "fortunes.txt")
    
    if os.path.exists(fortunes_file_path):
        return (True, fortunes_file_path)
    
    return (False, "")

def load_my_fortunes_log_file_path():
    fortunes_log_file_folder = os.environ.get('LOGPATH')
    if fortunes_log_file_folder is None:
        fortunes_log_file_folder = '../data'
    fortunes_log_file_path = os.path.join(fortunes_log_file_folder, "my_fortunes.txt")
    
    if os.path.exists(fortunes_log_file_path):
        return (True, fortunes_log_file_path)
    
    return (False, "")

def cookie_maker():
    # 포춘쿠키 내용이 담긴 텍스트 파일의 경로
    _, fortunes_file = load_fortunes_file_path()

    # 포춘쿠키 문구를 저장할 파일의 이름과 경로
    _, log_file = load_my_fortunes_log_file_path()

    # 텍스트 파일에서 포춘쿠키 문구 읽어오기
    with open(fortunes_file, "r", encoding="utf-8") as file:
        fortunes = file.readlines()

    # 랜덤으로 한 문구 선택
    random_fortune = random.choice(fortunes).strip()

    # 현재 시간과 함께 문구를 추가할 파일에 기록
    current_time = ""
    with open(log_file, "a", encoding="utf-8") as file:
        current_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        file.write(f"[{current_time}] {random_fortune}\n")

    print(current_time + "포춘쿠키 문구가 파일에 추가되었습니다.")
    
if __name__ == "__main__":
    cookie_maker()