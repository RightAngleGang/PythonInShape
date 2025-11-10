# PythonInShape
CERI M1 IA PDDL - Projet de bibliothèque de calcul géométrique

# Sprint 1

**Auteurs : M1 IA Informatique**

- Angelo Adragna
- Arthur Buren
- Colin Palazzetti Rubera
- Théo Torres

**lien vers Github**
[README Sprint 1][(https://github.com/conception-logicielle-CERI/parseur-pdf/edit/sprint-4/README_sprint4.md](https://github.com/RightAngleGang/PythonInShape/blob/sprint1-scrum/README.md))

## **Rôles**

- Angelo est `SCRUM Master`, il doit rédiger le rapport avec les différents artefacts.
- Arthur, Colin et Théo sont développeurs.


# **Product Backlog**

1. Créer et afficher un points dans un espace 2D (flottants) avec un retour de son nom
2. Créer et afficher un polygone quelconque de N points (choisis) dans un espace 2D
3. Calculer et afficher la distance euclidienne 2D entre 2 points
4. Afficher la liste des formes crées (points + forme)
5. Créer un menu textuel dans le terminal
6. Créer et afficher un carré en 2D
7. Créer et afficher un triangle en 2D
8. Créer et afficher un rectangle en 2D
9. Créer et afficher un cercle en 2D
10. Créer et afficher un segment en 2D
11. Nommage automatique des points à la création de forme
12. Éditer les points (suppression, translation, changement de base ?) 
13. Éditer les formes (suppression, translation)  
14. Créer et afficher un points dans un espace 3D (flottants) avec un retour de son nom
15. Créer et afficher un polygone quelconque de N points (choisis) dans un espace 3D
16. Calculer et afficher la distance euclidienne 3D entre 2 points
17. Créer et afficher un carré en 3D
18. Créer et afficher un triangle en 3D
19. Créer et afficher un rectangle en 3D
20. Créer et afficher un cercle en 3D
21. Créer et afficher un segment en 3D
22. Créer et afficher un cone
23. Créer et afficher une pyramide
24. Créer et afficher un pave
25. Créer et afficher un cube
26. Créer et afficher une sphere
27. Affichage web ou export Three.js  
28. Appartenance de forme et intersection d’espace  
29. Import / Export des points (sur R potentiellement)  

---

# **Sprint Backlog — S1 (04/11/25)**

- Créer et afficher un points dans un espace 2D (flottants) avec un retour de son nom
- Créer et afficher un polygone quelconque de N points (choisis) dans un espace 2D 
- Afficher la liste des formes crées (points + forme)
- Calculer et afficher la distance euclidienne entre 2 points
- Créer un menu textuel

---

# **User Story**
- Depuis le menu, un utilisateur peut choisir l'option 'creation de points' et donne ses coordonnées de la manière suivante : `x.0;y.0`
- Depuis le menu, un utilisateur peut choisir l'option `creation de polygone` :
     - Il choisi le d'abord nombre de points : `n`
     - Pour chaque point, il peut soit indiqué le nom d'un point existant : `p0`
       ou indiquer ses coordonnées `x.0;y.0`
- Depuis le menu, un utilisateur peut choisir l'option `afficher l'espace` et affiche à la ligne pour chaque forme: `f0: p0(x.0;y.0); p1(x.0;y.0)`
- Depuis le menu un utilisateur peut choisie l'option `calcule la distance euclidienne` entre 2 points déjà existant depuis leur nom : `p0;p1`
  
---

# Definition of Done

Un élément du sprint est considéré **terminé** lorsque tous les critères suivants sont remplis :

## Fonctionnalités de création
- Les points peuvent être créés dans un espace 2D avec des coordonnées flottantes `x.0;y.0`.
- Les polygones peuvent être définis avec un nombre quelconque de points.
- Les points d’un polygone peuvent être soit :
  - des points déjà existants (référence par nom), ou  
  - de nouveaux points avec coordonnées `(x.0, y.0)`.

## Fonctionnalités de consultation
-  La liste complète des objets créés (points et polygones) peut être affichée.

## Calculs
- La distance euclidienne entre deux points existants peut être calculée et affiché (calcul en flottants)

## Menu textuel
- Un menu textuel fonctionne correctement et permet :
  - la création de points  
  - la création de polygones  
  - l’affichage de tous les objets  
  - le calcul de distance entre deux points

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

# **Daily Sprint 04/11/25**
 Ceci represente l'avancement, qui a du retard , si ça se passe bien ou non


---

# **Sprint planning**


### **details du travail effectué lors du sprint**

### **Exemples d'utilisation:**

### **analyse du travail effectué lors du sprint**

### **Remarques**

### **A faire **

---

# ** Rétrospective (Retour sur le travail effectué)**

### **Ce qui a été mis en place**


### **Ce qui a bien fonctionné**


### **Ce qui a posé problème**


### **Ce qu’on doit améliorer**


---

# **interne**

## _taches_ :

- Initialisation organisation GitHub commune  
- Mise en place de SonarQube qualité + règles + intégration  
- Création et configuration de l’environnement de développement  
- Écriture des premiers tests unitaires  

## _Consignes pour le compte rendu des développeurs_ :

- Creer pour chaque feature une branche **Sprint*X*-feat-*nom_de_vote_feature*** ou bien **Sprint*X*-scrum**.
- Penser à mettre à jour vos issues/tickets dans *Project*.
- Le code est commenté de manière claire pour chaque fonction principale.
-  Chaque fonctionnalité principale est testée manuellement pour vérifier son bon fonctionnement.

---
