#coding:latin1

### Infos ###
_version_ = "0.0.1"
_author_ = "Franck Awounang Nekdem"
_name_ = "VCapture"
_description_ = "Visualiseur à base de VideoCapture pour Tkinter"
### ----- ###

import vidcap
import ImageTk
import ImageEnhance
import time
import Tkinter
import threading




### Constants Definition ###
_QUANTUM_GET = 0.2
_QUANTUM_SET = 0.2
_DEFAULT_SIZE = (320, 240)
### END Definition ###

class Device:
    """Create instances of this class which will then represent video devices.

    For the lifetime of the instance, the device is blocked, so it can not be
    used by other applications (which is quite normal Windows behavior).
    If you want to access the device from another program, you have to delete
    the instance first (e.g. del cam).

    """
    def __init__(self, devnum=0,size=_DEFAULT_SIZE,color=False):
        """devnum:  VideoCapture enumerates the available video capture devices
                    on your system.  If you have more than one device, specify
                    the desired one here.  The device number starts from 0.

           size:    Size of the visualisator of the capture device.

        """
        ### Setting up the Camera ###
        try:
            self.dev = vidcap.new_Dev(devnum,0)
        except:
            return None
        ### Methods Redirection ###
        self.displayCaptureFilterProperties = self.dev.displaycapturefilterproperties
        self.displayCapturePinProperties = self.dev.displaycapturepinproperties
        self.displayPropertyPage = self.dev.displaypropertypage
        self.setResolution = self.dev.setresolution
        self.getBuffer = self.dev.getbuffer
        ### End Redirections ###
        ### Fields definition ###
        self.color = color
        self.alive = True
        self.size = size
        self.master = Tkinter.Tk()
        self.master.resizable(False,False)
        self.master.title("Camera N-%d" % (devnum))
        self.can = Tkinter.Canvas(self.master,width=size[0],height=size[1],bg="black")
        self.can.pack()
        self.img = ImageTk.Image.new("RGB",size,0)
        self.photo = ImageTk.PhotoImage(self.img, self.size, master = self.can)
        self.id = self.can.create_image(size[0]/2+1,size[1]/2+1,image=self.photo)
        self.nb_image = 0
        self.current_image = 0
        self.devnum = devnum

        
        self.master.wm_protocol("WM_DELETE_WINDOW",self.term)
        self.master.bind("<Alt-F>",self.displayCaptureFilterProperties)
        self.master.bind("<Alt-f>",self.displayCaptureFilterProperties)
        self.master.bind("<Alt-P>",self.displayCapturePinProperties)
        self.master.bind("<Alt-p>",self.displayCapturePinProperties)
        self.master.bind("<Escape>",self.term)
        
        self.mainloop = self.can.mainloop

     
    def _loop_(self):
        try:
            while self.alive:
                if 1:#self.nb_image>self.current_image:
                    self.current_image += 1
                    self.photo = ImageTk.PhotoImage(self.img, self.size, master=self.master)
                    self.can.itemconfigure(self.id,image=self.photo)
                    n_id = self.can.create_image(self.size[0]/2+1, self.size[1]/2+1, image=self.photo)
                    self.can.create_image(self.size[0]/2+1, self.size[1]/2+1, image=self.photo)
                    self.can.lift(n_id)
                    self.can.delete(self.id)
                    self.id = n_id
                    time.sleep(_QUANTUM_GET)
        except:
            self.alive = False
            return None
    
    def _setImages_(self):
        try:
            while self.alive:
                self.nb_image += 1
                img = self.getImage()
                if (img.size != self.size):
                    self.img = img.resize(self.size)
                else:
                    self.img = img
                time.sleep(_QUANTUM_SET)
        except:
            self.alive = False
            return None

    def getImage(self):
        """Returns a PIL Image instance."""
        buffer, width, height = self.getBuffer()
        if buffer:
            if self.color:
                return ImageTk.Image.fromstring('RGB', (width, height), buffer, 'raw', 'BGR', 0, -1)
            else:
                return ImageEnhance.Color(ImageTk.Image.fromstring('RGB', (width, height), buffer, 'raw', 'BGR', 0, -1)).enhance(self.color)

    def inited(self):
        """Tels if the device capture have been found and can be used."""
        return hasattr(self,"master")


                
    def saveSnapshot(self, filename, **keywords):
        """Saves a snapshot to the harddisk.

        The filetype depends on the filename extension.  Everything that PIL
        can handle can be specified (foo.jpg, foo.gif, foo.bmp, ...).

        filename:   String containing the name of the resulting file.
        
        Additional keyword arguments can be give which are just passed to the
        save() method of the Image class.  For example you can specify the
        compression level of a JPEG image by quality=75 (which is the default
        value anyway).

        """
        self.getImage().save(filename, **keywords)


    def start(self):
        """Start capturing"""
        self._Trd1 = threading.Thread(None,self._setImages_,)
        self._Trd2 = threading.Thread(None,self._loop_)
        self._Trd1.start()
        self._Trd2.start()

    def term(self,event=None):
        """Stop the cam and destroy the windows"""
        self.alive = False
        self.cam = None
        if self.inited():
            try:
                self.master.destroy()
                self._Trd1._Thread__stop()
                self._Trd2._Thread__stop()
            except :
                pass

               

if __name__ == "__main__":
    cam = Device(0)
    cam.start()
    cam.mainloop()
    cam.master.quit()
    del cam

