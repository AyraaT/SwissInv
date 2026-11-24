# Introduction
En cours d'élaboration…

# Audit de réemploi

<!-- Les tableaux entre GENERIERT:START et GENERIERT:ENDE sont générés par tools/build.py à partir de data/core/audits/. Les modifier là-bas, pas ici. Le reste du texte est rédigé à la main. -->
## But et étendue
L'audit de réemploi sert à relever les éléments de construction existants qui sont concernés par une transformation ou une déconstruction et dont le réemploi doit être examiné.

À cette fin, un rapport recense les données du projet, des bâtiments et des éléments. Ces données doivent servir de base pour choisir les éléments à placer auprès de repreneurs internes ou externes.

Si nécessaire, le relevé peut se faire en deux niveaux. Le niveau I est une estimation sommaire visant à déterminer si la substance bâtie considérée se prête à un réemploi et donc à un relevé approfondi au niveau II. Il délimite en outre les groupes d'éléments pour lesquels un relevé approfondi au niveau II est recommandé.

Le niveau II est un relevé approfondi des éléments. Il peut être choisi sur la base de la recommandation du niveau I ou sans examen préalable. Le niveau II a pour but de sélectionner les éléments appropriés en vue de leur placement auprès de repreneurs.
## Niveau d'observation et structuration
Pour structurer l'audit de réemploi, il faut définir comment le projet est subdivisé en projets, bâtiments et catalogues d'éléments.

Il convient d'abord d'indiquer aussi précisément que possible le périmètre de la substance bâtie concernée, y compris les espaces extérieurs environnants et, le cas échéant, les étapes de construction.

Regrouper plusieurs bâtiments en un seul projet est par exemple judicieux lorsque les bâtiments sont déconstruits ou transformés durant la même période et qu'un catalogue d'éléments commun peut être considéré pour l'ensemble des objets.

Pour chaque projet, les données du projet et les intervenants sont à saisir une seule fois selon le tableau X: «Champs de données Projet».

Pour tous les bâtiments d'un projet, les données des bâtiments sont à saisir selon le tableau X: «Champs de données Bâtiments sources». Pour des bâtiments identiques ou reliés, elles peuvent être regroupées et indiquées une seule fois.

L'étendue de la saisie des données des éléments diffère entre les niveaux I et II de l'audit de réemploi et ressort des sections suivantes. La structuration et les niveaux d'observation des éléments ne sont pas prescrits par le Swiss Inv.
## Audit de réemploi niveau I: but et démarche
L'audit de réemploi niveau I sert à estimer sommairement le potentiel de réemploi des éléments d'un bâtiment source. Il permet une première appréciation de l'opportunité et de l'étendue d'un examen approfondi. Pour un relevé adapté aux besoins, les objectifs du mandant ainsi que le périmètre de la substance bâtie concernée devraient être communiqués au mandataire avant la visite.

L'estimation du potentiel constitue la base d'un approfondissement ciblé et adapté aux besoins. Il s'agit en particulier de délimiter les groupes d'éléments pertinents pour un examen approfondi.

Au terme de l'audit, le mandant reçoit un rapport qui sert de base de décision pour les questions suivantes:

- Faut-il réaliser un audit de réemploi niveau II pour le bâtiment source examiné?

- Quels groupes d'éléments doivent être relevés et évalués de manière approfondie dans le cadre de l'audit de réemploi niveau II?

Une fois le rapport terminé, les résultats devraient être confrontés aux objectifs et aux ressources du mandant afin de décider de la suite de la démarche.
## Audit de réemploi niveau I: format et étendue
L'audit de réemploi niveau I comprend les sections suivantes:

- Projet: indications sur le projet et les intervenants

- Introduction: description du projet, objectifs, délais, périmètre, bases (p. ex. plans / rapport sur les polluants) ainsi que démarche du mandataire

- Bâtiments: indications sur les bâtiments sources considérés

- Éléments: relevé sommaire de tous les éléments, avec pour chacun la recommandation pour ou contre un relevé approfondi

- Conclusion: recommandation motivée pour ou contre un audit de réemploi niveau II des bâtiments sources considérés

Le format de remise est à convenir entre le mandant et le mandataire. Il est recommandé de remettre l'ensemble du rapport au format PDF.

Les données du projet et des bâtiments sont à saisir conformément à la section «Niveau d'observation et structuration».

Pour le projet et les bâtiments sources, il faut saisir au minimum les informations du tableau suivant.

<!-- GENERIERT:START profil=stage-1 bereich=projekt -->
**Tableau: informations à saisir sur le projet et les bâtiments sources dans l'Audit de réemploi niveau I**

