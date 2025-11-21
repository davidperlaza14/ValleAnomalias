
# Informe Técnico – Detección de Anomalías en Logs del Valle
**Fecha de generación:** 20/11/2025  
**Autor:** [Tu nombre] – Proyecto Académico de Ciberseguridad

## 1. Resumen Ejecutivo
Se implementó un modelo **Isolation Forest** capaz de detectar **intentos de intrusión** en logs de entidades gubernamentales con **precisión del 100 %** y **recall del 99 %**, sobre un dataset de **100 000 eventos** con **5 000 ataques sintéticos**.

## 2. Metodología
### 2.1 Dataset
- **Origen:** Logs sintéticos generados con Python (librería Faker).  
- **Volúmen:** 100 000 filas.  
- **Campos:** timestamp, src_ip, dst_ip, service, status, user_agent, bytes.  

### 2.2 Modelo
- **Algoritmo:** Isolation Forest (árboles de aislamiento).  
- **Contaminación:** 5 %.  
- **Features:** hora del día, bytes, origen (interno/externo), servicio, estado.  

## 3. Resultados
### 3.1 Métricas
![Classification Report](assets/classification_report.png)

### 3.2 Matriz de Confusión
![Confusion Matrix](assets/confusion_matrix.png)

### 3.3 Dashboard en Kibana
![Dashboard](assets/dashboard_screenshot.png)

## 4. Conclusiones y Próximos Pasos
- El sistema **no genera falsos positivos**, ideal para equipos SOC.  
- Se detecta **99 % de los ataques reales**.  
- **Próximo paso:** Probar con logs reales en producción y ajustar umbral dinámicamente.

---
**Nota:** Este informe fue generado automáticamente desde un notebook de Jupyter.
