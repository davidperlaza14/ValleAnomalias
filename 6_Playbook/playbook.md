# 🛡️ Playbook de Respuesta ante Anomalías – Valle 2025
**Versión:** 1.0  
**Autor:** David Stiven Peraza Valencia 
**Fecha:** 2025-11-20

## 1. Objetivo
Proporcionar instrucciones claras y automatizadas para actuar cuando el modelo `Isolation Forest` detecte una anomalía en los logs de la entidad gubernamental del Valle.

## 2. Ciclo de respuesta rápida (SLA 30 min)
| Fase | Tiempo máx | Acción |
|------|------------|--------|
| Detección | 0 min | Alerta en índice `alertas-anomalia-*` |
| Análisis | 5 min | Ejecutar `analizar_alerta.py` |
| Contención | 10 min | Ejecutar `bloquear_ip.sh` si aplica |
| Escalamiento | 15 min | Enviar plantilla `email_ciso.md` |
| Cierre | 30 min | Registrar en `log_playbook.csv` |

## 3. Escenarios y acciones
### 3.1 Fuerza bruta SSH (service:ssh AND user:root)
- **Gravedad:** Alta  
- **Acción:** Bloquear IP y generar ticket.

### 3.2 Escaneo masivo (>50 puertos)
- **Gravedad:** Media  
- **Acción:** Bloquear IP y notificar ISP.

### 3.3 HTTP con user-agent sospechoso (masscan, nmap)
- **Gravedad:** Baja  
- **Acción:** Solo registrar.

## 4. Scripts rápidos
### 4.1 bloquear_ip.sh
```bash
sudo ./bloquear_ip.sh 198.51.100.15