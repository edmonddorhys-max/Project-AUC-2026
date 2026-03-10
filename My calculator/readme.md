alculatrice Python - Architecture MVC
Une calculatrice de bureau moderne développée en Python, utilisant la bibliothèque CustomTkinter pour offrir une interface utilisateur élégante et soignée. Ce projet est structuré selon le patron de conception Modèle-Vue-Contrôleur (MVC), garantissant un code propre, modulaire et facilement évolutif.

1 Fonctionnalités
Opérations arithmétiques : Prise en charge des calculs de base (addition, soustraction, multiplication, division).

Historique des opérations : Sauvegarde et affichage des calculs précédents pour faciliter le suivi.

Interface UI/UX Moderne : Design fluide et réactif grâce aux composants de CustomTkinter.

Code Modulaire : Architecture stricte permettant de modifier l'interface sans toucher à la logique mathématique, et vice versa.

2 Architecture (MVC)
Le code est divisé en trois parties distinctes :

Modèle (Model) : Le cerveau de l'application. Il contient la logique mathématique, effectue les calculs de manière sécurisée et gère le stockage des données (comme l'historique des entrées).

Vue (View) : L'interface visuelle construite avec CustomTkinter. Elle gère l'affichage de l'écran, le placement des boutons et la capture des clics de l'utilisateur. Elle ne contient aucune logique de calcul.

Contrôleur (Controller) : Le chef d'orchestre. Il écoute les actions de l'utilisateur transmises par la Vue, interroge le Modèle pour traiter les données, puis ordonne à la Vue de se mettre à jour avec les nouveaux résultats.

3 Prérequis et Installation
Assurez-vous d'avoir Python 3.x installé sur votre machine.

Clonez ce dépôt sur votre machine locale :

Bash
git clone https://github.com/edmonddorhys-max/Project-AUC-2026.git
cd nom-du-repo
Installez la dépendance requise pour l'interface graphique :

Bash
pip install customtkinter
 Comment lancer l'application
Pour démarrer la calculatrice, exécutez le fichier principal depuis votre terminal :

Bash
python main.py
(Remarque : remplacez main.py par le nom de votre fichier d'entrée si celui-ci est différent).

4 Structure du Projet
Plaintext
calculatrice/
│
├── model.py        # Logique des calculs et gestion de l'historique
├── view.py         # Interface utilisateur (CustomTkinter)
├── controller.py   # Gestion des événements et liaison Model-View
└── main.py         # Point d'entrée pour initialiser l'application