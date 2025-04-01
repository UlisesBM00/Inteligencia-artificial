# 📧 Detección de Spam en Correos Electrónicos

Este proyecto utiliza **Python** y **Naive Bayes** para detectar correos electrónicos de spam.  
Se implementa procesamiento de texto, transformación TF-IDF y clasificación con `MultinomialNB`.

---

## 🚀 Tecnologías utilizadas
🔹 Python 3  
🔹 Pandas y NumPy  
🔹 Scikit-learn  
🔹 NLTKs

---

## 📂 Estructura del Proyecto
```
📁 Detector de Spam
│-- 📂 images
│   │-- Captura_de_pantalla_Resultados.png
│-- 📄 spam_assassin.csv        # Dataset con correos spam y no spam
│-- 📄 ClasificadorCorreos.py   # Código del detector
│-- 📄 README.md                # Documentación del proyecto
│-- 📄 requirements.txt         # Librerias necesarias
```

---

## ⚙️ Instalación y configuración

1️⃣ Clonar el repositorio
```bash
@@@@@@@@@Cambiar@@@@@@@@@@@ git clone https://github.com/tu_usuario/Spam_Detection.git
cd Spam_Detection
```

2️⃣ Instalar dependencias  
```bash
pip install -r requirements.txt
```

3️⃣ Descargar los datos de NLTK (si no los tienes)  
```python
import nltk
nltk.download('punkt')
nltk.download('stopwords')
```

---

## 🎯 Cómo funciona el modelo
El sistema usa **Naive Bayes**, un algoritmo de probabilidad que clasifica correos basándose en la frecuencia de palabras.

**🔹 Paso 1:** Preprocesamiento del texto  
- Convertir a minúsculas  
- Eliminar caracteres especiales y números  
- Tokenizar y eliminar palabras vacías  

**🔹 Paso 2:** Convertir texto a valores numéricos  
Se usa `CountVectorizer` para contar palabras y `TfidfTransformer` para ponderarlas.

**🔹 Paso 3:** Entrenamiento con `MultinomialNB`  
Se entrena el modelo con los datos preprocesados.

**🔹 Paso 4:** Clasificación de nuevos correos  
Se evalúan correos desconocidos para determinar si son **spam** o **no spam**.

---

## 📊 Ejemplo de uso

```python
correos = [
    "Congratulations! You've won a $1000 gift card. Click here to claim now!",
    "Hey, are we still on for the meeting tomorrow?"
]

# Preprocesar y predecir
correosPreprocesados = [preprocesar_texto(correo) for correo in correos]
CorreosCounts = vectorizador.transform(correosPreprocesados)
CorreosTfidf = tfidf_transformer.transform(CorreosCounts)
prediccionesCorreos = modelo.predict(CorreosTfidf)

# Resultado
for i, prediccion in enumerate(prediccionesCorreos):
    tipo = "Spam" if prediccion == 1 else "No Spam"
    print(f"Correo {i+1}: {tipo}")
```

**📝 Salida esperada:**
```
Correo 1: Spam
Correo 2: No Spam
```

---

## 📸 Ejemplo gráfico del resultado  

![Descripción de la imagen](images\Captura_de_pantalla_Resultados.png)

Explicación de Resultados del Modelo de Detección de Spam
________________________________________
1. Probabilidad previa de spam (P(Spam))

    •	Valor: 0.3173203227622443

    •	Significado: Antes de analizar el contenido de los correos, la probabilidad general de que un correo sea spam en el conjunto de datos es de aproximadamente 31.73%.

    •	Cálculo:

        P(Spam) = Número de correos spam / Total de correos
________________________________________
2. Probabilidad de las características dado que es spam (P(Características|Spam))

    •	Valor: Vector con valores muy pequeños (ejemplo: 9.61362137e-06, 1.00796315e-05, etc.).

    •	Significado: Este vector representa la probabilidad de aparición de cada palabra en un correo, considerando que el correo es spam. Valores cercanos a cero indican palabras que aparecen muy raramente, mientras que valores mayores indican mayor frecuencia en correos spam.
________________________________________
3. Probabilidad de las características dado que no es spam (P(Características|NoSpam))

    •	Valor: Vector con valores (ejemplo: 3.11725099e-05, 9.37624265e-05, etc.).

    •	Significado: Representa la probabilidad de aparición de cada palabra en correos que no son spam. Al comparar este vector con el de spam se pueden identificar las diferencias en la frecuencia de palabras entre correos spam y no spam.
________________________________________
4. Probabilidad posterior de que el correo sea spam (P(Spam|Características))

    •	Valor: Vector (ejemplo: 0.12537679, 0.04759052, 0.0, ...).

    •	Significado: Indica la probabilidad de que cada correo sea spam, luego de analizar las características del texto.

    •	Interpretación:

        o	Un valor cercano a 1 indica que el correo es muy probable que sea spam.
        o	Un valor cercano a 0 indica que el correo es poco probable que sea spam.
        o	Por ejemplo, un primer valor de 0.125 significa que hay un 12.5% de probabilidad de que ese correo sea spam.
________________________________________
5. Clasificación final del modelo

    •	Valor: Vector de clasificaciones (ejemplo: [0 0 0 ... 0 0 0]).

    •	Significado: Cada elemento representa la clasificación del modelo para cada correo, donde:

        o	0 = No Spam
        o	1 = Spam
________________________________________
6. Evaluación del modelo

    •	Precisión (Precision): 0.9936575052854123

        o	Significado: De todos los correos clasificados como spam, el 99.36% efectivamente son spam.

    •	Recuperación (Recall): 0.9270216962524654

        o	Significado: El 92.7% de todos los correos spam reales fueron correctamente identificados.

    Interpretación general:

        •	El modelo muestra una alta precisión, lo que significa que casi no hay falsos positivos.

        •	La recuperación es buena, aunque hay un pequeño porcentaje de correos spam que no se detectaron.
________________________________________
7. Clasificación de nuevos correos

    Se procesaron y clasificaron 4 nuevos correos de la siguiente manera:

        •	Correo 1: "Your account is locked. Please update your information." → Spam

        •	Correo 2: "Hey, are we still on for the meeting tomorrow?" → No Spam

        •	Correo 3: "Important update: Your subscription is about to expire." → No Spam

        •	Correo 4: "Congratulations! You've won a $1000 gift card. Click here to claim now!" → Spam
________________________________________
Resumen Final

    •	Dataset: 31.73% de los correos son spam.

    •	Proceso: Se calcula la probabilidad de cada palabra para correos spam y no spam, y se utiliza la regla de Bayes para obtener la probabilidad posterior.

    •	Evaluación: Alta precisión (99.36%) y buena recuperación (92.7%).

    •	Nuevos correos: El modelo clasifica correctamente los correos evaluados.
________________________________________


---

### 📌 Autor: **[Beltrán Magaña Ulises]**  
¡Gracias por revisar este proyecto! 😊
