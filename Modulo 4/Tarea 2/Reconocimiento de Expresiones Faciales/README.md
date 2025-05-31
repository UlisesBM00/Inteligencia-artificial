
# Reconocimiento de Expresiones Faciales

Este proyecto utiliza redes neuronales convolucionales (CNN) para reconocer emociones en rostros humanos. Las emociones detectadas son:

- 😠 Angry  
- 🤢 Disgust  
- 😱 Fear  
- 😀 Happy  
- 😐 Neutral  
- 😢 Sad  
- 😲 Surprise  

---

## Estructura del Proyecto

```
├── face_detector/
│   ├── deploy.prototxt
│   ├── res10_300x300_ssd_iter_140000.caffemodel
│   └── haarcascade_frontalface2.xml
├── images/
│   ├── train/
        ├── angry/
│       ├── disgust/
│       ├── fear/
│       ├── happy/
│       ├── neutral/
│       ├── sad/
│       └── surprise/
│   └── validation/
│       ├── angry/
│       ├── disgust/
│       ├── fear/
│       ├── happy/
│       ├── neutral/
│       ├── sad/
│       └── surprise/
├── FaceEmotion.py
├── FaceEmotionVideo.py
├── model.h5
└── README.md
```

---

## Requisitos

- Python 3.8 o 3.10  
- TensorFlow 2.4.1  
- Keras 2.4.3  
- OpenCV  
- imutils  

Instalación recomendada:

```bash
pip install keras==2.4.3
pip install tensorflow==2.4.1
pip install opencv-python
pip install imutils
```

---

## Dataset

El dataset fue obtenido desde Kaggle:  
🔗 https://www.kaggle.com/datasets/jonathanoheix/face-expression-recognition-dataset

```

---

## 1️⃣ Entrenamiento del modelo

El archivo `FaceEmotion.py` entrena una red convolucional profunda que reconoce emociones a partir de imágenes en escala de grises (48x48 píxeles).

Ejecútalo con:

```bash
python FaceEmotion.py
```

El modelo entrenado se guardará como `model.h5`.

---

## 2️⃣ Detección de emociones desde webcam

El archivo `FaceEmotionVideo.py` detecta rostros usando un modelo SSD y predice emociones en tiempo real.

Para ejecutarlo:

```bash
python FaceEmotionVideo.py
```

Presiona `q` para salir.

Asegúrate de tener los archivos del detector de rostros en la carpeta `face_detector/`:

- `deploy.prototxt`
- `res10_300x300_ssd_iter_140000.caffemodel`

El modelo `model.h5` debe estar en la raíz del proyecto.

---

## 🎥 Video de Demostración

Puedes ver un video de demostración del sistema funcionando en tiempo real en el siguiente enlace:

🔗 [Ver demostración en Google Drive](https://drive.google.com/file/d/12jUUSmsXwQbDTSS2syj53erBb-KzyXvR/view?usp=sharing)

---

## Autor
- 👨‍💻 Ulises Beltrán Magaña 
