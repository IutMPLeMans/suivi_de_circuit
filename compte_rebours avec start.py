from __future__ import division
import tkinter
import threading
import time
 
###############################################################################
def sec2hms(sd):
    """Transforme les secondes sd en chaine "hh:mm:ss" pour affichage"""
    h=0
    m=0
    s=sd
    if s >= 60:
        m = s//60
        s -= m*60
        if m >= 60:
            h = m//60
            m -= h*60
    return "%02d:%02d:%02d" % (h, m, s)
 
##################################################################
class Comptearebours(threading.Thread):
 
    def __init__(self, h, m, s):
        threading.Thread.__init__(self)
        self.t = h*3600 + m*60 + s
        self.encore = True
 
    def run(self):
        global app
        t1 = int(time.time())
        app.varsaisie.set(sec2hms(self.t))
        while self.encore:
            t2 = int(time.time())
            if t2>t1:
                self.t -= t2-t1
                if self.t <= 0:
                    self.t = 0
                    self.encore = False
                app.varsaisie.set(sec2hms(self.t))
                t1 = t2
            time.sleep(0.01)
 
    def stop(self):
        self.encore = False
 
##################################################################
class Application(tkinter.Frame):
 
    def __init__(self, master=None):
 
        tkinter.Frame.__init__(self, master)
 
        self.grid()
        self.varsaisie = tkinter.StringVar()
        self.varsaisie.set("")
        self.saisie=tkinter.Entry(self,  background="white", width=50, textvariable=self.varsaisie)
        self.saisie.grid(row=0,column=0,padx=3, pady=6)
 
        self.depart = tkinter.Button(self, text="  Départ  ", command=lambda:self.partir(self))
        self.depart.grid(row=1, column=0, padx=3, pady=3, sticky="e")
 
        self.stop = tkinter.Button(self, text="  stop  ", command=lambda:self.stopper(self))
        self.stop.grid(row=1, column=1, padx=3, pady=3, sticky="w")
 
        self.saisie.focus_set()
 
    def partir(self,event):
        """Lance le compte à rebours"""
        self.chrono = Comptearebours(0,0,10)
        self.chrono.setDaemon(True)
        self.chrono.start()
 
    def stopper(self,event):
        """Arrête le compte à rebours avant la fin normale"""
        self.chrono.stop()
 
##############################################################################
# lancement et affichage de la fenetre
#
if __name__ == "__main__":
    fen=tkinter.Tk()
    fen.title(u"Compte à rebours")
    app=Application(fen)
    fen.mainloop()