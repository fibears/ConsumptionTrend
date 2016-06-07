# -*- coding: utf-8 -*-
# @Author: fibears
# @Date:   2016-06-07 22:32:52
# @Last Modified by:   fibears
# @Last Modified time: 2016-06-08 00:16:54

import urllib
import urllib2
import cookielib
import time

from lxml.html import parse
from bs4 import BeautifulSoup

LoginUrl = 'http://idstar.xmu.edu.cn/amserver/UI/Login'

LoginData = urllib.urlencode({
    'IDToken1': 'xxxx',
    'IDToken2': 'xxxx'
})
Headers = {
    'Referer': 'http://idstar.xmu.edu.cn/amserver/UI/Login',
    'Host': 'idstar.xmu.edu.cn',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.11; rv:46.0) Gecko/20100101 Firefox/46.0'
}

# cookiejar object
# save cookie
cookie = cookielib.CookieJar()
# 利用urllib2库的HTTPCookieProcessor对象来创建cookie处理器
opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cookie))
req1 = urllib2.Request(LoginUrl, LoginData, Headers)
result1 = opener.open(req1)
res1 = opener.open('http://i.xmu.edu.cn/?.pn=p768')

# Parse Website To Extract PostData #
soup = BeautifulSoup(res1.read(), 'lxml')
PostParameters1 = soup.select('form[id="f1106_daily"]')[0]
PostParameters2 = soup.select('form[id="insertForm2"]')[0].select('input')

PostUrl = 'http://i.xmu.edu.cn/' + PostParameters1.attrs['action']

# Visit Website With cookie
PostData = urllib.urlencode({
    'endmonth': '06',
    'endtime': '2016-06-05',
    'endyear': '2016',
    'searchtype': 'days',
    'jylxselect': PostParameters2[3].attrs['value'],
    'startmonth': '09',
    'starttime': '2014-09-11',
    'startyear': '2014',
    'pagetogo':PostParameters1.select('input[name="pagetogo"]')[0].attrs['value'],
    'ordernameD': PostParameters2[10].attrs['value'],
    'ordertypeD': PostParameters2[11].attrs['value'],
    'kh': PostParameters2[12].attrs['value']
    })

res2 = opener.open(PostUrl, PostData)
