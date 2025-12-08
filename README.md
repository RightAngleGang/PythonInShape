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
31. **Éditer les points en 3D** (suppression, translation) 
32. **Éditer les points des formes en 3D** (suppression points, translation points) 

## Fonctions avancées
27. Gérer l’**affichage web** ou **l’export vers Three.js**  x
28. Déterminer l’**appartenance d’une forme à un espace** et les **intersections** entre formes  x
29. **Importer** les points et formes (Via Json)  
30. **Exporter** les points et formes (Via Json)
33. **Importer** les points et formes 3D (Via Json)
34. **Exporter** les points et formes 3D (Via Json)


## Calcul
35. Calculer l'aire
36. Calculer le volume
37. Scale de formes

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
| Créer et afficher un **cône** | 3 | Théo |
| Calcul air | 3 | Théo |
| Calcul volume | 4 | Théo |
| Éditer les points en 3D | 1 | Colin |
| Éditer les points des formes en 3D | 2 | Colin |
| fix le segment | 1 | Colin |
| refactor terminal | 2 | Colin |
| refactor backend (separation des fonctions) | 4 | Colin |
| Import des points 3D | 4 | Arthur |
| Export des points 3D | 4 | Arthur |
| tests | 2 | Arthur |
| Mise en forme du poker planning | 2 | Angelo |
| Mise en forme du Sprint Backlog | 1 | Angelo |
| Mise en forme de l'User Story et DOD | 3 | Angelo |
| Mise en forme du Sprint Review | 1 | Angelo |
| Mise en forme de la rétrospective | 1 | Angelo |


---

# **Sprint Backlog — (01/12/2025)**
22. Créer et afficher un **cône**  
31. **Éditer les points en 3D** (suppression, translation) 
32. **Éditer les points des formes en 3D** (suppression points, translation points) 
33. **Importer** les points et formes 3D (Via Json)
34. **Exporter** les points et formes 3D (Via Json)
35. Calculer l'aire
36. Calculer le volume
37. Scale de formes

---
# **User Story** et **Definition of Done – Sprint (3D)**

## 22. Créer et afficher un cône

**User Story**  
En tant qu’utilisateur, je veux pouvoir créer et afficher un cône en 3D à partir d’un centre de base, d’un rayon et d’une hauteur afin de représenter un solide géométrique.

**Definition of Done**
- L’utilisateur sélectionne "Cône" dans le sous-menu "Ajouter une forme".
- Un point définit le centre de la base.
- Un rayon et une hauteur définissent le cône.
- 2 angles définissent l'orientation
- La forme est affichée de façon textuelle.
- Les coordonnées sont stockées.

## 31. Éditer les points en 3D (suppression, translation)

**User Story**  
En tant qu’utilisateur, je veux pouvoir modifier ou supprimer un point en 3D afin de corriger ou ajuster sa position dans l’espace.

**Definition of Done**
- L’utilisateur sélectionne **Gestion des Points → Éditer un point**.
- Une liste des points existants est affichée.
- L’utilisateur peut :
  - **Supprimer un point**
  - **Translater un point** via un vecteur (dx, dy, dz)
- Le point mis à jour est affiché.
- Les modifications sont **enregistrées**.


## 32. Éditer les points des formes en 3D (suppression, translation)

**User Story**  
En tant qu’utilisateur, je veux pouvoir modifier ou supprimer les points composant une forme 3D afin de faire évoluer sa géométrie.

**Definition of Done**
- L’utilisateur sélectionne **Gestion des Formes 3D → Éditer une forme**.
- Une liste des formes existantes est affichée.
- L’utilisateur sélectionne une forme.
- L’utilisateur peut :
  - supprimer un ou plusieurs points de la forme
  - translater un ou plusieurs points de la forme (dx, dy, dz)
- La nouvelle forme est affichée.
- Les modifications sont **enregistrées**.


## 33. Importer les points et formes 3D (JSON)

**User Story**  
En tant qu’utilisateur, je veux pouvoir importer des points et des formes 3D à partir d’un fichier JSON afin de récupérer rapidement des données existantes.

**Definition of Done**
- L’utilisateur sélectionne **Gestion des données → Importer (JSON)**.
- Le programme lit un fichier JSON valide contenant :
  - des points
  - des formes 2D/3D
- Les données sont chargées dans le système.
- Un message de confirmation est affiché.
- En cas d’erreur, un message explicite est affiché.


## 34. Exporter les points et formes 3D (JSON)

**User Story**  
En tant qu’utilisateur, je veux pouvoir exporter mes points et formes 3D dans un fichier JSON afin de sauvegarder et réutiliser mes données.

