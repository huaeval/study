# coding=utf-8
import json
import time
import datetime
import requests

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
thatTime = datetime.datetime.now()
#店铺采集错误列表，做二次收集
errorShopList = [] 
def start(driver):
    "启动"
    print "任务开始".center(50,"-")
    try:
        #访问生意参谋
        # time.sleep(1)
        # driver.get("https://sycm.taobao.com/flow/monitor/shopsource?activeKey=1&dateRange=2018-06-07%7C2018-06-07&dateType=today&device=2&spm=a21ag.8198212.LeftMenu.d754.e3b1410ceulRon")
        # shopName = getShopName(driver)
        # print shopName
        print json.dumps(driver,getShopLinkList())
        #切换到PC端
        # time.sleep(1)
        # changeSelect(driver)
        # # #展开二级类目
        # time.sleep(1)
        # expland(driver)
        # # #采集数据
        # time.sleep(1)
        # jsonData = gather(driver)
        # print jsonData
        # #提交采集数据
        # postData(jsonData)
        # # #切换无线端
        # time.sleep(1)
        # changeSelect(driver,1)
        # time.sleep(1)
        # expland(driver)
        # # #采集数据
        # jsonData = gather(driver)
        # # #提交采集数据
        # postData(jsonData)
        # changeSelect(driver,1)
        # #切换tab
        # print "获取商品来源-PC".center(50,"*")
        # changeSelect(driver)
        # time.sleep(1)
        # list = table2list(driver)
        # print list
        # print "获取商品来源-WAP".center(50,"*")
        # changeSelect(driver,1)
        # time.sleep(1)
        # list = table2list(driver)
        # print list

    except Exception:
        print "小错误,请联系开发人员"


def expland(driver):
    "展开全部二级类目"
    items = mclass(driver,"ebase-Table__levelExpand")
    if len(items) > 0 :
        for item in items:
            item.click()
            time.sleep(1)
        print "expland-end".center(50,"*")
    else:
        print "展开类目失败".center(50,"-")

def gather(driver):
    "采集数据"
    print "gather-end".center(50,"*")
    trs = mclass(driver,"ebase-Table__tbodyTr")
    results = {}
    psoureFrom = ""
    for tr in trs:
        result = {}
        trClassName =  tr.get_attribute("class")
        tds = tr.find_elements_by_tag_name("td")
        soureFrom = tds[0].text
        result["soureFrom"] = soureFrom
        result["visitorNum"] = tds[1].text
        result["percentage"] = tds[2].text
        if "ebase-Table__childRow" in trClassName:
            results[psoureFrom]["child"].append(result)
        else:
            psoureFrom = soureFrom
            child = {}
            child = result
            child["child"] = []
            results[psoureFrom] = child
    rjson = json.dumps(results.values())
    return rjson

def postData(jsonDate):
    "提交采集数据"
    #print jsonDate
    r = requests.post("http://127.0.0.1:8081/post/json",data=jsonDate,json=None,headers = {"Content-Type":"application/json"})
    print r.json()
    print "postData-end".center(50,"*")

def changeSelect(driver,index = 0):
    "切换PC和端和无线端0/1 0表示PC端 1表示无线端"
    sui = mclass(driver,"oui-select-container")
    if len(sui) > 0 :
        sui[0].click()
        time.sleep(1)
        mclass(driver,"oui-dropdown-item")[index].click()
    else :
        print "切换无线/pc失败"

def changeTab(driver,label = "店铺来源"):
    "切换tab"
    try:
        driver.find_element_by_link_text(label).click()
    except Exception:
        print "切换Tab失败".center(50,"-")

def table2list(driver):
    "获取商品来源"
    try:
        changeTab(driver,"商品来源")
        WebDriverWait(driver, 10).until(lambda x: x.find_elements_by_class_name("ebase-Table__tbodyTr"))
        trs = mclass(driver,"ebase-Table__tbodyTr")
    except Exception:
        print "获取商品dom元素失败"
    results = []
    if len(trs) > 0 :
        for tr in trs :
            result = {}
            tds = tr.find_elements_by_tag_name("td")
            if len(tds) >0 :
                result["seq"] = tds[0].text
                result["name"] = tds[1].text
                span = tds[2].find_elements_by_tag_name("span")
                result["visitor"] = span[0].text
                result["visitorConversion"] = str(span[1].text)[1:-1]
                result["paynum"] = tds[3].text
                result["conversion"] = tds[4].text
                linka = tds[5].find_element_by_link_text("商品来源")
                #后面采集
                result["link"] = linka.get_attribute("href")
                results.append(result)  
    else:
        print "获取商品dom元素失败".center(50,"*")
    info = getlistInfo(driver,results)
    return info

def getlistInfo(driver,list):
    "商品来源详情获取"
    for item in list:
        driver.get(item["link"])
        changeSelect(driver)
        #等待出现tr原素
        try:
            WebDriverWait(driver, 5).until(lambda x: x.find_elements_by_class_name("ebase-Table__tbodyTr"))
            info1 = getinfo(driver)
        except Exception:
            info1 = []
        item['pcinfo'] = info1
        changeSelect(driver,1)
        #等待出现tr原素 并且和原来不一样。
        try:
            WebDriverWait(driver, 5).until(lambda x: x.find_elements_by_class_name("ebase-Table__tbodyTr") and len(x.find_elements_by_class_name("ebase-Table__tbodyTr")) != len(info1))
            info2 = getinfo(driver)
        except Exception:
            info2 = []
        item['wapinfo'] = info2
        del item["link"]
    rjson = json.dumps(list)
    return rjson

def getinfo(driver):
    print "getinfo"
    info = []
    try:
        trs = mclass(driver,"ebase-Table__tbodyTr")
        if trs and len(trs) > 0:
            for tr in trs:
                result = {}
                tds = tr.find_elements_by_tag_name("td")
                if tds and len(tds) > 0:
                    result["soureFrom"] = tds[0].text
                    result["visitorNum"] = tds[1].text
                    result["percentage"] = tds[2].text
                    info.append(result)
    except Exception:
        print "error"
    return info

def getShopName(driver):
    name = driver.find_element_by_class_name("ebase-Selector__title")
    return name.text

def mclass(driver,className):
    elemtes = []
    try:
        elemtes = driver.find_elements_by_class_name(className)
    except Exception:
        print "获取都能出错吗？"
    return elemtes
    
def getStartMoth():
    return thatTime.month - 3

def startDay(days = 90):
    "获取时间，目前测可查询时间为90天"
    day = thatTime-datetime.timedelta(days = days)
    return (day.strftime("|%Y-%m-%d") * 2)[1:]

def getShopLinkList(gatherDay = 90):
    "获取需要采集的全部店铺连接，便于出错后继续采集"
    results = []
    i = 0
    while i <= gatherDay :
        linkPc = 'https://sycm.taobao.com/flow/monitor/itemsource?dateRange=%s&dateType=day&device=1'%(startDay(i))
        results.append(linkPc)
        i+=1
    return results

def gatherShopInfo(driver,gatherInfo):
    lenght = len(gatherInfo)
    i = 0
    while i <= lenght :
        pcLink = gatherInfo[i]
        try:
            driver.get(pcLink)
            #关闭所有选项
            closeAllShopCheck(driver)
        except Exception:
            #收集错误，尝试二次请求
            errorShopList.append(pcLink)

def closeAllShopCheck(driver):
    checkboxs = mclass(driver,"oui-checked")
    for checkbox in checkboxs:
        checkbox.click()
    return {}
