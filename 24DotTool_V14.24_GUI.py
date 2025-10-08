import tkinter as tk
from tkinter import filedialog
import os
import sys
import time
import webbrowser
from plyer import notification
ver="14.24"
root=tk.Tk()
root.title(f"24DotTool V{ver}")
root.geometry("600x365")
root.resizable(False,False)
def resource_path(relative_path):
    """Return absolute path to resource, works for dev and for PyInstaller one-file bundle.

    Usage: resource_path('icon.ico')
    """
    try:
        base_dir = os.path.abspath(os.path.dirname(__file__))
    except Exception:
        base_dir = os.getcwd()
    if getattr(sys, 'frozen', False):
        # PyInstaller bundles files into _MEIPASS
        base_dir = getattr(sys, '_MEIPASS', base_dir)
    return os.path.join(base_dir, relative_path)
def set_app_icon(win):
    global APP_ICON_IMG
    # Use resource_path so it works both when running from source and when bundled by PyInstaller
    ico_path = resource_path('icon.ico')
    png_path = resource_path('icon.png')
    gif_path = resource_path('icon.gif')
    # Try .ico via iconbitmap (Windows)
    try:
        if os.path.exists(ico_path):
            win.iconbitmap(ico_path)
            return
    except Exception as e:
        print('iconbitmap failed:', e)
    # Fallback: try PhotoImage + iconphoto (PNG or GIF)
    try:
        if os.path.exists(png_path):
            APP_ICON_IMG = tk.PhotoImage(file=png_path)
            win.iconphoto(False, APP_ICON_IMG)
            return
        if os.path.exists(gif_path):
            APP_ICON_IMG = tk.PhotoImage(file=gif_path)
            win.iconphoto(False, APP_ICON_IMG)
            return
    except Exception as e:
        print('iconphoto fallback failed:', e)


_IMAGE_CACHE = {}
def load_image(filename):
    """Load PhotoImage robustly using script directory or PyInstaller bundle.
    Caches images to avoid being garbage-collected.
    """
    # Use resource_path to support both normal and PyInstaller-packed execution
    path = resource_path(filename)
    if path in _IMAGE_CACHE:
        return _IMAGE_CACHE[path]
    if not os.path.exists(path):
        raise FileNotFoundError(f"Image not found: {path}")
    img = tk.PhotoImage(file=path)
    _IMAGE_CACHE[path] = img
    return img

# set icon for main window
APP_ICON_IMG = None
set_app_icon(root)
jkh=1
dlsx=1
sytime=0
a=0
b=0
c=0
d=0
setting_open=0
aboutp_open=0
yx_open=0
kx_open=0
yz_open=0
def sws(wn):
    global setting_open,aboutp_open,yx_open,kx_open,yz_open,setting,kyxy,yhxy,yszc,ap
    if wn==0:
        setting_open=0
        setting.destroy()
    elif wn==1:
        aboutp_open=0
        ap.destroy()
    elif wn==2:
        yx_open=0
        yhxy.destroy()
    elif wn==3:
        yz_open=0
        yszc.destroy()
    elif wn==4:
        kx_open=0
        kyxy.destroy()
def config():
    global setting_open
    if setting_open==0:
        global c1,c2,jkh,dlsx,setting
        setting_open=1
        setting=tk.Toplevel()
        setting.title("24DotTool 设置")
        setting.geometry("200x115")
        setting.protocol("WM_DELETE_WINDOW",lambda:sws(0))
        setting.resizable(False,False)
        set_app_icon(setting)
        st=tk.Label(setting,text="设置",font=("宋体",15))
        st.pack()
        if jkh==1:
            c1=tk.Button(setting,text="允许破解时\n添加括号",height=3,width=10,command=changec1)
        elif jkh==0:
            c1=tk.Button(setting,text="不允许破解时\n添加括号",height=3,width=10,command=changec1)
        c1.pack(side="left",padx=10,pady=5)
        if dlsx==1:
            c2=tk.Button(setting,text="允许破解时\n打乱数字顺序",height=3,width=10,command=changec2)
        elif dlsx==0:
            c2=tk.Button(setting,text="不允许破解时\n打乱数字顺序",height=3,width=10,command=changec2)
        c2.pack(side="right",padx=10,pady=5)
