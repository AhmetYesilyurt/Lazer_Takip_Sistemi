import cv2

#Yüz şeklinin öğretilmiş .xml uzantılı dosyası
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

cap = cv2.VideoCapture(0)

while 1:
    ret, img = cap.read()
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.5, 3)
  
  # Algılanan yüzü kare içerisine alma
    for (x,y,w,h) in faces:
        cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
                       
    #Yüzü kare içine aldıktan sonra, karenin merkezini bulma
        x_eksen=x+(w/2)
        y_eksen=y+(h/2)
        print ("[",int(x_eksen),int(y_eksen),"]")
        
        cv2.imshow('img',img)
   
   # ESC tuşuna bastığımızda programdan çıkması için gereken kısım
    k = cv2.waitKey(30) & 0xff
    if k == 27:
        break

cap.release()
cv2.destroyAllWindows()
