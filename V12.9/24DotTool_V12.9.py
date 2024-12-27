import time
import os
#
def m2(text):
    temp=""
    for k in text:
        if k=="*":
            temp+="×"
        elif k=="/":
            temp+="÷"
        else :
            temp+=k
    return temp

def  mian(jkh):
    n=0
    ysf=['+','-','*','/']
    num2=[a,b,c,d]
    yyss=[]
    for q in num2:
        for w in num2:
            for e in num2:
                for r in num2:
                    for j in ysf:
                        for l in ysf:
                            for i in ysf:
                                ss=f"{q}{j}{w}{l}{e}{i}{r}"
                                if ss.count(str(a))<=num.count(str(a)) and ss.count(str(b))<=num.count(str(b)) and ss.count(str(c))<=num.count(str(c)) and ss.count(str(d))<=num.count(str(d)):
                                    try :
                                        if  eval(str(ss))==24:
                                            yyss.append(ss)
                                            if  yyss.count(ss)>=2:
                                                pass
                                            else :
                                                n+=1
                                                print(f"({n}) {m2(ss)}")
                                    except :
                                        pass
    if jkh=="":
        for q in num2:
            for w in num2:
                for e in num2:
                    for r in num2:
                        for j in ysf:
                            for l in ysf:
                                for i in ysf:
                                    ss=f"({q}{j}{w}){l}{e}{i}{r}"
                                    if ss.count(str(a))<=num.count(str(a)) and ss.count(str(b))<=num.count(str(b)) and ss.count(str(c))<=num.count(str(c)) and ss.count(str(d))<=num.count(str(d)):
                                        try :
                                            if  eval(str(ss))==24:
                                                yyss.append(ss)
                                                if  yyss.count(ss)>=2:
                                                    pass
                                                else :
                                                    n+=1
                                                    print(f"({n}) {m2(ss)}")
                                        except :
                                            pass
        for q in num2:
            for w in num2:
                for e in num2:
                    for r in num2:
                        for j in ysf:
                            for l in ysf:
                                for i in ysf:
                                    ss=f"({q}{j}{w}{l}{e}){i}{r}"
                                    if ss.count(str(a))<=num.count(str(a)) and ss.count(str(b))<=num.count(str(b)) and ss.count(str(c))<=num.count(str(c)) and ss.count(str(d))<=num.count(str(d)):
                                        try :
                                            if  eval(str(ss))==24:
                                                yyss.append(ss)
                                                if  yyss.count(ss)>=2:
                                                    pass
                                                else :
                                                    n+=1
                                                    print(f"({n}) {m2(ss)}")
                                        except :
                                            pass
        for q in num2:
            for w in num2:
                for e in num2:
                    for r in num2:
                        for j in ysf:
                            for l in ysf:
                                for i in ysf:
                                    ss=f"{q}{j}{w}{l}({e}{i}{r})"
                                    if ss.count(str(a))<=num.count(str(a)) and ss.count(str(b))<=num.count(str(b)) and ss.count(str(c))<=num.count(str(c)) and ss.count(str(d))<=num.count(str(d)):
                                        try :
                                            if  eval(str(ss))==24:
                                                yyss.append(ss)
                                                if  yyss.count(ss)>=2:
                                                    pass
                                                else :
                                                    n+=1
                                                    print(f"({n}) {m2(ss)}")
                                        except :
                                            pass
        for q in num2:
            for w in num2:
                for e in num2:
                    for r in num2:
                        for j in ysf:
                            for l in ysf:
                                for i in ysf:
                                    ss=f"{q}{j}({w}{l}{e}{i}{r})"
                                    if ss.count(str(a))<=num.count(str(a)) and ss.count(str(b))<=num.count(str(b)) and ss.count(str(c))<=num.count(str(c)) and ss.count(str(d))<=num.count(str(d)):
                                        try :
                                            if  eval(str(ss))==24:
                                                yyss.append(ss)
                                                if  yyss.count(ss)>=2:
                                                    pass
                                                else :
                                                    n+=1
                                                    print(f"({n}) {m2(ss)}")
                                        except :
                                            pass
        for q in num2:
            for w in num2:
                for e in num2:
                    for r in num2:
                        for j in ysf:
                            for l in ysf:
                                for i in ysf:
                                    ss=f"{q}{j}({w}{l}{e}){i}{r}"
                                    if ss.count(str(a))<=num.count(str(a)) and ss.count(str(b))<=num.count(str(b)) and ss.count(str(c))<=num.count(str(c)) and ss.count(str(d))<=num.count(str(d)):
                                        try :
                                            if  eval(str(ss))==24:
                                                yyss.append(ss)
                                                if  yyss.count(ss)>=2:
                                                    pass
                                                else :
                                                    n+=1
                                                    print(f"({n}) {m2(ss)}")
                                        except :
                                            pass
        for q in num2:
            for w in num2:
                for e in num2:
                    for r in num2:
                        for j in ysf:
                            for l in ysf:
                                for i in ysf:
                                    ss=f"({q}{j}{w}){l}({e}{i}{r})"
                                    if ss.count(str(a))<=num.count(str(a)) and ss.count(str(b))<=num.count(str(b)) and ss.count(str(c))<=num.count(str(c)) and ss.count(str(d))<=num.count(str(d)):
                                        try :
                                            if  eval(str(ss))==24:
                                                yyss.append(ss)
                                                if  yyss.count(ss)>=2:
                                                    pass
                                                else :
                                                    n+=1
                                                    print(f"({n}) {m2(ss)}")
                                        except :
                                            pass
    return n
