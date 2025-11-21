Asunto: [ALERTA] Intrusión detectada en servicio **{{service}}**

Estimado equipo de seguridad,

El modelo de ML ha detectado una anomalía:
- IP: {{src_ip}}
- Servicio: {{service}}
- Hora: {{timestamp}}
- Acción tomada: IP bloqueada vía fail2ban

Favor revisar el dashboard: http://localhost:5601/app/dashboards

Saludos,  
Analista de Seguridad Valle