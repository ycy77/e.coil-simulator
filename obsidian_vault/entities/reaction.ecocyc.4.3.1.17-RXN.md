---
entity_id: "reaction.ecocyc.4.3.1.17-RXN"
entity_type: "reaction"
name: "4.3.1.17-RXN"
source_database: "EcoCyc"
source_id: "4.3.1.17-RXN"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# 4.3.1.17-RXN

`reaction.ecocyc.4.3.1.17-RXN`

## Static

- Type: `reaction`
- Source: `EcoCyc:4.3.1.17-RXN`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

This reaction degrades L-serine to pyruvate. EcoCyc reaction equation: SER -> PYRUVATE + AMMONIUM; direction=PHYSIOL-LEFT-TO-RIGHT. This reaction degrades L-serine to pyruvate.

## Biological Role

Catalyzed by L-serine deaminase III (complex.ecocyc.CPLX0-7622), catabolic threonine dehydratase (complex.ecocyc.THREDEHYDCAT-CPLX), sdaA (protein.P16095), sdaB (protein.P30744). Substrates: L-Serine (molecule.C00065). Products: Pyruvate (molecule.C00022), ammonium (molecule.ecocyc.AMMONIUM).

## Enriched Pathways

- `ecocyc.PWY0-1608` glycine degradation (EcoCyc)

## Annotation

This reaction degrades L-serine to pyruvate.

## Pathways

- `ecocyc.PWY0-1608` glycine degradation (EcoCyc)

## Outgoing Edges (0)

_None._

## Incoming Edges (14)

- `activates` <-- [[molecule.C00020|molecule.C00020]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `catalyzes` <-- [[complex.ecocyc.CPLX0-7622|complex.ecocyc.CPLX0-7622]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` <-- [[complex.ecocyc.THREDEHYDCAT-CPLX|complex.ecocyc.THREDEHYDCAT-CPLX]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` <-- [[protein.P16095|protein.P16095]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` <-- [[protein.P30744|protein.P30744]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00022|molecule.C00022]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.ecocyc.AMMONIUM|molecule.ecocyc.AMMONIUM]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00065|molecule.C00065]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `represses` <-- [[molecule.C00038|molecule.C00038]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.C00097|molecule.C00097]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.C00189|molecule.C00189]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.C00740|molecule.C00740]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.ecocyc.CU_2|molecule.ecocyc.CU_2]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.ecocyc.O-PHENANTHROLINE|molecule.ecocyc.O-PHENANTHROLINE]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity

## External IDs

- `EcoCyc:4.3.1.17-RXN`

## Notes

SER -> PYRUVATE + AMMONIUM; direction=PHYSIOL-LEFT-TO-RIGHT
