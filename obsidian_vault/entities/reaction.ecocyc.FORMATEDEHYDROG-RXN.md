---
entity_id: "reaction.ecocyc.FORMATEDEHYDROG-RXN"
entity_type: "reaction"
name: "formate dehydrogenase (menaquinone)"
source_database: "EcoCyc"
source_id: "FORMATEDEHYDROG-RXN"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: "CCO-PM-BAC-NEG"
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# formate dehydrogenase (menaquinone)

`reaction.ecocyc.FORMATEDEHYDROG-RXN`

## Static

- Type: `reaction`
- Source: `EcoCyc:FORMATEDEHYDROG-RXN`
- Default state: `active`
- Allowed states: `active|blocked`
- Location: CCO-PM-BAC-NEG

## Enriched Summary

This is the first step in the metabolism of formate under anaerobic conditions. EcoCyc reaction equation: FORMATE + PROTON + Menaquinones -> PROTON + CARBON-DIOXIDE + Menaquinols; direction=PHYSIOL-LEFT-TO-RIGHT. This is the first step in the metabolism of formate under anaerobic conditions.

## Biological Role

Catalyzed by formate dehydrogenase O (complex.ecocyc.CPLX0-13310), formate dehydrogenase N (complex.ecocyc.FORMATEDEHYDROGN-CPLX). Substrates: Formate (molecule.C00058), H+ (molecule.C00080), Menaquinone (molecule.C00828). Products: CO2 (molecule.C00011), H+ (molecule.C00080), Menaquinol (molecule.C05819).

## Enriched Pathways

- `ecocyc.PWY0-1321` nitrate reduction III (dissimilatory) (EcoCyc)
- `ecocyc.PWY0-1355` formate to trimethylamine N-oxide electron transfer (EcoCyc)
- `ecocyc.PWY0-1356` formate to dimethyl sulfoxide electron transfer (EcoCyc)
- `ecocyc.PWY0-1585` formate to nitrite electron transfer (EcoCyc)

## Annotation

This is the first step in the metabolism of formate under anaerobic conditions.

## Pathways

- `ecocyc.PWY0-1321` nitrate reduction III (dissimilatory) (EcoCyc)
- `ecocyc.PWY0-1355` formate to trimethylamine N-oxide electron transfer (EcoCyc)
- `ecocyc.PWY0-1356` formate to dimethyl sulfoxide electron transfer (EcoCyc)
- `ecocyc.PWY0-1585` formate to nitrite electron transfer (EcoCyc)

## Outgoing Edges (0)

_None._

## Incoming Edges (13)

- `catalyzes` <-- [[complex.ecocyc.CPLX0-13310|complex.ecocyc.CPLX0-13310]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` <-- [[complex.ecocyc.FORMATEDEHYDROGN-CPLX|complex.ecocyc.FORMATEDEHYDROGN-CPLX]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00011|molecule.C00011]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C05819|molecule.C05819]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00058|molecule.C00058]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C00828|molecule.C00828]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `represses` <-- [[molecule.C00007|molecule.C00007]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.C01326|molecule.C01326]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.ecocyc.CPD-2841|molecule.ecocyc.CPD-2841]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.ecocyc.IODOACETAMIDE|molecule.ecocyc.IODOACETAMIDE]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.ecocyc.PHMB|molecule.ecocyc.PHMB]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity

## External IDs

- `EcoCyc:FORMATEDEHYDROG-RXN`

## Notes

FORMATE + PROTON + Menaquinones -> PROTON + CARBON-DIOXIDE + Menaquinols; direction=PHYSIOL-LEFT-TO-RIGHT
