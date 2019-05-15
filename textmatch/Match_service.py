import Item_match_func


def match(filepath,sendtime):
    # 打开传进来的路径
    f1 = open(filepath, "rt",encoding="utf-8")
    # 读取所有行
    lines = f1.readlines()
    mailtext = "".join(lines)
    lines = Item_match_func.delete_blank(lines)
    classify_result=Item_match_func.classify_mail(lines)
    if classify_result == '1':
        Item_match_func.vessel_mail_match2(lines, sendtime, mailtext)
    if classify_result == '2':
        Item_match_func.cargo_mail_match(lines, sendtime, mailtext)
    if classify_result == '3':
        Item_match_func.tc_mail_match(lines,sendtime,mailtext)

match('C:\\Users\\user\\Desktop\\test\\1.txt',"1900/01/01 11:11")