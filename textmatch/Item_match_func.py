# encoding: utf-8
import re
import time
from flashtext import KeywordProcessor
import pymysql

date_keyword_processor = KeywordProcessor()
date_keyword_processor.add_keyword_from_file('Date.txt')

vessel_name_keyword_processor = KeywordProcessor()
vessel_name_keyword_processor.add_keyword_from_file('Vessel_keywords.txt')

port_keyword_processor = KeywordProcessor()
port_keyword_processor.add_keyword_from_file('Port_keywords.txt')

cargo_name_keyword_processor = KeywordProcessor()
cargo_name_keyword_processor.add_keyword_from_file('Cargo_names.txt')

account_name_keyword_processor = KeywordProcessor()
account_name_keyword_processor.add_keyword_from_file('Account_keywords.txt')

#切分邮件，以'+'号为界
def cut_mail_by_symbol(lines):
    line_index_list = []
    patt1 = re.compile(r'^[+][+]*$')
    for n in range(0,len(lines)):
        if re.match(patt1,lines[n]):
            line_index_list.append(n)
    line_index_list.append(len(lines))
    print(line_index_list)
    return line_index_list



#删除文件中空行
def delete_blank(lines):
    del_index_list = []
    n = 0
    while n < len(lines):
        if lines[n] == '\n':
            del_index_list.append(n)
        n += 1
    m = len(del_index_list) - 1
    while m >= 0:
        del lines[del_index_list[m]]
        m -= 1
    return lines


#分类邮件
def classify_mail(lines):
    lines_count = len(lines)
    for n in range(0, lines_count):
        if vessel_name_keyword_processor.extract_keywords(lines[n]):
            print('vessel mail match')
            return '1'
        elif cargo_name_keyword_processor.extract_keywords(lines[n]):
            print('cargo mail match')
            return '2'
        elif account_name_keyword_processor.extract_keywords(lines[n]):
            print('account mail match')
            return '3'


#从一行中找数字，s为起始下标，e为终止下标
def find_digit(s, e, line):
    cnt=0
    num1 = num2 = "none"
    while s < e:
        if line[s].isdigit():
            if cnt == 0:
                if line[s + 1].isdigit():
                    # 找到第一个数字
                    num1 = line[s:s + 2]
                    cnt += 1
                    s += 1
                elif line[s + 1] == '-' or line[s + 1] == ' ' or line[s + 1] == 'S' or line[s + 1] == 'N' or line[s + 1] == 'R' \
                        or line[s + 1] == 'T' or line[s + 1] == 's' or line[s + 1] == 'n' or line[s + 1] == 'r' or line[s + 1] == 't' or line[s+1] == '/':
                    num1 = line[s:s + 1]
                    cnt += 1
            elif cnt == 1:
                if line[s + 1].isdigit():
                    # 找到第二个数字
                    num2 = line[s:s + 2]
                    # 最多两个日期
                    break
                elif line[s + 1] == '-' or line[s + 1] == ' ' or line[s + 1] == 'S' or line[s + 1] == 'N' or line[s + 1] == 'R' \
                        or line[s + 1] == 'T' or line[s + 1] == 's' or line[s + 1] == 'n' or line[s + 1] == 'r' or line[s + 1] == 't' or line[s+1] == '/':
                    num2 = line[s:s + 1]
                    break
        s += 1
    return num1, num2


#拼接日期
def date_format(m1, d1, m2, d2):
    return "2019/"+m1+"/"+d1, "2019/"+m2+"/"+d2


