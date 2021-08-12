# python_goruntu_isleme(Opencv)

Bu projede görüntüleri binary hale çevirirken oluşan veri kaybi için local threshold hesaplayan algoritma geliştirilmiştir.

1. Bölüm Algoritma Çalışma Mantığı
    Soldan saga doğru ve ardından bir alt bloğa geçmesi için iki for döngüsü kullandım. İlk döngü aşağı,y ekseni için ikinci döngü ise sağa,x ekseni için tanımlandı. Burada blokları elde ettikten sonra bu blogun piksellerinde gezinmek için bir tane daha içe içe döngü tanımladım bu döngü tüm pikselleri soldan saga gezip degerlerini topladı. Bu piksel toplamı değerini blok piksel sayısına bölüp ortalamasını buldum.
    Local threshold bulunduntan sonra tekrar o bloğun başına gidip pikselleri bulunan local threshold degeri ile karşılaştırdım . Büyükse 255’e küçükse 0’a yeni pikseli set ettim.
    Görüntünün analizi veya sonuçların daha iyi incelenmesi için bloklari çizdirip ve hesaplanan local threshold değerlerini yazdırdım.
Not kullanılacak görüntü boyutu: kare ve 2,3,5 in katında olmalı

