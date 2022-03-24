import requests,bs4,time
from fake_useragent import UserAgent

from selenium import webdriver

#driver = webdriver.Chrome()




#   ## //*[@id="jp_audio_0"]
url = 'https://ting55.com/book/2317-'

ua = UserAgent()


i = 1
while i <= 913:
    page = str(i)
    url = url + page

    header = {
        'origin': 'https://ting55.com',  # 请求来源
        'referer': url ,  # 请求来源，携带的信息比“origin”更丰富，
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36',
    }

    '''
    'Accept-Encoding':'gzip, deflate, br',
    'Accept-Language': 'zh-CN,zh;q=0.9',
    'Connection': 'keep-alive',
    'Content-Length': '26',
    'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
    'Cookie': 'JSESSIONID=73EA5BBD10277FD83360D3164F8E7A6A; Hm_lvt_ac3da4632dc24e9d361235e3b2d3a131=1625412563,1625456217; Hm_lpvt_ac3da4632dc24e9d361235e3b2d3a131=1625460857; ting55_history=https%3A%2F%2Fting55.com%2Fbook%2F2317-10%2560%25E6%2588%2591%25E5%25BD%2593%25E7%25AE%2597%25E5%2591%25BD%25E5%2585%2588%25E7%2594%259F%25E9%2582%25A3%25E5%2587%25A0%25E5%25B9%25B4%25E6%259C%2589%25E5%25A3%25B0%25E5%25B0%258F%25E8%25AF%25B4%25E7%25AC%25AC10%25E7%25AB%25A0',
    'DNT': '1',
    'sec-ch-ua': '" Not;A Brand";v="99", "Google Chrome";v="91", "Chromium";v="91"',
    'X-Requested-With': 'XMLHttpRequest',
    'xt': 'ce616274efdfb10c5f538e69abf34054',
    'Host': 'ting55.com'
    '''

    params = {

    }

    nowtime = str(int(time.time()))

    data = {
        'bookid' : '2317',
        'isPay' : 0 ,
        'page' : page
    }
    xhr_url = 'https://pp.ting55.com/202107051420/f70e7179aec46fca08f0db9a2655a007/2015/09/2317/'+ page +'.mp3?v=' + nowtime
    # Request URL: https://pp.ting55.com/202107051420/f70e7179aec46fca08f0db9a2655a007/2015/09/2317/828.mp3?v=1625464239848

    request = requests.get(xhr_url, headers = header)

    #resource = driver.get(url)

    #content = driver.find_element_by_id('jp_audio_0')

    #print(content.text)

    #request = requests.get(url,headers = header)

    #
    content = request.text
    #
    # soup = bs4.BeautifulSoup(request.text, "html.parser")
    #
    #
    # url = 'https://ting55.com/nlinka'
    #
    # url = soup.find_all("div",id="jquery_jplayer_1")
    #
    # print(url)

    i+=1

