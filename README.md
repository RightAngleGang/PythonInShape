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