def openweb(wl):
    weblink=["https://cxybbs.top","https://space.bilibili.com/3493142110144946","https://user.qzone.qq.com/3766908125","https://space.bilibili.com/413055811","https://user.qzone.qq.com/2832383568"]
    webbrowser.open(weblink[wl])
def kyxy():
    global kx_open
    if kx_open==0:
        global kyxy
        kx_open=1
        kyxy=tk.Toplevel()
        kyxy.title("24DotTool的MIT License开源协议")
        kyxy.geometry("625x325")
        kyxy.protocol("WM_DELETE_WINDOW",lambda:sws(4))
        kyxy.resizable(False,False)
        set_app_icon(kyxy)
        kxt=tk.Label(kyxy,text="24DotTool开源协议",font=("宋体",20))
        kxt.pack()
        kxm=tk.Text(kyxy)
        kxm.pack(padx=3,pady=3)
        kxm.insert(tk.END,"MIT License\n\nCopyright 2024 RMDCXY\n\nPermission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the “Software”), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:\n\nThe above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.\n\nTHE SOFTWARE IS PROVIDED “AS IS”, WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.")
        kxm.config(state=tk.DISABLED)
def yhxy():
    global yx_open
    if yx_open==0:
        global yhxy
        yx_open=1
        yhxy=tk.Toplevel()
        yhxy.title("24DotTool的用户协议")
        yhxy.geometry("625x325")
        yhxy.resizable(False,False)
        yhxy.protocol("WM_DELETE_WINDOW",lambda:sws(2))
        set_app_icon(yhxy)
        yxt=tk.Label(yhxy,text="24DotTool用户协议",font=("宋体",20))
        yxt.pack()
        yxm=tk.Text(yhxy)
        yxm.pack(padx=3,pady=3)
        yxm.insert(tk.END,f"用户协议\n\n项目名称: 24DotTool\n\n版本: {ver}\n\n日期: 2024年12月13日\n\n1. 概述\n\n本协议（以下简称“协议”）是您（以下简称“用户”）与RMDCXY（以下简称“开发者”）之间关于使用24DotTool的法律协议。请仔细阅读本协议的所有条款和条件。使用本项目即表示您已接受并同意遵守本协议的所有条款和条件。\n\n2. 使用条款\n\n2.1 授权范围：开发者授予用户非独占、不可转让、不可再许可的使用权，允许用户在个人用途下使用本项目。\n\n2.2 限制：用户不得将本项目用于商业用途，不得对本项目进行反向工程、反编译或试图提取源代码。\n\n2.3 数据隐私：本项目不收集任何用户数据。用户自行负责其在使用过程中产生的所有数据的安全性和隐私保护。\n\n3. 知识产权\n\n3.1 所有权：本项目及其所有内容，包括但不限于代码、文档、图像等，均受版权法和其他适用法律保护，所有权归属于开发者。\n\n3.2 许可：开发者授予用户有限的、不可转让的许可，允许用户在遵守本协议的前提下使用本项目。\n\n4. 免责声明\n\n4.1 责任限制：开发者不对因使用本项目而产生的任何直接、间接、附带、特殊或后果性损害承担责任，包括但不限于数据丢失、利润损失或业务中断。\n\n4.2 适用法律：本协议受中华人民共和国法律管辖，并按其解释。\n\n5. 协议变更\n\n开发者保留随时修改本协议的权利。修改后的协议将在发布时生效，用户继续使用本项目即视为接受修改后的协议。\n\n6. 联系方式\n\n如对本协议有任何疑问或建议，请通过以下方式联系开发者：\n\n邮箱:rmdcxypgm@outlook.com\n\n其它联系方式均可在关于界面的“RMDCXY”处找到。")
        yxm.config(state=tk.DISABLED)
