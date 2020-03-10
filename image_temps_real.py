import numpy as np
from matplotlib import pyplot as plt
import cv2 as cv


#Travail avec une video enregistré pour tester le programme

#v = cv.VideoCapture(r"H:\S4\Python\vidéo_tel_2.mp4")
v = cv.VideoCapture(0)

#Verification que la video est fermée

if not v.isOpened():
    print('verifier le chemin')
    exit()
print('Camera OK')

#affichage video couleur et noir/blanc
pourcentagenoir=100
while pourcentagenoir>10: 
    ret, img = v.read()
    
    if ret:
        z=img[50:350, 50:500] #definition d'un cadre dans l'image
        cv.imshow('video',img)
        u=cv.cvtColor(z, cv.COLOR_BGR2GRAY); #on convertit en noir et blanc
        cv.imshow('videoNB',u)
        ind = np.where(u<75)
        x=img.shape[0]
        y=img.shape[1]
        p = 300*450
        pourcentagenoir=(ind[0].shape[0]/p)*100
        cv.waitKey(30) 
 

    else:
        print('Perdu')
        break
cv.destroyAllWindows()	

#calcul moyenne des pixels pour savoir si proche du noir (permet de gerer le niveau de difficulte) ainsi que le pourcentage de noir

print(img.shape)
print(ind[0].shape)
moyenne_u = np.mean(u[ind])
print("moyenne des pixels", moyenne_u)
print("pourcentage noir dans l'image", pourcentagenoir)