#
def mianl(jkh):
    n=0
    ysf=["+","-","*","/"]
    yyss=[]
    for j in ysf:
        for l in ysf:
            for i in ysf:
                ss=f"{a}{j}{b}{l}{c}{i}{d}"
                try :
                    if  eval(str(ss))==24:
                        yyss.append(ss)
                        if  yyss.count(ss)>=2:
                            pass
                        else :
                            n+=1
                            print(f"({n}) {m2(ss)}")
                except :
                    pass
    if jkh=="":
        for j in ysf:
            for l in ysf:
                for i in ysf:
                    ss=f"({a}{j}{b}){l}{c}{i}{d}"
                    try :
                        if  eval(str(ss))==24:
                            yyss.append(ss)
                            if  yyss.count(ss)>=2:
                                pass
                            else :
                                n+=1
                                print(f"({n}) {m2(ss)}")
                    except :
                        pass
        for j in ysf:
            for l in ysf:
                for i in ysf:
                    ss=f"({a}{j}{b}{l}{c}){i}{d}"
                    try :
                        if  eval(str(ss))==24:
                            yyss.append(ss)
                            if  yyss.count(ss)>=2:
                                pass
                            else :
                                n+=1
                                print(f"({n}) {m2(ss)}")
                    except :
                        pass
        for j in ysf:
            for l in ysf:
                for i in ysf:
                    ss=f"{a}{j}{b}{l}({c}{i}{d})"
                    try :
                        if  eval(str(ss))==24:
                            yyss.append(ss)
                            if  yyss.count(ss)>=2:
                                pass
                            else :
                                n+=1
                                print(f"({n}) {m2(ss)}")
                    except :
                        pass
        for j in ysf:
            for l in ysf:
                for i in ysf:
                    ss=f"{a}{j}({b}{l}{c}{i}{d})"
                    try :
                        if  eval(str(ss))==24:
                            yyss.append(ss)
                            if  yyss.count(ss)>=2:
                                pass
                            else :
                                n+=1
                                print(f"({n}) {m2(ss)}")
                    except :
                        pass
        for j in ysf:
            for l in ysf:
                for i in ysf:
                    ss=f"({a}{j}{b}){l}({c}{i}{d})"
                    try :
                        if  eval(str(ss))==24:
                            yyss.append(ss)
                            if  yyss.count(ss)>=2:
                                pass
                            else :
                                n+=1
                                print(f"({n}) {m2(ss)}")
                    except :
                        pass
        for j in ysf:
            for l in ysf:
                for i in ysf:
                    ss=f"{a}{j}({b}{l}{c}){i}{d}"
                    try :
                        if  eval(str(ss))==24:
                            yyss.append(ss)
                            if  yyss.count(ss)>=2:
                                pass
                            else :
                                n+=1
                                print(f"({n}) {m2(ss)}")
                    except :
                        pass
    return n
#
num=input('请输入需要破解的4个数字，数字之间用空格隔开(例如4 5 1 4)：')
try :
    list=num.split(" ")
    a=int(list[0])
    b=int(list[1])
    c=int(list[2])
    d=int(list[3])
    kh=input("是否允许破解时添加括号？(允许请回车，不允许按下空格后回车)")
    if kh=="":
        print("添加括号：允许")
    else :
        print("添加括号：不允许")
    dlsx=input("是否允许破解时打乱数字顺序？(允许请回车，不允许按下空格后回车)")
    if dlsx=="":
        print("打乱数字顺序：允许")
    else :
        print("打乱数字顺序：不允许")
    time.sleep(2)
    os.system("cls")
    starttime=time.time()
    if dlsx=="":
        if mian(kh)==0:
            print("这组数字似乎无解欸......")
        else :
            print("破解成功！以上是所有解法。")
            sytime=str(time.time()-starttime)
            print(f"本次破解共用{sytime[0:4]}秒。")
    else :
        if mianl(kh)==0:
            print("这组数字似乎无解欸......")
        else :
            print("破解成功！以上是所有解法。")
            sytime=str(time.time()-starttime)
            print(f"本次破解共用{sytime[0:4]}秒。")
except :
    os.system("cls")
    print("输入的格式似乎不正确哦~请尝试重启程序按照示例输入！")
print('感谢使用！')
print('Copyright 2024-2114 RMDCXY.All Rights Reserved.')
time.sleep(999999999)
