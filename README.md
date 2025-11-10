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

<!--pandoc README_sprint1.md -o README_sprint1.pdf --pdf-engine=xelatex-->

# **Product Backlog**

1. Créer et afficher un points dans un espace 2D (flottants) avec un retour de son nom
2. Créer et afficher un polygone quelconque de N points (choisis) dans un espace 2D
4. Calculer et afficher la distance euclidienne 2D entre 2 points
3. Afficher la liste des formes crées (points + forme)
5. Créer un menu textuel
6. Créer et afficher un points dans un espace 3D (flottants) avec un retour de son nom
7. Créer et afficher un polygone quelconque de N points (choisis) dans un espace 3D
8. Calculer et afficher la distance euclidienne 3D entre 2 points
9. Créer et afficher un carré en 2D
10. Créer et afficher un triangle en 2D
11. Créer et afficher un rectangle en 2D
12. Créer et afficher un cercle en 2D
13. Créer et afficher un segment en 2D
9. Créer et afficher un carré en 3D
10. Créer et afficher un triangle en 3D
11. Créer et afficher un rectangle en 3D
12. Créer et afficher un cercle en 3D
13. Créer et afficher un segment en 3D
14. Créer et afficher un cone
10. Créer et afficher une pyramide
11. Créer et afficher un pave
12. Créer et afficher un cube
13. Créer et afficher une sphere
13. Éditer les points (suppression, translation, changement de base ?) 
14. Éditer les formes (suppression, translation)  
15. Appartenance de forme et intersection d’espace  
16. Terminal -> déclarer + calcul (distance, volume, périmètre, surface)  
17. Menu terminal  
18. Que dans le terminal  
19. Import / Export des points  
20. Export sur R  
21. Affichage web ou export Three.js  
22. User peut ajouter des polygones quelconques

---

# **Sprint Backlog — S1 (04/11/25)**

- Créer et afficher un points dans un espace 2D (flottants) avec un retour de son nom
- Créer et afficher un polygone quelconque de N points (choisis) dans un espace 2D 
- Afficher la liste des formes crées (points + forme)
- Calculer et afficher la distance euclidienne entre 2 points
- Créer un menu textuel

---

# **User Story**
- Depuis un menu un utilisateur choisi l'option creeation de points et donne sa coordonnée x.0 ; y.0
- Depuis un menu un utilisateur choisi l'option creeation de polygone :
     - Il choisi le nombre de points
     - Pour chaque il peut soit indiqué le nom d'un point existant (exemple p0) ou indiquer ses coordonnées  x.0;y.0
- Depuis un menu un utilisateur choisi l'option 3 pour afficher tous l'espace f0: p0(x.0;y.0); p1(x.0;y.0) puis à la ligne pour chaque objet
- Depuis un menu textuelle l'utilisateur choisi une option pour calculer la distance en 2 points déjà existant depuis leur nom : p0;p1
- Une fois un objet crééer par un utilisateur, il s'affiche dans le menu textuel f0: p0(x.0;y.0); p1(x.0;y.0) ou  p0(x.0;y.0)
  
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
# **interne**
## _Consignes pour le compte rendu des développeurs_ :

- Creer pour chaque feature une branche **Sprint*X*-feat-*nom_de_vote_feature*** ou bien **Sprint*X*-scrum**.
- Penser à mettre à jour vos issues/tickets dans *Project*.
- Le code est commenté de manière claire pour chaque fonction principale.
-  Chaque fonctionnalité principale est testée manuellement pour vérifier son bon fonctionnement.


## _Sprint planning_ :

Sprint S1 était principalement un sprint d’initialisation technique :
- Initialisation organisation GitHub commune  
- Mise en place de SonarQube qualité + règles + intégration  
- Création et configuration de l’environnement de développement  
- Écriture des premiers tests unitaires  
- Préparation structure future console (sans implémentation fonctionnelle)



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

