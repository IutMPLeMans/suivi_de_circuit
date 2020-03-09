import numpy as np
from matplotlib import pyplot as plt
import cv2 as cv

#Ouverture du bouton décompte
from tkinter import *
import time
import tkinter.messagebox
#C'est un bouton décompte de 10s avec un bouton "commencer" et un bouton "quitter"

class App:
 def __init__(self,master):
  frame = Frame(master)
  frame.pack()
  self.entryWidget = Entry(frame)
  self.entryWidget["width"] = 15
  self.entryWidget.pack(side=LEFT)
  self.hi_there = Button(frame, text="Commencer", command=self.start)
  self.hi_there.pack(side=LEFT)
  self.button = Button(frame, text="Quitter", fg="red", command=frame.quit)
  self.button.pack(side=LEFT)
   
 def start(self):
  text = self.entryWidget.get().strip()
  if text != "":
   num = int(text)
   self.countDown(num)
   
 def countDown(self,seconds):
  lbl1.config(bg='yellow')
  lbl1.config(height=3, font=('times', 20, 'bold'))
  for k in range(seconds, 0, -1):
   if k == 30:
    print("\a")
   if k== 29:
    print("\a")
   if k== 28:
    print("\a")
   lbl1["text"] = k
   root.update()
   time.sleep(1)
  lbl1.config(bg='red')
  lbl1.config(fg='white')
  lbl1["text"] = "Compte à rebours terminé"
  tkMessageBox.showinfo("Compte à rebours terminé","Compte à rebours terminé")
  
 def GetSource():
  get_window = Tkinter.Toplevel(root)
  get_window.title('Source File?')
  Tkinter.Entry(get_window, width=30,
      textvariable=source).pack()
  Tkinter.Button(get_window, text="Change",
      command=lambda: update_specs()).pack()
  
root = Tk()
root.title("Countdown")
lbl1 = Label()
lbl1.pack(fill=BOTH, expand=1)
app = App(root)
root.mainloop()

#Travail avec une vidéo enregistré pour tester le programme

#video = cv.VideoCapture(r"H:\S4\Python\vidéo_tel_2.mp4")
video = cv.VideoCapture(0)
#Vérification que la vidéo est fermée
if not video.isOpened():
    print('verifier le chemin')
    exit()
print('OK')

#définition de la taille du rectangle à analyser
def fdifficulté(img):
    z=int(input("choisir niveau de difficulté 1,2,3"))
    if z==1:
        x=img.shape[0]
        y=img.shape[1]
    elif z==2:
        x=img.shape[0]/2+img.shape[0]/4
        y=img.shape[1]/2+img.shape[0]/4
    else:
        x=(img.shape[0]/2+img.shape[0]/4)/2+(img.shape[0]/2+img.shape[0]/4)/4
        y=(img.shape[1]/2+img.shape[0]/4)/2+(img.shape[1]/2+img.shape[0]/4)/4
    return x, y 

#calcul moyenne des pixels pour savoir si proche du noir 
#(permet de gérer le niveau de difficulté) ainsi que le pourcentage de noir
def fpourcentage(img):
    ind = np.where(img<10)
    print(ind[0].shape)
    fdifficulté(img)
    p=x*y
    pourcentagenoir=(ind[0].shape[0]/p)*100
    moyenne_u = np.mean(u[ind])
    #print("moyenne des pixels", moyenne_u)
    #print("pourcentage noire dans l'image", pourcentagenoir)
    return moyenne_u

#affichage video couleur et noir/blanc
i=0
while i<20: 
    ret, img = video.read()
    i=i+1
    if ret:
        print(img.shape)
        cv.imshow('video',img)
        u=cv.cvtColor(img, cv.COLOR_BGR2GRAY); #on convertit en noir et blanc
        cv.imshow('videoNB',u)
        cv.waitKey(30)
        print("ok", fpourcentage(u))  
       
    else:
        print('Perdu')
        break
cv.destroyAllWindows()	