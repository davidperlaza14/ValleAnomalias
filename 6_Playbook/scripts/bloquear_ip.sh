#!/bin/bash
# Usage: sudo ./bloquear_ip.sh 198.51.100.15
IP=$1
if [[ -z "$IP" ]]; then
    echo "Usage: $0 <IP>"
    exit 1
fi
# Bloquear con iptables (temporal hasta reboot)
iptables -A INPUT -s "$IP" -j DROP
# Banear en fail2ban (persistente)
fail2ban-client set sshd banip "$IP" 2>/dev/null || echo "fail2ban no disponible, solo iptables"
# Log local
LOG_FILE="/var/log/playbook_bloqueos.log"
sudo mkdir -p /var/log
echo "$(date '+%F %T'): $IP bloqueada por playbook" | sudo tee -a "$LOG_FILE"
echo "✅ IP $IP bloqueada"