| Information | Obligation | Champ | Clé | Format |
| --- | --- | --- | --- | --- |
| Nom du projet | Obligatoire | Nom du projet | `projectName` | Texte libre (une ligne) |
| Propriétaire, mandant et mandataire | Obligatoire | Propriétaire | `projectOwner` | Contact |
|  |  | Mandant | `projectAuditClient` | Contact |
|  |  | Mandataire | `projectAuditor` | Contact |
| Adresse du bâtiment source | Obligatoire | Rue | `donorBuildingStreet` | Texte libre (une ligne) |
|  |  | Numéro | `donorBuildingHouseNumber` | Texte libre (une ligne) |
|  |  | Code postal | `donorBuildingPostalCode` | Code postal |
|  |  | Localité | `donorBuildingCity` | Texte libre (une ligne) |
| Pays du bâtiment source | Recommandé | Pays | `donorBuildingCountry` | Code pays selon ISO 3166 |
| Données du bâtiment selon le RegBL et mode de construction | Recommandé | Classe de bâtiment | `donorBuildingGklas` | Liste de sélection |
|  |  | Catégorie de bâtiment | `donorBuildingGkat` | Liste de sélection |
|  |  | Epoque de construction | `donorBuildingGbaup` | Liste de sélection |
|  |  | Mode de construction | `donorBuildingConstructionType` | Liste de sélection |
|  |  | Année de construction du bâtiment | `donorBuildingGbauj` | AAAA |
|  |  | Volume du bâtiment | `donorBuildingGvol` | Valeur numérique [m³] |
|  |  | Surface du bâtiment | `donorBuildingGarea` | Valeur numérique [m²] |
|  |  | Nombre de niveaux | `donorBuildingGastw` | Valeur numérique |
<!-- GENERIERT:ENDE -->

Pour chaque élément, il faut saisir au minimum les informations désignées comme «Obligatoire» dans la colonne «Obligation» du tableau X: «Informations à saisir par élément dans l'audit de réemploi niveau I». La colonne «Champ» recommande des champs appropriés du tableau Y: «Champs de données Éléments de réemploi», qui devraient être utilisés pour ces informations.

L'**indication de la quantité** des éléments peut être donnée de manière approximative sous forme de plage. Afin que les limites inférieure et supérieure de la plage soient lisibles par machine, les champs Quantité (min) et Quantité (max) doivent être indiqués sous forme de valeurs numériques. Une quantité vérifiée peut être signalée en saisissant la même quantité dans les deux champs.

Une **évaluation de la pollution** en vue du réemploi ne fait pas partie des exigences minimales des audits de réemploi niveau I.

Les **autres propriétés** des éléments doivent être saisies sous forme de texte dans le champ «Informations complémentaires» ou dans d'autres champs appropriés. Pour un échange de données optimal, il faut privilégier à cet effet les champs standardisés du tableau Y: «Champs de données Éléments de réemploi».

<!-- GENERIERT:START profil=stage-1 bereich=bauteile -->
**Tableau: informations à saisir par élément dans l'Audit de réemploi niveau I**

| Information | Obligation | Champ | Clé | Format |
| --- | --- | --- | --- | --- |
| Désignation courte | Obligatoire | Désignation | `name` | Texte libre (une ligne) |
| eCCC-Bât | Obligatoire | Code eCCC-Bât | `ebkphCode` | Liste de sélection |
|  |  | Désignation eCCC-Bât | `ebkphLabel` | Texte libre (une ligne) |
| Quantité, le cas échéant approximative, avec indication de l'imprécision | Obligatoire | Quantité (min) | `quantityMin` | Valeur numérique |
|  |  | Quantité (max) | `quantityMax` | Valeur numérique |
|  |  | Unité | `unit` | Liste de sélection |
| Au moins une catégorie de matériau | Obligatoire | Catégorie de matériau | `material` | Liste de sélection (choix multiple) |
| Informations complémentaires | Recommandé | Informations complémentaires | `description` | Texte libre (plusieurs lignes) |
| Recommandation pour ou contre un relevé approfondi | Obligatoire | Recommandation relevé détaillé | `recDetailedAssessment` | Liste de sélection |
<!-- GENERIERT:ENDE -->

Les définitions et les formats des champs figurent dans le [répertoire des champs de données](../dictionary/FR.md).

