# -*- coding=utf-8 -*-


# 手机号码
CELL_PHONE_PATTERN = '(?<=[^\d])(((\+86)?([- ])?)?((13[0-9])|(14[0-9])|(15[0-9])|(17[0-9])|(18[0-9])|(19[0-9]))([- ])?\d{4}([- ])?\d{4})(?=[^\d])'

# 中文字符正则
CHINESE_CHAR_PATTERN = '[\u4E00-\u9FA5]'

# 国内固定电话号码
LANDLINE_PHONE_PATTERN = '(?<=[^\d])(([\(（])?0\d{2,3}[\)） —-]\d{7,8}|\d{3,4}[ -]\d{3,4}[ -]\d{4})(?=[^\d])'
# PHONE_NUMBER_PATTERN_2 = '(?<!\d) \d{2,3}-\d{7,8}  (?!\d)'  # 固话

# 电子邮箱
# 邮箱中，允许中文等字符存在。但是，中文字符、#、* 会对结果造成较大干扰故忽略
EMAIL_PATTERN = '(?<=[^0-9a-zA-Z.\-])([a-zA-Z0-9_.-]+@[a-zA-Z0-9_.-]+(?:\.[a-zA-Z0-9_.-]+)*\.[a-zA-Z0-9]{2,6})(?=[^0-9a-zA-Z.\-])'
# 抽取邮箱的域名
EMAIL_DOMAIN_PATTERN = '(?<=@)([0-9a-zA-Z]+)(?=\.)'

# 异常字符
EXCEPTION_PATTERN = '[^ ¥～「」％－＋\n　一-龥!-~·×—‘’“”…、。《》『』【】！（），：；？]'

# HTML 标签
HTML_TAG_PATTERN = '<[^<\u4E00-\u9FA5，。；！？、“”‘’（）—《》…●]+?>'

# 中国身份证号
# 身份证共计18位，1,2位省份，3,4位城市，5,6位县区码，7~14位为出生日期，最后一位为校验码，做了严格限定
ID_CARD_PATTERN = '(?<=[^0-9a-zA-Z])((1[1-5]|2[1-3]|3[1-7]|4[1-6]|5[0-4]|6[1-5]|71|81|82|91)(0[0-9]|1[0-9]|2[0-9]|3[0-4]|4[0-3]|5[1-3]|90)(0[0-9]|1[0-9]|2[0-9]|3[0-9]|4[0-3]|5[1-7]|6[1-4]|7[1-4]|8[1-7])(18|19|20)\d{2}(0[1-9]|1[0-2])(0[1-9]|[12][0-9]|3[01])\d{3}[0-9xX])(?=[^0-9a-zA-Z])'
ID_CARD_CHECK_PATTERN = '^(1[1-5]|2[1-3]|3[1-7]|4[1-6]|5[0-4]|6[1-5]|71|81|82|91)(0[0-9]|1[0-9]|2[0-9]|3[0-4]|4[0-3]|5[1-3]|90)(0[0-9]|1[0-9]|2[0-9]|3[0-9]|4[0-3]|5[1-7]|6[1-4]|7[1-4]|8[1-7])(18|19|20)\d{2}(0[1-9]|1[0-2])(0[1-9]|[12][0-9]|3[01])\d{3}[0-9xX]$'

# IP地址
# 0~255.0~255.0~255.0~255
IP_ADDRESS_PATTERN = '(?<=[^0-9])((25[0-5]|2[0-4]\d|[0-1]\d{2}|[1-9]?\d)\.(25[0-5]|2[0-4]\d|[0-1]\d{2}|[1-9]?\d)\.(25[0-5]|2[0-4]\d|[0-1]\d{2}|[1-9]?\d)\.(25[0-5]|2[0-4]\d|[0-1]\d{2}|[1-9]?\d))(?=[^0-9])'

# 金额表达式
# start: (?<=[^\d一二三四五六七八九十壹贰叁肆伍陆柒捌玖拾两〇O零百千万萬亿佰仟])
# end: (?=[^\d一二三四五六七八九十壹贰叁肆伍陆柒捌玖拾两〇O零百千万萬亿佰仟美元块钱角分毛])
MONEY_PATTERN = '(\d[,，\d]*\.?\d+|[一二三四五六七八九十壹贰叁肆伍陆柒捌玖拾两][一二三四五六七八九十壹贰叁肆伍陆柒捌玖拾两〇O零百千万萬亿佰仟]*?)(余?)[百千万萬亿佰仟]*?美?(元|块钱)((\d[,.，\d]*|[一二三四五六七八九十壹贰叁肆伍陆柒捌玖拾两零][一二三四五六七八九十壹贰叁肆伍陆柒捌玖拾两〇O零百千万萬亿佰仟]*?)(角|毛))?((\d[,.\d]*|[>一二三四五六七八九十壹贰叁肆伍陆柒捌玖拾两零][一二三四五六七八九十壹贰叁肆伍陆柒捌玖拾两〇O零百千万萬亿佰仟]*?)分)?'

# 中文括号
PARENTHESES_PATTERN = '{}「」[]【】()（）<>《》'

# 腾讯QQ号
QQ_PATTERN = '(?<=[^0-9])([1-9][0-9]{5,10})(?=[^0-9])'
STRICT_QQ_PATTERN = '(qq|QQ|\+q|\+Q|加q|加Q)'
#STRICT_QQ_PATTERN = '([qQ]{2}[:： ]{0,5}[1-9][0-9]{5,10})(?=[^0-9])'

# 冗余字符处理
# 文本中有连续的 “哈哈哈哈哈” 等字符串，需要删除冗余字符串，返回为 “哈”
REDUNDENT_PATTERN = ' -\t\n啊哈呀~'

# URL
URL_PATTERN = '(?<=[^.])((?:(?:https?|ftp|file)://|(?<![a-zA-Z\-\.])www\.)[\-A-Za-z0-9+&@#/%?=~_|!:,.;]+[-A-Za-z0-9+&@#/%=~_|])(?=[^<\u4E00-\u9FA5，。；！？、“”‘’（）—《》…●])'