#匹配日期(Open date,Laycan)
def date_match(line):
    #定位到月份的位置
    location = date_keyword_processor.extract_keywords(line, span_info=True)
    date_s = '1900/01/01'
    date_e = '1900/01/01'

    if len(location) == 1:
        if location[0][0] != "t2":
            #e.g 08-09 月份 /  01ST - 02ND 月份(最长) / 03RD - 15TH 月份 / 15 月份
            n = location[0][1] - 12
            if n < 0:
                n = 0
            e = location[0][1] - 1
            one, two = find_digit(n, e, line)

            if one != "none":
                if two == "none":
                    date_s, date_e = date_format(location[0][0], one, location[0][0], one)
                else:
                    date_s, date_e = date_format(location[0][0], one, location[0][0], two)

            elif two == "none":
                #可能为 月份 08-09 / 月份 01ST - 02ND(最长) / 月份 03RD - 15TH / 月份 15
                m = location[0][2]+1
                k = location[0][2]+11
                if m >= len(line):
                    return date_s,date_e
                if k >= len(line):
                    k = len(line)-1
                first, second = find_digit(m, k, line)

                if first != "none":
                    if second == "none":
                        date_s, date_e = date_format(location[0][0], first, location[0][0], first)
                    else:
                        date_s, date_e = date_format(location[0][0], first, location[0][0], second)
                elif second == "none":
                    return date_s, date_e
        if location[0][0] == "t2":
            localtime = time.localtime(time.time())
            date_s, date_e = date_format(str(localtime.tm_mon), str(localtime.tm_mday), str(localtime.tm_mon), str(localtime.tm_mday))
            return date_s, date_e

    elif len(location) == 2:
        # e.g. 09 月份1 - 09 月份2 / 09TH 月份1 - 09TH 月份2(最长)
        n = location[0][1] - 5
        e = location[1][2]
        if n < 0:
            n = 0
        one, two = find_digit(n, e, line)

        if one != "none" and two != "none":
            date_s, date_e = date_format(location[0][0], one, location[1][0], two)
        else:
            #可能为 月份1 01st - 月份2 02nd（最长）
            m = location[0][2]
            k = location[1][2] + 4
            if k >= len(line):
                k = len(line)-1
            first, second = find_digit(m, k, line)

            if first != "none" and second != "none":
                date_s, date_e = date_format(location[0][0], first, location[1][0], second)
            else:
                return date_s, date_e

    return date_s,date_e


#船名一定要有MV,M/V,否则没有结果
#附带BLT,DWT
def vessel_name_match(line):
    keyword_found = vessel_name_keyword_processor.extract_keywords(line)
    if keyword_found:
        patt = re.compile(r'^[M|m][/]*[v|V][:]*$')
        word = line.split(" ")
        check = []
        for s in range(0, len(word)):
            sub = patt.findall(word[s])
            if sub:
                check.append(sub[0])
        if len(check) > 0:
            for a in range(0, len(keyword_found)):
                sub_str = keyword_found[a].split("+")
                if sub_str[1] == "none":
                    sub_str[1] = "0"
                if not sub_str[2]:
                    sub_str[2] = "0"
                return sub_str[0], int(sub_str[1]), int(sub_str[2])
    return "none", 0, 0


#港口匹配
def port_match(port1,port2,line):
    keyword_found = port_keyword_processor.extract_keywords(line)
    if keyword_found:
        if len(keyword_found) == 1:
            if port1 == "none" and port2 == "none":
                return keyword_found[0], port2
            if port1 != "none" and port2 == "none":
                return port1, keyword_found[0]
        if len(keyword_found) == 2:
            return keyword_found[0], keyword_found[1]
    return "none","none"


#数量匹配
def quantity_match(line):
    line = re.sub('[-]', ' ', line)
    patt1 = re.compile(r'^[0-9]+[,]*[0-9]{3}[MT|mt]*$')
    patt2 = re.compile(r'^[0-9]*[k]*')
    word = line.split(" ")
    result_list = []
    quantity_s = quantity_e = 0
    #28,000-30,000
    for n in range(0, len(word)):
        sub_str1 = patt1.findall(word[n])
        sub_str1="".join(sub_str1)
        sub_str1 = re.sub('[^0-9]', '', sub_str1)
        if len(sub_str1) != 0:
            result_list.append(sub_str1)
    #28k-30k
    if len(result_list) == 0:
        for m in range(0, len(word)):
            sub_str2 = patt2.findall(word[m])
            sub_str2 = "".join(sub_str2)
            sub_str2 = re.sub('[^0-9]', '', sub_str2)
            if len(sub_str2) != 0:
                result_list.append(sub_str2+"000")
    if len(result_list) == 1:
        quantity_s = quantity_e = int(result_list[0])
    elif len(result_list) >= 2:
        quantity_s = int(result_list[0])
        quantity_e = int(result_list[1])
    return quantity_s, quantity_e