## Audit de réemploi niveau II: but et démarche
L'audit de réemploi niveau II sert à préparer le placement des éléments auprès de repreneurs internes ou externes. Pour un relevé adapté aux besoins, les objectifs du mandant ainsi que le périmètre de la substance bâtie concernée devraient être communiqués au mandataire avant la visite.

Au terme de l'audit, le mandant reçoit un rapport permettant de choisir les éléments à rendre visibles en vue d'un placement.

Les informations saisies doivent pouvoir être réutilisées au moins pour une clarification informelle des besoins auprès de repreneurs potentiels. Selon les stratégies et les canaux de placement, des clarifications de détail complémentaires sur les éléments peuvent être nécessaires.

L'élaboration des stratégies de placement, la gestion des canaux de placement ainsi que les clarifications complémentaires en vue du placement ne font pas partie de l'audit de réemploi niveau II. Ces prestations qui s'appuient sur l'audit ne sont pas standardisées par le Swiss Inv.

Une fois le rapport terminé, les résultats devraient être confrontés aux objectifs et aux ressources du mandant afin de décider de la suite de la démarche.
## Audit de réemploi niveau II: format et étendue
L'audit de réemploi niveau II comprend les sections suivantes:

- Projet: indications sur le projet et les intervenants

- Introduction: description du projet, objectifs, délais, périmètre, bases (p. ex. plans / rapport sur les polluants) ainsi que démarche du mandataire

- Bâtiments: indications sur les bâtiments sources considérés

- Éléments: relevé approfondi de tous les éléments, avec pour chacun la recommandation pour ou contre un placement

- Conclusion: synthèse des résultats

Le format de remise est à convenir entre le mandant et le mandataire. Il est recommandé de remettre l'ensemble du rapport au format PDF, les éléments saisis dans un format de données tabulaire et les fichiers d'images des bâtiments et des éléments.

Les données du projet et des bâtiments sont à saisir conformément à la section «Niveau d'observation et structuration».

Pour le projet et les bâtiments sources, il faut saisir au minimum les informations du tableau suivant.

<!-- GENERIERT:START profil=stage-2 bereich=projekt -->
**Tableau: informations à saisir sur le projet et les bâtiments sources dans l'Audit de réemploi niveau II**

| Information | Obligation | Champ | Clé | Format |
| --- | --- | --- | --- | --- |
| Nom du projet | Obligatoire | Nom du projet | `projectName` | Texte libre (une ligne) |
| Propriétaire, mandant et mandataire | Obligatoire | Propriétaire | `projectOwner` | Contact |
|  |  | Mandant | `projectAuditClient` | Contact |
|  |  | Mandataire | `projectAuditor` | Contact |
| Adresse du bâtiment source | Obligatoire | Rue | `donorBuildingStreet` | Texte libre (une ligne) |
|  |  | Numéro | `donorBuildingHouseNumber` | Texte libre (une ligne) |
|  |  | Code postal | `donorBuildingPostalCode` | Code postal |
|  |  | Localité | `donorBuildingCity` | Texte libre (une ligne) |
| Pays du bâtiment source | Recommandé | Pays | `donorBuildingCountry` | Code pays selon ISO 3166 |
| Données du bâtiment selon le RegBL et mode de construction | Recommandé | Classe de bâtiment | `donorBuildingGklas` | Liste de sélection |
|  |  | Catégorie de bâtiment | `donorBuildingGkat` | Liste de sélection |
|  |  | Epoque de construction | `donorBuildingGbaup` | Liste de sélection |
|  |  | Mode de construction | `donorBuildingConstructionType` | Liste de sélection |
|  |  | Année de construction du bâtiment | `donorBuildingGbauj` | AAAA |
|  |  | Volume du bâtiment | `donorBuildingGvol` | Valeur numérique [m³] |
|  |  | Surface du bâtiment | `donorBuildingGarea` | Valeur numérique [m²] |
|  |  | Nombre de niveaux | `donorBuildingGastw` | Valeur numérique |
| EGID et EGRID | Obligatoire | EGID | `donorBuildingEgid` | Texte libre (une ligne) |
|  |  | EGRID | `donorBuildingEgrid` | Texte libre (une ligne) |
| Accès | Obligatoire | Accès | `donorBuildingAccess` | Texte libre (plusieurs lignes) |
<!-- GENERIERT:ENDE -->

Pour chaque élément, il faut saisir au minimum les informations désignées comme «Obligatoire» dans la colonne «Obligation» du tableau X: «Informations à saisir par élément dans l'audit de réemploi niveau II». La colonne «Champ» recommande des champs appropriés du tableau Y: «Champs de données Éléments de réemploi», qui devraient être utilisés pour ces informations.

