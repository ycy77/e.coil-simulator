---
entity_id: "reaction.ecocyc.INOSINATE-NUCLEOSIDASE-RXN"
entity_type: "reaction"
name: "INOSINATE-NUCLEOSIDASE-RXN"
source_database: "EcoCyc"
source_id: "INOSINATE-NUCLEOSIDASE-RXN"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# INOSINATE-NUCLEOSIDASE-RXN

`reaction.ecocyc.INOSINATE-NUCLEOSIDASE-RXN`

## Static

- Type: `reaction`
- Source: `EcoCyc:INOSINATE-NUCLEOSIDASE-RXN`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

IMP + WATER -> HYPOXANTHINE + CPD-15317; direction=PHYSIOL-LEFT-TO-RIGHT EcoCyc reaction equation: IMP + WATER -> HYPOXANTHINE + CPD-15317; direction=PHYSIOL-LEFT-TO-RIGHT.

## Biological Role

Catalyzed by nucleotide 5'-monophosphate nucleosidase (complex.ecocyc.CPLX0-8262). Substrates: H2O (molecule.C00001), IMP (molecule.C00130). Products: Hypoxanthine (molecule.C00262), D-ribofuranose 5-phosphate (molecule.ecocyc.CPD-15317).

## Annotation

IMP + WATER -> HYPOXANTHINE + CPD-15317; direction=PHYSIOL-LEFT-TO-RIGHT

## Outgoing Edges (0)

_None._

## Incoming Edges (5)

- `catalyzes` <-- [[complex.ecocyc.CPLX0-8262|complex.ecocyc.CPLX0-8262]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00262|molecule.C00262]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.ecocyc.CPD-15317|molecule.ecocyc.CPD-15317]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00001|molecule.C00001]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C00130|molecule.C00130]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:INOSINATE-NUCLEOSIDASE-RXN`

## Notes

IMP + WATER -> HYPOXANTHINE + CPD-15317; direction=PHYSIOL-LEFT-TO-RIGHT
