# 📊 Informe Ejecutivo de Análisis Comercial - Campañas de Marketing Bancario

**Proyecto:** Dashboard de Marketing Bancario  
**Archivo Power BI:** `Dashboard_Bank_Marketing.pbix`  
**Herramientas:** Power BI, Python (Pandas/Matplotlib)  

---

## 📄 Resumen Ejecutivo

El presente informe consolida los hallazgos del análisis de campaña de telemarketing sobre una base de **43.000 contactos**, alcanzando **5.000 clientes convertidos** y una tasa de conversión global del **11,25%**. 

El objetivo es identificar los drivers clave de conversión y optimizar la eficiencia operativa reduciendo costos por contacto.

---

## 📈 Indicadores Clave de Rendimiento (KPIs Globales)

| Métrica | Valor General |
| :--- | :--- |
| **Total Contactos** | 43,000 gestiones |
| **Clientes Convertidos (`y = yes`)** | 5,000 clientes |
| **Tasa de Conversión Global** | 11,25% |
| **Promedio Euribor 3M** | 3,88% |
| **Edad Promedio** | 40 años |
| **Porcentaje Clientes Nuevos** | 96,3% |
| **Duración Promedio por Llamada** | 4,30 minutos |
| **Llamadas Promedio por Cliente** | 3 llamadas |

---

## 🔍 Hallazgos Principales por Módulo

### 1. Monitoreo Estratégico y Contexto Macroeconómico
* **Resultado Previo (`poutcome`):** Es la variable predictiva más fuerte. Los clientes con conversión previa exitosa (`success`) alcanzan un **65,4%** de efectividad, frente al **14,2%** con fallos previos y un **8,8%** en prospectos sin historial.
* **Estacionalidad:** La tasa de conversión alcanza su punto más alto en **Octubre (~12,0%)** y su valle en **Septiembre (~10,2%)**, influenciada por la evolución de la tasa Euribor 3M.

![Monitoreo Estratégico](1.%20monitoreo_estrategico.png)

### 2. Segmentación y Perfil del Cliente
* **Ocupación (`job`):** **Estudiantes (31,4%)** y **Jubilados (25,3%)** muestran el mayor apetito por depósitos. Sectores operativos (*blue-collar* 6,9%, *services* 8,1%) presentan los rendimientos más bajos.
* **Antigüedad (`Customer_tenure_year`):** Los clientes nuevos (0 a 1 año) convierten al **20,6%**, mientras que la conversión cae paulatinamente hasta el **4,4%** en clientes con 7 años de antigüedad.
* **Perfil de Deuda:** Contar con préstamos o hipotecas no afecta sustancialmente la conversión (**10,76% – 11,74%**).

![Segmentación y Perfil de Cliente](2.%20segmentacion_perfil_cliente.png)

### 3. Eficiencia Operativa y Campaña
* **Regla de Parada Comercial:** La tasa de conversión alcanza su máximo en la 1.ª llamada (**13,0%**) y decae de forma progresiva (2.ª: 11,5%, 3.ª: 10,8%). A partir de la **4.ª llamada (9,2%)**, el retorno no justifica el costo operativo.
* **Canal de Contacto:** El canal móvil (*cellular*) es casi 3 veces más efectivo (**14,73%**) que el fijo (*telephone*, **5,15%**).

![Eficiencia Operativa](3.%20eficiencia_operativa.png)
---

## 💡 Recomendaciones Estratégicas para el Negocio

1. **Implementar "Regla de Parada":** Limitar los intentos telefónicos a un máximo de **3 llamadas por cliente** por campaña.
2. **Priorización de Base (Lead Scoring):** Focalizar las gestiones prioritarias en clientes con historial `success` y clientes con 0-1 año de antigüedad.
3. **Optimización de Canales:** Concentrar la pauta telefónica exclusivamente en líneas móviles (*cellular*).