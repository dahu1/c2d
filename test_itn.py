import pytest
from chinese2digits import itn

itn_tool = itn()

## zh_cn：需要将中文数字转为阿拉伯数字的一些case
def test_number_itn():
    inputText = [
        '三十二点四', '二零一九年三月', '茅台跌到一千八百块钱的时候',
        '百分之三十二', '三千十二', '负三十二', '十的九次方每升', 
        '十四点二乘以十的九次方每升', 
    ]

    target = [
        '32.4', '2019年3月', '茅台跌到1800块钱的时候',
        "32%",   "3012",   "-32",   "10^9/L",
        "14.2*10^9/L",  

    ]
    
    for i, item in enumerate(inputText):
        predict = itn_tool.takeChineseNumberFromString(item)['replacedText']
        assert target[i] == predict


## zh_cn：数字不能转的一些case
def test_number_nochange():
    inputText = [
        '到一定程度', '万一', '考四六级',
        '先给大家两个关键字提点一下',
        '九到十万', '再加一点', '加满油',
        '三兆一','五兆网络','千兆宽带'
    ]

    target = [
        '到一定程度', '万一', '考四六级',
        '先给大家两个关键字提点一下',
        '九到十万', '再加一点',"加满油",
        '三兆一','五兆网络','千兆宽带'
    ]
    
    for i, item in enumerate(inputText):
        predict = itn_tool.takeChineseNumberFromString(item)['replacedText']
        assert target[i] == predict


## zh_cn：汉字符号可以转为字母的一些case
def test_symbol_itn():
    inputText = [
        '百分之三十二点四',
    ]

    target = [
        '32.4%',
    ]
    
    for i, item in enumerate(inputText):
        predict = itn_tool.takeChineseNumberFromString(item)['replacedText']
        assert target[i] == predict

## zh_cn：汉字符号最好不转的一些case
def test_symbol_nochange():
    inputText = [
        '一个多小时', '十分钟', '小时', '一个多小时', 
        '多少分钟', '几分钟', '三分钟', '二十分钟', '八小时',
    ]

    target = [
        '一个多小时', '十分钟', "小时",   "一个多小时",   
        "多少分钟",   "几分钟", "三分钟",   "20分钟",   "八小时",
    ]
    
    for i, item in enumerate(inputText):
        predict = itn_tool.takeChineseNumberFromString(item)['replacedText']
        assert target[i] == predict

## zh_cn：日期要转的一些case
def test_symbol_riqi():
    inputText = [ 
        "二零一八年十月十八日", "二零一八年九月十一号", '二零二一年三月四号', '二零三四年十二月三十号',
        '二零零八年九月一号', '零八年九月一号', '二零零八年九月', '零八年九月',
        '二零零八年十月十号', '零八年十月十号', '二零零八年十月', '零八年十月',
        '二零零八年十一月十一号', '零八年十一月十一号', '二零零八年十一月', '零八年十一月',
    ]

    target = [
        "2018年10月18日", "2018年9月11号", "2021年3月4号", "2034年12月30号",
        '2008年9月1号',   '08年9月1号', '2008年9月', '08年9月',
        '2008年10月10号', '08年10月10号', '2008年10月', '08年10月',
        '2008年11月11号', '08年11月11号', '2008年11月', '08年11月',
    ]
    
    for i, item in enumerate(inputText):
        predict = itn_tool.takeChineseNumberFromString(item)['replacedText']
        assert target[i] == predict

## zh_cn：时间要转的一些case
def test_symbol_time():
    inputText = [
        '九点二十三分', '九点零三','十点半','十一点整',
        '九点一刻','十点一刻','十一点一刻', '现在时间是九点一刻对吧',
    ]

    target = [
        "9点23分",   "9.03",   "十点半",   "十一点整",
        "九点一刻",   "十点一刻",   "十一点一刻",   "现在时间是九点一刻对吧",
    ]
    
    for i, item in enumerate(inputText):
        predict = itn_tool.takeChineseNumberFromString(item)['replacedText']
        assert target[i] == predict

