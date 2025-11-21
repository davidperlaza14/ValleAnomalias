#!/bin/bash
# Envia alertas y actualiza dashboard
cd ~/Proyectos/ValleAnomalia/3_Model
source ../venv/bin/activate
papermill 04_Enviar_Alertas_a_ELK.ipynb 04_out.ipynb
echo "Alertas actualizadas -> $(date)"
