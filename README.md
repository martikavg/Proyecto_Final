# 📊 Proyecto Final: Optimización de Campañas de Marketing Bancario mediante Data Analytics (Python & Power BI)

## 📌 Descripción del Proyecto
Este proyecto combina técnicas avanzadas de **Análisis Exploratorio de Datos (EDA)** en Python con el desarrollo de un **Dashboard Operativo** en Power BI. El objetivo principal es evaluar y optimizar las campañas de telemarketing para la captación de depósitos a plazo fijo en una institución bancaria, transformando datos brutos en decisiones estratégicas e insights de negocio.

## 📁 Estructura del Repositorio

```text
Proyecto_Final/
├── data/
│   ├── processed/              # Datasets limpios y transformados
│   └── raw/                    # Datos originales sin procesar
├── notebooks/
│   ├── 01_limpieza_y_transformacion.ipynb  # Limpieza y feature engineering
│   └── 02_analisis_exploratorio.ipynb     # EDA (univariado, bivariado, correlaciones)
├── power_bi/
│   ├── 1. monitoreo_estrategico.png       # Captura de Vista 1
│   ├── 2. segmentacion_perfil_cliente.png  # Captura de Vista 2
│   ├── 3. eficiencia_operativa.png        # Captura de Vista 3
│   ├── Dashboard_Bank_Marketing.pbix      # Archivo fuente de Power BI
│   ├── informe_analisis_bancario.pdf      # Informe ejecutivo formal en PDF
│   └── informe_analisis.md               # Informe analítico en Markdown
├── src/
│   └── utils.py                # Funciones auxiliares reutilizables
├── .gitignore
├── README.md                   # Documentación principal del proyecto
└── requirements.txt            # Dependencias del entorno de Python
```

## 🛠️ Requisitos y Pasos para Ejecutar el Proyecto

### Requisitos Previos
* Python 3.10 o superior.
* Entorno de ejecución de Jupyter
* Notebooks (VS Code con extensión de Jupyter o JupyterLab).

### Librerías Utilizadas
* **pandas:** Manipulación, integración de fuentes y limpieza de datos.
* **numpy:** Operaciones vectorizadas y cálculo numérico.
* **matplotlib:** Creación y personalización de la estructura de gráficos.
* **seaborn:** Visualizaciones estadísticas avanzadas (distribuciones, boxplots y heatmaps).
* **openpyxl:** Lectura e integración del archivo Excel multihoja (`customer-details.xlsx`).
* **jupyter / ipykernel:** Entorno para la ejecución de los notebooks interactivos.

### Pasos de Ejecución

#### **1. Clonar el repositorio público de GitHub**
Asegúrate de que tu repositorio sea público para la evaluación:
```bash
git clone <https://github.com/martikavg/Proyecto_Final.git>
cd <Proyecto_Final>
```
#### **2. Instalar dependencias**

```bash
pip install -r requirements.txt
```

### 3. Ejecución en Visual Studio Code
* Abre y ejecuta `notebooks/01_limpieza_y_transformacion.ipynb` para procesar las fuentes primarias y generar `bank_marketing_cleaned.csv`.
* Abre y ejecuta `notebooks/02_analisis_exploratorio.ipynb` para reproducir el análisis descriptivo y gráfico.
* Para limpiar la memoria de ejecuciones desordenadas anteriores y asegurar la linealidad, haz clic en el botón superior **Restart Kernel and Clear All Outputs**.
* Haz clic en **Run All** o ejecuta de manera secuencial (celda por celda de arriba hacia abajo) para reproducir el pipeline completo.

### 4. Abrir el Dashboard 
* Requiere tener instalado `Power BI Desktop` para abrir el archivo `power_bi/Dashboard_Bank_Marketing.pbix`

## 📝 Informe Explicativo del Proyecto y Principales Hallazgos

### 🔍 Resumen del Análisis Exploratorio de Datos (EDA)

### ⚙️ Módulo 1: Transformación, Limpieza e Integración de Datos (Python)

***Integración:*** 
Unificación mediante merge interno entre `bank-additional.csv` y las 3 pestañas de `customer-details.xlsx` utilizando el identificador único de cliente (ID).

***Tratamiento de Nulos (unknown):*** Conservación explícita de categorías desconocidas para evitar sesgos de selección e identificar patrones de abstención.

