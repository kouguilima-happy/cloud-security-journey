import socket
import sys
import json

# Vérification : l'utilisateur doit donner une cible
if len(sys.argv) < 2:
    print("Erreur : Donne une cible.")
    sys.exit()

target = sys.argv[1]
open_ports = [] # Liste vide pour stocker les ports ouverts trouvés

print(f"\nScanning {target}...\n")

# Boucle sur la plage de ports
for port in range(20, 101):

    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(0.5)

    result = sock.connect_ex((target, port))

    # Si le port répond, on l'ajoute à notre liste
    if result == 0:
        print(f"[OPEN] Port {port}")
        open_ports.append(port) # On enregistre le numéro du port

    sock.close()

# Création du dictionnaire simple pour le JSON
scan_report = {
    "target_host": target,
    "status": "completed",
    "detected_open_ports": open_ports
}

# Sauvegarde des résultats dans le fichier report.json
with open("report.json", "w") as f:
    json.dump(scan_report, f, indent=4)

print("\nScan completed. Results saved to report.json")
