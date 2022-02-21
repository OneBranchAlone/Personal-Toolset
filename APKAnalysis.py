import tkinter as tk
from tkinter.messagebox import showinfo
import windnd
import json
from apkutils import  APK

def dragged_files(files):
    msg = '\n'.join((item.decode('gbk') for item in files))
    apk = APK(msg)
    if apk.get_manifest():
        # print(json.dumps(apk.get_manifest(), indent=1))
        re = json.dumps(apk.get_manifest(), indent=1)
        re = json.loads(re)
        enter.delete(0.0, tk.END)
        enter.insert(tk.INSERT,"包名："+re['@package'])
        print("版本：" + re['@android:versionCode'])
        print("包名：" + re['@package'])
        #showinfo('zheshisha',"包名：" + re['@package'])
    #showinfo('放入文件',msg)

root = tk.Tk()   #初始化窗口
root.title('By:一枝独秀')  #顶层窗口名称
root.geometry("500x300+200+20")  #设置窗口大小
root.resizable(width=True,height=True) #设置窗口是否可变，宽不可变，高可变，默认为True

windnd.hook_dropfiles(root,func=dragged_files)

enter = tk.Text(root,height=2)
enter1 = tk.Text(root,height=2)

enter.pack()
#创建文本框
# entry = Entry(root,width=20,height='22',bg='black',fg='green',command='hello')
# #输入默认值
# entry.insert(END, 'default text')
# entry.pack(side=LEFT,fill=BOTH,padx=2)

tk.mainloop()