#duration匹配
def duration_match(line):
    duration_s = duration_e = 0
    dur_kp = KeywordProcessor()
    dur_kp.add_keyword("DAYS","DURATION")
    if dur_kp.extract_keywords(line):
        line = re.sub('[-]', ' ', line)
        patt = re.compile(r'^\d+$')
        word = line.split(" ")
        result_list = []
        for n in range(0, len(word)):
            sub_str = patt.findall(word[n])
            sub_str="".join(sub_str)
            if sub_str:
                result_list.append(sub_str)
        print(result_list)
        if len(result_list) == 1:
            duration_s = duration_e = int(result_list[0])
        elif len(result_list) >= 2:
            duration_s = int(result_list[0])
            duration_e = int(result_list[1])
    return duration_s, duration_e


#货物名匹配
def cargo_match(line):
    location = cargo_name_keyword_processor.extract_keywords(line, span_info=True)
    if location:
        return location[0][0]
    else:
        temp_kp = KeywordProcessor()
        temp_kp.add_keyword('CARGO')
        temp_kp.add_keyword('ITEM')
        temp_kp.add_keyword('IN')
        L = temp_kp.extract_keywords(line, span_info=True)
        if len(L) == 2:
            return line[L[0][2]:L[1][1]]
    return 'none'


#account匹配
def account_match(line):
    location = account_name_keyword_processor.extract_keywords(line, span_info=True)
    if location:
        return location[0][0]
    else:
        temp_kp = KeywordProcessor()
        temp_kp.add_keyword('ACCT')
        temp_kp.add_keyword('ACCOUNT')
        L = temp_kp.extract_keywords(line, span_info=True)
        if L:
            for n in range(L[0][2], len(line)):
                if line[n].isalpha():
                    return line[n:len(line) - 1]
    return "none"


#写入数据库操作
def write_to_tonnage_card(vessel_name, dwt, blt, open_area, sent_time, open_date_s, open_date_e, mail_text):
    db = pymysql.connect(host="47.103.63.138", user="root", passwd="tcloudsjtu", db="trade_mail")
    cursor = db.cursor()
    sql = "INSERT INTO tonnage_card(Vessel_name, DWT, BLT, Open_area,Sent,Open_date_S,Open_date_E, mail_text) " \
          "VALUES ('%s','%s','%s','%s','%s','%s','%s', '%s')" % \
          (vessel_name, dwt, blt, open_area, sent_time, open_date_s, open_date_e, pymysql.escape_string(mail_text))
    try:
        cursor.execute(sql)
        db.commit()
        print('write ok')
    except Exception as e:
        db.rollback()
        print('write fail')
        print(e)
        print(sql)
    db.close()


def write_to_tc_card(account, delivery_area, redelivery_area, sent_time, laycan_s, laycan_e, mail_text, quantity_s, quantity_e, duration_s, duration_e):
    db = pymysql.connect("47.103.63.138", "root", "tcloudsjtu", "trade_mail")
    cursor = db.cursor()
    sql = "INSERT INTO tc_card(Account, Delivery_area, Redelivery_area, Sent, LayCan_S, LayCan_E, " \
          "mail_text, Quantity_s, Quantity_e, DUR_S, DUR_E) " \
          "VALUES ('%s','%s','%s','%s','%s','%s','%s','%d', '%d', '%d', '%d')" % \
          (account, delivery_area, redelivery_area, sent_time, laycan_s, laycan_e,
           pymysql.escape_string(mail_text), quantity_s, quantity_e, duration_s, duration_e)
    try:
        cursor.execute(sql)
        db.commit()
        print('write ok')
    except Exception as e:
        db.rollback()
        print('write fail')
        print(e)
        print(sql)
    db.close()