## zh_cn：四则运算要转的一些case
def test_symbol_sizeyunsuan():
    inputText = [
        '五加三','五减去三',"五乘九","九除以三",
        '十减三','十减去十三',"十五乘以十九","二十九除以十三",
        '二十五除三十二','五百减去三',"二百五乘以十九","九百零三除以三十三",
        '十五加二十一',  '五减一', '五减去一', '四加上三',
        '九减掉十二',  "小于零点四九九毫克每升", '大于五', '等于三点五',
        '二十四乘以十','同比减少百分之三十四毛利',
    ]

    target = [
        "5+3",   "5-3",   "5*9",   "9/3",
        "10-3",   "10-13",   "15*19",   "29/13",
        "25/32",   "500-3",   "250*19",   "903/33",
        "15+21","5-1", "5-1",   "4+3",
        "9-12", "<0.499mg/L",   ">5",   "=3.5",
        "24*10","同比减少34%毛利",
    ]
    
    for i, item in enumerate(inputText):
        predict = itn_tool.takeChineseNumberFromString(item)['replacedText']
        assert target[i] == predict

## zh_cn：带有一些单位
def test_symbol_danwei():
    inputText = [
        '八千克', '十八千克', '二十九毫升', '二十毫升',
        '十千克', '二毫克每日', '百分之一点五乘以三袋',
        '百分之一点五乘以十三袋', '百分之一点五乘三袋',
        '四点二乘以十的十九次方每升', '六点一八毫摩尔每毫升', '五十公里每小时',
        "十四点二乘以十的九次方每升", "六点一八毫摩尔每升", 
        "百分之六十六点二", "三千二百毫升", 
        "CPR六十五点七四毫克每升",
        "三十八摄氏度","十九摄氏度","三十七点五摄氏度"
        "五十克", "四十七点六微摩尔每升", "一点五厘米",
        "二十六毫米", "百分之五十加", "二十八乘十一毫米", 
        "D减", "零点四克加二百五十毫升","二十四克每升", 
        "一次每日", "三百一十一乘以十的九次方每升", 
        "一百一十八点九毫米汞柱", "零点五乘零点五厘米", 
        "百分之一点五乘以三袋","二毫克每日", "五百毫升每二十四小时",
        "小于零点四九九毫克每升",
    ]

    target = [
        "8kg",   "18kg",   "29mL",   "20mL",
        "10kg",   "2mg/日",   "1.5%*3袋",   "1.5%*13袋",
        "1.5%*3袋","4.2*10^19/L",   "6.18mmol/mL",   "50km/h",
        "14.2*10^9/L",   "6.18mmol/L",   "66.2%",   "3200mL",
        "CPR65.74mg/L", "38°C","19°C","37.5°C"
        "50g",    "47.6umol/L", "1.5cm",   "26mm",   
        "50%加",   "28*11mm", "D减",   "0.4g+250mL",
        "24g/L",   "一次/日", "311*10^9/L", "118.9mmHg",
        "0.5*0.5cm", "1.5%*3袋", "2mg/日", "500mL/24h",
        "<0.499mg/L",
    ]
    
    for i, item in enumerate(inputText):
        predict = itn_tool.takeChineseNumberFromString(item)['replacedText']
        assert target[i] == predict


## zh_cn：之前常见的badcase
def test_symbol_norm_badcase():
    inputText = [
        '说那么个五分钟十分钟的', '再加一点', '三四十分钟', "到一定程度", 
        "万一", "先给大家两个关键字提点一下", "考四六级 ", "二零一七年的二月份", 
        "九到十万", "一个多小时", '二零一九年三月', '九点三十分',
        '十分钟', '茅台跌到一千八', '海拔两千七百米', '一八年九月',
        '二零二一年十一月','二一年三月','零八年十月十一号','二零二一年一月十号',
        '十点零三', '八点半', '现在九点三十分', '二十一点三十九分',
        '现在九点二十三分',
    ]

    target = [
        "说那么个五分钟十分钟的",   "再加一点",   "三四十分钟",   "到一定程度",
        "万一",   "先给大家两个关键字提点一下",   "考四六级 ",   "2017年的2月份",
        "九到十万",   "一个多小时",   "2019年3月",   "9点30分",
        "十分钟",   "茅台跌到1800",   "海拔2700米",   "18年9月",
        "2021年11月",   "21年3月",   "08年10月11号",   "2021年1月10号",
        "10.03",   "八点半",   "现在9点30分",   "21点39分",
        "现在9点23分"
    ]
    
    for i, item in enumerate(inputText):
        predict = itn_tool.takeChineseNumberFromString(item)['replacedText']
        assert target[i] == predict

