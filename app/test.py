# fortunes.txt 파일이 존재하는 지 테스트
## 서비스의 베이스가 되는 데이터이므로 실수로 삭제할 경우 큰 문제가 생김
import unittest
import os

class TestFortunesFile(unittest.TestCase):
    def test_fortunes_file_exists(self):
        filename = "fortunes.txt"
        self.assertTrue(os.path.exists(filename), f"File '{filename}' does not exist.")

if __name__ == '__main__':
    unittest.main()