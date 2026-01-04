# PythonInShape
CERI M1 IA PDDL - Projet de bibliothèque de calcul géométrique
**Auteurs : M1 IA Informatique**

- Angelo Adragna
- Arthur Buren
- Colin Palazzetti Rubera
- Théo Torres

# Sprint 2

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
29. **Importer** les points et formes (Via Json)  
30. **Exporter** les points et formes (Via Json)  

---

# **Poker planning**
Première utilisation d'un poker planning, on part du principe que nous avons 2h de travail effectif pour les développeurs.
Car nous déduisons 20 minutes de réunion qui centralise avec le Client/PO le spring planning, spring retrospective.
Le poker planning de 10 minutes.
Le spring review de 20 minutes.
La rétrospective de 10 minutes.

En définissant qu'un points vaut environs 10 minutes. Cela fait normalement 12 points par personne cependant nous préférons prendre une marge de 20% au cas de sous estimation.
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
| Importer les points et formes en Json | 4 | Arthur |
| Exporter les points et formes en Json | 4 | Arthur |
| Documentation du code produit | 1 | chaque développeur |
| Ecriture des tests du code produit | 1 | chaque développeur |
| Mise en forme du poker planning | 2 | Angelo |
| Mise en forme du Sprint Backlog | 1 | Angelo |
| Mise en forme de l'User Story et DOD | 3 | Angelo |
| Mise en forme du Sprint Review | 1 | Angelo |
| Mise en forme de la rétrospective | 1 | Angelo |


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
## 1. Créer et afficher un carré en 2D

**User Story**  
En tant qu’utilisateur, je veux pouvoir créer et afficher un carré en 2D à partir d’un point de départ (pas encore existant) et une taille de segment et un angle.

**Definition of Done**
- L’utilisateur peut sélectionner le type de forme dans le sous menu "Ajouter une forme" depuis l'option "Actions de Formes" dans le menu. 
- Un point, la taille d'un côté et un angle définissent un carré.
- 0° correspondant à l’axe des abscisses dans un repère orthonormé.
- La forme est affichées de façon textuelle.
- Les coordonnées sont stockées.

## 2. Créer et afficher un triangle en 2D

**User Story**  
En tant qu’utilisateur, je veux pouvoir créer et afficher un triangle en 2D à partir de 3 points (pas encore existant).

**Definition of Done**
- L’utilisateur peut sélectionner le type de forme dans le sous menu "Ajouter une forme" depuis l'option "Actions de Formes" dans le menu. 
- Trois points définissent le triangle.
- La forme est affichées de façon textuelle.
- Les coordonnées sont stockées.


## 3. Créer et afficher un rectangle en 2D

**User Story**  
En tant qu’utilisateur, je veux pouvoir créer et afficher un rectangle en 2D à partir d'un point, une longueur, une largeur et un angle.

**Definition of Done**
- L’utilisateur peut sélectionner le type de forme dans le sous menu "Ajouter une forme" depuis l'option "Actions de Formes" dans le menu. 
- Un point, la longueur, la largeur et un angle définissent un rectangle.
- 0° correspondant à l’axe des abscisses dans un repère orthonormé.
- La forme est affichées de façon textuelle.
- Les coordonnées sont stockées.

## 4. Créer et afficher un cercle en 2D

**User Story**  
En tant qu’utilisateur, je veux pouvoir créer et afficher un cercle en 2D afin de représenter une forme définie par un centre et un rayon.

**Definition of Done**
- L’utilisateur peut sélectionner le type de forme dans le sous menu "Ajouter une forme" depuis l'option "Actions de Formes" dans le menu. 
- Un point et un rayon définissent un cercle.
- La forme est affichées de façon textuelle.
- Les coordonnées sont stockées.


## 5. Créer et afficher un segment en 2D

**User Story**  
En tant qu’utilisateur, je veux pouvoir tracer un segment.

**Definition of Done**
- L’utilisateur peut sélectionner le type de forme dans le sous menu "Ajouter une forme" depuis l'option "Actions de Formes" dans le menu. 
- Deux points définissent un segment.
- La forme est affichées de façon textuelle.
- Les coordonnées sont stockées.


## 6. Nommage automatique des points

**User Story**  
En tant qu’utilisateur, je veux que lors de la création d'une forme, les points qui la compose soient nommés automatiquement.

