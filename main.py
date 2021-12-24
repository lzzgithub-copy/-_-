# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
#爬取刑法2020
#参考教程 https://www.bilibili.com/video/BV1j4411c7ny?from=search&seid=8976763725493733519&spm_id_from=333.337.0.0
import requests
from bs4 import BeautifulSoup
import xlwt
import re
#面向对象
class Fabao:
    #设置URL和请求头
    def __init__(self):
        self.URL ='https://www.pkulaw.com/chl/39c1b78830b970eabdfb.html?keyword=%e4%b8%ad%e5%8d%8e%e4%ba%ba%e6%b0%91%e5%85%b1%e5%92%8c%e5%9b%bd%e5%88%91%e6%b3%95'
        self.header = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36 Edg/96.0.1054.62'}
    #获取网址并解析，通过元素选择器爬取
    def get_law(self):
        #定位元素
        html = requests.get(self.URL,headers = self.header)
        soup = BeautifulSoup(html.text,"html.parser")
        law_list_o = soup.select('#divFullText > div > div')
        # 获取文本
        law_list_1 = []
        for law in law_list_o:
            law_list_1.append(law.get_text())
            # print(law.get_text())
        # 合并同一条法条
        law_list = []
        reg = r"\s\s第([零一二三四五六七八九十百])+条"
        for law in law_list_1:
            # print(law)
            if  re.match(reg,law)==None:
                n = len(law_list)
                if n != 0:
                    law_list[-1] = law_list[-1] + '\n' + law
            else:
                law_list.append(law)
        #写入excel
        workbook = xlwt.Workbook()
        sheet = workbook.add_sheet('刑法法条')
        sheet.col(0).width = 256 * 120
        sheet.row(0).height_mismatch = True
        sheet.row(0).height = 20 * 20
        basic_style = xlwt.XFStyle()
        al = xlwt.Alignment()
        # 垂直对齐
        # al.horz = al.HORZ_CENTER
        # 水平对齐
        al.vert = al.VERT_CENTER
        # 换行
        al.wrap = al.WRAP_AT_RIGHT
        basic_style.alignment = al
        sheet.write(0,0,"刑法法条",basic_style)
        # 从第1行开始写入
        i = 1
        for law in law_list:
            sheet.write(i,0,law,basic_style)
            i +=1
        workbook.save("刑法法条.xls")
    def get_knowledgeOflaw(self):
        html = requests.get(self.URL, headers=self.header)
        soup = BeautifulSoup(html.text, "html.parser")
        knowledge_list_o = soup.select('div.fields > ul >li >div.box')
        # 写入excel
        workbook = xlwt.Workbook()
        sheet = workbook.add_sheet('刑法知识')
        sheet.col(0).width = 256 * 20
        sheet.col(1).width = 256 * 20
        sheet.col(2).width = 256 * 20
        sheet.col(3).width = 256 * 20
        sheet.col(4).width = 256 * 20
        sheet.col(5).width = 256 * 20
        sheet.col(6).width = 256 * 20
        sheet.row(0).height_mismatch = True
        sheet.row(0).height = 20 * 20
        basic_style = xlwt.XFStyle()
        al = xlwt.Alignment()
        # 垂直对齐
        # al.horz = al.HORZ_CENTER
        # 水平对齐
        al.vert = al.VERT_CENTER
        # 换行
        al.wrap = al.WRAP_AT_RIGHT
        basic_style.alignment = al
        #清洗内容，将key,value分别储存
        knowledge_list = []
        knowledge_head_list = []
        knowledge_content_list =[]
        for knowledge in knowledge_list_o:
            knowledge_list.append(knowledge.get_text().replace('\n',''))
        for knowledge in knowledge_list:
            knowledge_head_list.append(knowledge.split('：')[0])
            knowledge_content_list.append(knowledge.split('：')[1])
        for i in range(len(knowledge_head_list)-1):
            sheet.write(0,i,knowledge_head_list[i],basic_style)
            sheet.write(1,i,knowledge_content_list[i],basic_style)
        workbook.save(("刑法知识.xls"))
# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    fb = Fabao()
    # fb.get_law()
    # fb.get_knowledgeOflaw()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
