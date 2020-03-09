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


#définition de la taille du rectangle à analyser
def fdifficulté(img):
    z=int(input("choisir niveau de difficulté 1,2,3"))
    if z==1:
        h=img.shape[0]
        l=img.shape[1]
    elif z==2:
        h=img.shape[0]//2
        l=img.shape[1]//2
    else:
        h=img.shape[0]//4
        l=img.shape[1]//4
    return h, l 

#calcul moyenne des pixels pour savoir si proche du noir 
#(permet de gérer le niveau de difficulté) ainsi que le pourcentage de noir
def fpourcentage(img,h,l):
    centre=(img.shape[0]//2,img.shape[1]//2)
    u=img[centre[0]-h//2:centre[0]+h//2,centre[1]-l//2:centre[1]+l//2]
    ind = np.where(u<10)
    print(ind[0].shape)
    p=h*l
    pourcentagenoir=(ind[0].shape[0]/p)*100
    moyenne_u = np.mean(u[ind])
    #print("moyenne des pixels", moyenne_u)
    #print("pourcentage noire dans l'image", pourcentagenoir)
    return moyenne_u, cv.imshow("zone",u)

#affichage video couleur et noir/blanc
i=0
ret, img = video.read()
h,l=fdifficulté(img)
while i<4000: 
    ret, img = video.read()
    i=i+1
    if ret:
        print(img.shape)
        cv.imshow('video',img)
        u=cv.cvtColor(img, cv.COLOR_BGR2GRAY); #on convertit en noir et blanc
        cv.imshow('videoNB',u)
        cv.waitKey(30)
        fpourcentage(u,h,l)
        print("ok")  
       
    else:
        print('Perdu')
        break
cv.destroyAllWindows()