#!/usr/bin/env python
# coding: utf-8

# ハローワークの求人情報をスクレイピング（Python + Selenium + Beautiful Soup）

from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time
from bs4 import BeautifulSoup
import re

# ハローワークインターネットサービスのURL
url = "https://www.hellowork.mhlw.go.jp/"

# 以下からご自分で使用しているChromeのバージョンに合ったChromeDriverをダウンロードして下さい
# https://chromedriver.chromium.org/downloads

# ChromeDriverをご自分のPCの任意の場所に保存して、以下のDRIVER_PATHに設定して下さい。
DRIVER_PATH = 'D:\source\py\ChromeWebDriver\chromedriver_win32\chromedriver.exe'
driver = webdriver.Chrome(executable_path=DRIVER_PATH)
driver.get(url)
time.sleep(1)

# 「求人情報検索」をクリック
driver.find_element_by_class_name("retrieval_icn").click()
time.sleep(1)

# 福岡県内で探す
element = driver.find_element_by_id("ID_tDFK1CmbBox")
Select(element).select_by_value("40") #福岡
time.sleep(1)

# 「市区町村」を選ぶために「選択」をクリック
buttons = driver.find_elements_by_css_selector("input.button");
buttons[1].click()
time.sleep(1)

# 市区町村名のドロップダウンリストを選択
element = driver.find_element_by_id("ID_rank1CodeMulti")

# 【東日本】市区町村名コード(5桁・6桁)一覧（更新：2019.9.15）
# http://www13.plala.or.jp/bigdata/municipal_code_1.html

# 【西日本】市区町村名コード(5桁・6桁)一覧（更新：2019.9.15）
# http://www13.plala.or.jp/bigdata/municipal_code_2.html

# 市区町村名コードを基に、5つまで市区町村名を選択
Select(element).select_by_value("40131") #東区
Select(element).select_by_value("40132") #博多区
Select(element).select_by_value("40133") #中央区
Select(element).select_by_value("40134") #南区
Select(element).select_by_value("40135") #西区
time.sleep(1)

# OKをクリック
driver.find_element_by_id("ID_ok").click()
time.sleep(1)

# 佐賀県内で探す
element = driver.find_element_by_id("ID_tDFK2CmbBox")
Select(element).select_by_value("41") #佐賀
time.sleep(1)

# 「市区町村」を選ぶために「選択」をクリック
buttons = driver.find_elements_by_css_selector("input.button");
buttons[2].click()
time.sleep(1)

# 市区町村名のドロップダウンリストを選択
element = driver.find_element_by_id("ID_rank1CodeMulti")

# 市区町村名コードを基に、5つまで市区町村名を選択
Select(element).select_by_value("41201") #佐賀市
Select(element).select_by_value("41203") #鳥栖市
time.sleep(1)

# OKをクリック
driver.find_element_by_id("ID_ok").click()
time.sleep(1)

# 長崎県内で探す
element = driver.find_element_by_id("ID_tDFK3CmbBox")
Select(element).select_by_value("42") #長崎
time.sleep(1)

# 「市区町村」を選ぶために「選択」をクリック
buttons = driver.find_elements_by_css_selector("input.button");
buttons[3].click()
time.sleep(1)

# 市区町村名のドロップダウンリストを選択
element = driver.find_element_by_id("ID_rank1CodeMulti")

# 市区町村名コードを基に、5つまで市区町村名を選択
Select(element).select_by_value("42202") #佐世保市
Select(element).select_by_value("42204") #諫早市
Select(element).select_by_value("42205") #大村市
time.sleep(1)

# 「OK」をクリック
driver.find_element_by_id("ID_ok").click()
time.sleep(1)

# 「職業分類を選択」をクリック
buttons = driver.find_elements_by_css_selector("input.button");
buttons[7].click()
time.sleep(1)

# 「職業分類」のドロップダウンリストを選択
element = driver.find_element_by_id("ID_rank00Code")

# 「B 専門的・技術的職業」を選択
Select(element).select_by_value("B")

# 「下位」をクリック
driver.find_element_by_id("ID_down").click()
time.sleep(1)

# 「下位」のドロップダウンリストを選択
element = driver.find_element_by_id("ID_rank00Code")

# 「10 情報処理・通信技術者」を選択
Select(element).select_by_value("10")

# 「下位」をクリック
driver.find_element_by_id("ID_down").click()
time.sleep(1)

# 「下位」のドロップダウンリストを選択
element = driver.find_element_by_id("ID_rank00Code")

# 「104 ソフトウェア開発技術者」を選択
Select(element).select_by_value("104")

# 「下位」をクリック
driver.find_element_by_id("ID_down").click()
time.sleep(1)

# 「10401 ソフトウェア開発技術者（WEB・オープン系）」が既に選択されているので、「決定」をクリック
driver.find_element_by_id("ID_ok").click()
time.sleep(1)

