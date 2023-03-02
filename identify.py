import face_recognition
from PIL import Image, ImageDraw
import notify
import cv2
import time

camera = cv2.VideoCapture(0)
faceCascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
while True:
  ret, frame = camera.read()
  gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
  faces = faceCascade.detectMultiScale(
    gray,
    scaleFactor=1.5,
    minSize=(30, 30)
  )
  if cv2.waitKey(1) & 0xFF == ord('q'):
    break
  if len(faces)!=0:
    time.sleep(2)
    return_value, image = camera.read()
    cv2.imwrite('test.png', image)
    del(camera)
    break

jeff = face_recognition.load_image_file('C:/Users/surab/Desktop/College/3RD YEAR/5TH SEM/IOTES/IOT_PROJ/Jeff Bezos.png')
jeff_face_encoding = face_recognition.face_encodings(jeff)[0]

elon = face_recognition.load_image_file('C:/Users/surab/Desktop/College/3RD YEAR/5TH SEM/IOTES/IOT_PROJ/Elon Musk.jpg')
elon_face_encoding = face_recognition.face_encodings(elon)[0]

known_face_encodings = [ jeff_face_encoding,
  elon_face_encoding
]

known_face_names = [
  "Jeff Bezos",
  "Elon Musk"
]

test_image = face_recognition.load_image_file(
    'test.png')

face_locations = face_recognition.face_locations(test_image)
face_encodings = face_recognition.face_encodings(test_image, face_locations)

pil_image = Image.fromarray(test_image)

draw = ImageDraw.Draw(pil_image)

for(top, right, bottom, left), face_encoding in zip(face_locations, face_encodings):
  matches = face_recognition.compare_faces(known_face_encodings, face_encoding)

  name = "Unknown Person"

  if True in matches:
    first_match_index = matches.index(True)
    name = known_face_names[first_match_index]

  draw.rectangle(((left, top), (right, bottom)), outline=(255,255,0))

  text_width, text_height = draw.textsize(name)
  draw.rectangle(((left,bottom - text_height - 10), (right, bottom)), fill=(255,255,0), outline=(255,255,0))
  draw.text((left + 6, bottom - text_height - 5), name, fill=(0,0,0))

del draw


pil_image.save('pic.jpg')

notify.send_email('email@gmail.com','pic.jpg')