def yszc():
    global yz_open
    if yz_open==0:
        global yszc
        yz_open=1
        yszc=tk.Toplevel()
        yszc.title("24DotTool的隐私政策")
        yszc.geometry("625x325")
        yszc.resizable(False,False)
        yszc.protocol("WM_DELETE_WINDOW",lambda:sws(3))
        set_app_icon(yszc)
        yzt=tk.Label(yszc,text="24DotTool隐私政策",font=("宋体",20))
        yzt.pack()
        yzm=tk.Text(yszc)
        yzm.pack(padx=3,pady=3)
        yzm.insert(tk.END,f"1. 引言\n项目名称：24DotTool\n版本信息：{ver}\n最后更新日期：2024年12月13日\n2. 联系信息\n开发者/所有者：RMDCXY\n电子邮件地址：rmdcxypgm@outlook.com\n3. 收集的数据类型\n个人信息：本项目不收集任何个人信息。\n使用数据：本项目不收集任何使用数据\n5. 数据共享和披露\n第三方共享：本项目不会与任何第三方共享您的数据。\n法律要求下的披露：在法律要求或政府主管部门的强制性要求下，我们可能需要披露您的数据。\n6. 用户权利\n访问权：用户有权访问其在本项目中提供的任何信息。\n更正权：用户有权更正其在本项目中提供的任何信息。\n删除权：用户有权请求删除其在本项目中提供的任何信息。\n7. 法律合规性\n适用法律：本隐私政策符合《中华人民共和国个人信息保护法》的要求。\n更新通知：我们将定期更新本隐私政策以适应法律法规的变化。\n8. 其他信息\n隐私政策的解释权：本隐私政策的解释权归RMDCXY所有。\n联系方式：如有任何疑问，请通过上述联系方式与我们联系。")
        yzm.config(state=tk.DISABLED)
def aboutp():
    global aboutp_open
    if aboutp_open==0:
        global ver
        global ap
        aboutp_open=1
        ap=tk.Toplevel()
        ap.title(f"关于 24DotTool V{ver}")
        ap.geometry("375x350")
        ap.resizable(False,False)
        ap.protocol("WM_DELETE_WINDOW",lambda:sws(1))
        set_app_icon(ap)
        at=tk.Label(ap,text="关于 24DotTool",font=("宋体",25))
        at.pack()
        #title
        pgmicon=load_image("icon.gif")
        apicon=tk.Label(ap,image=pgmicon)
        apicon.place(x=10,y=35)
        aptext=tk.Label(ap,text=f"24DotTool Ver{ver}\n为破解24点数学游戏而生",font=("楷体",17))
        aptext.place(x=100,y=40)
        apweb=tk.Button(ap,text="打开官方网站",command=lambda:openweb(0))
        apweb.place(x=105,y=95)
        apxy=tk.Button(ap,text="开源协议",command=kyxy)
        apxy.place(x=185,y=95)
        apyh=tk.Button(ap,text="用户协议",command=yhxy)
        apyh.place(x=245,y=95)
        apys=tk.Button(ap,text="隐私政策",command=yszc)
        apys.place(x=305,y=95)
        #people
        ast=tk.Label(ap,text="感谢每一位为24DotTool做出贡献的人！",font=("楷体",13))
        ast.place(x=35,y=135)
        #r
        cxyiconi=load_image("rmdcxy.gif")
        cxyicon=tk.Label(ap,image=cxyiconi)
        cxyicon.place(x=10,y=155)
        cxyjs=tk.Label(ap,text="RMDCXY\n程序主要开发策划",font=("楷体",16))
        cxyjs.place(x=115,y=155)
        cxyb=tk.Button(ap,text="打开他的哔哔空间",command=lambda:openweb(1))
        cxyb.place(x=115,y=205)
        cxyq=tk.Button(ap,text="打开他的企鹅空间",command=lambda:openweb(2))
        cxyq.place(x=225,y=205)
        #y
        yaoiconi=load_image("yaoyao.gif")
        yaoicon=tk.Label(ap,image=yaoiconi)
        yaoicon.place(x=10,y=245)
        yaojs=tk.Label(ap,text="药药\n帮助修复了BUG",font=("楷体",17))
        yaojs.place(x=115,y=235)
        yaob=tk.Button(ap,text="打开TA的哔哔空间",command=lambda:openweb(3))
        yaob.place(x=115,y=290)
        yaoq=tk.Button(ap,text="打开TA的企鹅空间",command=lambda:openweb(4))
        yaoq.place(x=225,y=290)
        #m
        ap.mainloop()
def changec1():
    global jkh
    if jkh==1:
        c1.config(text="不允许破解时\n添加括号")
        jkh=0
    elif jkh==0:
        c1.config(text="允许破解时\n添加括号")
        jkh=1
