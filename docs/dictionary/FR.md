<!-- Automatisch erzeugt von tools/build.py - nicht von Hand bearbeiten. -->

# Répertoire des champs de données Swiss Inv

[Deutsch](DE.md) · **Français** · [Italiano](IT.md) · [English](EN.md)

Version: `2.0.0-draft`

**Noyau** = stable, ne change qu'avec une nouvelle édition de la norme. **Extension** = champs facultatifs qui s'étoffent au fil des propositions.

## Champs de données Projet

### Identification

| Champ | Clé | Format | Niveau | Niveau I | Niveau II | Définition |
| --- | --- | --- | --- | --- | --- | --- |
| Nom du projet | `projectName` | Texte libre (une ligne) | Noyau | Obligatoire | Obligatoire | Désignation du projet regroupant un ou plusieurs bâtiments sources |
| ID du projet | `projectId` | Texte libre (une ligne) | Noyau |  |  | Identifiant du projet; le format et l'attribution de l'ID ne sont pas prescrits par le Swiss Inv |

### Intervenants du projet

| Champ | Clé | Format | Niveau | Niveau I | Niveau II | Définition |
| --- | --- | --- | --- | --- | --- | --- |
| Propriétaire | `projectOwner` | Contact | Noyau | Obligatoire | Obligatoire | Propriétaire des bâtiments sources concernés |
| Planificateur | `projectPlanner` | Contact | Noyau |  |  | Bureau chargé de la planification de la transformation ou de la déconstruction |
| Mandant | `projectAuditClient` | Contact | Noyau | Obligatoire | Obligatoire | Mandant de l'audit de réemploi |
| Mandataire | `projectAuditor` | Contact | Noyau | Obligatoire | Obligatoire | Mandataire qui réalise l'audit de réemploi |

## Champs de données Contacts

### Personne de contact

| Champ | Clé | Format | Niveau | Définition |
| --- | --- | --- | --- | --- |
| Nom | `contactName` | Texte libre (une ligne) | Noyau | Prénom et nom de la personne de contact |
| Rôle dans le projet | `contactRole` | Texte libre (une ligne) | Noyau | Rôle ou fonction de la personne de contact dans le projet |

### Adresse

| Champ | Clé | Format | Niveau | Définition |
| --- | --- | --- | --- | --- |
| Entreprise | `contactCompany` | Texte libre (plusieurs lignes) | Noyau | Nom de l'entreprise ou de l'organisation |
| Rue | `contactStreet` | Texte libre (une ligne) | Noyau | Nom de la rue de l'adresse de la personne de contact |
| Numéro | `contactHouseNumber` | Texte libre (une ligne) | Noyau | Numéro de maison de l'adresse de la personne de contact |
| Code postal | `contactPostalCode` | Code postal | Noyau | Code postal de l'adresse de la personne de contact |
| Localité | `contactCity` | Texte libre (une ligne) | Noyau | Localité de l'adresse de la personne de contact |
| Pays | `contactCountry` | Code pays selon ISO 3166 | Noyau | Pays de l'adresse de la personne de contact sous forme de code pays à deux lettres selon ISO 3166-1 (p. ex. CH) |

### Coordonnées

| Champ | Clé | Format | Niveau | Définition |
| --- | --- | --- | --- | --- |
| Téléphone | `contactPhone` | Numéro de téléphone | Noyau | Numéro de téléphone de la personne de contact, si possible au format international avec indicatif du pays |
| E-mail | `contactEmail` | Adresse e-mail | Noyau | Adresse e-mail de la personne de contact |

## Champs de données Bâtiments sources

### Adresse

| Champ | Clé | Format | Niveau | Niveau I | Niveau II | Définition |
| --- | --- | --- | --- | --- | --- | --- |
| EGID | `donorBuildingEgid` | Texte libre (une ligne) | Noyau |  | Obligatoire | Identificateur fédéral de bâtiment: numéro d'identification du bâtiment dans le RegBL fédéral. Source: catalogue des caractères RegBL 5.0, caractère EGID. |
| EGRID | `donorBuildingEgrid` | Texte libre (une ligne) | Noyau |  | Obligatoire | Identificateur fédéral (E-GRID) de l'immeuble (bien-fonds), objet de la propriété foncière, sur lequel le bâtiment est construit. Source: catalogue des caractères RegBL 5.0, caractère GEGRID. |
| Rue | `donorBuildingStreet` | Texte libre (une ligne) | Noyau | Obligatoire | Obligatoire | Nom de la rue de l'adresse du bâtiment source |
| Numéro | `donorBuildingHouseNumber` | Texte libre (une ligne) | Noyau | Obligatoire | Obligatoire | Numéro de maison de l'adresse du bâtiment source |
| Code postal | `donorBuildingPostalCode` | Code postal | Noyau | Obligatoire | Obligatoire | Code postal de l'adresse du bâtiment source |
| Localité | `donorBuildingCity` | Texte libre (une ligne) | Noyau | Obligatoire | Obligatoire | Localité de l'adresse du bâtiment source |
| Pays | `donorBuildingCountry` | Code pays selon ISO 3166 | Noyau | Recommandé | Recommandé | Pays de l'adresse du bâtiment source sous forme de code pays à deux lettres selon ISO 3166-1 (p. ex. CH) |

