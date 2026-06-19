Cloud Security Journey
Ce dépôt rassemble mes projets pratiques en cybersécurité et sécurité Cloud. L'objectif est de comprendre les bases du système et du réseau avant de déployer des infrastructures sécurisées.

Phase 1 : Sécurité Système (Linux)
Projet : Script d'audit de sécurité local (dans le dossier linux-audit-script/)

Description : Un script Python qui vérifie les configurations critiques d'une machine Linux (droits du fichier /etc/shadow, intégrité des fichiers, etc.).

Résultat : Calcule un score de sécurité global et génère un rapport au format JSON.

Phase 2 : Sécurité Réseau
Projet : Scanner de ports TCP dynamique (dans le dossier labs/port-scanner/)

Description : Un outil en Python utilisant le module socket pour tester la disponibilité des ports (de 20 à 100) sur une cible donnée en argument.

Résultat : Identifie les ports ouverts (comme le SSH 22 ou le HTTP 80) et exporte les résultats dans un fichier report.json.

Phase 3 : Sécurité Cloud (AWS)
En cours de préparation : Étude théorique du Modèle de Responsabilité Partagée, des VPC, des Security Groups et des NACLs.

Avis et Améliorations (Code Review)
Ce projet est un laboratoire d'apprentissage. Si vous êtes un professionnel ou un passionné, n'hésitez pas à ouvrir une Issue pour me signaler ce qui peut être amélioré dans la structure du code ou la logique de sécurité. Les critiques constructives sont les bienvenues.# Cloud Security Journey
