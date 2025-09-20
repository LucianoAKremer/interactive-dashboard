# 📊 Dashboard Interactivo de Insurance - Luciano Kremer

Este proyecto es un **dashboard interactivo** construido con **Streamlit** para visualizar y analizar datos del sector de **seguros de salud**.  

El dataset utilizado contiene información sobre costos médicos y características de los asegurados, lo que permite explorar cómo variables como **edad, sexo, índice de masa corporal (BMI), número de hijos, hábito de fumar y región** influyen en los **charges** (costos del seguro).

---

## 🚀 Características
- Visualización de costos médicos según:
  - **Grupo de edad** (jóvenes, adultos, adultos mayores).
  - **Género**.
  - **Índice de masa corporal (BMI)**.
  - **Número de hijos**.
  - **Condición de fumador o no fumador**.
  - **Región geográfica**.
- Filtrado dinámico por columnas y valores.
- Gráficos interactivos (barras, histogramas, boxplots).
- Métricas resumidas en tarjetas para una visión rápida.
- Estructura modular y escalable.

---

## 🗂️ Estructura de Archivos
- `app.py` → Entrada principal del dashboard.
- `dashboards/` → Contiene la lógica de cada página de análisis.
- `components/` → Componentes reutilizables (filtros, gráficos, métricas).
- `data/` → Dataset en formato CSV (`insurance.csv`).
- `tests/` → Pruebas unitarias para garantizar calidad del código.
- `requirements.txt` → Dependencias del proyecto.

---

## 🛠️ Tecnologías
- **Python 3.10+**
- **Streamlit** → Visualización interactiva.
- **Pandas** → Manipulación de datos.
- **Plotly / Seaborn / Matplotlib** → Gráficos y análisis visual.
- **pytest** → Testing.

---

## ⚡ Cómo correr el proyecto

1. Clonar el repositorio:
   ```bash
   git clone [https://github.com/tuusuario/dashboard-insurance.git](https://github.com/LucianoAKremer/interactive-dashboard.git)
   cd interactive-dashboard
2. Crear y activar un entorno virtual:
  python -m venv venv
  source venv/bin/activate   # Linux/Mac
  venv\Scripts\activate      # Windows
3. Instalar dependencias:
  pip install -r requirements.txt
4. Ejecutar la aplicacion:
  streamlit run app.py
5. Abrir el navegador en (si es que no se abrio solo):
   http://localhost:8501

---

#📊 Dataset

El dataset Insurance contiene las siguientes columnas:

-`age`: Edad del beneficiario principal.

-`sex`: Género del asegurado (male, female).

-`bmi`: Índice de masa corporal.

-`children`: Número de hijos a cargo.

-`smoker`: Si la persona es fumadora o no.

-`region`: Región de residencia (northeast, southeast, southwest, northwest).

-`charges`: Costos médicos facturados al seguro.


<img width="1902" height="704" alt="image" src="https://github.com/user-attachments/assets/71e44349-ca91-4409-8a25-ce62d2379c6a" />
<img width="1896" height="741" alt="image" src="https://github.com/user-attachments/assets/40397bd7-d903-40fc-9733-a45777c4a3fa" />
<img width="1614" height="499" alt="image" src="https://github.com/user-attachments/assets/e17d0f65-20ba-458c-9dc4-fad939ccde08" />
<img width="1572" height="550" alt="image" src="https://github.com/user-attachments/assets/8b967aa3-114f-41b6-a835-c0e86c592075" />
<img width="1896" height="955" alt="image" src="https://github.com/user-attachments/assets/46afadb6-01db-460f-9aaf-883547f3f7a5" />
