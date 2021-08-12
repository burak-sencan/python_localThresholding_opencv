# python_goruntu_isleme(Opencv)

Bu projede görüntüleri binary hale çevirirken oluşan veri kaybi için local threshold hesaplayan algoritma geliştirilmiştir.

1. Bölüm Algoritma Çalışma Mantığı
    Soldan saga doğru ve ardından bir alt bloğa geçmesi için iki for döngüsü kullandım. İlk döngü aşağı,y ekseni için ikinci döngü ise sağa,x ekseni için tanımlandı. Burada blokları elde ettikten sonra bu blogun piksellerinde gezinmek için bir tane daha içe içe döngü tanımladım bu döngü tüm pikselleri soldan saga gezip degerlerini topladı. Bu piksel toplamı değerini blok piksel sayısına bölüp ortalamasını buldum.
    Local threshold bulunduntan sonra tekrar o bloğun başına gidip pikselleri bulunan local threshold degeri ile karşılaştırdım . Büyükse 255’e küçükse 0’a yeni pikseli set ettim.
    Görüntünün analizi veya sonuçların daha iyi incelenmesi için bloklari çizdirip ve hesaplanan local threshold değerlerini yazdırdım.
Not kullanılacak görüntü boyutu: kare ve 2,3,5 in katında olmalı


2.Bölüm Kod
import cv2
size=10 #block size
sensivite= 5 #gürültünün azaltılması için 

x1,x2=(0,size)
y1,y2=(0,size)

orjinal = cv2.imread("sayfa2.png") #orjinal
img = cv2.imread("sayfa2.png",0)   #işlenecek görüntü
img_blc = cv2.imread("sayfa2.png") #bloklara ayrılmış görsel için  
w,h = img.shape
toplam=0



for i in range(0,int(h/size)):
    for j in range(0,int(w/size)):
        #print(x1,x2,y1,y2)
        #===================Local_threshold_val_bulunması=======================
        for k in range(y1,y2):
            for l in range(x1,x2):
                #print(img[k][l])
                toplam+=img[k][l]
        
        local_threshold = int(toplam/size**2)
        #print(local_threshold)
        
        toplam=0
        #=======================local_threshold_uygulaması=======================
        
        for k in range(y1,y2):
            for l in range(x1,x2):
                if img[k][l]>=local_threshold-sensivite:
                    img[k][l]=255
                else:
                    img[k][l]=0

         #====================Blokların Analizi için======================
        font_scale=size/100
        cv2.rectangle(img_blc,(x1,y1),(x2,y2),(255,255,255),(1))
        img_blc = cv2.putText(img_blc, str(local_threshold), 
                              (x1,int(y1+10+int(size/10))), 
                              cv2.FONT_HERSHEY_SIMPLEX, font_scale, 
                              (255,255,255), 1, cv2.LINE_AA)

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

