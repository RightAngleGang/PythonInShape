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

# **Sprint Review (Et planning)**

Sprint S1 était principalement un sprint d’initialisation technique.

Travail réalisé pendant ce sprint :
- Mise en place de l’organisation GitHub
- Création et configuration de l’environnement de développement
- Mise en place de SonarQube (qualité / dette technique / couverture)
- Écriture des premiers tests unitaires (base du futur TDD)

Livrable du sprint : infrastructure stable + pipeline qualité ready  
Les fonctionnalités console 2D commenceront réellement à être implémentées au Sprint 2.


---

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

**Objectif Sprint** : construire l’infrastructure du projet et l’environnement qualité.

Items du Sprint :

- Initialisation organisation GitHub commune  
- Mise en place de SonarQube qualité + règles + intégration  
- Création et configuration de l’environnement de développement  
- Écriture des premiers tests unitaires  
- Préparation structure future console (sans implémentation fonctionnelle)

**NOTE** : Pas de features 2D User dans ce sprint → tout l’effort était préparatoire.


---

# **Use Case — Sprint S1**

Pas de Use Case user final encore implémenté.  
Le Sprint S1 se concentrait sur “Enable” → préparer les futurs UCs.


---

# **Definition of Done**

- Pipeline qualité opérationnel  
- Environnement reproductible et fonctionnel  
- SonarQube actif + inspecte projet  
- Tests unitaires existants exécutables et passent  
- Base de code propre, structurée et lisible


---

# **Poker planning**

Pas encore mis en place.
<!--
| Item sprint | Estimation |
|-------------|------------|
| Setup GitHub | 3 |
| Setup SonarQube | 8 |
| Setup Environnement dev | 5 |
| Écrire premiers tests | 3 |
-->

---

# **Daily Sprint 04/11/25**

- Mise en place GitHub / accès pour tous  
- Setup SonarQube local + règles  
- Initialisation projet + premières classes vides  
- Premier test unitaire écrit et exécuté


## _Consignes pour le compte rendu des développeurs_ :

- Remplir votre revu de sprint, vous êtes libre de changer l'organisation définie par défaut, ce n'est qu'une suggestion.
- Remplir votre retrospective de sprint.
- Creer pour chaque feature une branche **Sprint*X*-feat-*nom_de_vote_feature*** ou bien **Sprint*X*-scrum**.
- Penser à mettre à jour vos issues/tickets dans *Project*.

---

## 1. **Angelo Adragna** :

### **details du travail effectué lors du sprint**

### **Exemples d'utilisation:**

### **analyse du travail effectué lors du sprint**

### **Remarques**

---

## 2. **Arthur Buren** :
   
### **details du travail effectué lors du sprint**

1 - j'ai créé la base de l'environnement avec un makefile et un requirements.txt
2 - j'ai créé une boucle de main qui propose un menu d'action

### **Exemples d'utilisation:**

- make run -> lancer le programme avec les vérification
- make lint -> à implémenter
- make clean -> néttoie le cache 
- make test -> lance les test

- lancer la boucle -> 1 -> script python executé

### **analyse du travail effectué lors du sprint**

ça marche, certains trucs reste à implémenter mais son bloqué par le travail des autres

### **Remarques**


---

## 3. **Colin Palazzetti Rubera** :
    
### **details du travail effectué lors du sprint**
- Initialisation de SonarQube
- Configuration de Github
- Adaptation des pratiques en fonction des besoin de SonarQube free

### **Exemples d'utilisation:**

### **analyse du travail effectué lors du sprint**
- La configuration du projet SonarQube
J'ai dû supprimer le projet deux fois, pour bien le reconfigurer  
Lors de nos sprint, la branche "principale" sera la branche dev, qui est analysée par SonarQube


- Configuration de Github
Création de l'orga et du repo, et d'un projet dans le repo, pour tester  

Protection des branche `main` et `dev` contre les commits, requiérant des PR

les PR nécessitent au moins 1 reviewer 

### **Remarques**
Il aurait fallu que je comprenne SonarQube avant que le groupe se mette d'accord sur les principes de dev, 
ce qui a délayé mon travail et a nécessité un nouvel accord compatible avec SonarQube free

---


## 4. **Théo Torres** :
   
### **details du travail effectué lors du sprint**
- Ajout d'un exemple d'utilisation de pytest
- Ajout de la class Point 
### **Exemples d'utilisation:**
p1 = Point(1.0,1.0)
print(p1)

pytest
### **analyse du travail effectué lors du sprint**
Ca marche ! 
### **Remarques**

---

# ** Rétrospective (Retour sur le travail effectué)**
## 1. **Angelo Adragna** 
### **Ce que j'ai mis en place**


### **Ce qui a bien fonctionné**


### **Ce qui a posé problème**


### **Ce qu’on doit améliorer**

---

## 2. **Arthur Buren** 

### **Ce que j'ai mis en place**
environnement de travail
menu principal
Boucle principal fonctionnelle dans le terminal 

### **Ce qui a bien fonctionné**
tout


### **Ce qui a posé problème**
formattage de l'env et utilisation 

### **Ce qu’on doit améliorer**
flexibilité du menu et de l'environnement d'execution

---

## 3. **Colin Palazzetti Rubera** 

### **Ce que j'ai mis en place**


### **Ce qui a bien fonctionné**


### **Ce qui a posé problème**


### **Ce qu’on doit améliorer**

---

## 4. **Théo Torres** 


### **Ce que j'ai mis en place**
On peut tester avec pytest et créer un point avec Point
### **Ce qui a bien fonctionné**
- Tout
### **Ce qui a posé problème**
- Rien
### **Ce qu’on doit améliorer**
- Productivité et communication

---

## 5. **Conclusion Global** :


