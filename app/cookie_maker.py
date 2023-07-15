# -*- coding: utf-8 -*-
import random
import datetime
from utils import *

# 오늘 생성된 문구가 이미 있는지 체크
def check_existing_fortune(output_file_path):
    today = datetime.date.today().strftime("%Y-%m-%d")
    if get_my_fortunes_log_file_path()[0]:
        with open(output_file_path, "r", encoding="utf-8") as file:
            for line in file:
                if today in line:
                    return True
    return False

# 랜덤으로 한 문구 선택
def get_random_fortune(fortunes_file_path):
    with open(fortunes_file_path, "r", encoding="utf-8") as file:
        fortunes = file.readlines()
        random_fortune = random.choice(fortunes).strip()
        return random_fortune

def cookie_maker():
    # 오늘 생성된 문구가 없으면 새로운 문구 추가
    _, fortunes_file_path = get_fortunes_file_path()
    _, output_file_path = get_my_fortunes_log_file_path()
    
    if not check_existing_fortune(output_file_path):
        random_fortune = get_random_fortune(fortunes_file_path)
        current_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        new_fortune = f"[{current_time}] {random_fortune}\n"
        with open(output_file_path, "a", encoding="utf-8") as file:
            file.write(new_fortune)
            print("새로운 포춘 쿠키 문구가 파일에 추가되었습니다.")
    else:
        print("오늘 이미 생성된 포춘 쿠키 문구가 있습니다.")
    
if __name__ == "__main__":
    cookie_maker()