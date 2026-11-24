<!-- Automatisch erzeugt von tools/build.py - nicht von Hand bearbeiten. -->

# Swiss Inv data dictionary

[Deutsch](DE.md) · [Français](FR.md) · [Italiano](IT.md) · **English**

Version: `2.0.0-draft`

**Core** = stable, changes only with a new edition of the standard. **Extension** = optional data fields that grow through proposals.

## Data fields Project

### Identification

| Data field | Key | Format | Layer | Stage I | Stage II | Definition |
| --- | --- | --- | --- | --- | --- | --- |
| Project name | `projectName` | Free text (single line) | Core | Must | Must | Name of the project under which one or more donor buildings are grouped |
| Project ID | `projectId` | Free text (single line) | Core |  |  | Identifier of the project; format and assignment of the ID are not prescribed by Swiss Inv |

### Project participants

| Data field | Key | Format | Layer | Stage I | Stage II | Definition |
| --- | --- | --- | --- | --- | --- | --- |
| Owner | `projectOwner` | Contact | Core | Must | Must | Owner of the donor buildings concerned |
| Planner | `projectPlanner` | Contact | Core |  |  | Planner of the conversion or deconstruction |
| Client | `projectAuditClient` | Contact | Core | Must | Must | Client commissioning the reuse audit |
| Auditor | `projectAuditor` | Contact | Core | Must | Must | Contractor carrying out the reuse audit |

## Data fields Contacts

### Contact person

| Data field | Key | Format | Layer | Definition |
| --- | --- | --- | --- | --- |
| Name | `contactName` | Free text (single line) | Core | First and last name of the contact person |
| Project role | `contactRole` | Free text (single line) | Core | Role or function of the contact person in the project |

### Address

| Data field | Key | Format | Layer | Definition |
| --- | --- | --- | --- | --- |
| Company | `contactCompany` | Free text (multi-line) | Core | Name of the company or organisation |
| Street | `contactStreet` | Free text (single line) | Core | Street name of the address of the contact person |
| House number | `contactHouseNumber` | Free text (single line) | Core | House number of the address of the contact person |
| Postal code | `contactPostalCode` | Postal code | Core | Postal code of the address of the contact person |
| City | `contactCity` | Free text (single line) | Core | Town or city of the address of the contact person |
| Country | `contactCountry` | Country code according to ISO 3166 | Core | Country of the address of the contact person as a two-letter country code according to ISO 3166-1 (e.g. CH) |

### Contact details

| Data field | Key | Format | Layer | Definition |
| --- | --- | --- | --- | --- |
| Phone | `contactPhone` | Telephone number | Core | Telephone number of the contact person, in international format with country code where possible |
| Email | `contactEmail` | Email address | Core | Email address of the contact person |

## Data fields Donor buildings

### Address

| Data field | Key | Format | Layer | Stage I | Stage II | Definition |
| --- | --- | --- | --- | --- | --- | --- |
| EGID | `donorBuildingEgid` | Free text (single line) | Core |  | Must | Federal building identifier: building identifier in the Federal RBD. Source: GWR catalogue of attributes 5.0, attribute EGID. |
| EGRID | `donorBuildingEgrid` | Free text (single line) | Core |  | Must | Federal identifier (E-GRID) of the parcel of land, object of the real property, on which the building is situated. Source: GWR catalogue of attributes 5.0, attribute GEGRID. |
| Street | `donorBuildingStreet` | Free text (single line) | Core | Must | Must | Street name of the address of the donor building |
| House number | `donorBuildingHouseNumber` | Free text (single line) | Core | Must | Must | House number of the address of the donor building |
| Postal code | `donorBuildingPostalCode` | Postal code | Core | Must | Must | Postal code of the address of the donor building |
| City | `donorBuildingCity` | Free text (single line) | Core | Must | Must | Town or city of the address of the donor building |
| Country | `donorBuildingCountry` | Country code according to ISO 3166 | Core | Should | Should | Country of the address of the donor building as a two-letter country code according to ISO 3166-1 (e.g. CH) |

