import numpy as np
from matplotlib import pyplot as plt
import cv2 as cv


#Travail avec une vidéo enregistré pour tester le programme

#video = cv.VideoCapture(r"H:\S4\Python\vidéo_tel_2.mp4")
video = cv.VideoCapture(0)
#Vérification que la vidéo est fermée

#calcul moyenne des pixels pour savoir si proche du noir 
#(permet de gérer le niveau de difficulté) ainsi que le pourcentage de noir
def f1()
ind = np.where(u<10)
print(ind[0].shape)
x=img.shape[0]
y=img.shape[1]
p=x*y
pourcentagenoir=(ind[0].shape[0]/p)*100
moyenne_u = np.mean(u[ind])
if not video.isOpened():
    print('verifier le chemin')
    exit()
print('OK')
#choix difficulté

D=int(input("rentrer le pourcentage de difficulté"))
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

        if pourcentagenoir>D:
            print("ok")
        else:
        
        #print("moyenne des pixels", moyenne_u)
        #print("pourcentage noire dans l'image", pourcentagenoir)
    else:
        print('Perdu')
        break
cv.destroyAllWindows()	