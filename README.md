# PythonInShape
CERI M1 IA PDDL - Projet de bibliothèque de calcul géométrique
**Auteurs : M1 IA Informatique**

- Angelo Adragna
- Arthur Buren
- Colin Palazzetti Rubera
- Théo Torres

# Sprint 5

**lien vers Github**
[README Sprint 5][(https://github.com/RightAngleGang/PythonInShape/tree/sprint5-scrum)](https://github.com/RightAngleGang/PythonInShape/tree/sprint5-scrum)

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
27. Gérer l’**affichage web** ou **l’export vers Three.js** 
28. Déterminer l’**appartenance d’une forme à un espace** et les **intersections** entre formes  x
29. **Importer** les points et formes (Via Json)  
30. **Exporter** les points et formes (Via Json)
33. **Importer** les points et formes 3D (Via Json)
34. **Exporter** les points et formes 3D (Via Json)
35. Réattribution automatique d'une catégorie de forme selon ses proprités géométrique après modification 


## Calcul
35. Calculer l'aire
36. Calculer le volume
37. Scale de formes
38. Deplacement de formes

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
| Scale de formes | 7 | Théo |
| Deplacement de formes | 5 | Théo |
| Réattribution automatique d'une catégorie de forme selon ses proprités géométrique après modification | 10 | Colin |
| Gérer l’**affichage web** ou **l’export vers Three.js** | 10 | Arthur |
| Mise en forme du poker planning | 2 | Angelo |
| Mise en forme du Sprint Backlog | 1 | Angelo |
| Mise en forme de l'User Story et DOD | 3 | Angelo |
| Mise en forme du Sprint Review | 1 | Angelo |
| Mise en forme de la rétrospective | 1 | Angelo |


---

# **Sprint Backlog — (15/12/2025)**
27. Gérer l’**affichage web** ou **l’export vers Three.js** 
35. Réattribution automatique d'une catégorie de forme selon ses proprités géométrique après modification 
37. Scale de formes
38. Deplacement de formes


---
# **User Story** et **Definition of Done – Sprint (3D)**

## 27. Gérer l’affichage web ou l’export vers Three.js

**User Story**  
En tant qu’utilisateur, je veux pouvoir visualiser mes points et formes dans une interface web ou exporter la scène vers Three.js afin d’obtenir un rendu 3D interactif.

**Definition of Done**
- L’utilisateur sélectionne **Gestion des données → Affichage Web / Export Three.js**.
- Le système propose :
  - un affichage web interne (si disponible)
  - un export compatible **Three.js**
- Les données exportées incluent :
  - points (x, y, z, nom)
  - formes (type, sommets, dimensions, angles)
- Un fichier ou une structure Three.js valide est générée.
- Les formes sont correctement positionnées et orientées dans la scène.
- Un message de confirmation est affiché.
- En cas d’erreur, un message explicite est affiché.

## 35. Réattribution automatique d’une catégorie de forme après modification

**User Story**  
En tant qu’utilisateur, je veux que le système requalifie automatiquement une forme après modification de sa géométrie afin qu’elle conserve une catégorie cohérente avec ses propriétés géométriques.

**Definition of Done**
- Une modification géométrique est appliquée à une forme (édition de points, scale, déplacement).
- Le système analyse les propriétés de la forme :
  - nombre de sommets
  - longueurs des arêtes
  - angles
  - coplanarité / symétrie
- Si les propriétés correspondent à une forme connue :
  - Rectangle → Carré
  - Pavé → Cube
  - Polygone → Carré / Rectangle
- La catégorie de la forme est automatiquement mise à jour.
- La nouvelle catégorie est affichée.
- Les données sont enregistrées.

## 37. Scale (mise à l’échelle) d’une forme

**User Story**  
En tant qu’utilisateur, je veux pouvoir appliquer un facteur d’échelle à une forme afin d’en modifier les dimensions proportionnellement.

**Definition of Done**
- L’utilisateur sélectionne une forme existante.
- Il saisit :
  - un **coefficient de scale** (ex : 0.5, 2, 3…)
  - un **point d’origine du scale** (x, y, z)
- Les coordonnées des sommets sont recalculées selon le facteur et le point d’origine.
- Les dimensions de la forme sont mises à jour.
- La forme mise à l’échelle est affichée.
- Les nouvelles coordonnées sont enregistrées.
- La requalification automatique de la forme est déclenchée si nécessaire.

## 38. Déplacement (translation) d’une forme

**User Story**  
En tant qu’utilisateur, je veux pouvoir déplacer une forme entière dans l’espace 3D afin de modifier sa position sans changer sa géométrie.

**Definition of Done**
- L’utilisateur sélectionne une forme existante.
- Il saisit un vecteur de translation :
  - (dx, dy, dz)
- Tous les points composant la forme sont déplacés du même vecteur.
- La géométrie de la forme est conservée.
- La forme déplacée est affichée.
- Les nouvelles coordonnées sont enregistrées.

---

# **Sprint Review**

Dans ce dernier sprint, nous avons finalisé le cœur fonctionnel du projet et ouvert la bibliothèque vers l'extérieur.

### **Bilan Technique**
1.  **Visualisation (Ticket 27) :** L'objectif d'Arthur a été atteint. Nous ne sommes plus limités à l'affichage textuel dans le terminal. L'export Three.js permet désormais de visualiser concrètement les formes 3D créées.
2.  **Manipulation (Tickets 37 & 38) :** Théo a implémenté les transformations affines essentielles. Le déplacement et le redimensionnement fonctionnent et mettent à jour les coordonnées des objets.
3.  **Intelligence Géométrique (Ticket 35) :** Colin a livré la fonctionnalité de mutation dynamique des objets (ex: un pavé devenant cube), validant l'aspect polymorphe du projet.

Le MVP (Minimum Viable Product) est livré et fonctionnel.

### **Bilan Humain et Contexte**
Au-delà de la technique, ce sprint de clôture a représenté un véritable défi managérial et humain.

* **Difficulté de mobilisation :** Il a été particulièrement laborieux de maintenir l'engagement de l'équipe jusqu'à la fin. Le rôle de Scrum Master a nécessité beaucoup plus d'énergie pour "pousser" les développements et s'assurer que chacun fournisse sa part, malgré une baisse de régime évidente.
* **Intérêt du sujet :** Avec le recul, le sujet du projet (bibliothèque géométrique) s'est avéré moins stimulant que prévu. L'aspect très mathématique et abstrait, manquant parfois d'application concrète immédiate ("fun factor"), a rendu l'investissement personnel plus difficile à susciter chez les développeurs.
* **Fatigue contextuelle :** Ce sprint s'inscrit dans un contexte global de fin de semestre très dense. La fatigue mentale accumulée par l'ensemble du groupe a pesé sur la productivité. Terminer ce projet a demandé de puiser dans nos dernières réserves de motivation, transformant ce sprint en une épreuve d'endurance plutôt qu'en une phase d'innovation enthousiaste.

---

# **Rétrospective**

## **Ce qui a été mis en place**
- Le poker planning.
- Un ou deux tickets maximum par personne, afin de se concentrer sur des tâches à forte plus value.

## **Ce qui a bien fonctionné**
- Planning et rétrospective avec le client/PO s'est déroulé naturelement, nous avons pu exposer nos pistes de travail (visibles dans backolog) qui on été acceptés.
- Moins de tickets mais ils sont plus gros et importants.
- Sprint moins stressant.
  
- Globalement les taches ont été fini juste à temps, le sprint était mieux géré de mon côté du côté d'Arthur que Théo ou Colin car leurs backlogs était plus lourd. *

## **Ce qui a posé problème**
- La période créer de la fatigue au sein de l'équipe.
- Sprint moins stressant mais tous aussi crucial car il conclut la matière.

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
- Enum pour les prints
- Corriger SonarQube

## _Consignes pour le compte rendu des développeurs_ :

- Penser à mettre à jour vos issues/tickets dans *Project*.
- Le code est commenté de manière claire pour chaque fonction principale.
- Chaque fonctionnalité principale est testée (manuellement au moins) pour vérifier son bon fonctionnement.
