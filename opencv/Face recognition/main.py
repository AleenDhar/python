import cv2
from simple_facerec import SimpleFacerec 

sfr = SimpleFacerec()
sfr.load_encoding_images("images/")

cap=cv2.VideoCapture(0)
fps = cap.get(cv2.CAP_PROP_FPS)
while True:
    #reading the frames
    ret,frame = cap.read()
    #detecting the faces
    face_locations, face_names = sfr.detect_known_faces(frame)
    for face_loc,name in zip(face_locations,face_names):
        y1 , x1, y2,x2 = face_loc[0],face_loc[1],face_loc[2],face_loc[3]
        
        cv2.rectangle(frame,(x1,y1),(x2,y2),(0,0,225),2)
        cv2.putText(frame,name,(x2,y1-10),cv2.FONT_HERSHEY_DUPLEX,1,(0,0,200),2)



    cv2.imshow("Frame",frame)
    key=cv2.waitKey(10)
    if key & 0xFF == ord('q'):
        break  
cap.release()
cv2.destroyAllWindows

