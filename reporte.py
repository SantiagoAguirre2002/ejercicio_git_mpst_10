import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Cargar datos
file_path = "data.csv"  # Asegúrate de que el archivo esté en la misma carpeta
data = pd.read_csv(file_path)

# ------------------ EDA ------------------ #

# 1. Histograma de las notas
plt.figure(figsize=(8,5))
sns.histplot(data['Exam_Score'], bins=20, kde=True, color='blue')
plt.title('Distribución de las Notas')
plt.xlabel('Nota')
plt.ylabel('Frecuencia')
plt.show()

# 2. Relación entre horas de estudio y nota final
plt.figure(figsize=(8,5))
sns.scatterplot(x=data['Hours_Studied'], y=data['Exam_Score'], alpha=0.6)
plt.title('Relación entre Horas de Estudio y Nota')
plt.xlabel('Horas de Estudio')
plt.ylabel('Nota en el Examen')
plt.show()

# 3. Impacto de la asistencia en la nota
plt.figure(figsize=(8,5))
sns.scatterplot(x=data['Attendance'], y=data['Exam_Score'], alpha=0.6, color='green')
plt.title('Relación entre Asistencia y Nota')
plt.xlabel('Porcentaje de Asistencia')
plt.ylabel('Nota en el Examen')
plt.show()

# 4. Matriz de correlación de variables numéricas (CORRECCIÓN)
plt.figure(figsize=(10,6))
numeric_cols = data.select_dtypes(include=['number'])  # Solo columnas numéricas
sns.heatmap(numeric_cols.corr(), annot=True, cmap='coolwarm', linewidths=0.5)
plt.title('Matriz de Correlación de Variables Numéricas')
plt.show()

# 5. Comparación de notas por género
plt.figure(figsize=(8,5))
sns.boxplot(x=data['Gender'], y=data['Exam_Score'], palette='Set2')
plt.title('Comparación de Notas por Género')
plt.xlabel('Género')
plt.ylabel('Nota en el Examen')
plt.show()

# 6. Efecto del nivel educativo de los padres en las notas
plt.figure(figsize=(10,5))
sns.boxplot(x=data['Parental_Education_Level'], y=data['Exam_Score'], palette='muted')
plt.xticks(rotation=45)
plt.title('Impacto del Nivel Educativo de los Padres en el Examen')
plt.xlabel('Nivel Educativo de los Padres')
plt.ylabel('Nota en el Examen')
plt.show()

# 7. Comparación de notas entre estudiantes con y sin actividades extracurriculares
plt.figure(figsize=(8,5))
sns.boxplot(x=data['Extracurricular_Activities'], y=data['Exam_Score'], palette='Set3')
plt.title('Impacto de Actividades Extracurriculares en las Notas')
plt.xlabel('Participación en Actividades Extracurriculares')
plt.ylabel('Nota en el Examen')
plt.show()

# Guardar reporte en un archivo
with open("reporte_insights.txt", "w") as f:
    f.write("Análisis Exploratorio del Dataset\n")
    f.write("==================================\n\n")
    f.write(f"Media de las notas: {data['Exam_Score'].mean():.2f}\n")
    f.write(f"Mediana de las notas: {data['Exam_Score'].median():.2f}\n")
    f.write(f"Desviación estándar de las notas: {data['Exam_Score'].std():.2f}\n")
    f.write("\nCorrelaciones entre variables numéricas:\n")
    f.write(str(numeric_cols.corr()))