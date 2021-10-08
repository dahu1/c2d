import re

debug = 0
if debug:
    print('>> In debug model ')


class itn:
    def __init__(self):
        self.CHINESE_CHAR_LIST = ['幺', '零', '一', '二', '两', '三', '四', '五', '六', '七', '八', '九', '十', '百', '千', '万', '亿']
        self.CHINESE_SIGN_LIST = ['负', '正', '-', '+']
        self.CHINESE_CONNECTING_SIGN_LIST = ['.', '点', '·']
        self.CHINESE_PER_COUNTING_STRING_LIST = ['百分之', '千分之', '万分之']
        self.CHINESE_PER_COUNTING_SEG = '分之'
        self.CHINESE_PURE_NUMBER_LIST = ['幺', '一', '二', '两', '三', '四', '五', '六', '七', '八', '九', '十', '零']

        self.CHINESE_SIGN_DICT = {'负': '-', '正': '+', '-': '-', '+': '+'}
        self.CHINESE_PER_COUNTING_DICT = {'百分之': '%', '千分之': '‰', '万分之': '‱'}
        self.CHINESE_CONNECTING_SIGN_DICT = {'.': '.', '点': '.', '·': '.'}
        self.CHINESE_COUNTING_STRING = {'十': 10, '百': 100, '千': 1000, '万': 10000, '亿': 100000000}
        self.CHINESE_PURE_COUNTING_UNIT_LIST = ['十', '百', '千', '万', '亿']

        self.TRADITIONAl_CONVERT_DICT = {'壹': '一', '贰': '二', '叁': '三', '肆': '四', '伍': '五', '陆': '六', '柒': '七',
                                         '捌': '八', '玖': '九'}
        self.SPECIAL_TRADITIONAl_COUNTING_UNIT_CHAR_DICT = {'拾': '十', '佰': '百', '仟': '千', '萬': '万', '億': '亿'}

        self.SPECIAL_NUMBER_CHAR_DICT = {'两': '二', '俩': '二'}

        """
        中文转阿拉伯数字
        """
        self.common_used_ch_numerals = {'幺': 1, '零': 0, '一': 1, '二': 2, '两': 2, '三': 3, '四': 4, '五': 5, '六': 6, '七': 7,
                                        '八': 8, '九': 9, '十': 10, '百': 100, '千': 1000, '万': 10000, '亿': 100000000}

        """
        阿拉伯数字转中文
        """
        self.digits_char_ch_dict = {'0': '零', '1': '一', '2': '二', '3': '三', '4': '四', '5': '五', '6': '六', '7': '七',
                                    '8': '八', '9': '九', '%': '百分之', '‰': '千分之', '‱': '万分之', '.': '点'}

        # 以百分号作为大逻辑区分。 是否以百分号作为新的数字切割逻辑 所以同一套切割逻辑要有  或关系   有百分之结尾 或者  没有百分之结尾
        self.takingChineseNumberRERules = re.compile(
            '(?:(?:[正负]){0,1}(?:(?:[一二三四五六七八九十千万亿幺零百]+(?:点[一二三四五六七八九幺零]+){0,1})|(?:点[一二三四五六七八九幺零]+)))'
            '(?:(?:分之)(?:[正负]){0,1}(?:(?:[一二三四五六七八九十千万亿幺零百]+(?:点[一二三四五六七八九幺零]+){0,1})|'
            '(?:点[一二三四五六七八九幺零]+))){0,1}')
        # self.takingChineseNumberRERules = re.compile(
        #     '(?:(?:[正负]){0,1}(?:(?:[一二三四五六七八九十千万亿兆幺零百]+(?:点[一二三四五六七八九幺零]+){0,1})|(?:点[一二三四五六七八九幺零]+)))'
        #     '(?:(?:分之)(?:[正负]){0,1}(?:(?:[一二三四五六七八九十千万亿兆幺零百]+(?:点[一二三四五六七八九幺零]+){0,1})|'
        #     '(?:点[一二三四五六七八九幺零]+))){0,1}')

        # self.takingChineseDigitsMixRERules = re.compile('(?:(?:分之){0,1}(?:\+|\-){0,1}[正负]{0,1})'
        #                                                 '(?:(?:(?:\d+(?:\.\d+){0,1}(?:[\%\‰\‱]){0,1}|\.\d+(?:[\%\‰\‱]){0,1}){0,1}'
        #                                                 '(?:(?:(?:[一二三四五六七八九十千万亿兆幺零百]+(?:点[一二三四五六七八九幺零]+){0,1})|(?:点[一二三四五六七八九幺零]+))))'
        #                                                 '|(?:(?:\d+(?:\.\d+){0,1}(?:[\%\‰\‱]){0,1}|\.\d+(?:[\%\‰\‱]){0,1})'
        #                                                 '(?:(?:(?:[一二三四五六七八九十千万亿兆幺零百]+(?:点[一二三四五六七八九幺零]+){0,1})|(?:点[一二三四五六七八九幺零]+))){0,1}))')
        self.takingChineseDigitsMixRERules = re.compile('(?:(?:分之){0,1}(?:\+|\-){0,1}[正负]{0,1})'
                                                        '(?:(?:(?:\d+(?:\.\d+){0,1}(?:[\%\‰\‱]){0,1}|\.\d+(?:[\%\‰\‱]){0,1}){0,1}'
                                                        '(?:(?:(?:[一二三四五六七八九十千万亿幺零百]+(?:点[一二三四五六七八九幺零十]+){0,1})|(?:点[一二三四五六七八九幺零十]+))))'
                                                        '|(?:(?:\d+(?:\.\d+){0,1}(?:[\%\‰\‱]){0,1}|\.\d+(?:[\%\‰\‱]){0,1})'
                                                        '(?:(?:(?:[一二三四五六七八九十千万亿幺零百]+(?:点[一二三四五六七八九幺零十]+){0,1})|(?:点[一二三四五六七八九幺零十]+))){0,1}))')
        # self.takingChineseDigitsMixRERules = re.compile('(?:(?:分之){0,1}(?:\+|\-){0,1}[正负]{0,1})'
        #                                                 '(?:(?:(?:\d+(?:\.\d+){0,1}(?:[\%\‰\‱]){0,1}|\.\d+(?:[\%\‰\‱]){0,1}){0,1}'
        #                                                 '(?:(?:(?:[一二三四五六七八九十千万亿兆幺零百]+(?:点[一二三四五六七八九幺零十]+){0,1})|(?:点[一二三四五六七八九幺零十]+))))'
        #                                                 '|(?:(?:\d+(?:\.\d+){0,1}(?:[\%\‰\‱]){0,1}|\.\d+(?:[\%\‰\‱]){0,1})'
        #                                                 '(?:(?:(?:[一二三四五六七八九十千万亿兆幺零百]+(?:点[一二三四五六七八九幺零十]+){0,1})|(?:点[一二三四五六七八九幺零十]+))){0,1}))')
        self.PURE_DIGITS_RE = re.compile('[0-9]')
        self.PURE_DIGITS_RE = re.compile('[0-9]')
        self.DIGITS_CHAR_LIST = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
        self.DIGITS_SIGN_LIST = ['-', '+']
        self.DIGITS_CONNECTING_SIGN_LIST = ['.']
        self.DIGITS_PER_COUNTING_STRING_LIST = ['%', '‰', '‱']
        self.takingDigitsRERule = re.compile(
            '(?:(?:\+|\-){0,1}\d+(?:\.\d+){0,1}(?:[\%\‰\‱]){0,1}|(?:\+|\-){0,1}\.\d+(?:[\%\‰\‱]){0,1})')

    def coreCHToDigits(self, chineseChars):
        total = 0
        tempVal = ''  # 用以记录临时是否建议数字拼接的字符串 例如 三零万 的三零
        countingUnit = 1  # 表示单位：个十百千,用以计算单位相乘 例如八百万 百万是相乘的方法，但是如果万前面有 了一千八百万 这种，千和百不能相乘，要相加...
        countingUnitFromString = [
            1]  # 原始字符串提取的单位应该是一个list  在计算的时候，新的单位应该是本次取得的数字乘以已经发现的最大单位，例如 4千三百五十万， 等于 4000万+300万+50万
        for i in range(len(chineseChars) - 1, -1, -1):
            val = self.common_used_ch_numerals.get(chineseChars[i])
            # print(val,i,self.common_used_ch_numerals,chineseChars)
            if val >= 10 and i == 0:  # 应对 十三 十四 十*之类，说明为十以上的数字，看是不是十三这种
                # 说明循环到了第一位 也就是最后一个循环 看看是不是单位开头
                # 取最近一次的单位
                if val > countingUnit:  # 如果val大于 contingUnit 说明 是以一个更大的单位开头 例如 十三 千二这种
                    countingUnit = val  # 赋值新的计数单位
                    total = total + val  # 总值等于  全部值加上新的单位 类似于13 这种
                    countingUnitFromString.append(val)
                else:
                    countingUnitFromString.append(val)
                    # 计算用的单位是最新的单位乘以字符串中最大的原始单位  为了计算四百万这种
                    countingUnit = max(countingUnitFromString) * val
            elif val >= 10:
                if val > countingUnit:
                    countingUnit = val
                    countingUnitFromString.append(val)
                else:
                    countingUnitFromString.append(val)
                    # 计算用的单位是最新的单位乘以字符串中最大的原始单位 为了计算四百万这种
                    countingUnit = max(countingUnitFromString) * val
            else:
                if i > 0:
                    # 如果下一个不是单位 则本次也是拼接
                    if self.common_used_ch_numerals.get(chineseChars[i - 1]) < 10:
                        tempVal = str(val) + tempVal
                    else:
                        # 说明已经有大于10的单位插入 要数学计算了
                        # 先拼接再计算
                        # 如果取值不大于10 说明是0-9 则继续取值 直到取到最近一个大于10 的单位   应对这种30万20千 这样子
                        total = total + countingUnit * int(str(val) + tempVal)
                        # 计算后 把临时字符串置位空
                        tempVal = ''
                else:
                    # 那就是无论如何要收尾了
                    total = total + countingUnit * int(str(val) + tempVal)

        # 如果 total 为0  但是 countingUnit 不为0  说明结果是 十万这种  最终直接取结果 十万
        # 如果countingUnit 大于10 说明他是就是 汉字零
        if total == 0 and countingUnit > 10:
            total = str(countingUnit)
        else:
            total = str(total)
        if total.endswith('.0'):
            total = total[:-2]
        return total

    def chineseToDigits(self, chineseDigitsMixString, *args, **kwargs):
        # 之前已经做过罗马数字变汉字 所以不存在罗马数字部分问题了
        """
        分之  分号切割  要注意
        """
        chineseCharsListByDiv = chineseDigitsMixString.split('分之')
        convertResultList = []
        for k in range(len(chineseCharsListByDiv)):
            tempChineseChars = chineseCharsListByDiv[k]

            chineseChars = tempChineseChars
            chineseCharsDotSplitList = []

            """
            看有没有符号
            """
            sign = ''
            for chars in tempChineseChars:
                if self.CHINESE_SIGN_DICT.get(chars) is not None:
                    sign = self.CHINESE_SIGN_DICT.get(chars)
                    tempChineseChars = tempChineseChars.replace(chars, '')
            """
            防止没有循环完成就替换 报错
            """
            chineseChars = tempChineseChars

            """
            小数点切割，看看是不是有小数点
            """
            for chars in list(self.CHINESE_CONNECTING_SIGN_DICT.keys()):
                if chars in chineseChars:
                    chineseCharsDotSplitList = chineseChars.split(chars)

            if chineseCharsDotSplitList.__len__() == 0:
                convertResult = self.coreCHToDigits(chineseChars)
            else:
                convertResult = ''
                # 如果小数点右侧有 单位 比如 2.55万  4.3百万 的处理方式
                # 先把小数点右侧单位去掉
                tempCountString = ''
                for ii in range(len(chineseCharsDotSplitList[-1]) - 1, -1, -1):
                    if chineseCharsDotSplitList[-1][ii] in ['千', '百', '万']:
                        tempCountString = chineseCharsDotSplitList[-1][ii] + tempCountString
                    else:
                        chineseCharsDotSplitList[-1] = chineseCharsDotSplitList[-1][0:(ii + 1)]
                        break
                if tempCountString != '':
                    tempCountNum = float(self.coreCHToDigits(tempCountString))
                else:
                    tempCountNum = 1.0
                if chineseCharsDotSplitList[0] == '':
                    """
                    .01234 这种开头  用0 补位
                    """
                    convertResult = '0.' + self.coreCHToDigits(chineseCharsDotSplitList[1])
                elif chineseCharsDotSplitList[1][0]=='零':
                    """
                    10.03 这种情况
                    """
                    convertResult = self.coreCHToDigits(chineseCharsDotSplitList[0]) + '.0' + self.coreCHToDigits(
                        chineseCharsDotSplitList[1])
                else:
                    convertResult = self.coreCHToDigits(chineseCharsDotSplitList[0]) + '.' + self.coreCHToDigits(
                        chineseCharsDotSplitList[1])

                convertResult = str(float(convertResult) * tempCountNum)
            """
            如果 convertResult 是空字符串， 表示可能整体字符串是 负百分之10 这种  或者 -百分之10
            """
            if convertResult == '':
                convertResult = '1'

            convertResult = sign + convertResult
            # 最后在双向转换一下 防止出现 0.3000 或者 00.300的情况
            convertResult = str(float(convertResult))
            if convertResult.endswith('.0'):
                convertResult = convertResult[:-2]
            convertResultList.append(convertResult)
        if len(convertResultList) > 1:
            # 是否转换分号及百分比
            if convertResultList[0] == '100':
                finalTotal = convertResultList[1] + '%'
            elif convertResultList[0] == '1000':
                finalTotal = convertResultList[1] + '‰'
            elif convertResultList[0] == '10000':
                finalTotal = convertResultList[1] + '‱'
            else:
                finalTotal = convertResultList[1] + '/' + convertResultList[0]
        else:
            finalTotal = convertResultList[0]
        return finalTotal

    def chineseToDigitsHighTolerance(self, chineseDigitsMixString, skipError=False, errorChar=[], errorMsg=[]):
        if skipError:
            try:
                total = self.chineseToDigits(chineseDigitsMixString)
            except Exception as e:
                # 返回类型不能是none 是空字符串
                total = ''
                errorChar.append(chineseDigitsMixString)
                errorMsg.append(str(e))
        else:
            total = self.chineseToDigits(chineseDigitsMixString)
        return total

    def checkChineseNumberReasonable(self, chNumber):
        if chNumber.__len__() > 0:
            # 由于在上个检查点 已经把阿拉伯数字转为中文 因此不用检查阿拉伯数字部分
            """
            如果汉字长度大于0 则判断是不是 万  千  单字这种
            """
            # print(chNumber)
            if chNumber[0] in '点':
                return False
            elif len(chNumber) >= 3 and chNumber[2] in '点': #十四点二
                return True
            elif len(chNumber) >= 4 and re.search('^二零|^一[七八九]', chNumber):  # 日历的留着
                return True
            elif len(chNumber) >= 2 and chNumber[0] in '十百千万亿幺一二两三四五六七八九零' and chNumber[1] in '幺一二两三四五六七八九零万':  # 万一这种的不要转
                return False

            # # 万一 的这种不要转 
            # elif len(chNumber) >= 2 :
            #     if chNumber[0] in "千万亿" and chNumber[1] in "零一二两三四五六七八九":
            #         return False
            #     elif chNumber[0] in "零一二两三四五六七八九" and chNumber[1] in "万亿":
            #         return False
            # elif re.search('到[]')
            #self.CHINESE_PURE_NUMBER_LIST = ['幺', '一', '二', '两', '三', '四', '五', '六', '七', '八', '九', '十', '零']
            for i in self.CHINESE_PURE_NUMBER_LIST:
                if len(chNumber) > 1 and i in chNumber:
                    # 只要有数字在字符串 就说明不是 千千万万这种只有单位的表述
                    return True
        return False

    def checkChineseNumberReasonable2(self, chNumber):
        if chNumber.__len__() > 0:
            # 由于在上个检查点 已经把阿拉伯数字转为中文 因此不用检查阿拉伯数字部分
            """
            如果汉字长度大于0 则判断是不是 万  千  单字这种
            """
            count = 0
            if chNumber[0] == '点':
                return False
            if len(chNumber) == 2 and chNumber[0] in self.common_used_ch_numerals and chNumber[
                1] in self.common_used_ch_numerals:
                return False
            for i in self.CHINESE_PURE_NUMBER_LIST:
                if len(chNumber) > 1 and i in chNumber:
                    # 只要有数字在字符串 就说明不是 千千万万这种只有单位的表述
                    return True
        return False

    """
    繁体简体转换 及  单位  特殊字符转换 两千变二千
    """

    def traditionalTextConvertFunc(self, chString, traditionalConvertSwitch=True):
        chStringList = list(chString)
        stringLength = len(list(chStringList))

        if traditionalConvertSwitch == True:
            for i in range(stringLength):
                # 繁体中文数字转简体中文数字
                if self.TRADITIONAl_CONVERT_DICT.get(chStringList[i], '') != '':
                    chStringList[i] = self.TRADITIONAl_CONVERT_DICT.get(chStringList[i], '')

        # 检查繁体单体转换
        for i in range(stringLength):
            # 如果 前后有 pure 汉字数字 则转换单位为简体
            if self.SPECIAL_TRADITIONAl_COUNTING_UNIT_CHAR_DICT.get(chStringList[i], '') != '':
                # 如果前后有单纯的数字 则进行单位转换
                if i == 0:
                    if chStringList[i + 1] in self.CHINESE_PURE_NUMBER_LIST:
                        chStringList[i] = self.SPECIAL_TRADITIONAl_COUNTING_UNIT_CHAR_DICT.get(chStringList[i], '')
                elif i == stringLength - 1:
                    if chStringList[i - 1] in self.CHINESE_PURE_NUMBER_LIST:
                        chStringList[i] = self.SPECIAL_TRADITIONAl_COUNTING_UNIT_CHAR_DICT.get(chStringList[i], '')
                else:
                    if chStringList[i - 1] in self.CHINESE_PURE_NUMBER_LIST or \
                            chStringList[i + 1] in self.CHINESE_PURE_NUMBER_LIST:
                        chStringList[i] = self.SPECIAL_TRADITIONAl_COUNTING_UNIT_CHAR_DICT.get(chStringList[i], '')
            # 特殊变换 俩变二
            if self.SPECIAL_NUMBER_CHAR_DICT.get(chStringList[i], '') != '':
                # 如果前后有单位 则进行转换
                if i == 0:
                    if chStringList[i + 1] in self.CHINESE_PURE_COUNTING_UNIT_LIST:
                        chStringList[i] = self.SPECIAL_NUMBER_CHAR_DICT.get(chStringList[i], '')
                elif i == stringLength - 1:
                    if chStringList[i - 1] in self.CHINESE_PURE_COUNTING_UNIT_LIST:
                        chStringList[i] = self.SPECIAL_NUMBER_CHAR_DICT.get(chStringList[i], '')
                else:
                    if chStringList[i - 1] in self.CHINESE_PURE_COUNTING_UNIT_LIST or \
                            chStringList[i + 1] in self.CHINESE_PURE_COUNTING_UNIT_LIST:
                        chStringList[i] = self.SPECIAL_NUMBER_CHAR_DICT.get(chStringList[i], '')
        return ''.join(chStringList)

    """
    标准表述转换  三千二 变成 三千二百 三千十二变成 三千零一十二 四万十五变成四万零十五
    """

    def standardChNumberConvert(self, chNumberString):
        chNumberStringList = list(chNumberString)

        # 大于2的长度字符串才有检测和补位的必要
        if len(chNumberStringList) > 2:
            # 十位补一：
            try:
                tenNumberIndex = chNumberStringList.index('十')
                if tenNumberIndex == 0:
                    chNumberStringList.insert(tenNumberIndex, '一')
                else:
                    # 如果没有左边计数数字 插入1
                    if chNumberStringList[tenNumberIndex - 1] not in self.CHINESE_PURE_NUMBER_LIST:
                        chNumberStringList.insert(tenNumberIndex, '一')
            except:
                pass

            # 差位补零
            # 逻辑 如果最后一个单位 不是十结尾 而是百以上 则数字后面补一个比最后一个出现的单位小一级的单位
            # 从倒数第二位开始看,且必须是倒数第二位就是单位的才符合条件
            try:
                lastCountingUnit = self.CHINESE_PURE_COUNTING_UNIT_LIST.index(
                    chNumberStringList[len(chNumberStringList) - 2])
                # 如果最末位的是百开头
                if lastCountingUnit >= 1:
                    # 则字符串最后拼接一个比最后一个单位小一位的单位 例如四万三 变成四万三千

                    # 如果最后一位结束的是亿 则补千万
                    if lastCountingUnit == 4:
                        chNumberStringList.append('千万')
                    else:
                        chNumberStringList.append(self.CHINESE_PURE_COUNTING_UNIT_LIST[lastCountingUnit - 1])
            except:
                pass
        # 检查是否是 万三  千四点五这种表述 百三百四
        perCountSwitch = 0
        if len(chNumberStringList) > 1:
            if chNumberStringList[0] in ['千', '万', '百']:
                for i in range(1, len(chNumberStringList)):
                    # 其余位数都是纯数字 才能执行
                    if chNumberStringList[i] in self.CHINESE_PURE_NUMBER_LIST:
                        perCountSwitch = 1
                    else:
                        perCountSwitch = 0
                        # y有一个不是数字 直接退出循环
                        break
        if perCountSwitch == 1:
            chNumberStringList = chNumberStringList[:1] + ['分', '之'] + chNumberStringList[1:]
        return ''.join(chNumberStringList)

    def checkNumberSeg(self, chineseNumberList, originText):
        newChineseNumberList = []
        # 用来控制是否前一个已经合并过  防止多重合并
        tempPreText = ''
        tempMixedString = ''
        segLen = len(chineseNumberList)
        if segLen > 0:
            # 加入唯一的一个 或者第一个
            if chineseNumberList[0][:2] in self.CHINESE_PER_COUNTING_SEG:
                # 如果以分之开头 记录本次 防止后面要用 是否出现连续的 分之
                tempPreText = chineseNumberList[0]
                newChineseNumberList.append(chineseNumberList[0][2:])
            else:
                newChineseNumberList.append(chineseNumberList[0])

            if len(chineseNumberList) > 1:
                for i in range(1, segLen):
                    # 判断本字符是不是以  分之  开头
                    if chineseNumberList[i][:2] in self.CHINESE_PER_COUNTING_SEG:
                        # 如果是以 分之 开头 那么检查他和他见面的汉子数字是不是连续的 即 是否在原始字符串出现
                        tempMixedString = chineseNumberList[i - 1] + chineseNumberList[i]
                        if tempMixedString in originText:
                            # 如果连续的上一个字段是以分之开头的  本字段又以分之开头
                            if tempPreText != '':
                                # 检查上一个字段的末尾是不是 以 百 十 万 的单位结尾
                                if tempPreText[-1] in self.CHINESE_PURE_COUNTING_UNIT_LIST:
                                    # 先把上一个记录进去的最后一位去掉
                                    newChineseNumberList[-1] = newChineseNumberList[-1][:-1]
                                    # 如果结果是确定的，那么本次的字段应当加上上一个字段的最后一个字
                                    newChineseNumberList.append(tempPreText[-1] + chineseNumberList[i])
                                else:
                                    # 如果上一个字段不是以单位结尾  同时他又是以分之开头，那么 本次把分之去掉
                                    newChineseNumberList.append(chineseNumberList[i][2:])
                            else:
                                # 上一个字段不以分之开头，那么把两个字段合并记录
                                if newChineseNumberList.__len__() > 0:
                                    newChineseNumberList[-1] = tempMixedString
                                else:
                                    newChineseNumberList.append(tempMixedString)
                        else:
                            # 说明前一个数字 和本数字不是连续的
                            # 本数字去掉分之二字
                            newChineseNumberList.append(chineseNumberList[i][2:])

                        # 记录以 分之 开头的字段  用以下一个汉字字段判别
                        tempPreText = chineseNumberList[i]
                    else:
                        # 不是  分之 开头 那么把本数字加入序列
                        newChineseNumberList.append(chineseNumberList[i])
                        # 记录把不是 分之 开头的字段  临时变量记为空
                        tempPreText = ''
        return newChineseNumberList

    def checkSignSeg(self, chineseNumberList):
        newChineseNumberList = []
        tempSign = ''
        for i in range(len(chineseNumberList)):
            # 新字符串 需要加上上一个字符串 最后1位的判断结果
            newChNumberString = tempSign + chineseNumberList[i]
            lastString = newChNumberString[-1:]
            # 如果最后1位是正负号 那么本字符去掉最后1位  下一个数字加上最后3位
            if lastString in self.CHINESE_SIGN_LIST:
                tempSign = lastString
                # 如果最后1位 是  那么截掉最后1位
                newChNumberString = newChNumberString[:-1]
            else:
                tempSign = ''
            newChineseNumberList.append(newChNumberString)
        return newChineseNumberList

    def takeChineseNumberFromString(self, chText, traditionalConvert=True, verbose=False, *args, **kwargs):
        """
        :param chText: chinese string
        :param traditionalConvert: Switch to convert the Traditional Chinese character to Simplified chinese
        :return: Dict like result. 'inputText',replacedText','CHNumberStringList':CHNumberStringList,'digitsStringList'
        """

        """
        是否只提取数字
        """

        """
        简体转换开关
        """
        # originText = chText

        convertedCHString = self.traditionalTextConvertFunc(chText, traditionalConvert)
        if debug:
            print("convertedCHString  ", end="   ")
            print(convertedCHString)

        #不能光看数字判断是否要转，还得看上下文，例如： 九点一刻
        def convert_flag(s):  
            if re.search("点一刻",s):
                return False
            elif re.search("点.*分",s):
                return False
            elif re.search("[零一二两三四五六七八九十]千[克米]",s):
                return False
            return True
        c_flag = convert_flag(convertedCHString)

        """
        字符串 汉字数字字符串切割提取
        正则表达式方法
        """
        CHNumberStringListTemp = self.takingChineseDigitsMixRERules.findall(convertedCHString)
        if debug:
            print("find all dights rules CHNumberStringListTemp  ", end="   ")
            print(CHNumberStringListTemp)
        # 检查是不是  分之 切割不完整问题
        CHNumberStringListTemp = self.checkNumberSeg(CHNumberStringListTemp, convertedCHString)

        # 检查末位是不是正负号
        CHNumberStringListTemp = self.checkSignSeg(CHNumberStringListTemp)

        # # 将不标准的汉字表示去除
        # CHNumberStringListTemp = [i for i in
        #                           list(map(lambda x: self.standardChNumberConvert(x), CHNumberStringListTemp)) if i]

        if debug:
            print("CHNumberStringListTemp  ", end="   ")
            print(CHNumberStringListTemp)

        # 备份一个原始的提取，后期处结果的时候显示用
        OriginCHNumberTake = CHNumberStringListTemp.copy()

        # 检查合理性 是否是单纯的单位  等
        CHNumberStringList = []
        OriginCHNumberForOutput = []
        for i in range(len(CHNumberStringListTemp)):
            tempText = CHNumberStringListTemp[i]
            if debug:
                print("check tempText ", end='   ')
                print(tempText, end='   ')
                print('will be checked reasonable later ')
                print(self.checkChineseNumberReasonable(tempText) and c_flag)
            if self.checkChineseNumberReasonable(tempText) and c_flag :
                # 如果合理  则添加进被转换列表,True 进行转化，False 不转
                CHNumberStringList.append(tempText)
                # 则添加把原始提取的添加进来
                OriginCHNumberForOutput.append(OriginCHNumberTake[i])
        # TODO 检查是否 时间格式 五点四十  七点一刻
        # CHNumberStringListTemp = CHNumberStringList.copy()

        """
        进行标准汉字字符串转换 例如 二千二  转换成二千零二
        """
        CHNumberStringListTemp = list(map(lambda x: self.standardChNumberConvert(x), CHNumberStringList))
        if debug:
            print("CHNumberStringListTemp,CHNumberStringList", end='   ')
            print(CHNumberStringListTemp, CHNumberStringList)
        """
        将中文转换为数字
        """
        digitsStringList = []
        replacedText = convertedCHString
        # replacedText = self.danwei_change(convertedCHString)  # 原始数据先转，防止十八千克 的千 先转成数字
        # print(replacedText)
        # print(self.chineseToDigits(replacedText))
        # replacedText = self.rili_change(replacedText)   #原始数据先转，防止 七点一刻 先转成 七点一
        if debug:
            print('原始的 convertedCHString', end='   ')
            print(convertedCHString)
        errorCharList = []
        errorMsgList = []
        if CHNumberStringListTemp.__len__() > 0:
            for kk in range(len(CHNumberStringListTemp)):
                if debug:
                    print('chineseToDigitsHighTolerance', end='   ')
                    print(self.chineseToDigitsHighTolerance(CHNumberStringListTemp[kk], skipError=verbose,
                                                            errorChar=errorCharList, errorMsg=errorMsgList))
                digitsStringList.append(self.chineseToDigitsHighTolerance(CHNumberStringListTemp[kk], skipError=verbose,
                                                                          errorChar=errorCharList,
                                                                          errorMsg=errorMsgList))
            tupleToReplace = [(d, c, i) for d, c, i in
                              zip(OriginCHNumberForOutput, digitsStringList, list(map(len, OriginCHNumberForOutput))) if
                              c != '']

            """
            按照提取出的中文数字字符串长短排序，然后替换。防止百分之二十八 ，二十八，这样的先把短的替换完了的情况
            """
            tupleToReplace = sorted(tupleToReplace, key=lambda x: -x[2])
            for i in range(tupleToReplace.__len__()):
                replacedText = replacedText.replace(tupleToReplace[i][0], tupleToReplace[i][1])
        if debug:
            print('to do replaced text', end='   ')
            print(replacedText)

        if re.search(r'次方', replacedText):
            replacedText = self.scientific_count(replacedText)
            if debug:
                print('scientific_count', end='   ')
                print(replacedText)
        replacedText = self.danwei_change(replacedText)
        if debug:
            print('danwei_change', end='   ')
            print(replacedText)
        replacedText = self.yunsuan_change(replacedText)
        if debug:
            print('yunsuan_change', end='   ')
            print(replacedText)
        replacedText = self.fuhao_change(replacedText)
        if debug:
            print('fuhao_change', end='   ')
            print(replacedText)
        replacedText = self.rili_change(replacedText)
        if debug:
            print('rili_change', end='   ')
            print(replacedText)
        replacedText = self.time_change(replacedText)  
        if debug:
            print('time_change', end='   ')
            print(replacedText)

        finalResult = {
            'inputText': chText,
            'replacedText': replacedText,
            'CHNumberStringList': OriginCHNumberForOutput,
            'digitsStringList': digitsStringList,
            'errorWordList': errorCharList,
            'errorMsgList': errorMsgList
        }
        return finalResult

    def process(self, recog_seqs):
        for item in recog_seqs:
            item.result = self.takeChineseNumberFromString(item.result)['replacedText']

    # xuecheng 新加规则  :  支持科学计数法，   十四点二乘以十的九次方 ->   14.2*10^9
    def scientific_count(self, x):
        # print(x)
        # x = re.sub(r'乘以十', '*10', x)  # 只改 乘以十  的
        x = re.sub(r'十(的.*次方)', r'10\1', x)
        # print(x)
        # def c2d(x):
        #     x = self.chineseToDigits(x) if re.search('[零一二两三四五六七八九十百千]', x) else x
        #     return x
        # m_a = re.match('([^零一二两三四五六七八九十百千万]*)([零一二两三四五六七八九十百千万]*)', a)  # 不确定数字大小的，要设大一些
        # # print(m_a.groups())
        # a = m_a.group(1) + c2d(m_a.group(2))

        pattern = re.compile(r'([一二三四五六七八九十]+)(次方)')
        if pattern.search(x):
            num = pattern.search(x).group(1)
            num = self.chineseToDigits(num)
            x = pattern.sub(num + r'\2', x)  # 4.2*10的19次方
        pattern = re.compile(r'的([0-9]+)次方')
        x = pattern.sub(r'^\1', x)  # 10^19
        return x

    # xuecheng 新加规则  :  支持单位转换   5 每升 ->  5/L , 六点一八毫摩尔每升 -> 6.18mmol/L
    def danwei_change(self, res):
        # danwei_list=['升','摩尔','公里','千米','小时','克','厘米','毫米','千克','日','汞柱','分钟','单位','国际单位']
        # danwei_fuhao=['L','mol','km','km','h','g','cm','mm','kg','日','Hg','min','U','IU']
        danwei_list = ['升', '摩尔', '公里', '千米', '克', '厘米', '毫米', '日', '汞柱',  '单位', '国际单位',"小时","分钟"]
        danwei_fuhao = ['L', 'mol', 'km', 'km',  'g', 'cm', 'mm', '日', 'Hg',  'U', 'IU',"h","min"]
        danwei_prefix = ['毫', '微', '纳', '皮', '千']
        danwei_prefix_fuhao = ['m', 'u', 'n', 'p', 'k']

        # print('get',res)

        def shuzi_func(m):  # 十八千克 -> 18kg  , 九毫升 -> 9mL, # 先做转换，防止千转成数字，todo 应该收集 各种千、万 的词。
            # print(m.groups())
            a = m.group(1)
            b = m.group(2)

            def c2d(x):
                x = self.chineseToDigits(x) if re.search('[零一二两三四五六七八九十百千]', x) else x
                return x

            m_a = re.match('([^零一二两三四五六七八九十百千万]*)([零一二两三四五六七八九十百千万]*)', a)  # 不确定数字大小的，要设大一些
            # print(m_a.groups())
            a = m_a.group(1) + c2d(m_a.group(2))

            return a + b

        pat_shuzi = re.compile(r'(.*)(千克|毫升|毫克)')
        # pat_shuzi=re.compile(r'(.*)('+ '|'.join(danwei_list) +')')
        res = pat_shuzi.sub(shuzi_func, res)

        # print(res)

        def func_hasmei(m):  # 有 "每" 的情况下单位转换
            # print(m.groups())
            a = m.group(1)
            b = m.group(2)
            c = m.group(3)
            d = m.group(4)
            a = '' if a == '' else '/'
            c = danwei_prefix_fuhao[danwei_prefix.index(c)] if c else c
            d = danwei_fuhao[danwei_list.index(d)] if d else d
            return a + b + c + d

        # pattern_s = '(每)(' + '|'.join(danwei_prefix) + '?)(' + '|'.join(danwei_list) + ')'
        # pattern = re.compile(pattern_s.replace('\'', ''))
        # res = pattern.sub(func_hasmei, res)
        pattern_s = '(每)([零一二两三四五六七八九十百千万亿0-9]*)(' + '|'.join(danwei_prefix) + '?)(' + '|'.join(danwei_list) + ')'
        pattern = re.compile(pattern_s.replace('\'', ''))
        res = pattern.sub(func_hasmei, res)
        # print(res)

        def func_nomei(m):  # 没有"每"的情况下，单位转换,但是有前缀
            # print(m.groups())
            a = m.group(1)
            b = m.group(2)
            c = m.group(3)
            def c2d(x):
                x = self.chineseToDigits(x) if re.search('[零一二两三四五六七八九十百千]', x) else x
                return x

            if len(a) > 0 and re.search('[零一二两三四五六七八九十百千万亿0-9]', a[-1]):
                m_a = re.match('([^零一二两三四五六七八九十百千万]*)([零一二两三四五六七八九十百千万]*)', a)
                a = m_a.group(1) + c2d(m_a.group(2))

                b = danwei_prefix_fuhao[danwei_prefix.index(b)] if b else b
                c = danwei_fuhao[danwei_list.index(c)] if c else c
            return a + b + c

        # print(res)
        pattern_s = '(.*)(' + '|'.join(danwei_prefix) + ')(' + '|'.join(danwei_list) + ')'
        # print(pattern_s)  # (.*)(毫|微|纳|皮|千)(升|摩尔|公里|千米|小时|克|厘米|毫米|日|汞柱|分钟|单位|国际单位)
        pattern = re.compile(pattern_s.replace('\'', ''))
        res = pattern.sub(func_nomei, res)

        # print(res)
        def func_lianxu(m):  # 九毫米汞柱 ,连续单位
            # print(m.groups())
            a = m.group(1)
            b = m.group(2)
            c = m.group(3)
            def c2d(x):
                x = self.chineseToDigits(x) if re.search('[零一二两三四五六七八九十百千]', x) else x
                return x
            if len(a) > 0 and re.search('[零一二两三四五六七八九十百千万亿0-9]', a[-1]):
                m_a = re.match('([^零一二两三四五六七八九十百千万]*)([零一二两三四五六七八九十百千万]*)', a)
                a = m_a.group(1) + c2d(m_a.group(2))
                # if len(a) < 2 and not re.search('[0-9]', a):
                #     a = self.chineseToDigits(a)
                # else:
                #     a = self.takeChineseNumberFromString(a)['replacedText']

                b = danwei_fuhao[danwei_list.index(b)] if b else b
                c = danwei_fuhao[danwei_list.index(c)] if c else c
            return a + b + c

        pattern_s = '(.*)(' + '|'.join(danwei_list) + ')(' + '|'.join(danwei_list) + ')'
        # print(pattern_s) #(.*)(升|摩尔|公里|千米|小时|克|厘米|毫米|日|汞柱|分钟|单位|国际单位)(升|摩尔|公里|千米|小时|克|厘米|毫米|日|汞柱|分钟|单位|国际单位)
        pattern = re.compile(pattern_s.replace('\'', ''))
        res = pattern.sub(func_lianxu, res)

        # print(res)
        def func(m):  # 复杂的搞完了，最简单的单位转换
            # print(m.groups())
            a = m.group(1)
            c = m.group(2)
            def c2d(x):
                x = self.chineseToDigits(x) if re.search('[零一二两三四五六七八九十百千]', x) else x
                return x
            if len(a) > 0 and re.search('[零一二两三四五六七八九十百千万亿0-9]', a[-1]):
                m_a = re.match('([^零一二两三四五六七八九十百千万]*)([零一二两三四五六七八九十百千万]*)', a)
                a = m_a.group(1) + c2d(m_a.group(2))
                # if len(a) < 2 and not re.search('[0-9]', a):
                #     a = self.chineseToDigits(a)
                # else:
                #     a = self.takeChineseNumberFromString(a)['replacedText']

            if re.search('[0-9]', a):
                c = danwei_fuhao[danwei_list.index(c)] if c else c
            return a + c

        #去除一些不适合直接做单位的
        no_single_exit_list=['日','小时','分钟']
        for wrd in no_single_exit_list:
            to_remove_index=danwei_list.index(wrd)
            danwei_list.pop(to_remove_index)
            danwei_fuhao.pop(to_remove_index)
        pattern_s = '(.*)(' + '|'.join(danwei_list) + ')'
        pattern = re.compile(pattern_s.replace('\'', ''))
        res = pattern.sub(func, res)
        return res

    # xuecheng 新加规则  :  支持摄氏度 -> °C
    def fuhao_change(self, res):
        def func1(m):  
            # print(m.groups())  
            a = m.group(1)
            b = m.group(2)

            def c2d(x):
                x = self.chineseToDigits(x) if re.search('[零一二两三四五六七八九十]', x) else x
                return x

            m_a = re.match('([^零一二两三四五六七八九十百]*)([零一二两三四五六七八九十百千]*)', a)
            a = m_a.group(1) + c2d(m_a.group(2))
            b = '°C'

            return a + b

        pattern = re.compile(r'(.*)(摄氏度)')
        res = pattern.sub(func1, res)


        # pattern = re.compile(r'摄氏度')
        # res = pattern.sub('°C', res)

        # # 三级 -> III级
        # pattern = re.compile(r'([一二三])([级型])')
        # # print(res)
        # def ji_func(m):
        #     a = self.chineseToDigits(m.group(1))
        #     b = m.group(2)
        #     return 'I' * int(a) + b
        # res = pattern.sub(ji_func, res)

        # # L二 -> L2
        # pattern = re.compile(r'([a-zA-Z])([一二三四五六七八九十])')

        # def func(m):
        #     a = m.group(1)
        #     b = m.group(2)
        #     b = self.chineseToDigits(b)
        #     return a + b

        # res = pattern.sub(func, res)

        return res

    # xuecheng 新加规则  :  支持年月日 二零一八年九月十一号 -> 2018.9.11
    def rili_change(self, res):

        pattern = re.compile(r'(.{2})(年.+月.+)([日号])')  # 在func1 的基础上，修复年前面的两位数字 即可

        # print(res)
        def func2(m):  # 年月日不完整的  一八年九月十一号 -> 18.9.11
            # print(m.groups())
            a = m.group(1)
            b = m.group(2)
            c = m.group(3)

            def c2d(x):
                prefix = ''
                if len(x) == 2 and x[0] == '零':  #增加 08 年
                    prefix = '0'
                x = self.chineseToDigits(x) if re.search('[零一二两三四五六七八九十]', x) else x
                return prefix + x

            m_a = re.match('([^零一二两三四五六七八九十]*)([零一二两三四五六七八九十]*)', a)
            a = m_a.group(1) + c2d(m_a.group(2))

            return a +b + c

        res = pattern.sub(func2, res)

        pattern = re.compile(r'(年)(.{1,2})(月)(.{1,2})([日号])')
        # print(res)
        def func1(m):  # 年月日完整的  二零一八年九月十一号 -> 2018.9.11
            # print(m.groups())
            a = m.group(1)
            b = m.group(2)
            c = m.group(3)
            d = m.group(4)
            e = m.group(5)
            def c2d(x):
                x = self.chineseToDigits(x) if re.search('[零一二两三四五六七八九十]', x) else x
                return x
            m_b = re.match('([^零一二两三四五六七八九十]*)([零一二两三四五六七八九十]*)', b)
            b = m_b.group(1) + c2d(m_b.group(2))

            m_d = re.match('([^零一二两三四五六七八九十]*)([零一二两三四五六七八九十]*)', d)
            d = m_d.group(1) + c2d(m_d.group(2))

            return a + b + c + d + e

        res = pattern.sub(func1, res)

        pattern = re.compile(r'(.{2})(年.+月)')  # 在func3 的基础上，修复年前面的两位数字 即可

        def func4(m):  # 年月不完整的  一八年九月 -> 18.9
            a = m.group(1)
            b = m.group(2)
            def c2d(x):
                prefix = ''
                if len(x) == 2 and x[0] == '零':  #增加 08 年
                    prefix = '0'
                x = self.chineseToDigits(x) if re.search('[零一二两三四五六七八九十]', x) else x
                return prefix + x
            m_a = re.match('([^零一二两三四五六七八九十]*)([零一二两三四五六七八九十]*)', a)
            a = m_a.group(1) + c2d(m_a.group(2))
            return a + b

        res = pattern.sub(func4, res)

        pattern = re.compile(r'(年)(.{1,2})(月)')

        def func3(m):  # 年月完整的  二零一八年九月 -> 2018.9
            a = m.group(1)
            b = m.group(2)
            c = m.group(3)
            def c2d(x):
                x = self.chineseToDigits(x) if re.search('[零一二两三四五六七八九十]', x) else x
                return x
            m_b = re.match('([^零一二两三四五六七八九十]*)([零一二两三四五六七八九十]*)', b)
            b = m_b.group(1) + c2d(m_b.group(2))

            return a + b + c

        res = pattern.sub(func3, res)
        # 上面 func 1 - 4 都是表示日历的
        return res

    # xuecheng 新加规则  :  支持时间 九点四十 -> 9点40
    def time_change(self, res):
        pattern = re.compile(r'(.{1,3})(点)(.{1,3})(分)')

        def func1(m):  # 点 分完整的  九点三十分 -> 9:30
            # print(m.groups())  # ('二十一', '点', '三十九', '分')
            a = m.group(1)
            b = m.group(2)
            c = m.group(3)
            d = m.group(4)

            def c2d(x):
                prefix = ''
                if len(x) == 2 and x[0] == '零':  #增加 03 分 ，这种显示方式
                    prefix = '0'
                x = self.chineseToDigits(x) if re.search('[零一二两三四五六七八九十]', x) else x
                return prefix + x

            m_a = re.match('([^零一二两三四五六七八九十]*)([零一二两三四五六七八九十]*)', a)
            a = m_a.group(1) + c2d(m_a.group(2))

            m_c = re.match('([^零一二两三四五六七八九十]*)([零一二两三四五六七八九十]*)', c)
            c = m_c.group(1) + c2d(m_c.group(2))

            return a + b + c + d

        res = pattern.sub(func1, res)
        pattern = re.compile(r'(.{1,3})(点)(.{1,3})(分)')

        def func2(m):  # 没有分  九点三十 -> 9:30 ,九点零三 -> 9.03
            # print(m.groups())  # ('二十一', '点', '三十九', '分')
            a = m.group(1)
            b = m.group(2)
            c = m.group(3)
            d = m.group(4)

            def c2d(x):
                prefix = ''
                if len(x) == 2 and x[0] == '零':  #增加 03 分 ，这种显示方式
                    prefix = '0'
                x = self.chineseToDigits(x) if re.search('[零一二两三四五六七八九十]', x) else x
                return prefix + x

            m_a = re.match('([^零一二两三四五六七八九十]*)([零一二两三四五六七八九十]*)', a)
            a = m_a.group(1) + c2d(m_a.group(2))

            m_c = re.match('([^零一二两三四五六七八九十]*)([零一二两三四五六七八九十]*)', c)
            c = m_c.group(1) + c2d(m_c.group(2))

            return a + b + c + d
        # res = pattern.sub(func2, res)

        # # 八点整 -> 8:00 ,太复杂，暂时不要这样改
        # # print(res)
        # zheng_list = ['整', '半', '一刻']
        # zheng_fuhao = ['00', '30', '15']
        # # pattern=re.compile(r'(.)(点)([整|半|一刻])')
        # pattern = re.compile('(.)([点\.])(' + '|'.join(zheng_list) + ')')

        # def time_func(m):
        #     # print(m.groups())
        #     a = m.group(1)
        #     b = m.group(2)
        #     c = m.group(3)
        #     a = self.chineseToDigits(a) if not re.search('[0-9]', a) else a
        #     # b = ':'
        #     c = zheng_fuhao[zheng_list.index(c)]
        #     return a + b + c

        # # res = pattern.sub(time_func, res)
        # # print(res)
        return res

    # xuecheng 新加规则  :  支持四则运算 五加三 -> 5+3
    def yunsuan_change(self, res):
        # print(res)
        # yunsuan_list=['加','减','乘','除','至','杠','到']
        # yunsuan_fuhao=['+','-','*','/','-','-','-']
        yunsuan_list = ['加', '减', '乘', '除']
        yunsuan_fuhao = ['+', '-', '*', '/']
        yunsuan_list_tag = [['加上'], ['减去', '减掉'], ['乘上', '乘以'], ['除以']]
        yunsuan_chang_list = ['加上', '减去', '减掉', '乘上', '乘以', '除以']
        yunsuan_chang_fuhao = ['+', '-', '-', '*', '*', '/']
        shuzi_list = ['幺', '一', '二', '两', '三', '四', '五', '六', '七', '八', '九', '十', '零']
        shuzi_fuhao = ['1', '1', '2', '2', '3', '4', '5', '6', '7', '8', '9', '10', '0']

        # 1.5 % 乘以三袋  -> 1.5 % * 三袋 ,长的符号,2位数的
        pattern_chang = re.compile( '([a-zA-Z%])(' + '|'.join(yunsuan_chang_list) + ')([零一二两三四五六七八九十百千]+)')

        def zimu_func(m):
            # print(m.groups())
            a = m.group(1)
            b = m.group(2)
            c = m.group(3)
            # print(len(b))
            if len(b) < 2:
                b = yunsuan_fuhao[yunsuan_list.index(b)]
            else:
                b = yunsuan_chang_fuhao[yunsuan_chang_list.index(b)]
            c = self.chineseToDigits(c) if re.search('[零一二两三四五六七八九十百]', c) else c
            return a + b + c

        res = pattern_chang.sub(zimu_func, res)
        # print(res)

        # 不支持这种 D减 -> D- , ST杠T -> ST-T , 80%加 -> 80%+ 
        # 短 的符号，1位数的 加减乘除
        # print(res)
        pattern = re.compile('([a-zA-Z%])(' + str([''.join(yunsuan_list)]) + ')([一二三四五六七八九十零0-9]+)')  
        res = pattern.sub(zimu_func, res)
        # print(res)

        # 大于 5 ->  >5
        bijiao_list = ['大于', '小于', '等于']
        bijiao_fuhao = ['>', '<', '=']
        pattern = re.compile('(' + '|'.join(bijiao_list) + ')([一二三四五六七八九十零0-9])')

        def bijiao_func(m):
            a = m.group(1)
            b = m.group(2)
            a = bijiao_fuhao[bijiao_list.index(a)] if a else ''
            b = b if re.search('[0-9]', b) else self.chineseToDigits(b)
            return a + b

        res = pattern.sub(bijiao_func, res)
        # print(res)

        # pattern_s = '(' + str([''.join(shuzi_list)]) + '?)' + '(' + str(
        pattern_s = '([零一二两三四五六七八九十0-9]*)' + '(' + str(
            [''.join(yunsuan_list)]) + '[^零一二两三四五六七八九十0-9]?)([零一二两三四五六七八九十0-9]*)'
        pattern = re.compile(pattern_s.replace('\'', ''))  # 支持五减一 和 五减去一
        # print(pattern_s) #(['幺一二两三四五六七八九十零']?)(['加减乘除'][^零一二两三四五六七八九十0-9]?)([零一二两三四五六七八九十0-9]?)

        def func(m):
            # 处理 五加一 五 和 一 都转成5 1
            # print(m.groups())
            a = m.group(1)
            b = m.group(2)
            c = m.group(3)
            if a == '' and b == '到':
                return a + b + c  # 单独的一个"到"两边没有数字，不进行替换数字 : 到一定程度
            elif c == '' and b == '到':
                return a + b + c
            if a != "" and c != "":
                a = self.chineseToDigits(a) if re.search('[零一二两三四五六七八九十]', a) else a
                c = self.chineseToDigits(c) if re.search('[零一二两三四五六七八九十]', c) else c
            return a + b + c

        res = pattern.sub(func, res)
        # print(res)

        pattern_s1 = '' + str([''.join(shuzi_fuhao)]) + '' + str([''.join(yunsuan_list)]) + str(
            ["^" + ''.join(shuzi_fuhao)]) + '?'
        pattern_s2 = '' + str([''.join(yunsuan_list)]) + str(["^" + ''.join(shuzi_fuhao)]) + '?' + str(
            [''.join(shuzi_fuhao)]) + ''
        # print(pattern_s1)
        # print(pattern_s2)
        # ['11223456789100']['加减乘除']['^11223456789100']?
        # ['加减乘除']['^11223456789100']?['11223456789100']
        pattern1 = re.compile(pattern_s1.replace('\'', ''))
        pattern2 = re.compile(pattern_s2.replace('\'', ''))

        # print(res)
        flag = pattern1.search(res) or pattern2.search(res)  # 是否要转换 ,#todo 这个还不太科学，应该类似上面func的做法来修改加号，先临时处理一下。
        # print(flag)
        # 遍历，解决 5加1 变成5 + 1
        # n = len(yunsuan_list)
        # if flag:
        #     for i in range(n):
        #         if re.search(yunsuan_list[i], res):
        #             if i < len(yunsuan_list_tag):
        #                 for j in yunsuan_list_tag[i]:
        #                     if re.search(j, res):
        #                         res = re.sub(j, yunsuan_fuhao[i], res)
        #             res = re.sub(yunsuan_list[i], yunsuan_fuhao[i], res)

        def yunsuan_func(m): #用func的方式解决上面的遍历 
            # print(m.groups()) 
            a = m.group(1)
            b = m.group(2)
            c = m.group(3)
            flag = a!='' or c!=''
            if flag :
                if len(b)<2:
                    b = yunsuan_fuhao[yunsuan_list.index(b)]
                elif b in yunsuan_chang_list:
                    b = yunsuan_chang_fuhao[yunsuan_chang_list.index(b)]
            return a + b + c
                
        pattern_s1 = '([0-9]*)' + '(' + str([''.join(yunsuan_list)]) + '[^0-9]?)([0-9]*)'
        # print(pattern_s1)
        # ([0-9]*)(['加减乘除'][^0-9]?)([0-9]*)
        pattern = re.compile(pattern_s1.replace('\'', ''))  
        # print(res)
        res = pattern.sub(yunsuan_func , res)

        return res

        # yunsuan_list = ['加', '减', '乘', '除']
        # yunsuan_fuhao = ['+', '-', '*', '/']
        # yunsuan_list_tag = [['加上'], ['减去', '减掉'], ['乘上', '乘以'], ['除以']]
        # yunsuan_chang_list = ['加上', '减去', '减掉', '乘上', '乘以', '除以']
        # yunsuan_chang_fuhao = ['+', '-', '-', '*', '*', '/']
        # shuzi_list = ['幺', '一', '二', '两', '三', '四', '五', '六', '七', '八', '九', '十', '零']
        # shuzi_fuhao = ['1', '1', '2', '2', '3', '4', '5', '6', '7', '8', '9', '10', '0']


