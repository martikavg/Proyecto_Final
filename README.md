# 📊 Proyecto Final: Optimización de Campañas Comercial mediante Data Analytics (Python & Power BI)

## 📌 Descripción del Proyecto
Este proyecto combina técnicas avanzadas de **Análisis Exploratorio de Datos (EDA)** en Python con el desarrollo de un **Dashboard Operativo** en Power BI. El objetivo principal es evaluar y optimizar las campañas de telemarketing para la captación de depósitos a plazo fijo en una institución bancaria, transformando datos brutos en decisiones estratégicas e insights de negocio.

---

## 📁 Estructura del Repositorio

```text
Proyecto-Final/
├── data/
│   ├── raw/                        # Datasets originales heterogéneos
│   └── processed/                  # Dataset final limpio y transformado
├── notebooks/
│   └── 01_eda_limpieza_analisis.ipynb  # Cuaderno Jupyter con el flujo de EDA
├── power_bi/
│   ├── dashboard_telemarketing.pbix   # Archivo interactivo de Power BI
│   └── preview.png                    # Captura del dashboard operativo
├── images/                         # Gráficos exportados (.png) para la documentación
├── reports/
│   └── informe_ejecutivo.md        # Informe explicativo ejecutivo del proyecto
├── README.md                       # Documentación principal
└── requirements.txt                # Librerías de Python requeridas
⚙️ Módulo 1: Transformación, Limpieza e Integración de Datos (Python)
•	Integración: Unificación mediante merge interno entre bank-additional.csv y las 3 pestañas de customer-details.xlsx utilizando el identificador único de cliente (ID).
•	Tratamiento de Nulos (unknown): Conservación explícita de categorías desconocidas para evitar sesgos de selección e identificar patrones de abstención.
•	Ingeniería de Características:
o	Extracción de variables temporales (contact_month, contact_year).
o	Cálculo de la antigüedad del cliente (Customer_tenure_year) mediante el diferencial entre la fecha de contacto y la fecha de alta original.
📈 Módulo 2: Principales Hallazgos del EDA
1.	Desbalance de Clientes: La tasa global de suscripción al depósito es del 11.3% (yes), frente al 88.7% de rechazo (no).
2.	Historial Previo (poutcome): Es la variable con mayor poder de conversión. Clientes con un contacto previo exitoso (success) superan el 50% de tasa de conversión, frente al 8.8% en contactos nuevos.
3.	Efecto de la Antigüedad (Customer_tenure_year): Existe una relación inversa. Los clientes de 0 a 1 año de antigüedad muestran las tasas de conversión más altas (19.3% - 20.6%), mientras que en clientes antiguos (6-7 años) la conversión cae al 4.4%.
4.	Sensibilidad Macroeconómica: Alta correlación negativa con la tasa euribor3m. Entornos de menor tasa aumentan la receptividad hacia plazos fijos.
5.	Regla de Parada Comercial: La conversión cae drásticamente después de la 3.ª llamada dentro de la misma campaña (campaign > 3).
📊 Módulo 3: Dashboard Operativo en Power BI
El tablero de control en Power BI está diseñado para monitorear la operación en tiempo real y guiar a la fuerza de ventas mediante 3 vistas principales:
•	Página 1: Resumen Ejecutivo: Visión macro de KPIs globales (Total Contactos, Clientes Convertidos, % Conversión) y el impacto del Euribor 3M.
•	Página 2: Eficiencia Comercial: Análisis del resultado previo (poutcome), control de la cantidad de llamadas (campaign) y rendimiento por duración de llamada.
•	Página 3: Segmentación y Liquidez: Comportamiento por antigüedad (Customer_tenure_year), carga crediticia (loan x housing) y perfiles familiares.
🛠️ Requisitos e Instalación
1.	Clonar el repositorio:
Bash
git clone [https://github.com/TU_USUARIO/Proyecto-Final.git](https://github.com/TU_USUARIO/Proyecto-Final.git)
cd Proyecto-Final
2.	Instalar el entorno de Python:
Bash
pip install -r requirements.txt
3.	Abrir y ejecutar el notebook en Jupyter o VS Code:
Bash
jupyter notebook notebooks/01_eda_limpieza_analisis.ipynb

4.	Para explorar el tablero interactivo, abrir power_bi/dashboard_telemarketing.pbix usando Power BI Desktop.