### Building data

| Data field | Key | Format | Layer | Stage I | Stage II | Definition |
| --- | --- | --- | --- | --- | --- | --- |
| Building class | `donorBuildingGklas` | Code list → [gwr-gklas](#list-gwr-gklas) | Core | Should | Should | Break down of buildings according to Eurostat classification. Source: GWR catalogue of attributes 5.0, attribute GKLAS. |
| Building category | `donorBuildingGkat` | Code list → [gwr-gkat](#list-gwr-gkat) | Core | Should | Should | Subdivision of buildings according to purpose. Source: GWR catalogue of attributes 5.0, attribute GKAT. |
| Period of construction | `donorBuildingGbaup` | Code list → [gwr-gbaup](#list-gwr-gbaup) | Core | Should | Should | Information on the period of completion of the building. Source: GWR catalogue of attributes 5.0, attribute GBAUP. |
| Construction type | `donorBuildingConstructionType` | Code list → [construction-type](#list-construction-type) | Core | Should | Should | Predominant construction type or load-bearing structure of the building, for example solid, frame or timber construction |
| Year of construction of the building | `donorBuildingGbauj` | YYYY | Core | Should | Should | Information on the year of completion of the building. Source: GWR catalogue of attributes 5.0, attribute GBAUJ. |
| Building volume | `donorBuildingGvol` | Number [m³] | Core | Should | Should | Information on the volume of the building. Source: GWR catalogue of attributes 5.0, attribute GVOL. |
| Surface area of building (floor area) | `donorBuildingGarea` | Number [m²] | Core | Should | Should | Building surface area in square metres. Source: GWR catalogue of attributes 5.0, attribute GAREA. |
| Number of floors | `donorBuildingGastw` | Number | Core | Should | Should | Number of floors and basements, including ground floor. Source: GWR catalogue of attributes 5.0, attribute GASTW. |
| Construction date | `donorBuildingConstructionDate` | YYYY-MM-DD | Extension |  |  | Date of completion of the building, where known more precisely than the year of construction |

### Details

| Data field | Key | Format | Layer | Stage I | Stage II | Definition |
| --- | --- | --- | --- | --- | --- | --- |
| Previous renovations | `donorBuildingPreviousRenovations` | Free text (multi-line) | Core |  |  | Known earlier conversions, refurbishments or extensions of the building, with the year where possible |
| Access | `donorBuildingAccess` | Free text (multi-line) | Core |  | Must | Accessibility of the building for dismantling and removal, for example vehicle access, lift, crane position |
| Further information | `donorBuildingDetails` | Free text (multi-line) | Core |  |  | Further relevant information on the donor building not covered by the other data fields |
| Exceptional events | `donorBuildingSpecialEvents` | Free text (multi-line) | Extension |  |  | Exceptional events that may have affected the condition of the components, for example fire, water damage or a long vacancy |
| Year of last renovation | `donorBuildingLastRenovationYear` | YYYY | Extension |  |  | Year in which the building was last converted or refurbished |
| Dismantling from | `donorBuildingDismantlingStartDate` | YYYY-MM-DD | Extension |  |  | Date from which components can be dismantled in the donor building |
| Dismantling until | `donorBuildingDismantlingEndDate` | YYYY-MM-DD | Extension |  |  | Date by which dismantling of the components must be completed |
| Attachments | `donorBuildingAttachments` | Free text (multi-line) | Extension |  |  | Name and storage location of documents on the donor building, for example plans or the pollutant report |

## Data fields Reuse components

### Identification

| Data field | Key | Format | Layer | Stage I | Stage II | Definition |
| --- | --- | --- | --- | --- | --- | --- |
| Name | `name` | Free text (single line) | Core | Must | Must | Short name |
| Component ID | `componentId` | Free text (single line) | Core |  | Must | Number identifying the DPP; format and assignment of the ID are not prescribed by Swiss Inv |
| eBKP-H code | `ebkphCode` | Code list → [ebkph](#list-ebkph) | Core | Must | Must | According to eBKP-H SN 506 511; code and label are to be given in separate data fields; a selection of possible codes is listed in the eBKP-H reference table |
| eBKP-H label | `ebkphLabel` | Free text (single line) | Core | Must | Must | Label belonging to the eBKP-H code; code and label are to be given in separate data fields |
| Position in donor building | `positionInDonorBuilding` | Free text (multi-line) | Core |  | Should | Description of the position in the donor building, for example floor, room, etc. |
| UUID | `uuid` | UUID | Extension |  |  | according to ISO/IEC 9834-8:2014; ensures globally unique identification |
| UUID of the master item | `parentUuid` | UUID | Extension |  |  | Indicates that the component belongs to a higher-level overall item |
| eBKP-Gate code | `ebkpGateCode` | Code list → [ebkp-gate](#list-ebkp-gate) | Extension |  |  | According to eBKP-Gate; code and label are to be given in separate data fields |
| eBKP-Gate label | `ebkpGateLabel` | Free text (single line) | Extension |  |  | Label belonging to the eBKP-Gate code; code and label are to be given in separate data fields |

### Quantity

| Data field | Key | Format | Layer | Stage I | Stage II | Definition |
| --- | --- | --- | --- | --- | --- | --- |
| Quantity (min) | `quantityMin` | Number | Core | Must | Must | The quantity may deliberately be given as a range with a lower and an upper limit; for a precise figure enter the same value in both fields |
| Quantity (max) | `quantityMax` | Number | Core | Must | Must | The quantity may deliberately be given as a range with a lower and an upper limit; for a precise figure enter the same value in both fields |
| Unit | `unit` | Code list → [unit](#list-unit) | Core | Must | Must | A unit suitable for placing the components with takers is recommended |
| Quantity notes | `quantityNotes` | Free text (multi-line) | Extension |  |  | Additional information on the quantity, for example further reference quantities |

### Dimensions

| Data field | Key | Format | Layer | Stage I | Stage II | Definition |
| --- | --- | --- | --- | --- | --- | --- |
| Outer dimension height | `zDim` | Number [cm] | Core |  | Must | The three outer dimensions are intended to standardise how dimensions are given for as many component shapes as possible; they follow the bounding box of the buildingSMART IFC standard |
| Outer dimension width | `yDim` | Number [cm] | Core |  | Must | The three outer dimensions are intended to standardise how dimensions are given for as many component shapes as possible; they follow the bounding box of the buildingSMART IFC standard |
| Outer dimension depth / length | `xDim` | Number [cm] | Core |  | Must | The three outer dimensions are intended to standardise how dimensions are given for as many component shapes as possible; they follow the bounding box of the buildingSMART IFC standard |
| Free dimension details | `dimensionNotes` | Free text (multi-line) | Core |  | Must | Relevant dimensions not covered by the outer dimensions or other attributes |

### Details

| Data field | Key | Format | Layer | Stage I | Stage II | Definition |
| --- | --- | --- | --- | --- | --- | --- |
| Further information | `description` | Free text (multi-line) | Core | Should | Should | Description of relevant properties not covered by the outer dimensions or other attributes |
| Material category | `material` | Code list (multiple choice) → [material](#list-material) | Core | Must | Must | Material categories the component mainly consists of; several can be chosen, for example solid wood for the frame and glass for the glazing of a timber window |
| Material notes | `materialNotes` | Free text (multi-line) | Core |  | Must | Details on the material not covered by the material category |

### Assessment

| Data field | Key | Format | Layer | Stage I | Stage II | Definition |
| --- | --- | --- | --- | --- | --- | --- |
| Pollutant report | `pollutantReport` | Code list → [pollutant-report](#list-pollutant-report) | Core |  | Must | States whether an assessment of contamination by a pollutant report exists for the component |
| Visual condition | `visualCondition` | Code list → [visual-condition](#list-visual-condition) | Core |  | Must | Any remarks on the visual condition can be added in the data field «Explanation of the recommendation» |
| Functional condition | `functionalCondition` | Code list → [functional-condition](#list-functional-condition) | Core |  | Must | Any remarks on the functional condition can be added in the data field «Explanation of the recommendation» |
| Dismantling effort | `demountability` | Code list → [demountability](#list-demountability) | Core |  | Must | Any remarks on the dismantling effort can be added in the data field «Explanation of the recommendation» |
| Recommendation detailed survey | `recDetailedAssessment` | Code list → [rec-detailed-assessment](#list-rec-detailed-assessment) | Core | Must |  | The auditor of the reuse audit stage I recommends whether an in-depth survey of the component should be carried out in the reuse audit stage II |
| Recommendation placement | `recDistribution` | Code list → [rec-distribution](#list-rec-distribution) | Core |  | Must | The auditor of the reuse audit stage II recommends whether placement of the component should be sought |
| Explanation of the recommendation | `recNotes` | Free text (multi-line) | Core |  | Should | Any remarks on the assessment and on the recommendation to place the component |
| Pollutant notes | `pollutantNotes` | Free text (multi-line) | Extension |  |  | Further details on the pollutant report, for example author, date, and type and degree of contamination |
| Connection type | `connection` | Code list (multiple choice) → [connection](#list-connection) | Extension |  |  | All connections relevant to dismantling or installing the component; additional information not covered by the selection list can be added as free text in the data field «Connection notes» |
| Connection notes | `connectionNotes` | Free text (multi-line) | Extension |  |  | Additional information on the connection not covered by the selection list |

### Logistics

| Data field | Key | Format | Layer | Stage I | Stage II | Definition |
| --- | --- | --- | --- | --- | --- | --- |
| Reuse status | `reUseStatus` | Code list → [reuse-status](#list-reuse-status) | Extension |  |  | Current state of the component in the reuse process |
| Postal code of location | `locationPostalCode` | Postal code | Extension |  |  | Postal code of the current location of the component |
| Country of location | `locationCountry` | Country code according to ISO 3166 | Extension |  |  | Country of the current location of the component as a two-letter country code according to ISO 3166-1 (e.g. CH) |
| Storage start date | `storageStartDate` | YYYY-MM-DD | Extension |  |  | Date on which the component was put into storage |
| Storage end date | `storageEndDate` | YYYY-MM-DD | Extension |  |  | Date on which the component left storage or must leave it at the latest |
| Logistics notes | `logisticsNotes` | Free text (multi-line) | Extension |  |  | Additional information on storage, packaging and transport of the component |

### Terms

| Data field | Key | Format | Layer | Stage I | Stage II | Definition |
| --- | --- | --- | --- | --- | --- | --- |
| Availability start date | `availabilityStartDate` | YYYY-MM-DD | Extension |  |  | Date from which the component is available to takers |
| Availability end date | `availabilityEndDate` | YYYY-MM-DD | Extension |  |  | Date until which the component is available to takers |
| Selling price | `price` | Number [CHF] | Extension |  |  | Selling price in Swiss francs per unit chosen for the quantity |
| Handover conditions | `handoverConditions` | Free text (multi-line) | Extension |  |  | Terms of handover, for example collection from the donor building or warehouse, dismantling by the taker, deadlines |

### Analysis

| Data field | Key | Format | Layer | Stage I | Stage II | Definition |
| --- | --- | --- | --- | --- | --- | --- |
| GHG savings per unit | `emissionSavingsPerUnit` | Number [kg CO₂-eq] | Extension |  |  | According to KBOB; the approximate GHG savings from reusing the component compared with new production; the method should be described in the data field «Life cycle assessment notes» |
| GHG savings | `emissionSavings` | Number [kg CO₂-eq] | Extension |  |  | Total GHG savings for the quantity given; method as for «GHG savings per unit» |
| Life cycle assessment notes | `emissionNotes` | Free text (multi-line) | Extension |  |  | Remarks on the GHG balance or details of further climate and environmental indicators |

### Further attributes

| Data field | Key | Format | Layer | Stage I | Stage II | Definition |
| --- | --- | --- | --- | --- | --- | --- |
| Manufacturer | `manufacturer` | Free text (single line) | Extension |  |  | Name of the company that manufactured the component |
| Product name | `productName` | Free text (single line) | Extension |  |  | Full product name or brand name of the component |
| Year of installation | `yearOfInstallation` | YYYY | Extension |  |  | Year in which the component was installed in the donor building |
| Year of manufacture | `yearOfManufacture` | YYYY | Extension |  |  | Year in which the component was manufactured |
| Colour | `color` | Free text (single line) | Extension |  |  | Relevant colours of the component |
| Weight | `weight` | Number [kg] | Extension |  |  | Weight per unit chosen for the quantity |
| Weathering exposure | `weatheringExposure` | Free text (single line) | Extension |  |  | States whether and how strongly the component was exposed to the weather, for example indoors, outdoors sheltered, outdoors fully exposed |
| Zone in building | `zoneInDonorBuilding` | Free text (single line) | Extension |  |  | Zone or area of the donor building to which the component is assigned |
| Material according to KBOB | `materialKbob` | Free text (multi-line) | Extension |  |  | Materials of the component according to the KBOB list, with their respective shares |
| Colour as HEX | `colorInHex` | Free text (single line) | Extension |  |  | Colour of the component as a hexadecimal value, for example #A0522D |
| Warranty | `warranty` | Free text (multi-line) | Extension |  |  | Details of any warranty or guarantee given on the reused component |
| Original price | `priceOriginal` | Number [CHF] | Extension |  |  | Price of the component when new, in Swiss francs, where known |
| Defects | `defects` | Free text (multi-line) | Extension |  |  | Known defects of or damage to the component |

### Technical data

| Data field | Key | Format | Layer | Stage I | Stage II | Definition |
| --- | --- | --- | --- | --- | --- | --- |
| U-value | `uValue` | Number [W/m²K] | Extension |  |  | Thermal transmittance of the component according to the manufacturer or a measurement |
| Usable volume in litres | `volumeInLiters` | Number [l] | Extension |  |  | Usable volume of the component in litres, for example for tanks or basins |
| Usable volume in cubic metres | `volumeInM3` | Number [m³] | Extension |  |  | Usable volume of the component in cubic metres, for example for containers or silos |
| Electrical connection | `electricConnector` | Free text (single line) | Extension |  |  | Type of electrical connection, for example plug type or fixed connection |
| Voltage | `electricVoltage` | Number [V] | Extension |  |  | Rated voltage of the component |
| Electrical power | `electricWatt` | Number [W] | Extension |  |  | Rated power of the component |
| Current | `electricAmp` | Number [A] | Extension |  |  | Rated current of the component |
| Kitchen standard | `kitchenNorm` | Free text (single line) | Extension |  |  | Dimensional standard to which kitchen units are built, for example SMS (55 cm) or EURO (60 cm) |
| Hole spacing | `holeSpacing` | Number [mm] | Extension |  |  | Distance between fixing or connection holes, measured centre to centre |

### Platform

| Data field | Key | Format | Layer | Stage I | Stage II | Definition |
| --- | --- | --- | --- | --- | --- | --- |
| Active on platform | `activeOnPlatform` | Yes/No | Extension |  |  | States whether the component is visible on the placement platform |
| Top offer on platform | `topOfferOnPlatform` | Yes/No | Extension |  |  | States whether the component is featured on the platform |
| Payment method | `paymentMethod` | Free text (single line) | Extension |  |  | Accepted payment methods, for example invoice or advance payment |
| Shipping method | `shippingMethod` | Free text (single line) | Extension |  |  | Possible ways of handover or delivery, for example collection or haulier |
| Reserved stock | `reservedStock` | Number | Extension |  |  | Quantity already reserved for takers, in the chosen unit |

## Data fields Change log

### Change log

| Data field | Key | Format | Layer | Definition |
| --- | --- | --- | --- | --- |
| Author | `logAuthor` | Free text (single line) | Extension | Person who made the entry |
| Date | `logDate` | YYYY-MM-DD | Extension | Date of the event |
| Event | `logEvent` | Free text (single line) | Extension | What was created or changed, for example «Audit stage I completed» |
| Phone | `logPhone` | Telephone number | Extension | Telephone number of the author |
| Email | `logEmail` | Email address | Extension | Email address of the author |

## Code lists

<a id="list-ebkph"></a>

### eBKP-H (reference selection) (`ebkph`)

Core

Placeholders. The codes and labels according to eBKP-H SN 506 511 are not held here. eBKP-H should only be given at the level of element group or element.

| Key | Label | Definition |
| --- | --- | --- |
| `XY00` | Empty |  |
| `YZ00` | Empty |  |

<a id="list-unit"></a>

### Unit (`unit`)

Core

| Key | Label | Definition |
| --- | --- | --- |
| `pc` | pcs | Piece |
| `m` | lin. m | Linear metre |
| `m2` | m² | Square metre |
| `m3` | m³ | Cubic metre |
| `kg` | kg | Kilogram |
| `t` | t | Tonne |
| `na` | Not specified | Unit not known |

<a id="list-material"></a>

### Material category (`material`)

Core

| Key | Label | Group | Definition |
| --- | --- | --- | --- |
| `me00` | Metal | Metallic |  |
| `me01` | Steel and cast iron | Metallic |  |
| `me02` | Aluminium | Metallic |  |
| `me03` | Copper | Metallic |  |
| `on00` | Plant and animal materials | Organic: natural |  |
| `on01` | Solid wood | Organic: natural |  |
| `on02` | Wood-based material | Organic: natural |  |
| `os01` | Plastic | Organic: synthetic |  |
| `os02` | Bitumen | Organic: synthetic |  |
| `mi00` | Mineral building materials | Mineral |  |
| `mi01` | Natural stone | Mineral |  |
| `mi02` | Concrete and cement-bound materials | Mineral |  |
| `mi03` | Ceramics | Mineral |  |
| `mi04` | Gypsum | Mineral |  |
| `mi05` | Glass | Mineral |  |
| `mi06` | Mineral wool | Mineral |  |
| `co01` | Composite | Composite |  |
| `un01` | Unknown | Unknown |  |

<a id="list-pollutant-report"></a>

### Pollutant report (`pollutant-report`)

Core

| Key | Label | Definition |
| --- | --- | --- |
| `available` | Available | For the component concerned, there is an assessment of contamination by a pollutant report |
| `notAvailable` | Not available | For the component concerned, there is no assessment of contamination by a pollutant report |

<a id="list-visual-condition"></a>

### Visual condition (`visual-condition`)

Core

| Key | Label | Definition |
| --- | --- | --- |
| `0` | No assessment |  |
| `1` | As new |  |
| `2` | Light signs of use |  |
| `3` | Heavy signs of use |  |
| `4` | Damaged |  |

<a id="list-functional-condition"></a>

### Functional condition (`functional-condition`)

Core

| Key | Label | Definition |
| --- | --- | --- |
| `0` | No assessment |  |
| `1` | Fully functional |  |
| `2` | Limited function |  |
| `3` | Defective (repairable) |  |
| `4` | Defective (beyond repair) |  |

<a id="list-demountability"></a>

### Dismantling effort (`demountability`)

Core

| Key | Label | Definition |
| --- | --- | --- |
| `0` | No assessment |  |
| `1` | Very easy |  |
| `2` | Easy |  |
| `3` | Laborious |  |
| `4` | Very laborious |  |

<a id="list-rec-detailed-assessment"></a>

### Recommendation detailed survey (`rec-detailed-assessment`)

Core

| Key | Label | Definition |
| --- | --- | --- |
| `unknown` | Not specified | The auditor makes no recommendation |
| `yes` | Yes | The auditor of the reuse audit stage I recommends an in-depth survey of the component in the reuse audit stage II |
| `no` | No | The auditor of the reuse audit stage I does not recommend an in-depth survey of the component in the reuse audit stage II |

<a id="list-rec-distribution"></a>

### Recommendation placement (`rec-distribution`)

Core

| Key | Label | Definition |
| --- | --- | --- |
| `unknown` | Not specified | The auditor makes no recommendation |
| `yes` | Yes | The auditor of the reuse audit stage II recommends seeking to place the component |
| `no` | No | The auditor of the reuse audit stage II does not recommend seeking to place the component |

<a id="list-gwr-gkat"></a>

### Building category (RBD GKAT) (`gwr-gkat`)

Core

Codes and labels taken verbatim from the catalogue of attributes of the Federal Register of Buildings and Dwellings (FSO): German and French from version 5.0.0, Italian and English from version 4.3.2.

| Key | Label | Definition |
| --- | --- | --- |
| `1010` | Temporary accommodation |  |
| `1020` | Building for residential use only |  |
| `1030` | Other residential building (wit subsidiary use) |  |
| `1040` | Building with partial residential use |  |
| `1060` | Non-residential building |  |
| `1080` | Special construction |  |

<a id="list-gwr-gklas"></a>

### Building class (RBD GKLAS) (`gwr-gklas`)

Core

Codes and labels taken verbatim from the catalogue of attributes of the Federal Register of Buildings and Dwellings (FSO): German and French from version 5.0.0, Italian and English from version 4.3.2.

| Key | Label | Definition |
| --- | --- | --- |
| `1110` | Single-dwelling buildings |  |
| `1121` | Two-dwelling buildings |  |
| `1122` | Three- and more dwelling building |  |
| `1130` | Community residence |  |
| `1211` | Hotels |  |
| `1212` | Other short-stay accommodation buildings |  |
| `1220` | Office buildings |  |
| `1230` | Wholesale and retail trade buildings |  |
| `1231` | Restaurants and bars in non-residential buildings |  |
| `1241` | Rail stations, air terminals, telephone exchange buildings |  |
| `1242` | Garage buildings |  |
| `1251` | Industrial buildings |  |
| `1252` | Reservoirs, silos and warehouses |  |
| `1261` | Buildings for cultural, recreational, educational or health purposes |  |
| `1262` | Museums and libraries |  |
| `1263` | School, university and research buildings |  |
| `1264` | Hospital or institutional care buildings |  |
| `1265` | Sports halls |  |
| `1272` | Buildings used as places of worship and for religious activities |  |
| `1273` | Historic or protected monuments |  |
| `1274` | Other buildings not elsewhere classified |  |
| `1275` | Other buildings for collective households |  |
| `1276` | Buildings for keeping animals |  |
| `1277` | Buildings for growing crops |  |
| `1278` | Other agricultural buildings |  |

<a id="list-gwr-gbaup"></a>

### Period of construction (RBD GBAUP) (`gwr-gbaup`)

Core

Codes and labels taken verbatim from the catalogue of attributes of the Federal Register of Buildings and Dwellings (FSO): German and French from version 5.0.0, Italian and English from version 4.3.2.

| Key | Label | Definition |
| --- | --- | --- |
| `8011` | Period before 1919 |  |
| `8012` | Period from 1919 to 1945 |  |
| `8013` | Period from 1946 to 1960 |  |
| `8014` | Period from 1961 to 1970 |  |
| `8015` | Period from 1971 to 1980 |  |
| `8016` | Period from 1981 to 1985 |  |
| `8017` | Period from 1986 to 1990 |  |
| `8018` | Period from 1991 to 1995 |  |
| `8019` | Period from 1996 to 2000 |  |
| `8020` | Period from 2001 to 2005 |  |
| `8021` | Period from 2006 to 2010 |  |
| `8022` | Period from 2011 to 2015 |  |
| `8023` | Period from 2016 onwards |  |

<a id="list-construction-type"></a>

### Construction type (`construction-type`)

Extension

| Key | Label | Definition |
| --- | --- | --- |
| `solidHeavy` | Solid construction, heavy |  |
| `solidLight` | Solid construction, light |  |
| `logTimber` | Log construction |  |
| `lightTimber` | Lightweight timber construction |  |
| `lightSteel` | Lightweight steel construction |  |
| `mixed` | Mixed construction |  |
| `modular` | Modular construction |  |

<a id="list-connection"></a>

### Connection type (`connection`)

Extension

| Key | Label | Definition |
| --- | --- | --- |
| `0` | Not specified |  |
| `1` | Loose |  |
| `2` | Screwed / Plugged |  |
| `3` | Nailed / Riveted |  |
| `4` | Permanently fixed |  |
| `unknown` | Connection unknown |  |
| `screwed` | Screwed |  |
| `nailed` | Nailed |  |
| `glued` | Glued |  |
| `welded` | Welded |  |
| `riveted` | Riveted |  |
| `interlocked` | Interlocked | e.g. in timber joints |
| `plugged` | Plugged | e.g. in sheet-metal joints |
| `clamped` | Clamped |  |
| `clipped` | Clipped | e.g. for plastic elements |
| `flanged` | Flanged | e.g. in pipe joints |
| `dowelled` | Mortise and tenon | e.g. traditional timber joints |
| `soldered` | Soldered | e.g. for metal pipes |
| `other` | Other |  |

<a id="list-reuse-status"></a>

### Reuse status (`reuse-status`)

Extension

| Key | Label | Definition |
| --- | --- | --- |
| `unknown` | Not specified |  |
| `installedInDonorBuilding` | Installed in donor building | The component is installed in the donor building |
| `demounted` | Dismantled | The component has been dismantled |
| `stored` | In storage | The component is held temporarily in a warehouse |
| `reused` | Reused | The component has been successfully reused in a target building |
| `retainedInPlace` | Retained in place | The component is not reused because it is retained in the existing building |
| `noReuse` | No reuse | The component is neither reused nor retained but, for example, recycled or disposed of |

<a id="list-ebkp-gate"></a>

### eBKP-Gate (`ebkp-gate`)

Extension

External classification; Swiss Inv does not hold its own selection list.

## Formats

| Key | Label |
| --- | --- |
| `text` | Free text (single line) |
| `multiline` | Free text (multi-line) |
| `number` | Number |
| `boolean` | Yes/No |
| `code` | Code list / Code list (multiple choice) |
| `contact` | Contact |
| `country` | Country code according to ISO 3166 |
| `phone` | Telephone number |
| `email` | Email address |
| `uuid` | UUID |
| `year` | YYYY |
| `date` | YYYY-MM-DD |
| `postalCode` | Postal code |

## Obligation

| Key | Label |
| --- | --- |
| `muss` | Must |
| `sollte` | Should |

## Units

| Symbol | Label |
| --- | --- |
| mm | Millimetre |
| cm | Centimetre |
| m² | Square metre |
| m³ | Cubic metre |
| l | Litre |
| kg | Kilogram |
| kg CO₂-eq | Kilogram of CO₂ equivalent |
| CHF | Swiss franc |
| W/m²K | Watt per square metre kelvin |
| V | Volt |
| W | Watt |
| A | Ampere |
