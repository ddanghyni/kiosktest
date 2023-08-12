import sys
sys.path.append('/Users/ddanghyni0425/kiosktest/kiosk')
from fastapi import APIRouter, Depends, File, UploadFile, HTTPException
from sqlalchemy.orm import Session
from database import get_db
import cv2
import numpy as np
from tensorflow import keras
from keras.models import load_model
from keras.preprocessing.image import img_to_array
from models import FaceAnalysis  # FaceAnalysis 모델을 가져옴
import os

FILE_DIR = '/Users/ddanghyni0425/kiosktest/kiosk/domain/face_detect'

face_classifier = cv2.CascadeClassifier(os.path.join(FILE_DIR, 'haarcascade_frontalface_default.xml'))
emotion_model = load_model(os.path.join(FILE_DIR, 'emotion_deftection_model.h5'))
age_model = load_model(os.path.join(FILE_DIR, 'age_model_4.h5'))
gender_model = load_model(os.path.join(FILE_DIR, 'gender_model_.h5'))

router = APIRouter()

class_labels = ['Angry', 'Disgust', 'Fear', 'Happy', 'Neutral', 'Sad', 'Surprise']
gender_labels = ['Male', 'Female']

@router.post("/analyze_face")
def 얼굴_인식(file: UploadFile = File(...), db: Session = Depends(get_db)):
    image = cv2.imdecode(np.fromstring(file.file.read(), np.uint8), cv2.IMREAD_UNCHANGED)
    
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    faces = face_classifier.detectMultiScale(gray, 1.3, 5)
    
    for (x, y, w, h) in faces:
        roi_gray = gray[y:y+h, x:x+w]
        roi_gray = cv2.resize(roi_gray, (48, 48), interpolation=cv2.INTER_AREA)
        roi = roi_gray.astype('float')/255.0
        roi = img_to_array(roi)
        roi = np.expand_dims(roi, axis=0)

        preds = emotion_model.predict(roi)[0]
        emotion_label = class_labels[preds.argmax()]

        roi_color = image[y:y+h, x:x+w]
        roi_color = cv2.resize(roi_color, (200, 200), interpolation=cv2.INTER_AREA)

        gender_predict = gender_model.predict(np.array(roi_color).reshape(-1, 200, 200, 3))
        gender_label = gender_labels[int(gender_predict > 0.5)]
        
        age_predict = age_model.predict(np.array(roi_color).reshape(-1, 200, 200, 3))
        age_label = round(age_predict[0][0])

        # DB에 저장하는 코드를 여기에 추가...
        face_analysis = FaceAnalysis(
            emotion=emotion_label,
            gender=gender_label,
            age=age_label
        )
        db.add(face_analysis)
        db.commit()
        db.refresh(face_analysis)
        
        return {"emotion": emotion_label, "gender": gender_label, "age": age_label}
    
    raise HTTPException(status_code=400, detail="Face not detected")