**Definition of Done**
- Chaque point reçoit automatiquement un nom.
- Il est ajouté à l'espace.
- Le nom est affiché près du point.
- Aucun doublon n’est possible.

## 7. Éditer les points (suppression, translation)

**User Story**  
En tant qu’utilisateur, je veux pouvoir supprimer ou déplacer un point.

**Definition of Done**
- Le point est sélectionnable.
- L’utilisateur peut supprimer le point.
- Le point peut être déplacé (modification coordonnées).
- Le point est affichés de façon textuelle.

## 9. Éditer les formes (suppression de point, translation)

**User Story**  
En tant qu’utilisateur, je veux pouvoir modifier une forme en déplaçant ou supprimant ses points afin d’adapter sa géométrie.

**Definition of Done**
- Une forme peut être sélectionnée.
- Déplacer un point met à jour toute la forme.
- Supprimer un point supprime ou modifie la forme.
- Le point est affichés de façon textuelle.

## 10. Importer les points et formes via JSON

**User Story**  
En tant qu’utilisateur, je veux pouvoir importer des points depuis un fichier JSON afin de récupérer une scène existante.

**Definition of Done**
- Une option dans le menu "gestion des données" ouvre un sous menu avec l'option pour importer.
- Le programme accepte un fichier `.json`.
- Les points sont correctement chargés.
- Les points et formes sont affichés de façon textuelle.

## 11. Exporter les points et formes via JSON

**User Story**
En tant qu’utilisateur, je veux pouvoir exporter mes points vers un fichier JSON afin de les sauvegarder ou les partager.

**Definition of Done**
- Une option dans le menu "gestion des données" ouvre un sous menu avec l'option pour exporter.
- Un fichier .json est généré.
- Tous les points actuels sont enregistrés.
- L’utilisateur peut choisir l’emplacement de sauvegarde à condition que le dossier existe.
- Les points et formes sont affichés de façon textuelle.

---

# **Sprint Review**
## Objectif

Mettre en place les fonctionnalités principales en 2D :
- Création de formes de base
- Gestion avancée des points
- Import / export en JSON
- Amélioration de l’architecture du projet

## Fonctionnalités livrées

### Formes 2D
- Carré  
- Triangle  
- Rectangle  
- Cercle  
- Segment  

La création est possible via le menu « Actions de formes ».  
Les formes sont affichées de manière textuelle et les points sont générés et stockés automatiquement.


### Gestion des points
- Nommage automatique sans doublon  
- Suppression d’un point  
- Déplacement (translation)  
- Renommage  
- Mise à jour des formes liées  


### Import / Export JSON
- Export des points et formes dans un fichier `.json`  
- Import d’une scène à partir d’un fichier `.json`  
- Fonctionnalités intégrées dans le menu « Gestion des données »


## Amélioration de la structure du projet

- Refonte des classes `Shape`, `Polygon`, `Circle` et `Space`
- Mise en place de `PointManager` et `ShapeManager`
- Correction du `Makefile`
- Amélioration de la lisibilité (print et méthodes `__str__`)
- Organisation générale du projet améliorée


## Tests et qualité

- Ajout d’un fichier `pytest.ini`
- Premiers tests unitaires réalisés
- Tests fonctionnels effectués manuellement
- Début d’intégration d’outils de qualité (SonarQube)


## Résultat du sprint

Les objectifs du sprint ont été atteints.  
Les fonctionnalités prévues ont été implémentées et l’architecture du projet est maintenant plus stable et plus maintenable, en préparation du passage à la 3D et aux fonctionnalités avancées.

## Points d’amélioration

- Augmenter la couverture des tests
- Renforcer la gestion des erreurs
- Compléter la documentation

---

# **Rétrospective**

## **Ce qui a été mis en place**
- Le poker planning.
- L’équipe a choisi de se concentrer sur les applications 2D, dont la gestion complète ou presque des points et formes de bases.

## **Ce qui a bien fonctionné**
- Planning et rétrospective avec le client/PO plus fluide avec des questions déjà préparer et une idée du sprint baclog à venir.  

## **Ce qui a posé problème**
- Les users stories et les dod devaient s'entremeler. 
- Léger retard sur les tests.
- Bonne répartition des tâches entre les membres grâce au poker planning sauf pour Colin qui a eu un légé retard à cause d'un soucis personnel.  

## **Ce qu’on doit améliorer**
- Continuer de préparer à l’avance les questions à poser au client/PO pour gagner du temps.  
- Gestion d'erreurs.

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
