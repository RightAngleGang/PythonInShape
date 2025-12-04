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
31. **Éditer les points en 3D** (suppression, translation)  x
32. **Éditer les points des formes en 3D** (suppression points, translation points)  x

## Fonctions avancées
27. Gérer l’**affichage web** ou **l’export vers Three.js**  x
28. Déterminer l’**appartenance d’une forme à un espace** et les **intersections** entre formes  x
29. **Importer** les points et formes (Via Json)  
30. **Exporter** les points et formes (Via Json)

## Calcul
33. Calculer l'aire x
33. Calculer le volume x

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
| Créer et afficher un **point** dans un espace 3D (coordonnées flottantes) avec retour de son nom | 1 | Colin |
| Calculer et afficher la **distance euclidienne 3D** entre deux points | 1 | Colin |
| Créer et afficher un **segment en 3D** | 1 | Colin |
| Créer et afficher un **triangle en 3D** | 1 | Colin |
| Créer et afficher une **sphère** | 4 | Colin |
| Test et merge | 2 | Colin |
| Créer et afficher un **carré en 3D** | 2 | Arthur |
| Créer et afficher un **rectangle en 3D** | 2 | Arthur |
| Créer et afficher un **cône** | 2 | Arthur |
| Créer et afficher un **cercle en 3D** | 3 | Arthur |
| Test et merge | 1 | Arthur |
| Créer et afficher un **polygone quelconque** à partir de **N points choisis** dans un espace 3D | 2 | Arthur |
| Créer et afficher un **cube** | 4 | Théo |
| Créer et afficher une **pyramide** | 3 | Théo |
| Créer et afficher un **pavé** | 3 | Théo |
| Mise en forme du poker planning | 2 | Angelo |
| Mise en forme du Sprint Backlog | 1 | Angelo |
| Mise en forme de l'User Story et DOD | 3 | Angelo |
| Mise en forme du Sprint Review | 1 | Angelo |
| Mise en forme de la rétrospective | 1 | Angelo |


---

# **Sprint Backlog — (01/12/2025)**

14. Créer et afficher un **point** dans un espace 3D (coordonnées flottantes) avec retour de son nom  
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

---
# **User Story** et **Definition of Done – Sprint (3D)**

## 14. Créer et afficher un point en 3D

**User Story**  
En tant qu’utilisateur, je veux pouvoir créer et afficher un point dans un espace 3D à partir de coordonnées flottantes afin de définir une position dans l’espace.

**Definition of Done**
- L’utilisateur peut sélectionner l’option "Ajouter un point 3D" depuis le menu.
- Le point est défini par trois coordonnées flottantes (x, y, z).
- Le point est ajouté à l’espace.
- Un nom est automatiquement attribué au point.
- Le point et son nom sont affichés de façon textuelle.
- Les coordonnées sont stockées.

## 15. Créer et afficher un polygone quelconque (3D)

**User Story**  
En tant qu’utilisateur, je veux pouvoir créer et afficher un polygone quelconque en 3D à partir d’un ensemble de N points afin de représenter une forme libre orientée dans l’espace.

**Definition of Done**
- L’utilisateur sélectionne **Gestion des Formes 3D → Ajouter une forme 3D → Polygone (N)**.
- Le polygone est défini par :
  - un nombre de points **N (N ≥ 3)**
  - une liste de points dans l’espace 3D : `(x₁, y₁, z₁), (x₂, y₂, z₂), …, (xₙ, yₙ, zₙ)`
- Les segments reliant les points sont générés automatiquement dans l’ordre donné.
- Le dernier point est relié au premier pour **fermer le polygone**.
- Si **N < 3**, un message d’erreur s’affiche.
- La forme est affichée de façon **textuelle** (liste des sommets et des arêtes).
- Les coordonnées des points sont **stockées**.


## 16. Calculer la distance euclidienne entre deux points en 3D

**User Story**  
En tant qu’utilisateur, je veux pouvoir calculer et afficher la distance euclidienne en 3D entre deux points afin de mesurer un écart dans l’espace.

**Definition of Done**
- L’utilisateur sélectionne deux points existants dans l’espace.
- La distance euclidienne 3D est calculée selon la formule mathématique appropriée.
- La distance est affichée de façon textuelle.
- Les deux points restent inchangés dans l’espace.


## 17. Créer et afficher un carré en 3D

**User Story**  
En tant qu’utilisateur, je veux pouvoir créer et afficher un carré dans un espace 3D à partir d’un point, d’une taille et d’une orientation afin de représenter une surface plane carrée.

**Definition of Done**
- L’utilisateur peut sélectionner "Carré 3D" dans le sous-menu "Ajouter une forme".
- Un point, une longueur de côté et une orientation définissent le carré.
- Le carré est généré dans un plan de l’espace 3D.
- La forme est affichée de façon textuelle.
- Les coordonnées des points sont stockées.


## 18. Créer et afficher un triangle en 3D

**User Story**  
En tant qu’utilisateur, je veux pouvoir créer et afficher un triangle en 3D à partir de trois points afin de créer une surface élémentaire.

