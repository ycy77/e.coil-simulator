---
entity_id: "reaction.ecocyc.AICARSYN-RXN"
entity_type: "reaction"
name: "AICARSYN-RXN"
source_database: "EcoCyc"
source_id: "AICARSYN-RXN"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# AICARSYN-RXN

`reaction.ecocyc.AICARSYN-RXN`

## Static

- Type: `reaction`
- Source: `EcoCyc:AICARSYN-RXN`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

This is the eighth step in the de novo purine biosynthesis. EcoCyc reaction equation: P-RIBOSYL-4-SUCCCARB-AMINOIMIDAZOLE -> FUM + AICAR; direction=LEFT-TO-RIGHT. This is the eighth step in the de novo purine biosynthesis.

## Biological Role

Catalyzed by adenylosuccinate lyase (complex.ecocyc.CPLX0-7959). Substrates: 1-(5'-Phosphoribosyl)-5-amino-4-(N-succinocarboxamide)-imidazole (molecule.C04823). Products: Fumarate (molecule.C00122), 1-(5'-Phosphoribosyl)-5-amino-4-imidazolecarboxamide (molecule.C04677).

## Enriched Pathways

- `ecocyc.PWY-6123` inosine-5'-phosphate biosynthesis I (EcoCyc)

## Annotation

This is the eighth step in the de novo purine biosynthesis.

## Pathways

- `ecocyc.PWY-6123` inosine-5'-phosphate biosynthesis I (EcoCyc)

## Outgoing Edges (0)

_None._

## Incoming Edges (4)

- `catalyzes` <-- [[complex.ecocyc.CPLX0-7959|complex.ecocyc.CPLX0-7959]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00122|molecule.C00122]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C04677|molecule.C04677]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C04823|molecule.C04823]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:AICARSYN-RXN`

## Notes

P-RIBOSYL-4-SUCCCARB-AMINOIMIDAZOLE -> FUM + AICAR; direction=LEFT-TO-RIGHT
