#!/usr/bin/env python3
"""
Crea ticket markdown listo para pegar en Jira/Outlook
Uso: python3 generar_ticket.py 198.51.100.15 ssh
"""
import sys, datetime, os

# Crear carpeta tickets si no existe
os.makedirs("tickets", exist_ok=True)

src_ip  = sys.argv[1]
service = sys.argv[2]
now     = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
out_file= f"tickets/ticket_{src_ip}.md"

plantilla = f"""# Ticket de Incidente – Detección Isolation Forest

**Fecha:** {now}  
**IP origen:** `{src_ip}`  
**Servicio afectado:** `{service}`  
**Gravedad:** Alta (según playbook)  

## Acciones tomadas
- [x] IP bloqueada vía `fail2ban`
- [x] Notificación enviada a CISO
- [ ] Revisión de logs completos

## Recomendación
Verificar si la IP pertenece a un proveedor legítimo o a un atacante persistente.

---
**Analista responsable:** @tu_usuario  
**ID de caso:** `{src_ip}_{datetime.datetime.now().strftime("%s")}`
"""

with open(out_file, "w") as f:
    f.write(plantilla)

print(f"✅ Ticket creado: {out_file}")