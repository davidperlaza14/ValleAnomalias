h1. Incidente de seguridad detectado

* **Fecha:** {{timestamp}}
* **IP de origen:** {{src_ip}}
* **Servicio:** {{service}}
* **Gravedad:** Alta
* **Estado:** En análisis

h2. Descripción
El modelo Isolation Forest disparó una alerta por comportamiento anómalo.

h2. Acciones realizadas
# IP bloqueada con fail2ban
# Log recolectado y adjunto
# Notificación enviada a CISO

h2. Evidencia
Ver dashboard: [http://localhost:5601/app/dashboards|Dashboard Valle]

h2. Próximos pasos
# Verificar si la IP es de un proveedor legitimo
# Analizar posible compromiso