def write_to_cargo_card(cargo_name, loading_port, discharging_port, sent_time, laycan_s, laycan_e, mail_text, quantity_s, quantity_e):
    db = pymysql.connect("47.103.63.138", "root", "tcloudsjtu", "trade_mail")
    cursor = db.cursor()
    sql = "INSERT INTO cargo_card(Cargo_name, Loading_Port, Discharging_Port, Sent, " \
          "LayCan_S, LayCan_E, mail_text, Quantity_s, Quantity_e) " \
          "VALUES ('%s','%s','%s','%s','%s','%s','%s', '%s','%s')" % \
          (cargo_name, loading_port, discharging_port, sent_time,
           laycan_s, laycan_e, pymysql.escape_string(mail_text),quantity_s, quantity_e)
    try:
        cursor.execute(sql)
        db.commit()
        print('write ok')
    except Exception as e:
        db.rollback()
        print('write fail')
        print(e)
        print(sql)
    db.close()

######################
#格式：
#船名
#港口
#日期
#船名
#港口
#日期

#或：
# 日期/港口
# 船名
# 船名

#未处理实际有写但不在字库中所造成的错位
######################
def vessel_mail_match(lines, sendtime, mailtext):
    line_index_list = []
    vessel_name_list = []
    result_list =[]
    for n in range(0, len(lines)):
        vessel_name, dwt, blt = vessel_name_match(lines[n])
        if vessel_name != "none":
            vessel_name_list.append((vessel_name, dwt, blt))
            line_index_list.append(n)
    line_index_list.append(len(lines))
    print(line_index_list)
    if len(line_index_list) > 0:
        s = line_index_list[0]
        for m in range(1, len(line_index_list)):
            open_area_list = []
            date_list = []
            for k in range(s, line_index_list[m]):
                open_area = port_keyword_processor.extract_keywords(lines[k])
                date_s, date_e = date_match(lines[k])
                if open_area:
                    open_area_list.append(open_area[0])
                if date_s != "1900/01/01":
                    date_list.append((date_s,date_e))

            if len(open_area_list) == 0:
                open_area_list.append("no open area match")
            if len(date_list) == 0:
                date_list.append(("1900/01/01", "1900/01/01"))

            result_list.append([vessel_name_list[m-1], open_area_list[0], date_list[0]])

            s = line_index_list[m]
    if len(result_list) != 0:
        for i in range(0,line_index_list[0]):
            open_area, open_area2 = port_match("none", "none", lines[i])
            date_s, date_e = date_match(lines[i])
            if open_area != "none":
                for j in range(0,len(result_list)):
                    if result_list[j][1] == "no open area match":
                        result_list[j][1] = open_area

            if date_s !="1900/01/01":
                for u in range(0,len(result_list)):
                    if result_list[u][2] == ("1900/01/01", "1900/01/01"):
                        result_list[u][2] =(date_s, date_e)

    for o in range(0, len(result_list)):
        print(result_list[o])
        #write_to_tonnage_card(result_list[o][0][0],result_list[o][0][2],result_list[o][0][1],result_list[o][1],sendtime,result_list[o][2][0],result_list[o][2][1],mailtext)


######################
#格式：
#货物名+质量
#港口
#日期
#货物名+质量
#港口
#日期

#或：
# 日期/港口
# 货物名+质量
# 货物名+质量

