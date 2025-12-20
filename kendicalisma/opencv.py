import cv2

# 0 genellikle varsayılan webcam'dir
kamera = cv2.VideoCapture(0)

while True:
    ret, kare = kamera.read()
    
    # Görüntüyü griye çevir
    gri_kare = cv2.cvtColor(kare, cv2.COLOR_BGR2GRAY)
    
    cv2.imshow('Canli Kamera', gri_kare)
    
    # 'q' tuşuna basınca çık
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

kamera.release()
cv2.destroyAllWindows()