# 「フリーワード」の「OR検索」ラジオボタンをクリック
driver.find_element_by_id("ID_freeWordRadioBtn0").click()
time.sleep(1)

# 「フリーワード」の入力欄をクリック
element = driver.find_element_by_id("ID_freeWordInput")

# 「フリーワード」の入力欄に"Ｐｙｔｈｏｎ　Ｃ＃"と入力（注意：全角文字で入力すること！）
element.send_keys("Ｐｙｔｈｏｎ　Ｃ＃")

time.sleep(1)

# 「詳細検索条件」をクリック
driver.find_element_by_id("ID_searchShosaiBtn").click()
time.sleep(1)

# 「交代制（シフト制）を含まない」にチェック
driver.find_element_by_id("ID_LkiboShgJnCKBox1").click()
time.sleep(1)

# 「裁量労働制を含まない」にチェック

driver.find_element_by_id("ID_LkiboShgJnCKBox2").click()
time.sleep(1)
# 「変形労働時間制を含まない」にチェック
driver.find_element_by_id("ID_LkiboShgJnCKBox3").click()
time.sleep(1)

# 「派遣・請負を含まない」にチェック
driver.find_element_by_id("ID_hakenUkeoinCKBox3").click()
time.sleep(1)

# 「転勤の可能性なし」にチェック
driver.find_element_by_id("ID_LsonotaCKBox4").click()
time.sleep(1)
# print(driver.page_source)

# 「OK」をクリック
driver.find_element_by_id("ID_saveCondBtn").click()
time.sleep(1)

# 「検索」をクリック
driver.find_element_by_id("ID_searchBtn").click()
time.sleep(1)

# 「表示件数」ドロップダウンリストをクリック
element = driver.find_element_by_id("ID_fwListNaviDispBtm")

# 「50件」を選択
Select(element).select_by_value("50")
time.sleep(1)

# 今見ているページをBeautifulSoupで解析
soup = BeautifulSoup(driver.page_source, "html.parser")

# 「求人」のテーブルを検索
jobs = soup.find_all("table", attrs={"class": "kyujin"})

# 検索結果を格納する"message"を初期化
message = ""

# 「職種」「月給」「勤務地」「仕事の内容」を取得する
for i, job in enumerate(jobs):
    job_name = str(job.find("td", attrs={"class": "m13"}).text.strip())
    salary_tags = job.find_all("tr",attrs={"class": "border_new"})[5].select(".disp_inline_block")
    for t, salary_tag  in enumerate(salary_tags):
        job_salary = salary_tag.text

    # 月給の上限の金額を正規表現で抽出
    m = re.search('(〜)(\d{3}),(\d{3})', job_salary)
    highest = int(m.group(2) + m.group(3))
    
    # 月給の上限の金額が40万円以上だった場合にのみ、"message"に格納する
    if highest >= 400000:
        print("〇 ", highest)
        job_description = job.find(string='仕事の内容').parent.find_next_sibling().text.replace('\n', '')
        job_location = job.find(string='就業場所').parent.find_next_sibling().text.replace('\n', '')
        message = message + "■{0} （ {1} ）{2} \n□{3}\n".format(job_name, job_salary, job_location, job_description)
    else:
         print("× ", highest)

# 検索結果の出力
print(message)

# 「次へ」をクリックして、次ページを表示する
# TODO: 「次へ」がクリックできる限り、以下の表示をループで回す、多分簡単
# TODO: CSV形式で保存してもいい
driver.find_element_by_name("fwListNaviBtnNext").click()
time.sleep(5)

# 今見ているページをBeautifulSoupで解析
soup = BeautifulSoup(driver.page_source, "html.parser")

# 「求人」のテーブルを検索
jobs = soup.find_all("table", attrs={"class": "kyujin"})

# 検索結果を格納する"message"を初期化
message = ""

# 「職種」「月給」「勤務地」「仕事の内容」を取得する
for i, job in enumerate(jobs):
    job_name = str(job.find("td", attrs={"class": "m13"}).text.strip())
    salary_tags = job.find_all("tr",attrs={"class": "border_new"})[5].select(".disp_inline_block")
    for t, salary_tag  in enumerate(salary_tags):
        job_salary = salary_tag.text

    # 月給の上限の金額を正規表現で抽出
    m = re.search('(〜)(\d{3}),(\d{3})', job_salary)
    highest = int(m.group(2) + m.group(3))
    
    # 月給の上限の金額が40万円以上だった場合にのみ、"message"に格納する
    # if highest >= 400000:
    if highest >= 200000:
        print("〇 ", highest)
        job_description = job.find(string='仕事の内容').parent.find_next_sibling().text.replace('\n', '')
        job_location = job.find(string='就業場所').parent.find_next_sibling().text.replace('\n', '')
        message = message + "■{0} （ {1} ）{2} \n□{3}\n".format(job_name, job_salary, job_location, job_description)
    else:
         print("× ", highest)

# 検索結果の出力
print(message)
# driver.close()
