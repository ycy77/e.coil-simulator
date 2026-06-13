---
entity_id: "reaction.ecocyc.IMPCYCLOHYDROLASE-RXN"
entity_type: "reaction"
name: "IMPCYCLOHYDROLASE-RXN"
source_database: "EcoCyc"
source_id: "IMPCYCLOHYDROLASE-RXN"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# IMPCYCLOHYDROLASE-RXN

`reaction.ecocyc.IMPCYCLOHYDROLASE-RXN`

## Static

- Type: `reaction`
- Source: `EcoCyc:IMPCYCLOHYDROLASE-RXN`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

This is the tenth step in purine biosynthesis. EcoCyc reaction equation: IMP + WATER -> PHOSPHORIBOSYL-FORMAMIDO-CARBOXAMIDE; direction=REVERSIBLE. This is the tenth step in purine biosynthesis.

## Biological Role

Catalyzed by purH (protein.P15639). Substrates: H2O (molecule.C00001), IMP (molecule.C00130). Products: 1-(5'-Phosphoribosyl)-5-formamido-4-imidazolecarboxamide (molecule.C04734).

## Enriched Pathways

- `ecocyc.PWY-6123` inosine-5'-phosphate biosynthesis I (EcoCyc)

## Annotation

This is the tenth step in purine biosynthesis.

## Pathways

- `ecocyc.PWY-6123` inosine-5'-phosphate biosynthesis I (EcoCyc)

## Outgoing Edges (0)

_None._

## Incoming Edges (4)

- `catalyzes` <-- [[protein.P15639|protein.P15639]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C04734|molecule.C04734]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00001|molecule.C00001]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C00130|molecule.C00130]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:IMPCYCLOHYDROLASE-RXN`

## Notes

IMP + WATER -> PHOSPHORIBOSYL-FORMAMIDO-CARBOXAMIDE; direction=REVERSIBLE
