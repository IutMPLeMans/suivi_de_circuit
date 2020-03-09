
import wx

class MaFenetre(wx.Frame):    
    def __init__(self):
        super().__init__(parent=None, title='the pathfinder')
        
        bouton1 = wx.Button(self, id=1 , label='Démarrer', pos=(125, 55),size=(100,50))
        bouton2 = wx.Button(self, id=2, label='Quitter', pos=(125, 150),size=(100,50))
    
        self.Bind(wx.EVT_BUTTON, self.OnBouton1, bouton1)
        self.Bind(wx.EVT_BUTTON, self.OnBouton2, bouton2)
       
        self.Show()

    def PrintBouton(self, event):
        print("Bouton ",event.GetId())
        button = event.GetEventObject()
        s = button.GetLabel()
        return s, button
        
    def OnBouton1(self, event):
        s, button = self.PrintBouton(event)
        if s == "Démarrer":
            button.SetLabel("0") # il faut mettre en place un lien qui démarre le jeu
        else:
            button.SetLabel("Démarrer")
  

    def OnBouton2(self, event):
        s, button = self.PrintBouton(event)
        if s == "Quitter":
            self.Destroy()
        else:
            button.SetLabel("Quitter")
       
if __name__ == '__main__':
    app = wx.App()
    frame = MaFenetre()
    app.MainLoop()

