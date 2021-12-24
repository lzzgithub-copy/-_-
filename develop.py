import requests
from bs4 import BeautifulSoup
import xlwt
import re
# 爬取法条对应的案例
class Fabao:
    def __init__(self):
        self.URL = 'https://www.pkulaw.com/chl/39c1b78830b970eabdfb.html?keyword=%e4%b8%ad%e5%8d%8e%e4%ba%ba%e6%b0%91%e5%85%b1%e5%92%8c%e5%9b%bd%e5%88%91%e6%b3%95'
        self.header = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36 Edg/96.0.1054.62'}
    def get_case(self):
        html = requests.get(self.URL, headers=self.header)
        soup = BeautifulSoup(html.text, "html.parser")
        soup.select()
if __name__ == '__main__':
    fb = Fabao()
    fb.get_case()