**Definition of Done**
- L’utilisateur sélectionne **Gestion des données → Exporter (JSON)**.
- Tous les points et formes sont convertis au format JSON.
- Un fichier est généré et sauvegardé.
- Un message de confirmation est affiché.


## 35. Calculer l’aire d’une forme

**User Story**  
En tant qu’utilisateur, je veux pouvoir calculer l’aire d’une forme afin d’obtenir une information géométrique utile.

**Definition of Done**
- L’utilisateur sélectionne une forme existante.
- Le système détermine le type de forme (2D ou face d’une 3D).
- L’aire est calculée automatiquement.
- Le résultat est affiché.
- Si la forme n’a pas d’aire calculable → message d’erreur.


## 36. Calculer le volume d’une forme 3D

**User Story**  
En tant qu’utilisateur, je veux pouvoir calculer le volume d’une forme 3D afin d’analyser ses propriétés spatiales.

**Definition of Done**
- L’utilisateur sélectionne une forme 3D existante.
- Le volume est calculé en fonction du type de forme :
  - Cube / Pavé : L × l × h
  - Cône : (1/3) × π × r² × h
  - Pyramide : (1/3) × aireBase × h
  - Sphère : (4/3) × π × r³
- Le résultat est affiché.
- En cas d’erreur → message explicite.


## 37. Scale (mise à l’échelle) d’une forme

**User Story**  
En tant qu’utilisateur, je veux pouvoir appliquer un facteur d’échelle à une forme afin d’en modifier les dimensions proportionnellement.

**Definition of Done**
- L’utilisateur sélectionne une forme existante.
- Il saisit un **coefficient de scale** (ex : 0.5, 2, 3…).
- Les dimensions de la forme sont automatiquement recalculées.
- La nouvelle forme est affichée.
- Les nouvelles coordonnées sont mises à jour et **enregistrées**.


---

# **Sprint Review**

En réalité le passage de 2D à 3D s'est avéré être de la réutilisation et adaptation qu'un départ à 0 pour Théo. Ce qui conduit à beaucoup de duplication.
Un peu plus de refonte pour colin.
Sauf pour Arthur qui a un ressenti totalement différent pour le cercle.
Le cercle nécéssitait de repartir de 0, en effet on demande maintenant un rayon, un point et un vecteur, ce qui a néciessité une refonte.
Arthur à eu un soucis de merge, il a du recreer 2 branches depuis dev. 
Les objectifs du sprint ont été atteints et les fonctionnalités prévues ont été implémentées.
Par contre nous nous sommes rendu compte que nous avions oublié lors du poker planning la tache (15.) Créer et afficher un **polygone quelconque** à partir de **N points choisis** dans un espace 3D.
Arthur à souhaité prendre cette tâche à 2 points cependant mais il n'a pas réussi à tout finir car il a eu un soucis de merge.
Pour soulager Arthur, Théo à accepté de récuperer la création du Conne mais n'a pas pu le finir dans le temps imparti.

Penser à vraiment se concerter avant l'ajout de forme pour ne pas créer de conflits ou chercher longtemps quel developeur faire quelle forme.
Peut-être en maintenant en place une numérotation des formes en place.
---

# **Rétrospective**

## **Ce qui a été mis en place**
- Le poker planning.

## **Ce qui a bien fonctionné**
- Planning et rétrospective avec le client/PO plus libre et apaisée.
- Bonne entraide au niveau des tickets entre Arthur et Théo.

## **Ce qui a posé problème**
- Répartition satisfaisante des tâches entre les membres grâce au poker planning.
- Oublie de "Créer et afficher un **polygone quelconque** à partir de **N points choisis** dans un espace 3D" à cause d'un manque de vigilance.
- Sprint stressant, la fin du projet commence à se faire sentir.
- 
## **Ce qu’on doit améliorer**
- Continuer de préparer à l’avance les questions à poser au client/PO pour gagner du temps.
- Etre plus concentré sur le poker planning car nous avons failli dépasser les 20 minutes maximales.

---

# **interne**

## taches :

- Initialisation organisation GitHub commune  
- Mise en place de SonarQube qualité + règles + intégration  
- Création et configuration de l’environnement de développement  
- Écriture des premiers tests unitaires
- Refacor coté back avec Managers
- Mettre à jour l'affichage dans le terminal.
  
- Diminuer la dépendance entre les fonctions (fichiers trop gros)
- refactor le terminal
- Corriger SonarQube

## _Consignes pour le compte rendu des développeurs_ :

- Penser à mettre à jour vos issues/tickets dans *Project*.
- Le code est commenté de manière claire pour chaque fonction principale.
- Chaque fonctionnalité principale est testée (manuellement au moins) pour vérifier son bon fonctionnement.
