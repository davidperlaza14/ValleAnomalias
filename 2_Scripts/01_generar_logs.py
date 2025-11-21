#!/usr/bin/env python3
"""
Crea 1 000 000 de logs JSON simulando tráfico de una entidad gubernamental.
~5 % serán ataques (anomalías) para que tengamos positivos conocidos.
"""
import json, random, uuid, time
from datetime import datetime, timedelta
from faker import Faker

fake = Faker()

# Redes "oficiales" del gobierno y algunos IPs de Internet
GOV_NETS   = ["192.168.100.", "10.50."]
INTERNET   = ["45.33.32.156", "187.141.100.10", "200.10.20.30", "198.51.100.15"]
SERVICES   = ["ssh", "http", "https", "rdp", "ftp"]
USER_AGENTS = [
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64)",
    "curl/7.68.0",
    "python-requests/2.28.1",   # sospechoso
    "Go-http-client/1.1",       # sospechoso
    "masscan/1.3.10"            # muy sospechoso
]

def gov_ip():
    """Devuelve IP del segmento gubernamental"""
    prefix = random.choice(GOV_NETS)
    return prefix + str(random.randint(2, 254))

def internet_ip():
    """Devuelve IP externa conocida (atacante)"""
    return random.choice(INTERNET)

def timestamp_aleatorio():
    """Últimas 24 h en formato ISO8601"""
    delta = timedelta(seconds=random.randint(0, 86400))
    return (datetime.utcnow() - delta).isoformat()

def log_normal():
    """Comportamiento legítimo"""
    return {
        "timestamp": timestamp_aleatorio(),
        "src_ip": gov_ip(),
        "dst_ip": gov_ip(),
        "service": random.choice(SERVICES),
        "status": "success",
        "sospechoso": "no",
        "user_agent": random.choice(USER_AGENTS[:2]),  # Navegadores normales
        "bytes": random.randint(500, 8000)
    }

def log_ataque():
    """Comportamiento malicioso"""
    lg = log_normal()
    lg["src_ip"] = internet_ip()            # Viene de fuera
    lg["status"] = "failed"                 # Falla credencial o explota
    lg["user_agent"] = random.choice(USER_AGENTS[2:])  # scanners
    lg["bytes"] = random.randint(20, 300)   # Respuesta pequeña
    # Fuerza bruta ssh
    lg["sospechoso"] = "si"
    if lg["service"] == "ssh":
        lg["user"] = "root"
        lg["dst_ip"] = "192.168.100.10"     # Servidor público
    return lg

def main():
    TOTAL = 150_000
    RUTA  = "./1_Data/gov.log"
    with open(RUTA, "w") as f:
        for i in range(1, TOTAL + 1):
            if random.random() < 0.15:      # 5 % ataques
                f.write(json.dumps(log_ataque()) + "\n")
            else:
                f.write(json.dumps(log_normal()) + "\n")
            if i % 100_000 == 0:
                print(f"[+] {i//1000}k líneas escritas")
    print(f"[+] Listo: {RUTA}")

if __name__ == "__main__":
    main()