def changec2():
    global dlsx
    if dlsx==1:
        c2.config(text="不允许破解时\n打乱数字顺序")
        dlsx=0
    elif dlsx==0:
        c2.config(text="允许破解时\n打乱数字顺序")
        dlsx=1
def  mian(jkh):
    global r,m
    n=0
    ysf=['+','-','*','/']
    num2=[a,b,c,d]
    yyss=[]
    for q in num2:
        for w in num2:
            for e in num2:
                for r1 in num2:
                    for j in ysf:
                        for l in ysf:
                            for i in ysf:
                                ss=f"{q}{j}{w}{l}{e}{i}{r1}"
                                num=m.get()
                                if ss.count(str(a))<=num.count(str(a)) and ss.count(str(b))<=num.count(str(b)) and ss.count(str(c))<=num.count(str(c)) and ss.count(str(d))<=num.count(str(d)):
                                    if  eval(str(ss))==24:
                                        yyss.append(ss)
                                        if  yyss.count(ss)>=2:
                                            pass
                                        else :
                                            n+=1
                                            r.insert(tk.END,f"({n}) {m2(ss)} \n")
    if jkh==1:
        for q in num2:
            for w in num2:
                for e in num2:
                    for r1 in num2:
                        for j in ysf:
                            for l in ysf:
                                for i in ysf:
                                    ss=f"({q}{j}{w}){l}{e}{i}{r1}"
                                    num=m.get()
                                    if ss.count(str(a))<=num.count(str(a)) and ss.count(str(b))<=num.count(str(b)) and ss.count(str(c))<=num.count(str(c)) and ss.count(str(d))<=num.count(str(d)):
                                        try :
                                            if  eval(str(ss))==24:
                                                yyss.append(ss)
                                                if  yyss.count(ss)>=2:
                                                    pass
                                                else :
                                                    n+=1
                                                    r.insert(tk.END,f"({n}) {m2(ss)}\n")
                                        except :
                                            pass
        for q in num2:
            for w in num2:
                for e in num2:
                    for r1 in num2:
                        for j in ysf:
                            for l in ysf:
                                for i in ysf:
                                    ss=f"({q}{j}{w}{l}{e}){i}{r1}"
                                    num=m.get()
                                    if ss.count(str(a))<=num.count(str(a)) and ss.count(str(b))<=num.count(str(b)) and ss.count(str(c))<=num.count(str(c)) and ss.count(str(d))<=num.count(str(d)):
                                        try :
                                            if  eval(str(ss))==24:
                                                yyss.append(ss)
                                                if  yyss.count(ss)>=2:
                                                    pass
                                                else :
                                                    n+=1
                                                    r.insert(tk.END,f"({n}) {m2(ss)}\n")
                                        except :
                                            pass
        for q in num2:
            for w in num2:
                for e in num2:
                    for r1 in num2:
                        for j in ysf:
                            for l in ysf:
                                for i in ysf:
                                    ss=f"{q}{j}{w}{l}({e}{i}{r1})"
                                    num=m.get()
                                    if ss.count(str(a))<=num.count(str(a)) and ss.count(str(b))<=num.count(str(b)) and ss.count(str(c))<=num.count(str(c)) and ss.count(str(d))<=num.count(str(d)):
                                        try :
                                            if  eval(str(ss))==24:
                                                yyss.append(ss)
                                                if  yyss.count(ss)>=2:
                                                    pass
                                                else :
                                                    n+=1
                                                    r.insert(tk.END,f"({n}) {m2(ss)}\n")
                                        except :
                                            pass
        for q in num2:
            for w in num2:
                for e in num2:
                    for r1 in num2:
                        for j in ysf:
                            for l in ysf:
                                for i in ysf:
                                    ss=f"{q}{j}({w}{l}{e}{i}{r1})"
                                    num=m.get()
                                    if ss.count(str(a))<=num.count(str(a)) and ss.count(str(b))<=num.count(str(b)) and ss.count(str(c))<=num.count(str(c)) and ss.count(str(d))<=num.count(str(d)):
                                        try :
                                            if  eval(str(ss))==24:
                                                yyss.append(ss)
                                                if  yyss.count(ss)>=2:
                                                    pass
                                                else :
                                                    n+=1
                                                    r.insert(tk.END,f"({n}) {m2(ss)}\n")
                                        except :
                                            pass
        for q in num2:
            for w in num2:
                for e in num2:
                    for r1 in num2:
                        for j in ysf:
                            for l in ysf:
                                for i in ysf:
                                    ss=f"{q}{j}({w}{l}{e}){i}{r1}"
                                    num=m.get()
                                    if ss.count(str(a))<=num.count(str(a)) and ss.count(str(b))<=num.count(str(b)) and ss.count(str(c))<=num.count(str(c)) and ss.count(str(d))<=num.count(str(d)):
                                        try :
                                            if  eval(str(ss))==24:
                                                yyss.append(ss)
                                                if  yyss.count(ss)>=2:
                                                    pass
                                                else :
                                                    n+=1
                                                    r.insert(tk.END,f"({n}) {m2(ss)}\n")
                                        except :
                                            pass
        for q in num2:
            for w in num2:
                for e in num2:
                    for r1 in num2:
                        for j in ysf:
                            for l in ysf:
                                for i in ysf:
                                    ss=f"({q}{j}{w}){l}({e}{i}{r1})"
                                    num=m.get()
                                    if ss.count(str(a))<=num.count(str(a)) and ss.count(str(b))<=num.count(str(b)) and ss.count(str(c))<=num.count(str(c)) and ss.count(str(d))<=num.count(str(d)):
                                        try :
                                            if  eval(str(ss))==24:
                                                yyss.append(ss)
                                                if  yyss.count(ss)>=2:
                                                    pass
                                                else :
                                                    n+=1
                                                    r.insert(tk.END,f"({n}) {m2(ss)}\n")
                                        except :
                                            pass
    return n
