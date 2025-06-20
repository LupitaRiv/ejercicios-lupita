from datetime import datetime

# Define la fecha objetivo
fecha_objetivo = datetime(2025, 5,  3)  # Cambia esto por tu fecha objetivo

# Obtén la fecha actual
hoy = datetime.now()

# Calcula la diferencia de días
dias_restantes = (fecha_objetivo - hoy).days

# Pintar los días restantes
if dias_restantes > 0:
    print(f"Faltan {dias_restantes} días para llegar a {fecha_objetivo.strftime('%d/%m/%Y')}.")
elif dias_restantes == 0:
    print("¡Hoy es el día objetivo!")
else:
    print(f"El día objetivo ({fecha_objetivo.strftime('%d/%m/%Y')}) ya pasó hace {-dias_restantes} días.")
