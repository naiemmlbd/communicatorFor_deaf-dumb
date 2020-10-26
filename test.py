from keras.models import load_model
from keras.preprocessing import image
from keras.preprocessing.image import ImageDataGenerator
import numpy as np
import cv2

model = load_model('/Users/jhasan/STUDY/cse465_practice/trained_model.h5')

img_dim = 128

class_labels = [
    'A',
    'B',
    'C',
    'D',
    'E',
    'F',
    'G',
    'H',
    'I',
    'J',
    'K',
    'L',
    'M',
    'N',
    'O',
    'P',
    'Q',
    'R',
    'S',
    'T',
    'U',
    'V',
    'W',
    'X',
    'Y',
    'Z',
]

cap = cv2.VideoCapture(0)
font = cv2.FONT_HERSHEY_SIMPLEX

text = ""
word = ""
count_same_frame = 0

#####
temp=0
previouslabel=None
previousText=" "
label = None

while True:

    ret, frame = cap.read()

    # cv2.rectangle(frame, (900, 100), (1300, 500), (255, 0, 0),
    #               3)  # bounding box which captures ASL sign to be detected by the system
    # img1 = frame[100:500, 900:1300]
    # img_ycrcb = cv2.cvtColor(img1, cv2.COLOR_BGR2YCR_CB)
    # blur = cv2.GaussianBlur(img_ycrcb, (11, 11), 0)
    # skin_ycrcb_min = np.array((0, 138, 67))
    # skin_ycrcb_max = np.array((255, 173, 133))
    # mask = cv2.inRange(blur, skin_ycrcb_min,
    #                    skin_ycrcb_max)  # detecting the hand in the bounding box using skin detection

    cv2.rectangle(frame, (100, 100), (500, 500), (255, 255, 255), 2)
    roi = frame[100:500, 100:500]
    img = cv2.resize(roi, (img_dim, img_dim))
    img_ycrcb = cv2.cvtColor(roi, cv2.COLOR_BGR2YCR_CB)
    blur = cv2.GaussianBlur(img_ycrcb, (11, 11), 0)
    skin_ycrcb_min = np.array((0, 138, 67))
    skin_ycrcb_max = np.array((255, 173, 133))
    mask = cv2.inRange(blur, skin_ycrcb_min,
                       skin_ycrcb_max)  # detecting the hand in the bounding box using skin detection

    img = image.img_to_array(img)
    img = np.expand_dims(img, axis=0)
    img = img.astype('float32')/255
    label = np.argmax(model.predict(img))
    color = (0, 0, 255)

    if (label < 26):
        if (temp == 0):
            previouslabel = class_labels[label]
        if previouslabel == class_labels[label]:
           previouslabel = class_labels[label]
           temp += 1
        else:
           temp = 0
        if (temp == 40):
            if (class_labels[label] == 'P'):
                label = " "
            text = text + class_labels[label]
            if (class_labels[label] == 'Q'):
                words = re.split(" +", text)
                words.pop()
                text = " ".join(words)
        # text=previousText
            print (text)

        cv2.putText(frame, class_labels[label], (50, 150), font, 8, (0, 125, 155),
                    2)  # displaying the predicted letter on the main screen
        cv2.putText(frame, text, (50, 450), font, 3, (0, 0, 255), 2)

    cv2.imshow('Video', frame)
    cv2.imshow('Mask', mask)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()
