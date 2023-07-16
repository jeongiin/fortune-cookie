# -*- coding: utf-8 -*-
import unittest
from utils import get_fortunes_file_path
# fortunes.txt 파일이 존재하는 지 테스트
## 서비스의 베이스가 되는 데이터이므로 실수로 삭제할 경우 큰 문제가 생김
class TestFortunesFile(unittest.TestCase):
    def test_fortunes_file_exists(self):
        check_result, _ = get_fortunes_file_path()
        self.assertTrue(check_result, f"Fortune data does not exist.")

if __name__ == '__main__':
    unittest.main()