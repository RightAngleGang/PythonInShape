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

1. User peut définir les points  
2. Définir des points dans un espace 2D (création d’un point avec 2 coordonnées)  
3. Définir des points dans un espace 3D (création d’un point avec 3 coordonnées)  
4. Nommage automatique des points à la création  
5. Distance euclidienne entre les points  
6. Faire des formes de base (carré, triangle, cercle, segments) + (cube, pyramide, sphère)  
7. Polygones quelconques  
8. Éditer les points (suppression, translation, changement de base)  
9. Éditer les formes (suppression, translation)  
10. Appartenance + intersection d’espace  
11. Terminal -> déclarer + calcul (distance, volume, périmètre, surface)  
12. Menu terminal  
13. Que dans le terminal  
14. Import / Export des points  
15. Export sur R  
16. Affichage web ou export Three.js  
17. User peut ajouter des polygones quelconques

---

# **Sprint Backlog — S1 (04/11/25)**

- Créer un points dans un espace 2D (flottants) avec un retour de son nom
- Définir des polygones quelconques de N points (choisis) dans un espace 2D 
- voir la liste des ibjets crées (points + forme)
- Definir la distance euclidienne entre 2 points
- Affichage de l'objet après sa création
- Creer un menu textuel

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