#未处理实际有写但不在字库中所造成的错位
######################
def cargo_mail_match(lines, sendtime, mailtext):
    line_index_list = []
    cargo_name_list = []
    result_list = []
    for n in range(0, len(lines)):
        cargo_name = cargo_match(lines[n])
        if cargo_name != "none":
            cargo_name_list.append(cargo_name)
            line_index_list.append(n)
    line_index_list.append(len(lines))
    print(line_index_list)
    if len(line_index_list) > 0:
        s = line_index_list[0]
        for m in range(1, len(line_index_list)):
            quantity_list = []
            date_list = []
            port_list = []
            loading_port = discharging_port = "none"
            for k in range(s, line_index_list[m]):
                if loading_port == "none":
                    loading_port, discharging_port = port_match(loading_port, discharging_port, lines[k])
                elif discharging_port == "none":
                    loading_port, discharging_port = port_match(loading_port, discharging_port, lines[k])
                date_s, date_e = date_match(lines[k])
                quantity_s, quantity_e = quantity_match(lines[k])

                if date_s != "1900/01/01":
                    date_list.append((date_s,date_e))
                if quantity_s:
                    quantity_list.append((quantity_s,quantity_e))

            if loading_port != "none" or discharging_port != "none":
                port_list.append((loading_port, discharging_port))

            if len(port_list) == 0:
                port_list.append(("no loading port match","no discharging port match"))
            if len(date_list) == 0:
                date_list.append(("1900/01/01", "1900/01/01"))
            if len(quantity_list) == 0:
                quantity_list.append((0,0))

            result_list.append([cargo_name_list[m-1], port_list[0], date_list[0],quantity_list[0]])

            s = line_index_list[m]

    if len(result_list) == 0:
        result_list.append(["none item name match",("no loading port match","no discharging port match"),("1900/01/01", "1900/01/01"),(0,0)])

    loading_port = discharging_port = "none"
    for i in range(0, line_index_list[0]):
        loading_port, discharging_port = port_match(loading_port, discharging_port, lines[i])
        date_s, date_e = date_match(lines[i])
        if loading_port != "none" or discharging_port != "none":
            for j in range(0, len(result_list)):
                if result_list[j][1] == ("no loading port match","no discharging port match"):
                    if discharging_port != "none":
                        result_list[j][1] = (loading_port, discharging_port)
                    else:
                        result_list[j][1] = (loading_port, "no discharging port match")

        if date_s != "1900/01/01":
            for u in range(0, len(result_list)):
                if result_list[u][2] == ("1900/01/01", "1900/01/01"):
                    result_list[u][2] = (date_s, date_e)

    for o in range(0, len(result_list)):
        print(result_list[o])
        write_to_cargo_card(result_list[o][0],result_list[o][1][0],result_list[o][1][1],sendtime,result_list[o][2][0],result_list[o][2][1],mailtext,result_list[o][3][0],result_list[o][3][1])



