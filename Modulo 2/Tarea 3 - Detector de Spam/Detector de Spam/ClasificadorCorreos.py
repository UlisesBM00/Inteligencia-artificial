# Importar las librerías necesarias
import numpy as np
import pandas as pd
import re
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import CountVectorizer, TfidfTransformer
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import precision_score, recall_score
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
import nltk

# Descargar stopwords y tokenizer 
#nltk.download('punkt_tab')
#nltk.download('stopwords')

# Preprocesamiento del texto
def preprocesar_texto(texto):
    # Asegurar que el texto sea string
    texto=str(texto)
    # Convertir a minúsculas
    texto = texto.lower()
    # Eliminar caracteres especiales
    texto = re.sub(r'\W', ' ', texto)
    # Eliminar dígitos
    texto = re.sub(r'\d+', '', texto)
    # Tokenizar
    palabras = word_tokenize(texto)
    # Eliminar palabras vacías (stopwords)
    palabras_vacias = set(stopwords.words('english'))
    palabras = [palabra for palabra in palabras if palabra not in palabras_vacias]
    # Si el texto queda vacío, devolver un texto genérico para evitar que sea completamente vacío
    return ' '.join(palabras) if palabras else 'default_text'

# Cargar el dataset
data = pd.read_csv('spam_assassin.csv')

# Eliminar correos duplicados
data.drop_duplicates(inplace=True)

# Preprocesar el texto de los correos
data['text'] = data['text'].apply(preprocesar_texto)

# Dividir el conjunto de datos en entrenamiento y prueba
X_train, X_test, y_train, y_test = train_test_split(data['text'], data['target'], test_size=0.3, random_state=42)

# Eliminar correos vacíos
X_train = X_train[X_train.str.strip() != '']
# Convertir el texto a una representación numérica (frecuencia de palabras)
vectorizador = CountVectorizer(ngram_range=(1, 2), max_features=10000)
X_train_counts = vectorizador.fit_transform(X_train)

# Calcular el TF-IDF (Term Frequency - Inverse Document Frequency)
tfidf_transformer = TfidfTransformer()
X_train_tfidf = tfidf_transformer.fit_transform(X_train_counts)

# Entrenar el modelo de Naive Bayes
modelo = MultinomialNB()
modelo.fit(X_train_tfidf, y_train)

# Preparar los datos de prueba
X_test_counts = vectorizador.transform(X_test)
X_test_tfidf = tfidf_transformer.transform(X_test_counts)

# Realizar predicciones
predicciones = modelo.predict(X_test_tfidf)

# Calcular P(Spam)
total_correos = len(data)
numero_correos_spam = data['target'].sum()  # suma de los correos spam (1s)
P_spam = numero_correos_spam / total_correos

# Contar la frecuencia de palabras en correos spam
frecuencia_caracteristicas_spam = np.zeros(X_train_tfidf.shape[1])
for i in range(len(y_train)):
    if y_train.iloc[i] == 1:  # spam
        frecuencia_caracteristicas_spam += X_train_tfidf[i].toarray()[0]

# Calcular P(Características|Spam)
total_caracteristicas_spam = frecuencia_caracteristicas_spam.sum()
P_caracteristicas_spam = (frecuencia_caracteristicas_spam / total_caracteristicas_spam)

# Contar la frecuencia de palabras en correos no spam
frecuencia_caracteristicas_no_spam = np.zeros(X_train_tfidf.shape[1])
for i in range(len(y_train)):
    if y_train.iloc[i] == 0:  # no spam
        frecuencia_caracteristicas_no_spam += X_train_tfidf[i].toarray()[0]

# Calcular P(Características|NoSpam)
total_caracteristicas_no_spam = frecuencia_caracteristicas_no_spam.sum()
P_caracteristicas_no_spam = frecuencia_caracteristicas_no_spam / total_caracteristicas_no_spam

# Calcular P(NoSpam)
P_no_spam = (total_correos - numero_correos_spam) / total_correos

# Calcular P(Spam|Características)
P_spam_caracteristicas = (P_spam * P_caracteristicas_spam) / \
                         (P_spam * P_caracteristicas_spam + P_no_spam * P_caracteristicas_no_spam)

# Clasificación basada en la comparación de probabilidades
clasificaciones = (P_spam_caracteristicas > (1 - P_spam_caracteristicas)).astype(int)

# Evaluación
precision = precision_score(y_test, predicciones)
recuperacion = recall_score(y_test, predicciones)

print(f'Probabilidad previa de spam (P(Spam)): {P_spam}')
print()
print('Probabilidad de las características dado')
print(f'que es spam (P(Caracteristicas|Spam)): {P_caracteristicas_spam}')
print()
print('Probabilidad de las características dado que')
print(f'no es spam (P(Características|NoSpam)): {P_caracteristicas_no_spam}')
print()
print('Probabilidad posterior de que el correo electrónico')
print(f'sea spam (P(Spam|Características)): {P_spam_caracteristicas}')
print()
print(f'Clasificaciones: {clasificaciones}')
print()
print("-------EVALUACIÓN------- ")
print(f'Precisión: {precision}')
print()
print(f'Recuperación: {recuperacion}')

# Nuevos correos para clasificar
correos = [
    "Your account is locked. Please update your information.",
    "Hey, are we still on for the meeting tomorrow?",
    "Important update: Your subscription is about to expire.",
    "Congratulations! You've won a $1000 gift card. Click here to claim now!",
]

# Preprocesar los correos
correosPreprocesados = [preprocesar_texto(correo) for correo in correos]

# Convertir los correos a una representación numérica usando el mismo vectorizador y transformador
CorreosCounts = vectorizador.transform(correosPreprocesados)
CorreosTfidf = tfidf_transformer.transform(CorreosCounts)

# Hacer predicciones
prediccionesCorreos = modelo.predict(CorreosTfidf)

# Mostrar resultados
print()
for i, prediccion in enumerate(prediccionesCorreos):
    tipo = "Spam" if prediccion == 1 else "No Spam"
    print(f"Correo {i+1}: {tipo}")