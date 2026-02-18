import cv2
import numpy

resim=cv2.imread("cocukBayrami.jpg")
kesit=resim[50:150,300:400] # resimden kordinatlarını verdiğim bölgeyi değişkene atadık bellibir kesit aldık

# Aldığım resmi ana resmin bir köşesine yapıştırmak için;

resim[0:100,0:100]=kesit #resmin kordinatlarını belirledik ve resmi yapıştırdık
#kesitin sınırını aşan bir kısma yapıştırılmaz

resim[400:450,300:350]=(0,150,255) #kordinatları verilen alana RGB değerlerini atanması 

#cv2.imshow("KESIT",kesit)
cv2.imshow("BAYRAM",resim)



cv2.waitKey(0)
cv2.destroyAllWindows()