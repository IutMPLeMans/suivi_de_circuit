
import wx
import numpy as np
from matplotlib import pyplot as plt
import cv2 as cv

#Travail avec une vidéo enregistré pour tester le programme
#video = cv.VideoCapture(r"H:\S4\Python\vidéo_tel_2.mp4")
video = cv.VideoCapture(0)
#Vérification que la vidéo est fermée
if not video.isOpened():
    print('verifier le chemin')
    exit()
print('OK')

class MaFenetre(wx.Frame):    
    def __init__(self):
        super().__init__(parent=None, title='The Pathfinder')
        
        self.SetSize(100,150,1000,1000)
        self.Show()

        

        #Creation du menu (ne marche pas)

        def installer_menu (self):
          barre_menu = wx.MenuBar()
          menu_fichier = wx.Menu()
          article_apropos = menu_fichier.Append(wx.ID_ABOUT, 'A propos', 'A propos de moi')
          article_quitter = menu_fichier.Append(wx.ID_EXIT, 'Quitter', "Quitter l'application")
          barre_menu.Append(menu_fichier, '&Fichier')
          self.SetMenuBar(barre_menu)

        def OnQuit(self, e):
          print('Aticle : ',e.GetId() )
          print("Je quitte")


#Creation des boutons

        bouton1 = wx.Button(self, id=1 , label='Easy', pos=(150, 50),size=(100,50))
        bouton2 = wx.Button(self, id=2, label='Medium', pos=(150, 150),size=(100,50))
        bouton3= wx.Button(self, id=3, label='Hard', pos=(150, 250),size=(100,50))


        self.Bind(wx.EVT_BUTTON, self.OnBouton1, bouton1)
        self.Bind(wx.EVT_BUTTON, self.OnBouton2, bouton2)
        self.Bind(wx.EVT_BUTTON, self.OnBouton3, bouton3)
        #self.SetSize(450,150,400,400)
       
        #self.Show()

    def PrintBouton(self, event):
        print("Bouton ",event.GetId())
        button = event.GetEventObject()
        s = button.GetLabel()
        return s, button
        
    #Choix de la difficulté en cliquant sur le bouton "Easy", "Medium" ou "Hard"

    def OnBouton1(self, event):
        s, button = self.PrintBouton(event)
        if s == "Easy":
            h=img.shape[0]
            l=img.shape[1]
            self.Destroy()
        else:
            button.SetLabel("Easy")
  

    def OnBouton2(self, event):
        s, button = self.PrintBouton(event)
        if s == "Medium":
            h=img.shape[0]//2
            l=img.shape[1]//2
            self.Destroy()
        else:
            button.SetLabel("Medium")

    def OnBouton3(self, event):
        s, button = self.PrintBouton(event)
        if s == "Hard":
            h=img.shape[0]//4
            l=img.shape[1]//4
            self.Destroy()
        else:
            button.SetLabel("Hard")

if __name__ == '__main__':
    app = wx.App()
    frame = MaFenetre()
    app.MainLoop()

