# Architecture Technique - TrustScore AI

Ce document détaille la vision technique et l'infrastructure cible pour le déploiement de la solution TrustScore AI à grande échelle.

## 1. Flux de Données (Data Flow)
Le système repose sur une architecture de micro-services centrée sur l'IA multimodale :
1. **Collecte :** Capture d'écran via une application mobile (Flutter).
2. **Traitement Image :** Envoi sécurisé vers un bucket Cloud Storage.
3. **Analyse IA :** Appel à l'API Gemini 1.5 Flash pour l'extraction OCR et le raisonnement financier.
4. **Persistance :** Stockage du score et de l'historique anonymisé dans Firebase Firestore.
5. **Restitution :** Affichage du tableau de bord financier et du plan d'épargne sur l'interface utilisateur.

## 2. Stack Technique Cible
* **Frontend :** Flutter (pour une compatibilité Android/iOS rapide).
* **Backend :** Google Cloud Functions (Node.js ou Python) pour gérer les appels API.
* **IA :** Google AI SDK / Vertex AI (Gemini 1.5 Flash).
* **Base de données :** Firebase Firestore (NoSQL) pour la flexibilité des données transactionnelles.
* **Authentification :** Firebase Auth (connexion via numéro de téléphone, crucial pour les zones rurales).

## 3. Sécurité et Confidentialité
* **Anonymisation :** Les données sensibles (noms, numéros de téléphone complets) sont masquées avant l'analyse par le modèle d'IA.
* **Chiffrement :** Utilisation du protocole HTTPS pour tous les transferts de données et chiffrement au repos via Google Cloud.

## 4. Évolutivité (Scalability)
L'utilisation de **Gemini 1.5 Flash** permet une latence extrêmement faible, supportant des milliers de requêtes simultanées, ce qui est idéal pour une adoption massive dans les marchés émergents.