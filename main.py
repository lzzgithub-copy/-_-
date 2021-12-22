# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
#爬取刑法2020
#参考教程 https://www.bilibili.com/video/BV1j4411c7ny?from=search&seid=8976763725493733519&spm_id_from=333.337.0.0
import requests
from bs4 import BeautifulSoup
#面向对象
class Fabao:
    #设置URL和请求头
    def __init__(self):
        self.URL ='https://www.pkulaw.com/chl/39c1b78830b970eabdfb.html?keyword=%e4%b8%ad%e5%8d%8e%e4%ba%ba%e6%b0%91%e5%85%b1%e5%92%8c%e5%9b%bd%e5%88%91%e6%b3%95'
        self.header = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36 Edg/96.0.1054.62'}
    #获取网址并解析，通过元素选择器爬取
    def get_law(self):
        html = requests.get(self.URL,headers = self.header)
        soup = BeautifulSoup(html.text,"html.parser")
        law_list = soup.select('#divFullText > div > div')
        for law in law_list:
            print(law.get_text())
# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    fb = Fabao()
    fb.get_law()


# See PyCharm help at https://www.jetbrains.com/help/pycharm/