if __name__ == '__main__':
    # 正则引擎已经全部使用re2 规则 不再用pcre规则 防止出现递归炸弹
    a = itn()

    # # 四则运算
    # s= ['五加三','五减去三',"五乘九","九除以三"]
    # s.extend(['十减三','十减去十三',"十五乘以十九","二十九除以十三"])
    # s.extend(['二十五除三十二','五百减去三',"二百五乘以十九","九百零三除以三十三"])


    # s.extend( ["十四点二乘以十的九次方每升", "六点一八毫摩尔每升", "百分之六十六点二", "三千二百毫升", "N百分之七十八点八", "三加", "CPR六十五点七四毫克每升", "八百零七单位每升", "三十八摄氏度", "七至八"])
    # s.extend(["五十克", "ST杠T", "S杠一百", "四十七点六微摩尔每升", "一点五厘米", "二十六毫米", "百分之五十加", "二十八乘十一毫米", "D减", "零点四克加二百五十毫升"])
    # s.extend(["一千四百三十六国际单位每升", "二十四克每升", "八千克", "一次每日", "三至四次每日", "HB一百一十克每升", "CTNL十一点三纳克每毫升", "CKMB二十八点六纳克每毫升",           "三百一十一乘以十的九次方每升", "一百一十八点九毫米汞柱"])
    # s.extend(["二零一八年十月十八日", "PHTC", "CT一", "零点五乘零点五厘米", "二零一八年九月十一号", "百分之一点五乘以三袋", "六百至七百微摩尔每升", "二毫克每日", "五百毫升每二十四小时" ])#,
    #           # "百分之一点五到百分之二点五到百分之一点五到百分之二点五"])
    # s.extend(["零点五至一点二克每二十四小时", "二点五克每二十四小时", "L四杠五", "三十七点八至三十九点八摄氏度", "乘一", "三至五天", "加四", "二至三分钟", "十点一一HPF", "二零一八零九二二九"])
    s = []
    # s.extend(
    #     ["PCT四点六二微克每升", "一百三十八点四毫克每毫升", "ALT一百六十六个单位每升", "十至十五厘米", "CA一九九", "INR一点零九", "L二", "六十毫克", "一百零一皮克每毫升", "一型"])
    # s.extend(["二十点整", "小于零点四九九毫克每升", "二零一八一一一三", "三至五分钟", "LVEF 百分之二十三", "A一 forrest 三级", "C十三"])
    # s.extend(['万一呢是吧', '万分之五', '到一定程度'])
    # s.extend(['先给大家两个关键字提点一下', '考四六级', '九到十万', '百分之四百三十二万分之四三千分之五', 'llalala万三威风威风千四五', '百分之二点一六', '万一'])
    # s.extend(['千四五', '亿万', '五四运动', '一百'])
    # s=['千四五', '亿万', '五四运动', '一百']
    # s.extend(['小时', '一个多小时', '多少分钟', '几分钟', '三分钟', '二十分钟', '八小时'])
    # s=['一千四百三十六单位每升']
    # s=['一千四百三十六单位']
    # s=['十九毫米汞柱']
    # s = ['十五千克']
    # s = ['称重一千四百三十六千克']
    # badcase = ['说那么个五分钟十分钟的', '再加一点', '三四十分钟', "到一定程度", "万一", "先给大家两个关键字提点一下", "考四六级 ", "二零一七年的二月份", "九到十万", "一个多小时"]
    # s = badcase
    # s.extend(['二零一九年三月', '九点三十分', '十分钟', '茅台跌到一千八', '海拔两千七百米'])
    # s.extend(['一八年九月','二零二一年十一月','二一年三月','零八年十月十一号','二零二一年一月十号'])
    s.extend(['十点零三', '八点半', '现在九点三十分', '二十一点三十九分'])
    s = ['现在九点二十三分']
    s = ['一百二十万']
    s = ['再加一点','同比减少百分之三十四毛利']
    # s = ['七月二十三号,七月二十几号']

    j = 0
    for i in s:
        print("\""+a.takeChineseNumberFromString(i)['replacedText']+"\",", end="   ")
        j += 1
        if j % 4 == 0:
            print('')
    print('\n')
