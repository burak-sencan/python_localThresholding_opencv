"""
Bu çalısmada local threshold degeri bulmak için basitce resmi bloklara ayıran
bu blokların ortalamasını local thresgold degeri olarak hesaplayan ve bu değeri
ilgili bloga uygulayan local threshold algoritması geliştirilmiştir.

not resim kare olmalıdır ve 2,3,5 in katları olmalıdır.
Burak Şencan 2021
"""
import cv2
size=10 #block size
sensivite= 4  # arka plan gürültüsü için 

#sensivite= size/0.8
x1,x2=(0,size)
y1,y2=(0,size)

orjinal = cv2.imread("sayfa3.png")
img = cv2.imread("sayfa3.png",0)
img_blc = cv2.imread("sayfa3.png")
w,h = img.shape
toplam=0



for i in range(0,int(h/size)):
    for j in range(0,int(w/size)):
        #print(x1,x2,y1,y2)
        #===================Local_threshold_val===============================
        for k in range(y1,y2):
            for l in range(x1,x2):
                #print(img[k][l])
                toplam+=img[k][l]
        
        local_threshold = int(toplam/size**2)
        #print(local_threshold)
        
        toplam=0
        #=======================local_threshold_app============================
        
        for k in range(y1,y2):
            for l in range(x1,x2):
                if img[k][l]>=local_threshold-sensivite:
                    img[k][l]=255
                else:
                    img[k][l]=0

         #=====================================================================
        font_scale=size/100
        cv2.rectangle(img_blc,(x1,y1),(x2,y2),(255,255,255),(1))
        img_blc = cv2.putText(img_blc, str(local_threshold), (x1,int(y1+10+int(size/10))), cv2.FONT_HERSHEY_SIMPLEX, font_scale, (255,255,255), 1, cv2.LINE_AA)

        x1+=size
        x2+=size
        if x2>w:
            x1,x2=(0,size)
    
    y1+=size
    y2+=size
    if y2>h:
        y1,y2=(0,size)


cv2.imshow("orjinal",orjinal)
cv2.waitKey(0)



size_text = str(size)+"x"+str(size)+" px"
sens_text = str(sensivite)+" sens."
font = cv2.FONT_HERSHEY_SIMPLEX
# org
org = (0, 15)
# fontScale
fontScale =0.5
# Blue color in BGR
color = (0, 0, 255)
# Line thickness of 2 px
thickness = 1
img_blc = cv2.putText(img_blc, size_text, org, font, fontScale, color, thickness, cv2.LINE_AA)
img_blc = cv2.putText(img_blc, sens_text, (0,30), font, fontScale, color, thickness, cv2.LINE_AA)

cv2.imshow("blocklu",img_blc)
cv2.waitKey(0)



cv2.imshow("binary",img)
cv2.waitKey(0)
