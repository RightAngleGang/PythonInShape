# PythonInShape
CERI M1 IA PDDL - Projet de bibliothèque de calcul géométrique
**Auteurs : M1 IA Informatique**

- Angelo Adragna
- Arthur Buren
- Colin Palazzetti Rubera
- Théo Torres

# Sprint 1

**lien vers Github**
[README Sprint 1][(https://github.com/conception-logicielle-CERI/parseur-pdf/edit/sprint-4/README_sprint4.md](https://github.com/RightAngleGang/PythonInShape/blob/sprint1-scrum/README.md))

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
12. **Éditer les points** (suppression, translation, changement de base, etc.)  
13. **Éditer les formes** (suppression, translation, etc.)  

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
29. **Importer / Exporter** les points (par exemple via R ou un autre format compatible)  

---

# **Sprint Backlog — (04/11/25 et 10/11/25)**

1. Créer et afficher un **point** dans un espace 2D (coordonnées flottantes) avec retour de son nom  
2. Créer et afficher un **polygone quelconque** à partir de **N points choisis** dans un espace 2D  
3. Calculer et afficher la **distance euclidienne 2D** entre deux points  
4. Afficher la **liste des formes créées** (points + formes)  
5. Créer un **menu textuel** dans le terminal  

---

# **User Story**
En tant qu’utilisateur, je veux créer, visualiser et manipuler des points et des polygones dans un espace 2D à partir d’un menu textuel, afin d’explorer leurs relations géométriques.

### Cas d’usage :
- **Création de points** : saisie `x.0;y.0` → `p0(x.0;y.0)` créé
- **Création de polygones** :
  - saisie du nombre de points `n`
  - pour chaque point : saisir un nom (`p0`) ou des coordonnées (`x.0;y.0`)
- **Affichage de l’espace** :
  - chaque forme listée sur une ligne :  
    `f0: p0(x.0;y.0); p1(x.0;y.0)`
- **Calcul de distance euclidienne** :
  - saisie : `p0;p1`
  - sortie : `distance(p0,p1) = ...`
  
---

# **Definition of Done**
Un élément du sprint est considéré **terminé** lorsque tous les critères suivants sont remplis :

## Création
- Les points sont créés dans un espace 2D avec des coordonnées flottantes `x.0;y.0`.  
- Les polygones sont définis à partir d’un nombre quelconque de points.  
- Les points d’un polygone peuvent être :
  - des points déjà existants (référencés par nom), ou  
  - de nouveaux points définis par leurs coordonnées `(x.0;y.0)`.

## Consultation
- La liste complète des objets créés (points et polygones) est affichable à tout moment.

## Calculs
- La distance euclidienne entre deux points existants est calculée et affichée avec précision (valeur en flottants).

## Menu textuel
- Un menu textuel fonctionnel permet :
  - la création de points,  
  - la création de polygones,  
  - l’affichage de tous les objets,  
  - le calcul de distance entre deux points.  

## Qualité et validation
- Le code compile et s’exécute sans erreur.  
- Les fonctionnalités sont testées et validées.  
- Les entrées invalides sont gérées sans crash.  
- Les messages d’affichage sont clairs et cohérents.

---

# **Poker planning**
Pas encore mis en place

<!--
1pts = 10min
| Item sprint | Estimation |
|-------------|------------|
| Setup GitHub | 3 |
| Setup SonarQube | 8 |
| Setup Environnement dev | 5 |
| Écrire premiers tests | 3 |

-->

---

# **Daily Sprint 10/11/25**
L’équipe a pris du retard en raison d’un refactoring de l’architecture du code, nécessaire pour rendre la création et la gestion des entités (points/polygones) plus modulaires et réutilisables.
Cette réorganisation devrait faciliter la production et l’adaptation pour les prochains sprints.

---

# **Sprint Planning**
Le sprint a permis de poser les bases du projet PythonInShape : architecture du code, création et affichage des points, et développement du menu textuel.  

## **Détails du travail effectué**
Ce sprint s’est concentré sur la mise en place des fonctionnalités principales :  
- **Backend** : gestion des données et implémentation des classes de base.  
  Colin doit encore finaliser la logique applicative de certaines fonctions.
- **menu textuel** développé avec différentes options par Arthur. terminé.
- **Création et affichage de points 2D** (coordonnées flottantes) : terminé.  
- **Calcul de la distance euclidienne** : en cours, pris en charge par Théo.  
- **Création de polygones** : implémentation commencée, nécessite encore des ajustements par Théo.

L’avancement global est satisfaisant malgré un léger retard dû à des ajustements d’architecture nécessaires pour mieux structurer le code.


## **Analyse**
Le choix du **langage Python** s’est révélé pertinent :  
- bonne gestion des nombres flottants,  
- structures et classes faciles à manipuler,  
- syntaxe souple et moins contraignante pour ce type de prototype.

L’équipe a mieux réparti les tâches que lors du sprint précédent, ce qui a permis un meilleur avancement global.

## **Remarques**
- Quelques imprécisions subsistent dans l’architecture du code, ce qui a ralenti la progression.  
- Il faudra clarifier dès le prochain sprint la logique de création et de gestion des entités (points, polygones).  

## **À faire**
- Finaliser les fonctions manquantes du backend.  
- Terminer le calcul de distance euclidienne.  
- Améliorer la structure de l’architecture (organisation des classes et dépendances).  
- Préparer une courte documentation d’utilisation pour valider la DoD.

---

# **Rétrospective**

## **Ce qui a été mis en place**
- Aucun **poker planning** n’a été réalisé pour l’estimation des tâches.  
- L’équipe a choisi de se concentrer sur la production et les tests en séance cette fois-ci afin de rattraper son retard.

## **Ce qui a bien fonctionné**
- **Meilleure répartition des tâches** entre les membres.  
- **Moins de perte de temps** en réunion grâce à une communication plus directe.  
- Collaboration fluide et bonnes prises d’initiative pendant la séance.

## **Ce qui a posé problème**
- **Architecture initiale floue**, entraînant des réécritures et du retard.  
- **Trop d’objectifs** prévus dans un seul sprint de 3h en plus de la remodilisation de l'architecture interne menée par Colin et Arthur.
- Manque de clarté sur certaines responsabilités au sein du groupe.

## **Ce qu’on doit améliorer**
- Définir une **architecture des données plus claire et stable** avant le début du sprint.  
- **Préparer à l’avance les questions à poser au professeur** pour gagner du temps.  
- Continuer à améliorer la communication technique entre les membres.
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

- Creer pour chaque feature une branche **Sprint*X*-feat-*nom_de_vote_feature*** ou bien **Sprint*X*-scrum**.
- Penser à mettre à jour vos issues/tickets dans *Project*.
- Le code est commenté de manière claire pour chaque fonction principale.
-  Chaque fonctionnalité principale est testée manuellement pour vérifier son bon fonctionnement.
