import tkinter
import time
import threading

#创建应用程序窗口，设置标题和大小
#Créer un interface 
root = tkinter.Tk()
root.title('倒计时按钮')
root['width'] = 400
root['height'] = 300

#创建Text组件，放置一些文字
#Créer un texte, 
richText = tkinter.Text(root, width=380)
richText.place(x=10, y=10, width=380, height=230)
richText.insert('0.0', 'décompte de 10s')

#创建倒计时按钮组件
#Créer un bouton décompte
btnTime = tkinter.Button(root, text='', width=200)
btnTime.place(x=80, y=250, width=200, height=30)

def stop():
 # 禁用按钮，倒计时10秒后取消禁用
 # On ne peut pas toucher le bonton pendant 10s. Après 10s, on peut.
    btnTime['state'] = 'disabled'
    for i in range(10,-1,-1):
        btnTime['text'] = '剩余时间' + str(i) + '秒'
        time.sleep(1)
    btnTime['state'] = 'normal'
    btnTime['text'] = '单击按钮继续后续工作'

# 创建并启动线程
#Start
t = threading.Thread(target=stop)
t.start()

root.mainloop()