L'**indication de la quantité** des éléments doit être précise. Une quantité vérifiée peut être signalée en indiquant la même valeur dans Quantité (min) et Quantité (max).

Une **évaluation de la pollution** en vue du réemploi ne fait pas partie des exigences minimales des audits de réemploi niveau II. Le mandataire doit indiquer dans le champ «Diagnostic polluants» s'il existe, pour l'élément concerné, une évaluation de la pollution par un diagnostic polluants. Les indications complémentaires sur l'auteur et la date du diagnostic polluants ainsi que sur le type et le degré de pollution sont facultatives. Les conséquences d'une évaluation des polluants pour le réemploi de l'élément ne peuvent être interprétées que par des spécialistes des polluants.

Pour chaque élément, au moins une **photo principale** doit être fournie. En outre, au moins deux autres photos devraient être prises pour apporter des informations utiles sur des détails ou des vues d'ensemble. L'attribution des photos ou des autres annexes aux éléments concernés devrait être assurée par une dénomination appropriée des fichiers.

Outre les champs obligatoires, d'**autres propriétés** peuvent être saisies dans des champs supplémentaires appropriés. Pour un échange de données optimal, il faut privilégier à cet effet les champs standardisés du tableau Y: «Champs de données Éléments de réemploi».

<!-- GENERIERT:START profil=stage-2 bereich=bauteile -->
**Tableau: informations à saisir par élément dans l'Audit de réemploi niveau II**

| Information | Obligation | Champ | Clé | Format |
| --- | --- | --- | --- | --- |
| Désignation courte | Obligatoire | Désignation | `name` | Texte libre (une ligne) |
| ID de l'élément | Obligatoire | ID de l'élément | `componentId` | Texte libre (une ligne) |
| eCCC-Bât | Obligatoire | Code eCCC-Bât | `ebkphCode` | Liste de sélection |
|  |  | Désignation eCCC-Bât | `ebkphLabel` | Texte libre (une ligne) |
| Localisation dans le bâtiment source | Recommandé | Localisation dans le bâtiment source | `positionInDonorBuilding` | Texte libre (plusieurs lignes) |
| Indication précise de la quantité | Obligatoire | Quantité (min) | `quantityMin` | Valeur numérique |
|  |  | Quantité (max) | `quantityMax` | Valeur numérique |
|  |  | Unité | `unit` | Liste de sélection |
| Dimensions extérieures de l'élément ou dimensions pertinentes propres à la catégorie | Obligatoire | Dimension extérieure hauteur | `zDim` | Valeur numérique [cm] |
|  |  | Dimension extérieure largeur | `yDim` | Valeur numérique [cm] |
|  |  | Dimension extérieure profondeur / longueur | `xDim` | Valeur numérique [cm] |
|  |  | Indications libres sur les dimensions | `dimensionNotes` | Texte libre (plusieurs lignes) |
| Au moins une catégorie de matériau | Obligatoire | Catégorie de matériau | `material` | Liste de sélection (choix multiple) |
| Autres indications sur le matériau | Obligatoire | Informations complémentaires sur le matériau | `materialNotes` | Texte libre (plusieurs lignes) |
| Informations complémentaires | Recommandé | Informations complémentaires | `description` | Texte libre (plusieurs lignes) |
| Renvoi au diagnostic polluants | Obligatoire | Diagnostic polluants | `pollutantReport` | Liste de sélection |
| Évaluation de l'état | Obligatoire | État visuel | `visualCondition` | Liste de sélection |
|  |  | État fonctionnel | `functionalCondition` | Liste de sélection |
| Estimation de l'effort de démontage | Obligatoire | Effort de démontage | `demountability` | Liste de sélection |
| Recommandation pour ou contre un placement | Obligatoire | Recommandation placement | `recDistribution` | Liste de sélection |
| Justification de la recommandation | Recommandé | Explication de la recommandation | `recNotes` | Texte libre (plusieurs lignes) |
| Photo principale de l'élément | Obligatoire | Les fichiers d'images et autres annexes ne figurent pas dans le format de données tabulaire; ils sont à remettre séparément |  |  |
| Au moins deux autres photos d'ensemble ou de détail | Recommandé | Les fichiers d'images et autres annexes ne figurent pas dans le format de données tabulaire; ils sont à remettre séparément |  |  |
<!-- GENERIERT:ENDE -->

Les définitions et les formats des champs figurent dans le [répertoire des champs de données](../dictionary/FR.md).


# Exigences relatives aux interfaces numériques
En cours d'élaboration…
