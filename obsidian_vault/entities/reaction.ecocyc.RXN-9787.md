---
entity_id: "reaction.ecocyc.RXN-9787"
entity_type: "reaction"
name: "cysteine:[ThiI sulfur-carrier protein]-L-cysteine sulfurtransferase desulfurase"
source_database: "EcoCyc"
source_id: "RXN-9787"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# cysteine:[ThiI sulfur-carrier protein]-L-cysteine sulfurtransferase desulfurase

`reaction.ecocyc.RXN-9787`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN-9787`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

Sulfur-Carrier-Proteins-ThiI + CYS -> Sulfurylated-ThiI + L-ALPHA-ALANINE; direction=PHYSIOL-LEFT-TO-RIGHT EcoCyc reaction equation: Sulfur-Carrier-Proteins-ThiI + CYS -> Sulfurylated-ThiI + L-ALPHA-ALANINE; direction=PHYSIOL-LEFT-TO-RIGHT.

## Biological Role

Catalyzed by cysteine desulfurase IscS (complex.ecocyc.CPLX0-248). Substrates: L-Cysteine (molecule.C00097). Products: L-Alanine (molecule.C00041).

## Enriched Pathways

- `ecocyc.PWY-6892` thiazole component of thiamine diphosphate biosynthesis I (EcoCyc)
- `ecocyc.PWY-8618` tRNA-uridine 4-thiolation II (EcoCyc)

## Annotation

Sulfur-Carrier-Proteins-ThiI + CYS -> Sulfurylated-ThiI + L-ALPHA-ALANINE; direction=PHYSIOL-LEFT-TO-RIGHT

## Pathways

- `ecocyc.PWY-6892` thiazole component of thiamine diphosphate biosynthesis I (EcoCyc)
- `ecocyc.PWY-8618` tRNA-uridine 4-thiolation II (EcoCyc)

## Outgoing Edges (0)

_None._

## Incoming Edges (3)

- `catalyzes` <-- [[complex.ecocyc.CPLX0-248|complex.ecocyc.CPLX0-248]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00041|molecule.C00041]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00097|molecule.C00097]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:RXN-9787`

## Notes

Sulfur-Carrier-Proteins-ThiI + CYS -> Sulfurylated-ThiI + L-ALPHA-ALANINE; direction=PHYSIOL-LEFT-TO-RIGHT