### Données du bâtiment

| Champ | Clé | Format | Niveau | Niveau I | Niveau II | Définition |
| --- | --- | --- | --- | --- | --- | --- |
| Classe de bâtiment | `donorBuildingGklas` | Liste de sélection → [gwr-gklas](#list-gwr-gklas) | Noyau | Recommandé | Recommandé | Ventilation des bâtiments selon la classification d'Eurostat. Source: catalogue des caractères RegBL 5.0, caractère GKLAS. |
| Catégorie de bâtiment | `donorBuildingGkat` | Liste de sélection → [gwr-gkat](#list-gwr-gkat) | Noyau | Recommandé | Recommandé | Subdivision des bâtiments selon leur affectation. Source: catalogue des caractères RegBL 5.0, caractère GKAT. |
| Epoque de construction | `donorBuildingGbaup` | Liste de sélection → [gwr-gbaup](#list-gwr-gbaup) | Noyau | Recommandé | Recommandé | Indication sur l'époque de l'achèvement du bâtiment. Source: catalogue des caractères RegBL 5.0, caractère GBAUP. |
| Mode de construction | `donorBuildingConstructionType` | Liste de sélection → [construction-type](#list-construction-type) | Noyau | Recommandé | Recommandé | Mode de construction ou structure porteuse prédominante du bâtiment, par exemple construction massive, à ossature ou en bois |
| Année de construction du bâtiment | `donorBuildingGbauj` | AAAA | Noyau | Recommandé | Recommandé | Indication sur l'année de l'achèvement du bâtiment. Source: catalogue des caractères RegBL 5.0, caractère GBAUJ. |
| Volume du bâtiment | `donorBuildingGvol` | Valeur numérique [m³] | Noyau | Recommandé | Recommandé | Indication sur le volume du bâtiment. Source: catalogue des caractères RegBL 5.0, caractère GVOL. |
| Surface du bâtiment | `donorBuildingGarea` | Valeur numérique [m²] | Noyau | Recommandé | Recommandé | Surface du bâtiment en mètres carrés. Source: catalogue des caractères RegBL 5.0, caractère GAREA. |
| Nombre de niveaux | `donorBuildingGastw` | Valeur numérique | Noyau | Recommandé | Recommandé | Nombre d'étages et de sous-sols, rez-de-chaussée inclus. Source: catalogue des caractères RegBL 5.0, caractère GASTW. |
| Date de construction | `donorBuildingConstructionDate` | AAAA-MM-JJ | Extension |  |  | Date d'achèvement du bâtiment, si elle est connue plus précisément que l'année de construction |

### Détails

| Champ | Clé | Format | Niveau | Niveau I | Niveau II | Définition |
| --- | --- | --- | --- | --- | --- | --- |
| Transformations antérieures | `donorBuildingPreviousRenovations` | Texte libre (plusieurs lignes) | Noyau |  |  | Transformations, rénovations ou agrandissements antérieurs connus du bâtiment, si possible avec l'année |
| Accès | `donorBuildingAccess` | Texte libre (plusieurs lignes) | Noyau |  | Obligatoire | Accessibilité du bâtiment pour le démontage et l'évacuation, par exemple accès routier, ascenseur, emplacement pour grue |
| Informations complémentaires | `donorBuildingDetails` | Texte libre (plusieurs lignes) | Noyau |  |  | Autres indications pertinentes sur le bâtiment source qui ne sont pas couvertes par les autres champs |
| Événements exceptionnels | `donorBuildingSpecialEvents` | Texte libre (plusieurs lignes) | Extension |  |  | Événements exceptionnels ayant pu influencer l'état des éléments, par exemple incendie, dégât d'eau ou vacance prolongée |
| Année de la dernière transformation | `donorBuildingLastRenovationYear` | AAAA | Extension |  |  | Année de la dernière transformation ou rénovation du bâtiment |
| Démontage dès le | `donorBuildingDismantlingStartDate` | AAAA-MM-JJ | Extension |  |  | Date à partir de laquelle les éléments peuvent être démontés dans le bâtiment source |
| Démontage jusqu'au | `donorBuildingDismantlingEndDate` | AAAA-MM-JJ | Extension |  |  | Date à laquelle le démontage des éléments doit être terminé |
| Annexes | `donorBuildingAttachments` | Texte libre (plusieurs lignes) | Extension |  |  | Désignation et emplacement des documents relatifs au bâtiment source, par exemple plans ou diagnostic polluants |

## Champs de données Éléments de réemploi

### Identification

| Champ | Clé | Format | Niveau | Niveau I | Niveau II | Définition |
| --- | --- | --- | --- | --- | --- | --- |
| Désignation | `name` | Texte libre (une ligne) | Noyau | Obligatoire | Obligatoire | Désignation courte |
| ID de l'élément | `componentId` | Texte libre (une ligne) | Noyau |  | Obligatoire | Numéro d'identification du DPP; le format et l'attribution de l'ID ne sont pas prescrits par le Swiss Inv |
| Code eCCC-Bât | `ebkphCode` | Liste de sélection → [ebkph](#list-ebkph) | Noyau | Obligatoire | Obligatoire | Selon eCCC-Bât SN 506 511; le code et la désignation doivent figurer dans des champs séparés; une sélection de codes possibles figure dans le tableau de référence eCCC-Bât |
| Désignation eCCC-Bât | `ebkphLabel` | Texte libre (une ligne) | Noyau | Obligatoire | Obligatoire | Désignation correspondant au code eCCC-Bât; le code et la désignation doivent figurer dans des champs séparés |
| Localisation dans le bâtiment source | `positionInDonorBuilding` | Texte libre (plusieurs lignes) | Noyau |  | Recommandé | Description de la localisation dans le bâtiment source, par exemple étage, local, etc. |
| UUID | `uuid` | UUID | Extension |  |  | selon ISO/IEC 9834-8:2014; garantit une identification unique au niveau mondial |
| UUID de la position principale | `parentUuid` | UUID | Extension |  |  | Indique l'appartenance à une position globale supérieure |
| Code eBKP-Gate | `ebkpGateCode` | Liste de sélection → [ebkp-gate](#list-ebkp-gate) | Extension |  |  | Selon eBKP-Gate; le code et la désignation doivent figurer dans des champs séparés |
| Désignation eBKP-Gate | `ebkpGateLabel` | Texte libre (une ligne) | Extension |  |  | Désignation correspondant au code eBKP-Gate; le code et la désignation doivent figurer dans des champs séparés |

### Quantité

| Champ | Clé | Format | Niveau | Niveau I | Niveau II | Définition |
| --- | --- | --- | --- | --- | --- | --- |
| Quantité (min) | `quantityMin` | Valeur numérique | Noyau | Obligatoire | Obligatoire | La quantité peut être indiquée volontairement de manière approximative sous forme de plage avec une limite inférieure et une limite supérieure; pour une indication précise, saisir la même valeur dans les deux champs |
| Quantité (max) | `quantityMax` | Valeur numérique | Noyau | Obligatoire | Obligatoire | La quantité peut être indiquée volontairement de manière approximative sous forme de plage avec une limite inférieure et une limite supérieure; pour une indication précise, saisir la même valeur dans les deux champs |
| Unité | `unit` | Liste de sélection → [unit](#list-unit) | Noyau | Obligatoire | Obligatoire | Il est recommandé de choisir une unité adaptée au placement des éléments |
| Informations complémentaires sur la quantité | `quantityNotes` | Texte libre (plusieurs lignes) | Extension |  |  | Informations complémentaires sur la quantité, par exemple d'autres grandeurs de référence |

### Dimensions

| Champ | Clé | Format | Niveau | Niveau I | Niveau II | Définition |
| --- | --- | --- | --- | --- | --- | --- |
| Dimension extérieure hauteur | `zDim` | Valeur numérique [cm] | Noyau |  | Obligatoire | Les trois dimensions extérieures visent à uniformiser l'indication des dimensions pour le plus grand nombre possible de formes d'éléments; elles se fondent sur le parallélépipède englobant du standard IFC de buildingSMART |
| Dimension extérieure largeur | `yDim` | Valeur numérique [cm] | Noyau |  | Obligatoire | Les trois dimensions extérieures visent à uniformiser l'indication des dimensions pour le plus grand nombre possible de formes d'éléments; elles se fondent sur le parallélépipède englobant du standard IFC de buildingSMART |
| Dimension extérieure profondeur / longueur | `xDim` | Valeur numérique [cm] | Noyau |  | Obligatoire | Les trois dimensions extérieures visent à uniformiser l'indication des dimensions pour le plus grand nombre possible de formes d'éléments; elles se fondent sur le parallélépipède englobant du standard IFC de buildingSMART |
| Indications libres sur les dimensions | `dimensionNotes` | Texte libre (plusieurs lignes) | Noyau |  | Obligatoire | Indication des dimensions pertinentes qui ne sont pas couvertes par les dimensions extérieures ou d'autres attributs |

### Détails

| Champ | Clé | Format | Niveau | Niveau I | Niveau II | Définition |
| --- | --- | --- | --- | --- | --- | --- |
| Informations complémentaires | `description` | Texte libre (plusieurs lignes) | Noyau | Recommandé | Recommandé | Description des propriétés pertinentes qui ne sont pas couvertes par les dimensions extérieures ou d'autres attributs |
| Catégorie de matériau | `material` | Liste de sélection (choix multiple) → [material](#list-material) | Noyau | Obligatoire | Obligatoire | Catégories de matériau dont l'élément est principalement constitué; plusieurs peuvent être choisies, par exemple, pour une fenêtre en bois, bois massif pour le cadre et verre pour le vitrage |
| Informations complémentaires sur le matériau | `materialNotes` | Texte libre (plusieurs lignes) | Noyau |  | Obligatoire | Précisions sur le matériau qui ne sont pas couvertes par la catégorie de matériau |

### Évaluation

| Champ | Clé | Format | Niveau | Niveau I | Niveau II | Définition |
| --- | --- | --- | --- | --- | --- | --- |
| Diagnostic polluants | `pollutantReport` | Liste de sélection → [pollutant-report](#list-pollutant-report) | Noyau |  | Obligatoire | Indique s'il existe, pour l'élément, une évaluation de la pollution par un diagnostic polluants |
| État visuel | `visualCondition` | Liste de sélection → [visual-condition](#list-visual-condition) | Noyau |  | Obligatoire | D'éventuelles précisions sur l'état visuel peuvent être ajoutées dans le champ «Explication de la recommandation» |
| État fonctionnel | `functionalCondition` | Liste de sélection → [functional-condition](#list-functional-condition) | Noyau |  | Obligatoire | D'éventuelles précisions sur l'état fonctionnel peuvent être ajoutées dans le champ «Explication de la recommandation» |
| Effort de démontage | `demountability` | Liste de sélection → [demountability](#list-demountability) | Noyau |  | Obligatoire | D'éventuelles précisions sur l'effort de démontage peuvent être ajoutées dans le champ «Explication de la recommandation» |
| Recommandation relevé détaillé | `recDetailedAssessment` | Liste de sélection → [rec-detailed-assessment](#list-rec-detailed-assessment) | Noyau | Obligatoire |  | L'auditeur de l'audit de réemploi de niveau I recommande si un relevé approfondi de l'élément doit être réalisé dans l'audit de réemploi de niveau II |
| Recommandation placement | `recDistribution` | Liste de sélection → [rec-distribution](#list-rec-distribution) | Noyau |  | Obligatoire | L'auditeur de l'audit de réemploi de niveau II recommande si un placement de l'élément doit être visé |
| Explication de la recommandation | `recNotes` | Texte libre (plusieurs lignes) | Noyau |  | Recommandé | Éventuelles précisions sur l'évaluation ainsi que sur la recommandation de placement de l'élément |
| Informations complémentaires sur les polluants | `pollutantNotes` | Texte libre (plusieurs lignes) | Extension |  |  | Indications complémentaires sur le diagnostic polluants, par exemple auteur, date ainsi que type et degré de pollution |
| Type d'assemblage | `connection` | Liste de sélection (choix multiple) → [connection](#list-connection) | Extension |  |  | Sont visés tous les assemblages pertinents pour le démontage ou le montage de l'élément; les informations supplémentaires non couvertes par la liste de sélection peuvent être ajoutées en texte libre dans le champ «Informations complémentaires sur le type d'assemblage» |
| Informations complémentaires sur le type d'assemblage | `connectionNotes` | Texte libre (plusieurs lignes) | Extension |  |  | Informations supplémentaires sur l'assemblage qui ne sont pas couvertes par la liste de sélection |

### Logistique

| Champ | Clé | Format | Niveau | Niveau I | Niveau II | Définition |
| --- | --- | --- | --- | --- | --- | --- |
| Statut de réemploi | `reUseStatus` | Liste de sélection → [reuse-status](#list-reuse-status) | Extension |  |  | État actuel de l'élément dans le processus de réemploi |
| Code postal du lieu | `locationPostalCode` | Code postal | Extension |  |  | Code postal de l'emplacement actuel de l'élément |
| Pays du lieu | `locationCountry` | Code pays selon ISO 3166 | Extension |  |  | Pays de l'emplacement actuel de l'élément sous forme de code pays à deux lettres selon ISO 3166-1 (p. ex. CH) |
| Date d'entrée en stock | `storageStartDate` | AAAA-MM-JJ | Extension |  |  | Date à laquelle l'élément a été mis en stock |
| Date de sortie de stock | `storageEndDate` | AAAA-MM-JJ | Extension |  |  | Date à laquelle l'élément a quitté le stock ou doit le quitter au plus tard |
| Informations complémentaires sur la logistique | `logisticsNotes` | Texte libre (plusieurs lignes) | Extension |  |  | Informations complémentaires sur le stockage, l'emballage et le transport de l'élément |

### Conditions

| Champ | Clé | Format | Niveau | Niveau I | Niveau II | Définition |
| --- | --- | --- | --- | --- | --- | --- |
| Date de début de disponibilité | `availabilityStartDate` | AAAA-MM-JJ | Extension |  |  | Date à partir de laquelle l'élément est disponible pour les repreneurs |
| Date de fin de disponibilité | `availabilityEndDate` | AAAA-MM-JJ | Extension |  |  | Date jusqu'à laquelle l'élément est disponible pour les repreneurs |
| Prix de vente | `price` | Valeur numérique [CHF] | Extension |  |  | Prix de vente en francs suisses par unité choisie pour l'indication de la quantité |
| Conditions de remise | `handoverConditions` | Texte libre (plusieurs lignes) | Extension |  |  | Conditions de remise, par exemple retrait au bâtiment source ou au dépôt, démontage par le repreneur, délais |

### Analyse

| Champ | Clé | Format | Niveau | Niveau I | Niveau II | Définition |
| --- | --- | --- | --- | --- | --- | --- |
| Économie de GES par unité | `emissionSavingsPerUnit` | Valeur numérique [kg CO₂-eq] | Extension |  |  | Selon KBOB; il s'agit de l'économie approximative de GES réalisée grâce au réemploi de l'élément par rapport à une fabrication neuve; la méthode devrait être décrite dans le champ «Informations complémentaires sur l'écobilan» |
| Économie de GES | `emissionSavings` | Valeur numérique [kg CO₂-eq] | Extension |  |  | Économie totale de GES pour la quantité indiquée; méthode identique à «Économie de GES par unité» |
| Informations complémentaires sur l'écobilan | `emissionNotes` | Texte libre (plusieurs lignes) | Extension |  |  | Précisions sur le bilan de GES ou indications sur d'autres indicateurs climatiques et environnementaux |

### Autres attributs

| Champ | Clé | Format | Niveau | Niveau I | Niveau II | Définition |
| --- | --- | --- | --- | --- | --- | --- |
| Fabricant | `manufacturer` | Texte libre (une ligne) | Extension |  |  | Nom de l'entreprise qui a fabriqué l'élément |
| Désignation du produit | `productName` | Texte libre (une ligne) | Extension |  |  | Désignation complète du produit ou nom de marque de l'élément |
| Année de pose | `yearOfInstallation` | AAAA | Extension |  |  | Année au cours de laquelle l'élément a été posé dans le bâtiment source |
| Année de fabrication | `yearOfManufacture` | AAAA | Extension |  |  | Année au cours de laquelle l'élément a été fabriqué |
| Couleur | `color` | Texte libre (une ligne) | Extension |  |  | Couleurs pertinentes de l'élément |
| Poids | `weight` | Valeur numérique [kg] | Extension |  |  | Poids par unité choisie pour l'indication de la quantité |
| Exposition aux intempéries | `weatheringExposure` | Texte libre (une ligne) | Extension |  |  | Indique si et dans quelle mesure l'élément a été exposé aux intempéries, par exemple intérieur, extérieur protégé, extérieur exposé |
| Zone dans le bâtiment | `zoneInDonorBuilding` | Texte libre (une ligne) | Extension |  |  | Zone ou secteur du bâtiment source auquel l'élément est attribué |
| Matériau selon KBOB | `materialKbob` | Texte libre (plusieurs lignes) | Extension |  |  | Matériaux de l'élément selon la liste KBOB, avec leur part respective |
| Couleur en HEX | `colorInHex` | Texte libre (une ligne) | Extension |  |  | Couleur de l'élément en valeur hexadécimale, par exemple #A0522D |
| Garantie | `warranty` | Texte libre (plusieurs lignes) | Extension |  |  | Indications sur une garantie accordée pour l'élément réemployé |
| Prix d'origine | `priceOriginal` | Valeur numérique [CHF] | Extension |  |  | Prix à neuf de l'élément en francs suisses, s'il est connu |
| Défauts | `defects` | Texte libre (plusieurs lignes) | Extension |  |  | Défauts ou dommages connus de l'élément |

### Données techniques

| Champ | Clé | Format | Niveau | Niveau I | Niveau II | Définition |
| --- | --- | --- | --- | --- | --- | --- |
| Valeur U | `uValue` | Valeur numérique [W/m²K] | Extension |  |  | Coefficient de transmission thermique de l'élément selon les indications du fabricant ou une mesure |
| Volume utile en litres | `volumeInLiters` | Valeur numérique [l] | Extension |  |  | Volume utile de l'élément en litres, par exemple pour des réservoirs ou des bassins |
| Volume utile en mètres cubes | `volumeInM3` | Valeur numérique [m³] | Extension |  |  | Volume utile de l'élément en mètres cubes, par exemple pour des conteneurs ou des silos |
| Raccordement électrique | `electricConnector` | Texte libre (une ligne) | Extension |  |  | Type de raccordement électrique, par exemple type de fiche ou raccordement fixe |
| Tension électrique | `electricVoltage` | Valeur numérique [V] | Extension |  |  | Tension nominale de l'élément |
| Puissance électrique | `electricWatt` | Valeur numérique [W] | Extension |  |  | Puissance nominale de l'élément |
| Intensité du courant | `electricAmp` | Valeur numérique [A] | Extension |  |  | Courant nominal de l'élément |
| Norme de cuisine | `kitchenNorm` | Texte libre (une ligne) | Extension |  |  | Norme dimensionnelle des éléments de cuisine, par exemple SMS (55 cm) ou EURO (60 cm) |
| Entraxe des trous | `holeSpacing` | Valeur numérique [mm] | Extension |  |  | Distance entre les trous de fixation ou de raccordement, mesurée d'axe en axe |

### Plateforme

| Champ | Clé | Format | Niveau | Niveau I | Niveau II | Définition |
| --- | --- | --- | --- | --- | --- | --- |
| Activé sur la plateforme | `activeOnPlatform` | Oui/Non | Extension |  |  | Indique si l'élément est visible sur la plateforme de placement |
| Offre vedette sur la plateforme | `topOfferOnPlatform` | Oui/Non | Extension |  |  | Indique si l'élément est mis en avant sur la plateforme |
| Mode de paiement | `paymentMethod` | Texte libre (une ligne) | Extension |  |  | Modes de paiement admis, par exemple facture ou paiement anticipé |
| Mode d'expédition | `shippingMethod` | Texte libre (une ligne) | Extension |  |  | Modes de remise ou de livraison possibles, par exemple retrait ou transporteur |
| Stocks réservés | `reservedStock` | Valeur numérique | Extension |  |  | Quantité déjà réservée pour des repreneurs, dans l'unité choisie |

## Champs de données Journal des modifications

### Journal des modifications

| Champ | Clé | Format | Niveau | Définition |
| --- | --- | --- | --- | --- |
| Auteur | `logAuthor` | Texte libre (une ligne) | Extension | Personne qui a créé l'entrée |
| Date | `logDate` | AAAA-MM-JJ | Extension | Date de l'événement |
| Événement | `logEvent` | Texte libre (une ligne) | Extension | Ce qui a été créé ou modifié, par exemple «Audit niveau I établi» |
| Téléphone | `logPhone` | Numéro de téléphone | Extension | Numéro de téléphone de l'auteur |
| E-mail | `logEmail` | Adresse e-mail | Extension | Adresse e-mail de l'auteur |

## Listes de sélection

<a id="list-ebkph"></a>

### eCCC-Bât (sélection de référence) (`ebkph`)

Noyau

Valeurs fictives. Les codes et désignations selon eCCC-Bât SN 506 511 ne figurent pas ici. L'eCCC-Bât ne devrait être indiqué qu'au niveau du groupe d'éléments ou de l'élément.

| Clé | Désignation | Définition |
| --- | --- | --- |
| `XY00` | Empty |  |
| `YZ00` | Empty |  |

<a id="list-unit"></a>

### Unité (`unit`)

Noyau

| Clé | Désignation | Définition |
| --- | --- | --- |
| `pc` | pce | Pièce |
| `m` | ml | Mètre linéaire |
| `m2` | m² | Mètre carré |
| `m3` | m³ | Mètre cube |
| `kg` | kg | Kilogramme |
| `t` | t | Tonne |
| `na` | Aucune indication | Unité inconnue |

<a id="list-material"></a>

### Catégorie de matériau (`material`)

Noyau

| Clé | Désignation | Groupe | Définition |
| --- | --- | --- | --- |
| `me00` | Métal | Métallique |  |
| `me01` | Acier et fonte | Métallique |  |
| `me02` | Aluminium | Métallique |  |
| `me03` | Cuivre | Métallique |  |
| `on00` | Matières végétales et animales | Organique: naturel |  |
| `on01` | Bois massif | Organique: naturel |  |
| `on02` | Matériau dérivé du bois | Organique: naturel |  |
| `os01` | Matière plastique | Organique: synthétique |  |
| `os02` | Bitume | Organique: synthétique |  |
| `mi00` | Matériaux de construction minéraux | Minéral |  |
| `mi01` | Pierre naturelle | Minéral |  |
| `mi02` | Béton et matériaux à base de ciment | Minéral |  |
| `mi03` | Céramique | Minéral |  |
| `mi04` | Plâtre | Minéral |  |
| `mi05` | Verre | Minéral |  |
| `mi06` | Laine minérale | Minéral |  |
| `co01` | Composite | Composite |  |
| `un01` | Inconnu | Inconnu |  |

<a id="list-pollutant-report"></a>

### Diagnostic polluants (`pollutant-report`)

Noyau

| Clé | Désignation | Définition |
| --- | --- | --- |
| `available` | Disponible | Pour l'élément concerné, il existe une évaluation de la pollution par un diagnostic polluants |
| `notAvailable` | Non disponible | Pour l'élément concerné, il n'existe pas d'évaluation de la pollution par un diagnostic polluants |

<a id="list-visual-condition"></a>

### État visuel (`visual-condition`)

Noyau

| Clé | Désignation | Définition |
| --- | --- | --- |
| `0` | Aucune évaluation |  |
| `1` | Comme neuf |  |
| `2` | Légères traces d'usure |  |
| `3` | Fortes traces d'usure |  |
| `4` | Endommagé |  |

<a id="list-functional-condition"></a>

### État fonctionnel (`functional-condition`)

Noyau

| Clé | Désignation | Définition |
| --- | --- | --- |
| `0` | Aucune évaluation |  |
| `1` | Entièrement fonctionnel |  |
| `2` | Fonctionnement limité |  |
| `3` | Défectueux (réparable) |  |
| `4` | Défectueux (irréparable) |  |

<a id="list-demountability"></a>

### Effort de démontage (`demountability`)

Noyau

| Clé | Désignation | Définition |
| --- | --- | --- |
| `0` | Aucune évaluation |  |
| `1` | Très simple |  |
| `2` | Simple |  |
| `3` | Laborieux |  |
| `4` | Très laborieux |  |

<a id="list-rec-detailed-assessment"></a>

### Recommandation relevé détaillé (`rec-detailed-assessment`)

Noyau

| Clé | Désignation | Définition |
| --- | --- | --- |
| `unknown` | Aucune indication | L'auditeur ne formule pas de recommandation |
| `yes` | Oui | L'auditeur de l'audit de réemploi de niveau I recommande un relevé approfondi de l'élément dans l'audit de réemploi de niveau II |
| `no` | Non | L'auditeur de l'audit de réemploi de niveau I ne recommande pas de relevé approfondi de l'élément dans l'audit de réemploi de niveau II |

<a id="list-rec-distribution"></a>

### Recommandation placement (`rec-distribution`)

Noyau

| Clé | Désignation | Définition |
| --- | --- | --- |
| `unknown` | Aucune indication | L'auditeur ne formule pas de recommandation |
| `yes` | Oui | L'auditeur de l'audit de réemploi de niveau II recommande de viser un placement de l'élément |
| `no` | Non | L'auditeur de l'audit de réemploi de niveau II ne recommande pas de viser un placement de l'élément |

<a id="list-gwr-gkat"></a>

### Catégorie de bâtiment (RegBL GKAT) (`gwr-gkat`)

Noyau

Codes et désignations repris tels quels du catalogue des caractères du Registre fédéral des bâtiments et des logements (OFS): allemand et français de la version 5.0.0, italien et anglais de la version 4.3.2.

| Clé | Désignation | Définition |
| --- | --- | --- |
| `1010` | Habitation provisoire |  |
| `1020` | Bâtiment exclusivement à usage d'habitation |  |
| `1030` | Autre bâtiment d'habitation (Bâtiment d'habitation à usage annexe) |  |
| `1040` | Bâtiment partiellement à usage d'habitation |  |
| `1060` | Bâtiment sans usage d'habitation |  |
| `1080` | Construction particulière |  |

<a id="list-gwr-gklas"></a>

### Classe de bâtiment (RegBL GKLAS) (`gwr-gklas`)

Noyau

Codes et désignations repris tels quels du catalogue des caractères du Registre fédéral des bâtiments et des logements (OFS): allemand et français de la version 5.0.0, italien et anglais de la version 4.3.2.

| Clé | Désignation | Définition |
| --- | --- | --- |
| `1110` | Maisons à un logement |  |
| `1121` | Maisons à deux logements |  |
| `1122` | Immeubles à trois logements et plus |  |
| `1130` | Habitat communautaire |  |
| `1211` | Hôtels |  |
| `1212` | Autres bâtiments d'hébergement de tourisme |  |
| `1220` | Immeubles de bureaux |  |
| `1230` | Bâtiments commerciaux |  |
| `1231` | Restaurants et bars dans des bâtiments sans usage résidentiel |  |
| `1241` | Gares, aérogares, centraux téléphoniques |  |
| `1242` | Garages |  |
| `1251` | Bâtiments industriels |  |
| `1252` | Réservoirs, silos et entrepôts |  |
| `1261` | Bâtiments à usage culturel, récréatif, éducatif ou sanitaire |  |
| `1262` | Musées et bibliothèques |  |
| `1263` | Bâtiments pour l'enseignement et la recherche |  |
| `1264` | Hôpitaux et établissements de santé |  |
| `1265` | Salles de sport |  |
| `1272` | Edifices cultuels et religieux |  |
| `1273` | Monuments historiques ou classés |  |
| `1274` | Autres bâtiments non classés ailleurs |  |
| `1275` | Autres bâtiments pour l'hébergement collectif |  |
| `1276` | Bâtiments pour la garde d'animaux |  |
| `1277` | Bâtiments pour la culture végétale |  |
| `1278` | Autres bâtiments d'exploitation agricole |  |

<a id="list-gwr-gbaup"></a>

### Epoque de construction (RegBL GBAUP) (`gwr-gbaup`)

Noyau

Codes et désignations repris tels quels du catalogue des caractères du Registre fédéral des bâtiments et des logements (OFS): allemand et français de la version 5.0.0, italien et anglais de la version 4.3.2.

| Clé | Désignation | Définition |
| --- | --- | --- |
| `8011` | Période avant 1919 |  |
| `8012` | Période de 1919 à 1945 |  |
| `8013` | Période de 1946 à 1960 |  |
| `8014` | Période de 1961 à 1970 |  |
| `8015` | Période de 1971 à 1980 |  |
| `8016` | Période de 1981 à 1985 |  |
| `8017` | Période de 1986 à 1990 |  |
| `8018` | Période de 1991 à 1995 |  |
| `8019` | Période de 1996 à 2000 |  |
| `8020` | Période de 2001 à 2005 |  |
| `8021` | Période de 2006 à 2010 |  |
| `8022` | Période de 2011 à 2015 |  |
| `8023` | Période à partir de 2016 |  |

<a id="list-construction-type"></a>

### Mode de construction (`construction-type`)

Extension

| Clé | Désignation | Définition |
| --- | --- | --- |
| `solidHeavy` | Construction massive lourde |  |
| `solidLight` | Construction massive légère |  |
| `logTimber` | Construction en madriers |  |
| `lightTimber` | Construction légère en bois |  |
| `lightSteel` | Construction légère en acier |  |
| `mixed` | Construction mixte |  |
| `modular` | Construction modulaire |  |

<a id="list-connection"></a>

### Type d'assemblage (`connection`)

Extension

| Clé | Désignation | Définition |
| --- | --- | --- |
| `0` | Aucune indication |  |
| `1` | Posé librement |  |
| `2` | Vissé / Enfiché |  |
| `3` | Cloué / Riveté |  |
| `4` | Fixé à demeure |  |
| `unknown` | Assemblage inconnu |  |
| `screwed` | Vissé |  |
| `nailed` | Cloué |  |
| `glued` | Collé |  |
| `welded` | Soudé |  |
| `riveted` | Riveté |  |
| `interlocked` | Emboîté | p. ex. pour les assemblages en bois |
| `plugged` | Enfiché | p. ex. pour les assemblages en tôle |
| `clamped` | Serré |  |
| `clipped` | Clipsé | p. ex. pour les éléments en plastique |
| `flanged` | Serti | p. ex. pour les raccords de tuyaux |
| `dowelled` | Assemblé à tenon et mortaise | p. ex. assemblages traditionnels en bois |
| `soldered` | Brasé | p. ex. pour les tuyaux métalliques |
| `other` | Autre |  |

<a id="list-reuse-status"></a>

### Statut de réemploi (`reuse-status`)

Extension

| Clé | Désignation | Définition |
| --- | --- | --- |
| `unknown` | Aucune indication |  |
| `installedInDonorBuilding` | En place dans le bâtiment source | L'élément est en place dans le bâtiment source |
| `demounted` | Démonté | L'élément est démonté |
| `stored` | En stock | L'élément est entreposé temporairement dans un dépôt |
| `reused` | Réemployé | L'élément a été réemployé avec succès dans un bâtiment de destination |
| `retainedInPlace` | Maintien en place | L'élément n'est pas réemployé, car il est conservé dans le bâtiment existant |
| `noReuse` | Pas de réemploi | L'élément n'est ni réemployé ni conservé, mais p. ex. recyclé ou éliminé |

<a id="list-ebkp-gate"></a>

### eBKP-Gate (`ebkp-gate`)

Extension

Classification externe; le Swiss Inv ne contient pas de liste de sélection propre.

## Formats

| Clé | Désignation |
| --- | --- |
| `text` | Texte libre (une ligne) |
| `multiline` | Texte libre (plusieurs lignes) |
| `number` | Valeur numérique |
| `boolean` | Oui/Non |
| `code` | Liste de sélection / Liste de sélection (choix multiple) |
| `contact` | Contact |
| `country` | Code pays selon ISO 3166 |
| `phone` | Numéro de téléphone |
| `email` | Adresse e-mail |
| `uuid` | UUID |
| `year` | AAAA |
| `date` | AAAA-MM-JJ |
| `postalCode` | Code postal |

## Obligation

| Clé | Désignation |
| --- | --- |
| `muss` | Obligatoire |
| `sollte` | Recommandé |

## Unités

| Symbole | Désignation |
| --- | --- |
| mm | Millimètre |
| cm | Centimètre |
| m² | Mètre carré |
| m³ | Mètre cube |
| l | Litre |
| kg | Kilogramme |
| kg CO₂-eq | Kilogramme d'équivalent CO₂ |
| CHF | Franc suisse |
| W/m²K | Watt par mètre carré-kelvin |
| V | Volt |
| W | Watt |
| A | Ampère |
