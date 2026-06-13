---
entity_id: "reaction.ecocyc.IGPSYN-RXN"
entity_type: "reaction"
name: "IGPSYN-RXN"
source_database: "EcoCyc"
source_id: "IGPSYN-RXN"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# IGPSYN-RXN

`reaction.ecocyc.IGPSYN-RXN`

## Static

- Type: `reaction`
- Source: `EcoCyc:IGPSYN-RXN`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

this is the fourth reaction in the tryptophan synthesis pathway EcoCyc reaction equation: PROTON + CARBOXYPHENYLAMINO-DEOXYRIBULOSE-P -> INDOLE-3-GLYCEROL-P + CARBON-DIOXIDE + WATER; direction=LEFT-TO-RIGHT. this is the fourth reaction in the tryptophan synthesis pathway

## Biological Role

Catalyzed by trpC (protein.P00909). Substrates: H+ (molecule.C00080), 1-(2-Carboxyphenylamino)-1-deoxy-D-ribulose 5-phosphate (molecule.C01302). Products: H2O (molecule.C00001), CO2 (molecule.C00011), Indoleglycerol phosphate (molecule.C03506).

## Enriched Pathways

- `ecocyc.TRPSYN-PWY` L-tryptophan biosynthesis (EcoCyc)

## Annotation

this is the fourth reaction in the tryptophan synthesis pathway

## Pathways

- `ecocyc.TRPSYN-PWY` L-tryptophan biosynthesis (EcoCyc)

## Outgoing Edges (0)

_None._

## Incoming Edges (12)

- `catalyzes` <-- [[protein.P00909|protein.P00909]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00001|molecule.C00001]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00011|molecule.C00011]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C03506|molecule.C03506]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C01302|molecule.C01302]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `represses` <-- [[molecule.C00108|molecule.C00108]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.ecocyc.CPD0-1486|molecule.ecocyc.CPD0-1486]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.ecocyc.CPD0-1487|molecule.ecocyc.CPD0-1487]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.ecocyc.CPD0-1488|molecule.ecocyc.CPD0-1488]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.ecocyc.CPD0-1489|molecule.ecocyc.CPD0-1489]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.ecocyc.CPD0-1490|molecule.ecocyc.CPD0-1490]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity

## External IDs

- `EcoCyc:IGPSYN-RXN`

## Notes

PROTON + CARBOXYPHENYLAMINO-DEOXYRIBULOSE-P -> INDOLE-3-GLYCEROL-P + CARBON-DIOXIDE + WATER; direction=LEFT-TO-RIGHT