#
def mianl(jkh):
    global r
    n=0
    ysf=["+","-","*","/"]
    yyss=[]
    for j in ysf:
        for l in ysf:
            for i in ysf:
                ss=f"{a}{j}{b}{l}{c}{i}{d}"
                num=m.get()
                try :
                    if  eval(str(ss))==24:
                        yyss.append(ss)
                        if  yyss.count(ss)>=2:
                            pass
                        else :
                            n+=1
                            r.insert(tk.END,f"({n}) {m2(ss)}\n")
                except :
                    pass
    if jkh==1:
        for j in ysf:
            for l in ysf:
                for i in ysf:
                    ss=f"({a}{j}{b}){l}{c}{i}{d}"
                    num=m.get()
                    try :
                        if  eval(str(ss))==24:
                            yyss.append(ss)
                            if  yyss.count(ss)>=2:
                                pass
                            else :
                                n+=1
                                r.insert(tk.END,f"({n}) {m2(ss)}\n")
                    except :
                        pass
        for j in ysf:
            for l in ysf:
                for i in ysf:
                    ss=f"({a}{j}{b}{l}{c}){i}{d}"
                    num=m.get()
                    try :
                        if  eval(str(ss))==24:
                            yyss.append(ss)
                            if  yyss.count(ss)>=2:
                                pass
                            else :
                                n+=1
                                r.insert(tk.END,f"({n}) {m2(ss)}\n")
                    except :
                        pass
        for j in ysf:
            for l in ysf:
                for i in ysf:
                    ss=f"{a}{j}{b}{l}({c}{i}{d})"
                    num=m.get()
                    try :
                        if  eval(str(ss))==24:
                            yyss.append(ss)
                            if  yyss.count(ss)>=2:
                                pass
                            else :
                                n+=1
                                r.insert(tk.END,f"({n}) {m2(ss)}\n")
                    except :
                        pass
        for j in ysf:
            for l in ysf:
                for i in ysf:
                    ss=f"{a}{j}({b}{l}{c}{i}{d})"
                    num=m.get()
                    try :
                        if  eval(str(ss))==24:
                            yyss.append(ss)
                            if  yyss.count(ss)>=2:
                                pass
                            else :
                                n+=1
                                r.insert(tk.END,f"({n}) {m2(ss)}\n")
                    except :
                        pass
        for j in ysf:
            for l in ysf:
                for i in ysf:
                    ss=f"({a}{j}{b}){l}({c}{i}{d})"
                    num=m.get()
                    try :
                        if  eval(str(ss))==24:
                            yyss.append(ss)
                            if  yyss.count(ss)>=2:
                                pass
                            else :
                                n+=1
                                r.insert(tk.END,f"({n}) {m2(ss)}\n")
                    except :
                        pass
        for j in ysf:
            for l in ysf:
                for i in ysf:
                    ss=f"{a}{j}({b}{l}{c}){i}{d}"
                    num=m.get()
                    try :
                        if  eval(str(ss))==24:
                            yyss.append(ss)
                            if  yyss.count(ss)>=2:
                                pass
                            else :
                                n+=1
                                r.insert(tk.END,f"({n}) {m2(ss)}\n")
                    except :
                        pass
    return n
