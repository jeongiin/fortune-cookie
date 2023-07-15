# -*- coding: utf-8 -*-
from flask import Flask
from utils import *
import re

app = Flask(__name__)


def get_last_sentence(file_path):
    with open(file_path, "r", encoding="utf-8") as file:
        lines = file.readlines()
        if lines:
            last_line = lines[-1].strip()
            return last_line
        else:
            return None

@app.route('/')
def display_fortune():
    # 파일에서 오늘 생성된 문장 추출
    _, log_path = get_my_fortunes_log_file_path()
    last_fortune = get_last_sentence(log_path)
    today_fortune = re.sub(r'\[\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}\] ', '', last_fortune)
    
    if today_fortune:
        # 추출된 문장을 HTML 형식으로 반환
        html = "<h1>🥠 오늘의 포춘 쿠키 문구 🥠</h1>"
        html += "<ul>"
        html += f"<li>{today_fortune}</li>"
        html += "</ul>"
    else:
        html = "<h1>아직 쿠키 굽는 중이에요.😓</h1>"

    return html

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)