***Ingeniería de Características:***
* Extracción de variables temporales (`contact_month, contact_year`).
* Cálculo de la antigüedad del cliente (`Customer_tenure_year`) mediante el diferencial entre la fecha de contacto y la fecha de alta original.

***Variables Excluidas por Multicolinealidad ($|r| > 0.7$):***
* `emp.var.rate, nr.employed` y `cons.price.idx`: Excluidas debido a su alta correlación lineal con `euribor3m` ($0.77 \le r \le 0.91$), evitando problemas de multicolinealidad.
* `contact_year`: Eliminada por presentar dependencia matemática directa ($r = 0.81$) con la antigüedad del cliente (`Customer_tenure_year`).

***Variables Seleccionadas para el Modelo:***
* `poutcome`: Principal predictor de comportamiento histórico.
* `euribor3m`: Mantenida como la variable sintética representativa de todo el bloque macroeconómico.
* `job y age_group`: Variables clave para la segmentación demográfica.
* `Customer_tenure_year`: Refleja la antigüedad y lealtad del cliente.
* `loan` y `housing`: Utilizadas en combinación para medir la carga de endeudamiento y compromiso financiero.

### 📈 Módulo 2: Principales Hallazgos del EDA

***1.	Desbalance de Clientes:*** La tasa global de suscripción al depósito es del 11.3% (yes), frente al 88.7% de rechazo (no).

***2.	Historial Previo (poutcome):*** Es la variable con mayor poder de conversión. Clientes con un contacto previo exitoso (success) superan el 50% de tasa de conversión, frente al 8.8% en contactos nuevos.

***3.	Efecto de la Antigüedad (Customer_tenure_year):*** Existe una relación inversa. Los clientes de 0 a 1 año de antigüedad muestran las tasas de conversión más altas (19.3% - 20.6%), mientras que en clientes antiguos (6-7 años) la conversión cae al 4.4%.

***4.	Sensibilidad Macroeconómica:*** Alta correlación negativa con la tasa `euribor3m`. Entornos de menor tasa aumentan la receptividad hacia plazos fijos.

***5.	Regla de Parada Comercial:*** La conversión cae drásticamente después de la 3.ª llamada dentro de la misma campaña (`campaign` > 3).

### 📈 Dashboard en Power BI (power_bi/)

El modelo analítico se desplegó en Power BI (`Dashboard_Bank_Marketing.pbix`) organizado en tres paneles especializados:

***1. Monitoreo Estratégico y Macroeconómico***
Seguimiento de KPIs globales (conversión del 11.25% sobre 43.000 llamadas), métricas temporales e impacto del contexto financiero (Euribor 3M).

***2. Segmentación y Perfil del Cliente***
Análisis demográfico detallado por nivel de ocupación, antigüedad del cliente (Tenure), edad promedio y perfil de deuda.

***3. Eficiencia Operativa y Campaña***
Rendimiento del equipo comercial según el número de contactos realizados por cliente y la efectividad comparativa del canal de comunicación.

## 💡 Principales Hallazgos y Conclusiones de Negocio

El análisis integrado entre Python y Power BI permitió identificar los patrones clave de conversión de la campaña y definir directrices estratégicas para optimizar la operativa comercial:

* **Efecto Recurrencia (Historial Previo):** Los clientes con campañas previas exitosas presentan una tasa de conversión del **65.4%**, en comparación con solo el **8.8%** en prospectos sin contacto anterior. *Recomendación:* Priorizar la recontactación de clientes con histórico positivo para maximizar el ROI comercial.
* **Segmentación de Alto Valor:** Los perfiles con mayor propensión a contratar depósitos a plazo fijo son los **estudiantes (31.4%)** y **jubilados (25.3%)**, superando ampliamente el promedio general.
* **Regla de Parada Comercial:** La efectividad del contacto alcanza su punto máximo en las **primeras 3 llamadas (10.8% - 13.0%)** y decrece drásticamente a partir del 4.º intento. *Recomendación:* Establecer un límite máximo de 3 a 4 intentos por cliente para evitar el desgaste de la base de datos y optimizar las horas de los ejecutivos.
* **Dominio del Canal Celular:** Las gestiones realizadas a teléfonos celulares registran una conversión de **14.73%**, frente a un **5.15%** en teléfonos fijos. *Recomendación:* Priorizar la captura y validación de números móviles en la base de contactos del banco.

## 🖋️Autores

•	Martha Vergara

•	https://github.com/martikavg/Proyecto_Final.git



