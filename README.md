# PythonInShape
CERI M1 IA PDDL - Projet de bibliothèque de calcul géométrique
**Auteurs : M1 IA Informatique**

- Angelo Adragna
- Arthur Buren
- Colin Palazzetti Rubera
- Théo Torres

# Sprint 3

**lien vers Github**
[README Sprint 2][(https://github.com/conception-logicielle-CERI/parseur-pdf/edit/sprint-4/README_sprint4.md](https://github.com/RightAngleGang/PythonInShape/blob/sprint1-scrum/README.md))

## **Rôles**

- Angelo Adragna est `SCRUM Master`.
- Arthur Buren, Colin Palazzetti Rubera et Théo Torres sont `développeurs`.

---

# **Product Backlog**

## Espace 2D
1. Créer et afficher un **point** dans un espace 2D (coordonnées flottantes) avec retour de son nom  
2. Créer et afficher un **polygone quelconque** à partir de **N points choisis** dans un espace 2D  
3. Calculer et afficher la **distance euclidienne 2D** entre deux points  
4. Afficher la **liste des formes créées** (points + formes)  
5. Créer un **menu textuel** dans le terminal  
6. Créer et afficher un **carré en 2D**  
7. Créer et afficher un **triangle en 2D**  
8. Créer et afficher un **rectangle en 2D**  
9. Créer et afficher un **cercle en 2D**  
10. Créer et afficher un **segment en 2D**  
11. Gérer le **nommage automatique des points** lors de la création de formes  
12. **Éditer les points** (suppression, translation)  
13. **Éditer les formes** (suppression points, translation points)  

##  Espace 3D
14. Créer et afficher un **point** dans un espace 3D (coordonnées flottantes) avec retour de son nom  
15. Créer et afficher un **polygone quelconque** à partir de **N points choisis** dans un espace 3D  
16. Calculer et afficher la **distance euclidienne 3D** entre deux points  
17. Créer et afficher un **carré en 3D**  
18. Créer et afficher un **triangle en 3D**  
19. Créer et afficher un **rectangle en 3D**  
20. Créer et afficher un **cercle en 3D**  
21. Créer et afficher un **segment en 3D**  
22. Créer et afficher un **cône**  
23. Créer et afficher une **pyramide**  
24. Créer et afficher un **pavé**  
25. Créer et afficher un **cube**  
26. Créer et afficher une **sphère**  

## Fonctions avancées
27. Gérer l’**affichage web** ou **l’export vers Three.js**  
28. Déterminer l’**appartenance d’une forme à un espace** et les **intersections** entre formes  
29. **Importer** les points (Via Json)  
30. **Exporter** les points (Via Json)  

---

# **Poker planning**
Première utilisation d'un poker planning, on part du principe que nous avons 2h de travail effectif pour les développeurs.
Car nous déduisons 20 minutes de réunion qui centralise avec le Client/PO le spring planning, spring retrospective.
Le poker planning de 10 minutes.
Le spring review de 20 minutes.
La rétrospective de 10 minutes.

En définissant qu'un points vaut 10 minutes. Cela fait normalement 12 points par personne cependant nous préférons prendre une marge de 20% au cas de sous estimation.
Nous sommes ainsi à un total de 40 points.

| Item sprint backlog | Estimation | membre |
|-------------|------------|------------|
| Créer et afficher un carré en 2D | 3 | Théo |
| Créer et afficher un triangle en 2D | 1 | Théo |
| Créer et afficher un cercle en 2D | 2 | Théo |
| Créer et afficher un rectangle en 2D | 1 | Théo |
| Créer et afficher un segment en 2D | 1 | Théo |
| nommage automatique des points lors de la création de formes | 3 | Colin |
| Éditer les points | 2 | Colin |
| Éditer les points de formes | 3 | Colin |
| Ajouter des tests sur le code déjà existant | 2 | Colin |
| Importer les points en Json | 4 | Arthur |
| Exporter les points en Json | 4 | Arthur |
| Documentation du code produit | 1 | chaque développeur |
| Ecriture des tests du code produit | 1 | chaque développeur |
| Mise en forme du poker planning | 3 | Angelo |
| Mise en forme du Sprint Backlog | 1 | Angelo |
| Mise en forme de l'User Story et DOD | 2 | Angelo |


---

# **Sprint Backlog — (01/12/2025)**

6. Créer et afficher un **carré en 2D**  
7. Créer et afficher un **triangle en 2D**  
8. Créer et afficher un **rectangle en 2D**  
9. Créer et afficher un **cercle en 2D**  
10. Créer et afficher un **segment en 2D**  
11. Gérer le **nommage automatique des points** lors de la création de formes  
12. **Éditer les points** (suppression, translation)  
13. **Éditer les formes** (suppression point, translation point)
29. **Importer** les points (Via Json)  
30. **Exporter** les points (Via Json)  

---

# **User Story** et **Definition of Done**
## 6. Créer et afficher un carré en 2D

**User Story**  
En tant qu’utilisateur, je veux pouvoir créer et afficher un carré en 2D afin de visualiser une forme géométrique parfaite à partir d’un point de départ.

**Definition of Done**
- L’utilisateur peut sélectionner l’outil **Carré**.
- Un clic définit le premier point (coin ou centre selon l’option choisie).
- Le carré est dessiné avec 4 côtés égaux.
- Les 4 points sont affichés.
- Le carré est visible à l’écran.
- Les coordonnées sont correctement stockées.

---

## 7. Créer et afficher un triangle en 2D

**User Story**  
En tant qu’utilisateur, je veux pouvoir créer et afficher un triangle en 2D afin de représenter une forme à trois côtés.

**Definition of Done**
- L’utilisateur sélectionne l’outil **Triangle**.
- Trois clics définissent les 3 points.
- Les segments sont reliés automatiquement.
- La forme est correctement affichée.
- Les coordonnées sont stockées.

---

## 8. Créer et afficher un rectangle en 2D

**User Story**  
En tant qu’utilisateur, je veux pouvoir créer et afficher un rectangle en 2D afin de représenter une forme à quatre côtés avec deux longueurs et deux largeurs.

**Definition of Done**
- L’utilisateur sélectionne l’outil **Rectangle**.
- Deux clics définissent les coins opposés.
- Le rectangle est généré automatiquement.
- Les 4 points sont visibles.
- Les côtés opposés sont parallèles et égaux.

---

## 9. Créer et afficher un cercle en 2D

**User Story**  
En tant qu’utilisateur, je veux pouvoir créer et afficher un cercle en 2D afin de représenter une forme définie par un centre et un rayon.

**Definition of Done**
- L’utilisateur sélectionne l’outil **Cercle**.
- Le premier clic définit le centre.
- Le second clic définit le rayon.
- Le cercle est tracé à l’écran de manière fluide.
- Le rayon et le centre sont enregistrés.

---

## 10. Créer et afficher un segment en 2D

**User Story**  
En tant qu’utilisateur, je veux pouvoir tracer un segment afin de relier deux points sur le plan.

**Definition of Done**
- Deux clics définissent les extrémités.
- Un segment droit apparaît entre ces points.
- Les deux points sont affichés.

---

## 11. Nommage automatique des points

**User Story**  
En tant qu’utilisateur, je veux que les points soient nommés automatiquement afin de ne pas avoir à les nommer manuellement.

**Definition of Done**
- Chaque point reçoit automatiquement un nom (A, B, C... puis A1, B1...).
- Le nom est affiché près du point.
- Aucun doublon n’est possible.

---

## 12. Éditer les points (suppression, translation)

**User Story**  
En tant qu’utilisateur, je veux pouvoir supprimer ou déplacer un point afin de corriger et modifier mes figures.

**Definition of Done**
- Le point est sélectionnable.
- L’utilisateur peut supprimer le point.
- Le point peut être déplacé (drag & drop ou saisie de coordonnées).
- La vue est mise à jour en temps réel.

---

## 13. Éditer les formes (suppression de point, translation)

**User Story**  
En tant qu’utilisateur, je veux pouvoir modifier une forme en déplaçant ou supprimant ses points afin d’adapter sa géométrie.

**Definition of Done**
- Une forme peut être sélectionnée.
- Déplacer un point met à jour toute la forme.
- Supprimer un point supprime ou modifie la forme.
- L’affichage est mis à jour automatiquement.

---

## 29. Importer les points via JSON

**User Story**  
En tant qu’utilisateur, je veux pouvoir importer des points depuis un fichier JSON afin de récupérer une scène existante.

**Definition of Done**
- Un bouton ou menu **Importer** est disponible.
- Le programme accepte un fichier `.json`.
- Les points sont correctement chargés.
- Les points sont affichés à l’écran.
- Aucun crash avec un fichier valide.

---

# **Sprint Review**
Le sprint a permis de poser les bases du projet PythonInShape : architecture du code, création et affichage des points, et développement du menu textuel.  

## **Détails du travail effectué**
Ce sprint s’est concentré sur la mise en place des fonctionnalités principales :  
- Backend : gestion des données et implémentation des classes de base.  
  Colin doit encore finaliser la logique applicative de certaines fonctions.
- menu textuel développé avec différentes options par Arthur. terminé.
- Création et affichage de points 2D (coordonnées flottantes) , arthur et théo : terminé.  
- Calcul de la distance euclidienne : en cours, pris en charge par Théo.  
- Création de polygones : implémentation commencée, nécessite encore des ajustements par Arthur.
- Architecture : Shape Manager pour gerer les formmes
- Architecture : Point Manager pour gerer les points
- Architecture : Tests pret mais pas implémentés

L’avancement global est satisfaisant, le retard dû à des ajustements d’architecture nécessaires pour mieux structurer le code à été rattrapé.


## **Analyse**
Le choix du **langage Python** s’est révélé pertinent :  
- bonne gestion des nombres flottants,  
- structures et classes faciles à manipuler,  
- syntaxe souple et temoins contraignante pour ce type de prototype.
- scalabilité architecture

L’équipe a mieux réparti les tâches que lors du sprint précédent, ce qui a permis un meilleur avancement global.

## **Remarques**
- Quelques imprécisions subsistaient dans l’architecture du code.
- Il faudra clarifier dès le prochain sprint la logique de création et de gestion des entités (points, polygones) avec le PO/client  

## **À faire**
- Impleter tests
- Rajouter quelques commentaires
- Préparer une courte documentation d’utilisation pour valider la DoD.
- Préparer des queqtions pour le PO/client.

---

# **Rétrospective**

## **Ce qui a été mis en place**
- Aucun **poker planning** n’a été réalisé pour l’estimation des tâches.
- L’équipe a choisi de se concentrer sur la production et les tests en séance cette fois-ci afin de rattraper son retard.

## **Ce qui a bien fonctionné**
- Meilleure répartition des tâches entre les membres.  
- Moins de perte de temps en réunion grâce à une communication plus directe.  
- Collaboration fluide et bonnes prises d’initiative pendant la séance.

## **Ce qui a posé problème**
- Les artefacts n'ont pas collé aux attende du PO
- Architecture initiale floue, entraînant des réécritures et du retard.  
- Trop d’objectifs prévus dans un seul sprint de 3h en plus de la remodilisation de l'architecture interne menée par Colin et Arthur.
- Manque de clarté sur certaines responsabilités au sein du groupe.

## **Ce qu’on doit améliorer**
- Préparer à l’avance les questions à poser au professeur pour gagner du temps.  
- Meilleur gestions à prevoir pour la gestions des items dans "project" pour ameliorer la transparence du travail de chacun. 

---

# **interne**

## taches :

- Initialisation organisation GitHub commune  
- Mise en place de SonarQube qualité + règles + intégration  
- Création et configuration de l’environnement de développement  
- Écriture des premiers tests unitaires
- Refacor coté back avec Managers

## _Consignes pour le compte rendu des développeurs_ :

- Penser à mettre à jour vos issues/tickets dans *Project*.
- Le code est commenté de manière claire pour chaque fonction principale.
- Chaque fonctionnalité principale est testée (manuellement au moins) pour vérifier son bon fonctionnement.