**Definition of Done**
- L’utilisateur sélectionne "Triangle 3D" dans le sous-menu "Ajouter une forme".
- Trois points définissent le triangle.
- La forme est affichée de façon textuelle.
- Les coordonnées sont stockées.


## 19. Créer et afficher un rectangle en 3D

**User Story**  
En tant qu’utilisateur, je veux pouvoir créer et afficher un rectangle en 3D à partir d’un point, d’une longueur, d’une largeur et d’une orientation afin de représenter une surface rectangulaire.

**Definition of Done**
- L’utilisateur peut sélectionner "Rectangle 3D".
- Un point, une longueur, une largeur et une orientation définissent le rectangle.
- La forme est affichée de façon textuelle.
- Les coordonnées sont stockées.


## 20. Créer et afficher un cercle en 3D

**User Story**  
En tant qu’utilisateur, je veux pouvoir créer et afficher un cercle en 3D à partir d’un centre et d’un rayon afin de représenter une forme circulaire dans l’espace.

**Definition of Done**
- L’utilisateur sélectionne "Cercle 3D".
- Un point et un rayon définissent le cercle.
- Le cercle est situé dans un plan 3D définissable.
- La forme est affichée de façon textuelle.
- Les coordonnées sont stockées.


## 21. Créer et afficher un segment en 3D

**User Story**  
En tant qu’utilisateur, je veux pouvoir créer et afficher un segment en 3D afin de relier deux points dans l’espace.

**Definition of Done**
- L’utilisateur sélectionne "Segment 3D".
- Deux points définissent le segment.
- Le segment est affiché de façon textuelle.
- Les coordonnées sont stockées.


## 22. Créer et afficher un cône

**User Story**  
En tant qu’utilisateur, je veux pouvoir créer et afficher un cône en 3D à partir d’un centre de base, d’un rayon et d’une hauteur afin de représenter un solide géométrique.

**Definition of Done**
- L’utilisateur sélectionne "Cône" dans le sous-menu "Ajouter une forme".
- Un point définit le centre de la base.
- Un rayon et une hauteur définissent le cône.
- La forme est affichée de façon textuelle.
- Les coordonnées sont stockées.


## 23. Créer et afficher une pyramide (base carrée) en 3D

**User Story**  
En tant qu’utilisateur, je veux pouvoir créer et afficher une pyramide à base carrée en 3D à partir d’un point, de la taille d’un côté, d’une hauteur et de deux angles afin de représenter un solide orienté dans l’espace.

**Definition of Done**
- L’utilisateur sélectionne **Gestion des Formes 3D → Ajouter une forme 3D → Pyramide (3)**.
- La pyramide est définie par :
  - un point de base (x, y, z)
  - une taille de côté (base carrée)
  - une hauteur
  - deux angles d’orientation
- La base carrée et le sommet sont calculés automatiquement.
- La forme est affichée de façon textuelle.
- Les coordonnées sont stockées.



## 24. Créer et afficher un pavé droit (3D)

**User Story**  
En tant qu’utilisateur, je veux pouvoir créer et afficher un pavé droit en 3D à partir d’un point, de ses dimensions et de deux angles afin de représenter un solide rectangulaire orienté dans l’espace.

**Definition of Done**
- L’utilisateur sélectionne **Gestion des Formes 3D → Ajouter une forme 3D → Pavé droit (2)**.
- Le pavé est défini par :
  - un point d’origine (x, y, z)
  - une longueur
  - une largeur
  - une hauteur
  - deux angles d’orientation (rotation dans l’espace)
- Les sommets sont calculés automatiquement à partir de ces données.
- La forme est affichée de façon textuelle.
- Les coordonnées sont stockées.


## 25. Créer et afficher un cube en 3D

**User Story**  
En tant qu’utilisateur, je veux pouvoir créer et afficher un cube en 3D à partir d’un point, d’une longueur d’arête et de deux angles afin de représenter un solide régulier orienté dans l’espace.

**Definition of Done**
- L’utilisateur sélectionne **Gestion des Formes 3D → Ajouter une forme 3D → Cube (1)**.
- Le cube est défini par :
  - un point d’origine (x, y, z)
  - une longueur d’arête
  - deux angles d’orientation
- Les sommets sont générés automatiquement.
- La forme est affichée de façon textuelle.
- Les coordonnées sont stockées.



## 26. Créer et afficher une sphère en 3D

**User Story**  
En tant qu’utilisateur, je veux pouvoir créer et afficher une sphère en 3D à partir d’un point et d’un rayon afin de représenter un solide parfaitement symétrique dans l’espace.

**Definition of Done**
- L’utilisateur sélectionne **Gestion des Formes 3D → Ajouter une forme 3D → Sphère**.
- La sphère est définie par :
  - un point centre (x, y, z)
  - un rayon
- La forme est affichée de façon textuelle.
- Les coordonnées sont stockées.

---

# **Sprint Review**
## Objectif
## Résultat du sprint

Les objectifs du sprint ont été atteints.  
Les fonctionnalités prévues ont été implémentées et l’architecture du projet est maintenant plus stable et plus maintenable, en préparation du passage à la 3D et aux fonctionnalités avancées.

## Points d’amélioration

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
