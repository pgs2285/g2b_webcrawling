#-*- coding: utf-8 -*-

import sys
from revise_UI import Ui_MainWindow
from PyQt5 import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5 import QtWidgets
import csv
import requests
from bs4 import BeautifulSoup
import re, time
import urllib.parse
import webbrowser
from dateutil.relativedelta import relativedelta
import datetime

class crawling(QMainWindow, Ui_MainWindow):

    def __init__(self):

        super().__init__()
        self.setupUi(self)
        self.show()
        self.region = {"전국":"00", "서울":"11", "부산":"26", "인천":"28", "대구":"27", "광주":"29", "대전":"30", "울산":"31", "세종":"36", "경기":"41", "강원":"42", "충북":"43","충남":"44",
        "전북":"45", "전남":"46", "경북":"47", "경남":"48", "제주":"49"}
        self.cnt = 0
        self.limit_page = 0
        self.labels = [self.change1, self.change2,self.change3,self.change4,self.change5,self.change6,self.change7,self.change8, self.change9, self.change10]
        self.labels_answer = [self.change_1_answer, self.change_2_answer, self.change_3_answer, self.change_4_answer, self.change_5_answer, self.change_6_answer ,self.change_7_answer, self.change_8_answer, self.change_9_answer, self.change_10_answer]
        self.labels_2 = [self.change1_2, self.change2_2, self.change3_2, self.change4_2, self.change5_2, self.change6_2, self.change7_2, self.change8_2, self.change9_2, self.change10_2, self.change11_2, self.change12_2]
        self.labels_answer_2 = [self.change_1_answer_2, self.change_2_answer_2, self.change_3_answer_2, self.change_4_answer_2, self.change_5_answer_2, self.change_6_answer_2, self.change_7_answer_2, self.change_8_answer_2, self.change_9_answer_2, self.change_10_answer_2, self.change_11_answer_2, self.change_12_answer_2]
        
    def search_input(self):
        self.title_number = []
        self.title = ""
        self.min = None
        self.max = None
        self.count = "30"
        self.text = "00"
        if self.input_title.text():
            self.title = self.input_title.text()


        if self.input_min.text():
            self.min = self.input_min.text()   

        try:
            int(self.min) 
        except:
            self.min = None 
                        
    
        if self.input_max.text():
            self.max = self.input_max.text()
         
        try:
            int(self.max)

        except:
            self.max = None

        if self.input_count.text():
            self.count = self.input_count.text()    

        try:
            int(self.count)

        except:
            self.count = '30'    
    

        if self.comboBox.currentText():
            self.text = self.region[self.comboBox.currentText()]

        
    def click_search(self):    
  
        def replaced(rm):
            rm = rm.replace('\r',"")
            rm = rm.replace('\n',"")
            rm = rm.replace('\t',"")
            rm = rm.replace(' ',"")
            rm = rm.replace('\xa0',"")
            return rm

        self.search_input()
        month_ago = datetime.datetime.now()-relativedelta(months=1)
        
        get_time = time.strftime('%Y-%m-%d', time.localtime(time.time()))

        encoded =self.title.encode('euc-kr')
        ###########url 변환#############
        base_url = "http://www.g2b.go.kr:8101/ep/tbid/tbidList.do?searchType=1&bidSearchType=1&taskClCds=&bidNm="
        url_title = urllib.parse.quote(encoded)
        next_url=f"&searchDtType=1&fromBidDt={month_ago.year}%2F{month_ago.month}%2F{month_ago.day}&toBidDt={get_time[0:4]}%2F{get_time[5:7]}%2F{get_time[8:10]}&fromOpenBidDt=&toOpenBidDt=&radOrgan=1&instNm=&instSearchRangeType=&refNo=&area="
        extra_url = "&areaNm=&industry=&industryCd=&budget=&budgetCompare=UP&detailPrdnmNo=&detailPrdnm=&procmntReqNo=&intbidYn=&regYn=Y&recordCountPerPage="
        url_full = base_url+url_title+ next_url + self.text + extra_url + self.count
        ###############################
        res = requests.get(url_full)
        soup = BeautifulSoup(res.text,"lxml")
        save = soup.find("div",attrs = {"class":"results"})
        attri_save = save.find_all(["a"])

        link_list = []
        for i in attri_save:
            link_list.append(i.get('href'))
        #######중복제거#######

        remove = set(link_list)
        link_list = list(remove)

        #####################
        self.result = []
        self.listWidget.clear()
        self.limit_page = 0
        for i in link_list:
            res = requests.get(i)
            soup = BeautifulSoup(res.text,"lxml")

            D = {}
                    
            try: #공고명
                ll = soup.findAll('th',text = "공고명")
                tt = ll[0].find_next_sibling().div.find(text=True, recursive=False)
                
                D['공고명'] = replaced(tt)
            except:
                D['공고명'] = 'unknown'

            try:
                announce = soup.findAll('th',text = re.compile('공고종류'))
                content = announce[0].find_next_sibling().text
                D['공고종류'] = replaced(content)
                announce1 = soup.findAll('th',text = re.compile('[가-힣]+일시'))
                content1 = announce1[0].find_next_sibling().text
                D['게시일시'] = content1
                announce = soup.findAll('th',text = re.compile('입찰공고번호'))
                content2 = announce[0].find_next_sibling().text
                D['입찰공고번호'] = replaced(content2)
                        
            except:           
                D['공고종류'] = "unexpected error"
                D['게시일시'] = "unexpected error"
                D['입찰공고번호'] = "unexpected error"

                ############ 입찰집행 및 진행정보 테이블 전체 가져오기###########

            try:
                D['입찰진행 및 진행정보'] = {}

                info = soup.find('th',text = re.compile("개찰장소"))         
                info_bid = info.parent.parent # 다 가져오기

                            
                c = info_bid.findAll("th") # [0] 예가방법 ,추첨번호공개여부  http://www.g2b.go.kr:8081/ep/invitation/publish/bidInfoDtl.do?bidno=20210100533&bidseq=00&releaseYn=Y&taskClCd=3 기준
                d = info_bid.findAll("td") # [0] 예가방법, 추첨번호공개여부 값이 들어있음
                            
                for u in range(len(c)):            
                    name = c[u].text #[0]기준 예가방법의 값을 가져옴
                    answer = d[u].text
                    D['입찰진행 및 진행정보'][replaced(name)] = replaced(answer)
                    if c[u].text == "개찰장소": break
            except:
                D['입찰진행 진행정보'] = "정보없음"        
            #################예정가격 결정 및 입찰금액 정보 가져오기######################
            
            try:
                D['예정가격 결정 및 입찰금액 정보'] = {}

                info_price = info.parent.parent.parent.find_next_sibling().find_next_sibling()
                if replaced(info_price.findAll("th")[0].text) =="입찰분류" or replaced(info_price.findAll("th")[0].text) == "제안서제출":
                    info_price = info_price.find_next_sibling().find_next_sibling() 
                e = info_price.findAll("th")
                f = info_price.findAll("td")

                for j in range(len(e)):
                    name = e[j].text
                    answer = f[j].text
                    D['예정가격 결정 및 입찰금액 정보'][replaced(name)] = replaced(answer)

            except: 
                D['예정가격 결정 및 입찰금액 정보'] = "정보없음"                    

            D['링크'] = i

            ####추정가격 비교를 위해 int로 바꿔서 비교하기#########
            number = str()
            try:
                m = D['예정가격 결정 및 입찰금액 정보']['추정가격']
                
                numbers = re.findall("\d+", m)

                for j in range(len(numbers)):
                    number = number + numbers[j]
                number = int(number)
            except:
                number = 0

               
            #############################################
            if self.max == None and self.min:
                if number > int(self.min):
                    self.result.append(D)
                    self.title_number.append(D['공고명'])
                    self.listWidget.addItem(D['공고명'])
                    self.limit_page += 1
                    

            elif self.min == None and self.max:
                if number < int(self.max):
                    self.result.append(D)
                    self.title_number.append(D['공고명'])
                    self.listWidget.addItem(D['공고명'])
                    self.limit_page += 1

            elif self.min and self.max:
                if number < int(self.max) and number > int(self.min):
                    self.result.append(D)
                    self.title_number.append(D['공고명'])
                    self.listWidget.addItem(D['공고명'])
                    self.limit_page += 1

            else:
                self.result.append(D)
                self.title_number.append(D['공고명'])
                self.listWidget.addItem(D['공고명'])
                self.limit_page += 1


        self.state.setText("완료")     
        if self.limit_page!=0:
            self.cnt = 0
            self.change_title.setText(self.result[self.cnt]['공고명'])
            self.change_kind.setText(self.result[self.cnt]['공고종류'])
            self.change_info_date.setText(self.result[self.cnt]['게시일시'])
            self.change_bid_number.setText(self.result[self.cnt]['입찰공고번호'])
            self.result_list = list(self.result[self.cnt]['입찰진행 및 진행정보'].keys())
            self.result_list_2 = list(self.result[self.cnt]['예정가격 결정 및 입찰금액 정보'].keys())
            self.limit = 0
            self.limit_2 = 0       
            self.change_link.clear()
            self.change_link.setText(self.result[self.cnt]['링크'])     
            for k in range(len(self.result_list)):
                self.labels[k].setText(self.result_list[k])
                self.labels_answer[k].setText(self.result[self.cnt]['입찰진행 및 진행정보'][self.result_list[k]])
                if self.limit == 10: break
            for k in range(len(self.result_list_2)):
                self.labels_2[k].setText(self.result_list_2[k])
                self.labels_answer_2[k].setText(self.result[self.cnt]['예정가격 결정 및 입찰금액 정보'][self.result_list_2[k]])
            
                if self.limit_2 == 12:break    
        elif self.limit_page == 0:
            pass


        

    def click_next(self):
        self.state.setText("대기중 - 검색후 완료가 뜰때까지 기다려주세요")         
        if self.cnt < self.limit_page-1 and self.limit_page!=0:

            for m in range(len(self.labels)):
                self.labels[m].clear()
                self.labels_answer[m].clear()
            
            for m in range(len(self.labels_2)):
                self.labels_answer_2[m].clear()
                self.labels_2[m].clear()

            self.cnt += 1        
            self.change_title.setText(self.result[self.cnt]['공고명'])
            self.change_kind.setText(self.result[self.cnt]['공고종류'])
            self.change_info_date.setText(self.result[self.cnt]['게시일시'])
            self.change_bid_number.setText(self.result[self.cnt]['입찰공고번호'])
            self.result_list = list(self.result[self.cnt]['입찰진행 및 진행정보'].keys())
            self.result_list_2 = list(self.result[self.cnt]['예정가격 결정 및 입찰금액 정보'].keys())
            self.limit = 0
            self.limit_2 = 0
            self.change_link.clear()
            self.change_link.setText(self.result[self.cnt]['링크'])
            for k in range(len(self.result_list)):
                self.limit += 1
                self.labels[k].setText(self.result_list[k])
                self.labels_answer[k].setText(self.result[self.cnt]['입찰진행 및 진행정보'][self.result_list[k]])
                if self.limit == 10: break

            for k in range(len(self.result_list_2)):
                self.limit_2 += 1
                self.labels_2[k].setText(self.result_list_2[k])
                self.labels_answer_2[k].setText(self.result[self.cnt]['예정가격 결정 및 입찰금액 정보'][self.result_list_2[k]])
                if self.limit_2 == 12: break
            
        else: 
            pass    


    def click_before(self):
        self.state.setText("대기중 - 검색후 완료가 뜰때까지 기다려주세요")  
        if self.cnt != 0 and self.limit_page != 0:
            
            for m in range(len(self.labels)):
                self.labels[m].clear()
                self.labels_answer[m].clear()
            
            for m in range(len(self.labels_2)):
                self.labels_answer_2[m].clear()
                self.labels_2[m].clear()
            
            
            self.cnt -= 1
            self.change_title.setText(self.result[self.cnt]['공고명'])
            self.change_kind.setText(self.result[self.cnt]['공고종류'])
            self.change_info_date.setText(self.result[self.cnt]['게시일시'])
            self.change_bid_number.setText(self.result[self.cnt]['입찰공고번호'])
            self.result_list = list(self.result[self.cnt]['입찰진행 및 진행정보'].keys())
            self.result_list_2 = list(self.result[self.cnt]['예정가격 결정 및 입찰금액 정보'].keys())
            self.limit = 0
            self.limit_2 = 0
            self.change_link.clear()
            self.change_link.setText(self.result[self.cnt]['링크'])
            for k in range(len(self.result_list)):
                self.limit += 1
                self.labels[k].setText(self.result_list[k])
                self.labels_answer[k].setText(self.result[self.cnt]['입찰진행 및 진행정보'][self.result_list[k]])
                if self.limit == 10: break

            for k in range(len(self.result_list_2)):
                self.limit_2 += 1
                self.labels_2[k].setText(self.result_list_2[k])
                self.labels_answer_2[k].setText(self.result[self.cnt]['예정가격 결정 및 입찰금액 정보'][self.result_list_2[k]])                      
                if self.limit_2 == 12:break

        else:
            pass

    def click_link(self):
        webbrowser.open(self.result[self.cnt]['링크'])
    
    def click_title(self,title):
        self.state.setText("대기중 - 검색후 완료가 뜰때까지 기다려주세요")  
        for m in range(len(self.labels)):
            self.labels[m].clear()
            self.labels_answer[m].clear()
        
        for m in range(len(self.labels_2)):
            self.labels_answer_2[m].clear()
            self.labels_2[m].clear()
   
        for i in range(len(self.title_number)):
            if self.title_number[i] == title.text():
                self.cnt = i


        self.change_title.setText(self.result[self.cnt]['공고명'])
        self.change_kind.setText(self.result[self.cnt]['공고종류'])
        self.change_info_date.setText(self.result[self.cnt]['게시일시'])
        self.change_bid_number.setText(self.result[self.cnt]['입찰공고번호'])
        self.result_list = list(self.result[self.cnt]['입찰진행 및 진행정보'].keys())
        self.result_list_2 = list(self.result[self.cnt]['예정가격 결정 및 입찰금액 정보'].keys())
        self.limit = 0
        self.limit_2 = 0
        self.change_link.clear()
        self.change_link.setText(self.result[self.cnt]['링크'])
        for k in range(len(self.result_list)):
            self.limit += 1
            self.labels[k].setText(self.result_list[k])
            self.labels_answer[k].setText(self.result[self.cnt]['입찰진행 및 진행정보'][self.result_list[k]])
            if self.limit == 10: break

        for k in range(len(self.result_list_2)):
            self.limit_2 += 1
            self.labels_2[k].setText(self.result_list_2[k])
            self.labels_answer_2[k].setText(self.result[self.cnt]['예정가격 결정 및 입찰금액 정보'][self.result_list_2[k]])                      
            if self.limit_2 == 12:break        
                
        
        
app = QApplication([])
a = crawling()
QApplication.processEvents()
sys.exit(app.exec_())