def start():
    global a,b,c,d,m,sytime,jkh,dlsx,r,startb,dl
    r.config(state=tk.NORMAL)
    r.delete("1.0",tk.END)
    sytime=time.time()
    try :
        num=m.get()
        nlist=num.split(" ")
        if nlist[0]=="a" or nlist[0]=="A":
            a=1
        else :
            a=int(nlist[0])
        if nlist[1]=="a" or nlist[1]=="A":
            b=1
        else :
            b=int(nlist[1])
        if nlist[2]=="a" or nlist[2]=="A":
            c=1
        else :
            c=int(nlist[2])
        if nlist[3]=="a" or nlist[3]=="A":
            d=1
        else :
            d=int(nlist[3])
            #
        if dlsx==1:
            if mian(jkh)==0:
                startb.configure(height=4)
                dl.pack_forget()
                r.insert(tk.END,"这组数字似乎无解欸......\n")
            else :
                startb.configure(height=2)
                dl.pack()
                r.insert(tk.END,"破解成功！以上是所有解法。")
                sytime=str(time.time()-sytime)
                r.insert(tk.END,f"本次破解共用{sytime[0:4]}秒。\n")
        else :
            if mianl(jkh)==0:
                startb.configure(height=4)
                dl.pack_forget()
                r.insert(tk.END,"这组数字似乎无解欸......\n")
            else :
                startb.configure(height=2)
                dl.pack()
                r.insert(tk.END,"破解成功！以上是所有解法。")
                sytime=str(time.time()-sytime)
                r.insert(tk.END,f"本次破解共用{sytime[0:4]}秒。\n")
        r.insert(tk.END, "感谢您的使用！Copyright © 2024-2114 RMDCXY.")
        r.config(state=tk.DISABLED)
    except :
        startb.configure(height=4)
        dl.pack_forget()
        r.insert(tk.END,"输入的格式似乎不正确哦~")
        r.config(state=tk.DISABLED)
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
def savejg():
    global r,m
    tempfn=m.get()
    pickpath=filedialog.asksaveasfilename(filetypes=[("24DotTool破解记录文件","*.txt")],title="保存破解记录",initialfile=f"数组{tempfn.replace(" ","")}的解法.txt")
    if pickpath:
        try:
            with open(pickpath, 'w', encoding='utf-8') as file:
                r.config(state=tk.NORMAL)
                file.write(str(r.get("1.0","end")))
                r.config(state=tk.DISABLED)
                title="保存成功！"
                message="成功保存破解记录到指定位置！"
                notification.notify(
                    title=title,
                    message=message,
                    app_name="24DotTool",
                    app_icon=resource_path('icon.ico'),
                    timeout=5,
                )
        except Exception as e:
                print(f"保存失败{e}")
t=tk.Label(root,text="24DotTool",font=("宋体",35))
t.pack()
st=tk.Label(root,text="快速破解24点数学游戏",font=("仿宋",18))
st.pack()
st2=tk.Label(root,text="请输入你要破解的数字组，数字间使用空格隔开",font=("楷体",13))
st2.pack()
m=tk.Entry(root)
m.insert(0,"4 5 1 4")
m.config(fg="black")
m.pack()
startb=tk.Button(root,text="开始破解",height=4,width=15,command=start)
startb.pack(pady=3)
s=tk.Button(root,text="设置",command=config)
s.place(x=0,y=0)
about=tk.Button(root,text="关于",command=aboutp)
about.place(x=0,y=30)
dl=tk.Button(root,text="下载破解结果",command=savejg)
dl.pack_forget()
r=tk.Text(root,height=11,width=84)
r.place(x=2,y=215)
r.insert(tk.END,"等待开始破解...\n")
r.config(state=tk.DISABLED)
root.mainloop()