def tc_mail_match(lines, sendtime, mailtext):
    line_index_list = []
    account_name_list = []
    result_list = []
    for n in range(0, len(lines)):
        account_name = account_match(lines[n])
        if account_name != "none":
            account_name_list.append(account_name)
            line_index_list.append(n)
    line_index_list.append(len(lines))
    print(line_index_list)
    if len(line_index_list) > 0:
        s = line_index_list[0]
        for m in range(1, len(line_index_list)):
            quantity_list = []
            date_list = []
            port_list = []
            dur_list = []
            delivery_area = redelivery_area = "none"
            for k in range(s, line_index_list[m]):
                if delivery_area == "none":
                    delivery_area, redelivery_area = port_match(delivery_area, redelivery_area, lines[k])
                elif redelivery_area == "none":
                    delivery_area, redelivery_area = port_match(delivery_area, redelivery_area, lines[k])
                date_s, date_e = date_match(lines[k])
                quantity_s, quantity_e = quantity_match(lines[k])
                duration_s, duration_e = duration_match(lines[k])

                if date_s != "1900/01/01":
                    date_list.append((date_s, date_e))
                if quantity_s:
                    quantity_list.append((quantity_s, quantity_e))
                if duration_s:
                    dur_list.append((duration_s, duration_e))
            if delivery_area != "none" or redelivery_area != "none":
                port_list.append((delivery_area, redelivery_area))

            if len(port_list) == 0:
                port_list.append(("no delivery area match","no redelivery area match"))
            if len(date_list) == 0:
                date_list.append(("1900/01/01", "1900/01/01"))
            if len(quantity_list) == 0:
                quantity_list.append((0, 0))
            if len(dur_list) == 0:
                dur_list.append((0,0))

            result_list.append([account_name_list[m - 1], port_list[0], date_list[0], quantity_list[0],dur_list[0]])

            s = line_index_list[m]

    if len(result_list) == 0:
        result_list.append(["ANONYMOUS",("no delivery area match","no redelivery area match"),("1900/01/01", "1900/01/01"),(0,0),(0, 0)])

    delivery_area = redelivery_area = "none"
    for i in range(0, line_index_list[0]):
        delivery_area, redelivery_area = port_match(delivery_area, redelivery_area,lines[i])
        date_s, date_e = date_match(lines[i])
        duration_s, duration_e = duration_match(lines[i])
        if delivery_area != "none" or redelivery_area != "none":
            for j in range(0, len(result_list)):
                if result_list[j][1] == ("no delivery area match","no redelivery area match"):
                    if redelivery_area != "none":
                        result_list[j][1] = (delivery_area, redelivery_area)
                    else:
                        result_list[j][1] = (delivery_area, "no redelivery area match")

        if date_s != "1900/01/01":
            for u in range(0, len(result_list)):
                if result_list[u][2] == ("1900/01/01", "1900/01/01"):
                    result_list[u][2] = (date_s, date_e)

        if duration_s:
            for p in range(0,len(result_list)):
                if result_list[p][4] == (0,0):
                    result_list[p][4] == (duration_s, duration_e)

    for o in range(0, len(result_list)):
        print(result_list[o])
        write_to_tc_card(result_list[o][0],result_list[o][1][0],result_list[o][1][1],sendtime,result_list[o][2][0],result_list[o][2][1],mailtext,result_list[o][3][0],result_list[o][3][1],result_list[o][4][0],result_list[o][4][1])



def vessel_mail_match2(lines, sendtime, mailtext):
    line_index_list = cut_mail_by_symbol(lines)
    result_list = []
    if len(line_index_list) > 0:
        s = 0
        for m in range(0, len(line_index_list)):
            vessel_name_list = []
            open_area_list = []
            date_list = []
            for k in range(s, line_index_list[m]):
                vessel_name, dwt, blt = vessel_name_match(lines[k])
                open_area, open_area2 = port_match("none", "none", lines[k])

                date_s, date_e = date_match(lines[k])
                if vessel_name != "none":
                    vessel_name_list.append((vessel_name, dwt, blt))
                if open_area != "none":
                    open_area_list.append(open_area)
                if date_s != "1900/01/01":
                    date_list.append((date_s,date_e))

            if len(vessel_name_list) == 0:
                vessel_name_list.append(("none", "none", "none"))
            if len(open_area_list) == 0:
                open_area_list.append("no open area match")
            if len(date_list) == 0:
                date_list.append(("1900/01/01", "1900/01/01"))
            result_list.append([vessel_name_list[0], open_area_list[0], date_list[0]])

            s = line_index_list[m]

    if len(result_list) != 0 and result_list[0][0][0] == "none":
        if result_list[0][1] != "no open area match":
            for j in range(0, len(result_list)):
                if result_list[j][1] == "no open area match":
                    result_list[j][1] = open_area

        if result_list[0][2][0] != "1900/01/01":
            for u in range(0,len(result_list)):
                if result_list[u][2] == ("1900/01/01", "1900/01/01"):
                    result_list[u][2] = (result_list[0][2][0], result_list[0][2][1])

    for o in range(0, len(result_list)):
        print(result_list[o])
        #write_to_tonnage_card(result_list[o][0][0],result_list[o][0][2],result_list[o][0][1],result_list[o][1],sendtime,result_list[o][2][0],result_list[o][2][1],mailtext)
